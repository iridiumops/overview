# import libs
import os, yaml, re, shutil
import pandas as pd
from datetime import date, datetime
from pprint import pprint

temp_dir = "./temp"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

output_dir = "./output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

parts_dir = "./parts"

# list of all parts and corresponding names of yaml files
parts = {
    "general": "general",
    "filters": [
        "Brackets Combat",
        "Brackets Combat (+drones)",
        "Brackets Combat (-wrecks)",
        "DSCAN Ships",
        "DSCAN Basic",
        "DSCAN Extra",
        "All All",
        "System System",
        "System System (-citadels)",
        "System System (+belts)",
        "System Mining",
        "System Beacons",
        "Warp Warp out!",
        "Warp Travel (-citadels)",
        "Warp Travel",
        "Loot Loot and salvage",
        "Drones Drones and Fighters (all)",
        "Drones Drones and Fighters (red+neutral)",
        "Drones Fighters (red+neutral)",
        "Ships NPCs (+turrets)",
        "Ships Friendly",
        "Ships Fleet",
        "Ships Enemy All (red)",
        "Ships Enemy All (red -capsules)",
        "Ships Enemy All (red+neutral)",
        "Ships Enemy All (red+neutral -capsules)",
        "Ships Enemy All (war targets)",
        "Ships Enemy All (hisec criminals)",
        "Ships Enemy Logi (red+neutral)",
        "Ships Enemy Utility (red+neutral)",
        "Ships Enemy Capitals (red+neutral)",
        "Main PVX (+friendly +extra)",
        "Main PVX (+extra)",
        "Main PVX",
        "Main PVX (-npc)",
        "Main PVX (+mining)",
        "Main System & PVX (+extra)",
        "Main System & PVX (-npc)",
    ],
    "labels": "labels",
    "states": "states",
    "tabs": {
        "carbon": "tabs carbon",
        "icons": "tabs icons",
        "main": "tabs main"
    },
    "user": "user"
}


def yaml_append(yaml_content, name):
    """
    Load yaml from file and add it to the end of yaml document

    :param yaml_content: yaml document object
    :param name: file name part
    """
    part_file_path = parts_dir + "/" + name + ".yaml"
    with open(part_file_path, 'r', encoding="utf8") as part_file:
        part_content = yaml.safe_load(part_file)
        yaml_content.update(part_content)


def yaml_add_filter(yaml_content, name):
    """
    Load filter from yaml file and add it to filters inside yaml document

    :param yaml_content: yaml document object
    :param name: file name part
    """
    part_file_path = parts_dir + "/" + name + ".yaml"
    with open(part_file_path, 'r', encoding="utf8") as part_file:
        part_content = yaml.safe_load(part_file)
        yaml_content["presets"].extend(part_content)


def yaml_sort_section(data):
    """
    Sort groupIDs numerically in ascending order

    :param data: yaml document object
    """
    if isinstance(data, dict):
        for key, value in data.items():
            yaml_sort_section(value)
    elif isinstance(data, list):
        for item in data:
            if item == "groups":
                data[1] = sorted(data[1])
            yaml_sort_section(item)
    else:
        pass


def yaml_comment(data_inv_types, name):
    """
    Add groupName (string description) as yaml comment for each groupID

    :param data_inv_types: mapping of groupIDs to groupName data_inv_types
    :param name: file name part
    """
    part_file_path = parts_dir + "/" + name + ".yaml"
    part_file_path_temp = temp_dir + "/" + name + ".yaml"
    group_start_found = False

    # append group names for IDs, write to temp file
    with open(part_file_path, 'r', encoding="utf8") as in_file, open(part_file_path_temp, 'w', encoding="utf8") as out_file:
        for line in in_file:
            if group_start_found:
                match_id = re.search(r' - (\d+)', line)
                match_comment = re.search(r' # ', line)
                if match_id and not match_comment:
                    group_id = int(match_id.group(1))
                    if group_id in data_inv_types:
                        line = line.rstrip() + ' # ' + data_inv_types[group_id] + '\n'
            else:
                match_groups = re.search(r' - groups', line)
                if match_groups:
                    group_start_found = True

            out_file.write(line)

    # replace old file
    os.remove(part_file_path)
    shutil.move(part_file_path_temp, part_file_path)


if __name__ == '__main__':
    # set vars
    date_now = date.today().strftime("%Y%m%d")
    time_now = datetime.now().strftime("%H%M%S")

    # load groupIDs and corresponding groupNames from SDE csv
    data_inv_types = pd.read_csv('./data/invGroups.csv', sep=",", header=0, usecols=[0, 2], index_col=[0])
    data_inv_types = data_inv_types.to_dict()["groupName"]

    # build yaml file(s)
    print("Generating all files...")
    for tab_type, tab_file in parts["tabs"].items():
        yaml_content = {}

        # combine yaml parts
        yaml_append(yaml_content, parts["general"])
        for filter in parts["filters"]:                      # add all filters defined in parts["filters"]
            filter_name = "filter " + filter
            yaml_comment(data_inv_types, filter_name)        # optional step, adds comments to part files with groupNames for GroupIDs
            yaml_add_filter(yaml_content, filter_name)
        yaml_append(yaml_content, parts["labels"])
        yaml_append(yaml_content, parts["states"])
        yaml_append(yaml_content, parts["tabs"][tab_type])
        yaml_append(yaml_content, parts["user"])

        # sort group IDs
        yaml_sort_section(yaml_content)

        # save to file
        output_path = output_dir + "/iridium_overview_" + date_now + "-" + time_now + "_" + tab_type + ".yaml"
        with open(output_path, 'w', encoding="utf8") as outfile:
            yaml.safe_dump(yaml_content, outfile, sort_keys=False, encoding="utf8", allow_unicode=True)
            print(" - saved to file: " + output_path)

    print("Done")
