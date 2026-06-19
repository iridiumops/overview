# import libs
from pprint import pprint
from argparse import ArgumentParser
import api
import utils
from pathlib import Path

"""
WARNING: This script is mostly deprecated and superseded by monitor.py

analyze.py script is designed to to find new group type IDs and their names. 
How to use it:
   Ingame, in the overview settings update or create any filter to include all possible types. 
   For example use the `All: All` filter, tick all types and save it.
   On `Misc` tab click `Export Settings`, make sure this filter is ticked and export it to a file under any name you wish. 
   On Windows it will be located in `%USERPROFILE%/Documents/EVE/Overview/`.
   Run the `scripts/analyze.bat` script and provide path to this exported YAML file,
   it will call `src/analyze.py` and analyze differences and fetch data from API.
   Read the results, which will contain all new group type IDs and their respective names.
"""

if __name__ == '__main__':
    # Create arg parser
    parser = ArgumentParser(description='Analyze YAML export file for new IDs')
    parser.add_argument('file', type=str, help='Path to YAML file')

    # Execute arg parser
    args = parser.parse_args()
    
    # Get known old IDs
    old_ids = set(utils.yaml_load_part("part_all"))

    # Load provided YAML file and extract all groupIDs
    print("Analyzing file for new IDs..")
    file_path = Path(args.file)
    current_ids = utils.yaml_get_all_unique_group_ids(file_path)
    
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
            group = api.get_group(group_id)
            if group:
                print("- "+str(group_id)+" # "+group["name"])
            else:
                print("Failed to fetch name for ID "+str(group_id))
        print()
        print("Done")
