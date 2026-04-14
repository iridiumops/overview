# import libs
import glob
from datetime import date, datetime
from pathlib import Path
from pprint import pprint
from utils import yaml_load_part, yaml_save_to_output, yaml_comment
from dir_paths import *

# dict of all parts/sections of the final YAML config file and corresponding names of yaml files representing those modular pieces
parts = {
    # general section (mostly legacy definitions and common default settings)
    "general": "general",
    # list of filters/presets
    "filters": {
        # each filter is represented by a YAML file.
        # each filter has a list of YAML part files that contain group type ids for that filter
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
    # ship and bracket label configuration
    "labels": "labels",
    # visual representation for different states
    "states": "states",
    # tab settings, multiple variations
    "tabs": {
        "carbon": "tabs carbon",
        "icons": "tabs icons",
        "main": "tabs main"
    },
    # other user settings (empty)
    "user": "user"
}


if __name__ == '__main__':
    # optional step, adds comments to part files with groupNames for GroupIDs
    for filter_file_path in glob.glob(parts_dir + "/part*.yaml"):
        yaml_comment(Path(filter_file_path).stem)

    # build yaml file(s)
    print("Generating all files...")
    for tab_type, tab_file in parts["tabs"].items():
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
        output_name = "iridium_overview_" + date_now + "-" + time_now + "_" + tab_type + ".yaml"
        out = yaml_save_to_output(yaml_content, output_name)
        print(" - saved to file: " + out)

    print("Done")
