# import libs
from pprint import pprint
from argparse import ArgumentParser
from api import api_get_group
from utils import yaml_load_part, yaml_get_all_unique_group_ids
from pathlib import Path

if __name__ == '__main__':
    # Create arg parser
    parser = ArgumentParser(description='Analyze YAML export file for new IDs')
    parser.add_argument('file', type=str, help='Path to YAML file')

    # Execute arg parser
    args = parser.parse_args()
    
    # Get known old IDs
    old_ids = set(yaml_load_part("part all"))

    # Load provided YAML file and extract all groupIDs
    print("Analyzing file for new IDs..")
    file_path = Path(args.file)
    current_ids = yaml_get_all_unique_group_ids(file_path)
    
    # Find differences
    new_ids = sorted(set(current_ids - old_ids))

    # Print results
    if len(new_ids) == 0:
        print("Found no new IDs")
    else:
        print("Found "+str(len(new_ids))+" new IDs:")
        pprint(new_ids)
        print()
        print("Fetching names for IDs from api...")
        for group_id in new_ids:
            group = api_get_group(group_id)
            if group:
                print("- "+str(group_id)+" # "+group["name"])
            else:
                print("Failed to fetch name for ID "+str(group_id))
        print()
        print("Done")
