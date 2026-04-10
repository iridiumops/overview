# import libs
import os, yaml, re, shutil, glob, requests
from datetime import date, datetime
from pathlib import Path
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
    "filters": {
        "filter Brackets Combat": [
            "part ships", 
            "part wrecks", 
            "part npcs", 
            "part brackets"
        ],
        "filter Brackets Combat (+drones)": [
            "part ships", 
            "part drones", 
            "part fighters", 
            "part wrecks", 
            "part npcs", 
            "part brackets"
        ],
        "filter Brackets Combat (-wrecks)": [
            "part ships", 
            "part npcs", 
            "part brackets"
        ],
        "filter DSCAN Ships": [
            "part ships", 
            "part capsule"
        ],
        "filter DSCAN Basic": [
            "part dscan basic", 
            "part ships", 
            "part capsule"
        ],
        "filter DSCAN Extra": [
            "part dscan extra", 
            "part dscan basic", 
            "part ships", 
            "part capsule"
        ],
        "filter All All": [
            "part all"
        ],
        "filter System System": [
            "part system", 
            "part structures", 
            "part citadels"
        ],
        "filter System System (-citadels)": [
            "part system"
        ],
        "filter System System (+belts)": [
            "part system", 
            "part structures", 
            "part citadels", 
            "part belts"
        ],
        "filter System Mining": [
            "part belts", 
            "part mining"
        ],
        "filter System Beacons": [
            "part beacons"
        ],
        "filter Warp Warp out!": [
            "part warp"
        ],
        "filter Warp Travel (-citadels)": [
            "part travel"
        ],
        "filter Warp Travel": [
            "part citadels", 
            "part travel"
        ],
        "filter Loot Loot and salvage": [
            "part loot"
        ],
        "filter Drones Drones and Fighters (all)": [
            "part drones", 
            "part fighters"
        ],
        "filter Drones Drones and Fighters (red+neutral)": [
            "part drones", 
            "part fighters"
        ],
        "filter Drones Fighters (red+neutral)": [
            "part fighters"
        ],
        "filter Ships NPCs (+turrets)": [
            "part npcs", 
            "part police", 
            "part turrets"
        ],
        "filter Ships Friendly": [
            "part ships", 
            "part capsule"
        ],
        "filter Ships Fleet": [
            "part ships", 
            "part capsule"
        ],
        "filter Ships Enemy All (red)": [
            "part ships", 
            "part capsule"
        ],
        "filter Ships Enemy All (red -capsules)": [
            "part ships"
        ],
        "filter Ships Enemy All (red+neutral)": [
            "part ships", 
            "part capsule"
        ],
        "filter Ships Enemy All (red+neutral -capsules)": [
            "part ships"
        ],
        "filter Ships Enemy All (war targets)": [
            "part ships", 
            "part capsule"
        ],
        "filter Ships Enemy All (hisec criminals)": [
            "part ships", 
            "part capsule"
        ],
        "filter Ships Enemy Logi (red+neutral)": [
            "part ships logi"
        ],
        "filter Ships Enemy Utility (red+neutral)": [
            "part ships utility"
        ],
        "filter Ships Enemy Capitals (red+neutral)": [
            "part ships capitals"
        ],
        "filter Main PVX (+friendly +extra)": [
            "part npcs", 
            "part main pvx", 
            "part main extra", 
            "part capsule", 
            "part ships"
        ],
        "filter Main PVX (+extra)": [
            "part npcs", 
            "part main pvx", 
            "part main extra", 
            "part capsule", 
            "part ships"
        ],
        "filter Main PVX": [
            "part npcs", 
            "part main pvx", 
            "part capsule", 
            "part ships"
        ],
        "filter Main PVX (-npc)": [
            "part main pvx", 
            "part capsule", 
            "part ships"
        ],
        "filter Main PVX (+mining)": [
            "part npcs", 
            "part main pvx", 
            "part capsule", 
            "part ships", 
            "part mining"
        ],
        "filter Main System & PVX (+extra)": [
            "part npcs", 
            "part main pvx", 
            "part main extra", 
            "part capsule", 
            "part ships", 
            "part structures", 
            "part citadels", 
            "part system"
        ],
        "filter Main System & PVX (-npc)": [
            "part main pvx", 
            "part capsule", 
            "part ships", 
            "part structures", 
            "part citadels", 
            "part system"
        ]
    },
    "labels": "labels",
    "states": "states",
    "tabs": {
        "carbon": "tabs carbon",
        "icons": "tabs icons",
        "main": "tabs main"
    },
    "user": "user"
}


