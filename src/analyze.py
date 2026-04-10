# import libs
import os, sys
from pprint import pprint
from argparse import ArgumentParser
from build import *

if __name__ == '__main__':
    # Create arg parser
    parser = ArgumentParser(description='Analyze YAML export file for new IDs')
    parser.add_argument('file', type=str, help='Path to YAML file')

    # Execute arg parser
    args = parser.parse_args()
    
    # Get known old IDs
    old_ids = set(yaml_load_part("part all"))

    # Load provided YAML
    print("Analyzing file for new IDs..")
    if not os.path.isfile(args.file):
        print("Provided path is invalid")
        sys.exit()

    with open(args.file, 'r', encoding="utf8") as yaml_file:
        new_yaml = yaml.safe_load(yaml_file)

    # Extract all groupIDs from YAML file
    current_ids = set()
    for filter in new_yaml["presets"]:
        current_ids.update(filter[1][2][1])

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
        for id in new_ids:
            name = api_get_name_for_group_id(id)
            if name:
                print("- "+str(id)+" # "+name)
            else:
                print("Failed to fetch name for ID "+str(id))
        print()
        print("Done")
