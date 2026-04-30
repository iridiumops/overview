# imports
import sys
from pprint import pprint
from api import *
from utils import *


def main():
    """monitors api for new relevant group IDs"""

    try:
        # Extract group IDs from provided YAML from last release
        print("\n=== Extracting group IDs from latest release YAML file ===")
        releases = sorted(releases_dir.glob("*_main.yaml"), key=os.path.getmtime, reverse=True)
        if len(releases)<1:
            print("Error - could not find latest release yaml file")
            return None
        latest_yaml_file = releases[0]
        print(f"Reading file {latest_yaml_file} ...")
        current_group_ids = sorted(yaml_get_all_unique_group_ids(latest_yaml_file))
        print(f"Found {len(current_group_ids)} unique group IDs.")
        out = yaml_save_to_temp(current_group_ids, "extracted_group_ids.yaml")
        print(f"Saved to: {out}")

        # For each group ID, fetch its name
        print("\n=== Mapping current groups to their names ===")
        print("Querying API... (please wait)")
        current_group_id_to_name = {}
        for group_id in current_group_ids:
            group_details = api_get_group(group_id)
            if group_details and 'name' in group_details:
                current_group_id_to_name[group_id] = group_details['name']
        print(f"Mapped {len(current_group_id_to_name)} groups to names.")
        out = yaml_save_to_temp(current_group_id_to_name, "current_group_id_to_name.yaml")
        print(f"Saved to: {out}")

        # Fetch all categories
        print("\n=== Fetching categories ===")
        print("Fetching from API... (please wait)")
        all_category_ids = sorted(api_get_category_ids())
        print(f"Found {len(all_category_ids)} categories.")
        out = yaml_save_to_temp(all_category_ids, "all_category_ids.yaml")
        print(f"Saved to: {out}")
        
        # Fetch category names and create mapping
        print("\n=== Fetching category names ===")
        print("Retrieving from API... (please wait)")
        category_id_to_name = {}
        for cat_id in all_category_ids:
            cat_details = api_get_category(cat_id)
            if cat_details and 'name' in cat_details:
                category_id_to_name[cat_id] = cat_details['name']
        print(f"Mapped {len(category_id_to_name)} categories.")
        out = yaml_save_to_temp(category_id_to_name, "category_id_to_name.yaml")
        print(f"Saved to: {out}")

        # Fetch all groups
        print("\n=== Fetching all groups from api ===")
        print("Requesting data from API... (please wait)")
        all_group_ids = sorted(api_get_group_ids())
        print(f"Found {len(all_group_ids)} groups.")
        out = yaml_save_to_temp(all_group_ids, "all_group_ids.yaml")
        print(f"Saved to: {out}")

        # For each group ID, fetch its name
        print("\n=== Mapping all groups to their names ===")
        print("Loading data from API... (please wait)")
        all_group_id_to_name = {}
        for group_id in all_group_ids:
            group_details = api_get_group(group_id)
            if group_details and 'name' in group_details:
                all_group_id_to_name[group_id] = group_details['name']
        print(f"Mapped {len(all_group_id_to_name)} groups to names.")
        out = yaml_save_to_temp(all_group_id_to_name, "all_group_id_to_name.yaml")
        print(f"Saved to: {out}")
        
        # For each group ID, fetch its category ID and map to category name
        print("\n=== Mapping all groups to categories ===")
        print("Getting information from API... (please wait)")
        all_group_id_to_category_name = {}
        for group_id in all_group_ids:
            group_details = api_get_group(group_id)
            if group_details and 'category_id' in group_details:
                cat_id = group_details['category_id']
                if cat_id in category_id_to_name:
                    all_group_id_to_category_name[group_id] = category_id_to_name[cat_id]
        print(f"Mapped {len(all_group_id_to_category_name)} groups to categories.")
        out = yaml_save_to_temp(all_group_id_to_category_name, "all_group_id_to_category_name.yaml")
        print(f"Saved to: {out}")
        
        # For each group ID, fetch its category ID and map to category name
        print("\n=== Mapping current groups to categories ===")
        print("Extracting knowledge from API... (please wait)")
        current_group_id_to_category_name = {}
        for group_id in current_group_ids:
            group_details = api_get_group(group_id)
            if group_details and 'category_id' in group_details:
                cat_id = group_details['category_id']
                if cat_id in category_id_to_name:
                    current_group_id_to_category_name[group_id] = category_id_to_name[cat_id]
        print(f"Mapped {len(current_group_id_to_category_name)} groups to categories.")
        out = yaml_save_to_temp(current_group_id_to_category_name, "current_group_id_to_category_name.yaml")
        print(f"Saved to: {out}")

        # Get unique category IDs and names from the mapping
        print("\n=== Finding unique categories based on currently used groups ===")
        unique_categories = {}
        for group_id, cat_name in current_group_id_to_category_name.items():
            # Find the category ID for this name
            for cat_id, name in category_id_to_name.items():
                if name == cat_name:
                    unique_categories[cat_id] = name
                    break
        print(f"Found {len(unique_categories)} unique categories in the groups.")
        out = yaml_save_to_temp(unique_categories, "unique_categories.yaml")
        print(f"Saved to: {out}")  

        # Find filter all group IDs that belong to the unique_categories
        print("\n=== Filtering groups by computed categories ===")
        print("Reading bytes from API... (please wait)")
        filtered_group_ids = set()
        for group_id in all_group_ids:
            group_details = api_get_group(group_id)
            if group_details and 'category_id' in group_details and group_details['category_id'] in unique_categories:
                filtered_group_ids.add(group_id)
        print(f"Found {len(filtered_group_ids)} unique groups that belong to the unique categories among all groups.")
        out = yaml_save_to_temp(unique_categories, "unique_categories.yaml")
        print(f"Saved to: {out}")  

        # Read ids that should be ignored as they dont seem to be displayable on the overview
        print("\n=== Finding which groups to skip ===")
        ignored_file_path = parts_dir / "ignored.yaml"
        print(f"Reading file: {ignored_file_path}")  
        with open(ignored_file_path, 'r', encoding="utf8") as ignored_file:
            ignored_ids = sorted(yaml.safe_load(ignored_file).keys())
        print(f"Found {len(ignored_ids)} groups that likely should be ignored.")

        # Compare filtered group ids to current group ids - find new and removed ids. 
        print("\n=== Comparing group lists ===")
        print("Comparing and obtaining info from API... (please wait)")

        new_relevant_group_ids = sorted(filtered_group_ids - set(current_group_ids) - set(ignored_ids))
        removed_relevant_group_ids = sorted(set(current_group_ids) - filtered_group_ids - set(ignored_ids))

        print("\n=== Gathering final results ===")
        print("Comparing and obtaining info from API... (please wait)")
        print(f"\nFound {len(new_relevant_group_ids)} new candidate groups.")
        new_relevant_groups = {}
        for group_id in sorted(new_relevant_group_ids):
            group_details = api_get_group(group_id)
            new_relevant_groups[group_id] = group_details["name"]
            print("- " + str(group_id) + " # " + group_details["name"])
        out = yaml_save_to_temp(new_relevant_groups, "new_relevant_groups.yaml")
        print(f"Saved to: {out}")  

        print(f"\nFound {len(removed_relevant_group_ids)} relevant groups that are no longer present in api data.")
        removed_relevant_groups = {}
        for group_id in sorted(removed_relevant_group_ids):
            group_details = api_get_group(group_id)
            removed_relevant_groups[group_id] = group_details["name"]
            print("- " + str(group_id) + " # " + group_details["name"])
        out = yaml_save_to_temp(removed_relevant_groups, "removed_relevant_groups.yaml")
        print(f"Saved to: {out}")  
    
        print("\nDone")
    
    except:
        return 1 # error

    if len(new_relevant_group_ids) > 0 or len(removed_relevant_group_ids) > 0:
        return 2 # changes detected
    else:
        return 0 # no change


if __name__ == '__main__':
    sys.exit(main())
    