def yaml_load_part(file_name):
    """
    Load content of yaml file that is located in parts directory

    :param yaml_content: yaml document object
    :param name: file name part
    """
    part_file_path = parts_dir + "/" + file_name + ".yaml"
    with open(part_file_path, 'r', encoding="utf8") as part_file:
        return yaml.safe_load(part_file)
    

def yaml_comment(name):
    """
    Add groupName (descriptive string name) as yaml comment for each groupID number

    :param name: file name part
    """
    part_file_path = parts_dir + "/" + name + ".yaml"
    part_file_path_temp = temp_dir + "/" + name + ".yaml"

    # append group names for IDs, write to temp file
    with open(part_file_path, 'r', encoding="utf8") as in_file, open(part_file_path_temp, 'w', encoding="utf8") as out_file:
        for line in in_file:
            match_id = re.search(r'- (\d+)', line)
            match_comment = re.search(r' # ', line)
            if match_id and not match_comment:
                group_id = int(match_id.group(1))

                # fetch group name from api
                group_name = api_get_name_for_group_id(group_id)

                if group_name:
                    line = line.rstrip() + ' # ' + group_name + '\n'

            out_file.write(line)

    # replace old file
    os.remove(part_file_path)
    shutil.move(part_file_path_temp, part_file_path)


def api_get_name_for_group_id(group_id: int):
    """
    Tries to fetch descriptive string name for given groupID from ESI API.
    
    :param group_id: Int ID
    :returns: The group name string if found, None otherwise.
    """
    api_url = f"https://esi.evetech.net/universe/groups/{group_id}/"
    
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        if response.status_code == 200:
            data = response.json()
            return data.get("name")
    except:
        return None
        
    return None

if __name__ == '__main__':
    # optional step, adds comments to part files with groupNames for GroupIDs
    for filter_file_path in glob.glob(parts_dir + "/part*.yaml"):
        yaml_comment(Path(filter_file_path).stem)

    # build yaml file(s)
    print("Generating all files...")
    for tab_type, tab_file in parts["tabs"].items():
        yaml_content = {}

        # combine yaml parts, starting with general
        yaml_content = yaml_load_part(parts["general"])
        
        # add all filters defined in parts["filters"]
        for filter_name, filter_parts in parts["filters"].items():                      

            # get filter
            filter_content = yaml_load_part(filter_name)

            # build combined GroupIDs list for filter from parts
            filter_groups = []
            for part_name in filter_parts:
                part_content = yaml_load_part(part_name)
                filter_groups = sorted(list(set(filter_groups + part_content)))
            filter_content[0][1].append(["groups", filter_groups])

            # add filter to presets
            yaml_content["presets"].extend(filter_content)

        yaml_content.update(yaml_load_part(parts["labels"]))
        yaml_content.update(yaml_load_part(parts["states"]))
        yaml_content.update(yaml_load_part(parts["tabs"][tab_type]))
        yaml_content.update(yaml_load_part(parts["user"]))

        # save to file
        date_now = date.today().strftime("%Y%m%d")
        time_now = datetime.now().strftime("%H%M%S")
        output_path = output_dir + "/iridium_overview_" + date_now + "-" + time_now + "_" + tab_type + ".yaml"
        with open(output_path, 'w', encoding="utf8") as outfile:
            yaml.safe_dump(yaml_content, outfile, sort_keys=False, encoding="utf8", allow_unicode=True)
            print(" - saved to file: " + output_path)

    print("Done")
