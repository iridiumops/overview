# import libs
from datetime import date, datetime
from pathlib import Path
import utils
import dir_paths

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
        "main": [
            {
                "title" : "<b> SYSTEM </b>",
                "color" : [1.0, 1.0, 1.0],
                "filter" : "filter System System",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns navigation",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b> PVE </b>",
                "color" : [0.0784, 0.6901, 0.8235],
                "filter" : "filter Main PVX (+friendly +extra)",
                "bracket" : "filter Brackets Combat (+drones)",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b> PVP </b>",
                "color" : [1.0, 0.2705, 0.2705],
                "filter" : "filter Main PVX",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b> SHIPS </b>",
                "color" : [1.0, 0.6, 0.0],
                "filter" : "filter Ships Enemy All (red+neutral)",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b> CAPS </b>",
                "color" : [1.0, 0.6, 0.0],
                "filter" : "filter Ships Enemy Capitals (red+neutral)",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b> NPC </b>",
                "color" : [1.0, 0.6, 0.0],
                "filter" : "filter Ships NPCs (+turrets)",
                "bracket" : "filter Brackets Combat (-wrecks)",
                "columns" : "columns combat npc",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b> DRONES </b>",
                "color" : [1.0, 0.9333, 0.0],
                "filter" : "filter Drones Drones and Fighters (red+neutral)",
                "bracket" : "filter Brackets Combat (+drones)",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b> WARP </b>",
                "color" : [1.0, 0.3333, 0.0],
                "filter" : "filter Warp Warp out!",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns navigation",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b> LOOT </b>",
                "color" : [1.0, 1.0, 1.0],
                "filter" : "filter Loot Loot and salvage",
                "bracket" : "filter Brackets Combat (+drones)",
                "columns" : "columns combat npc",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b> ALL </b>",
                "color" : [1.0, 1.0, 1.0],
                "filter" : "filter All All",
                "bracket" : "_BracketFilterShowAll",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b> FLEET </b>",
                "color" : [0.9333, 0.1333, 0.9333],
                "filter" : "filter Ships Fleet",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b>FRIENDLY</b>",
                "color" : [0.098, 0.6, 0.098],
                "filter" : "filter Ships Friendly",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b> MINING </b>",
                "color" : [1.0, 1.0, 1.0],
                "filter" : "filter System Mining",
                "bracket" : "filter Brackets Combat (+drones)",
                "columns" : "columns navigation",
                "columns_order" : "columns all ordered",
            }
        ],
        "icons": [
            {
                "title" : "<fontsize=16> ✪ </fontsize>",
                "color" : [1.0, 1.0, 1.0],
                "filter" : "filter System System",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns navigation",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ✱ </fontsize>",
                "color" : [0.0784, 0.6901, 0.8235],
                "filter" : "filter Main PVX (+friendly +extra)",
                "bracket" : "filter Brackets Combat (+drones)",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ✱ </fontsize>",
                "color" : [1.0, 0.2705, 0.2705],
                "filter" : "filter Main PVX",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ❖ </fontsize>",
                "color" : [1.0, 0.6, 0.0],
                "filter" : "filter Ships Enemy All (red+neutral)",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ♦ </fontsize>",
                "color" : [1.0, 0.6, 0.0],
                "filter" : "filter Ships Enemy Capitals (red+neutral)",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ✿ </fontsize>",
                "color" : [1.0, 0.6, 0.0],
                "filter" : "filter Ships NPCs (+turrets)",
                "bracket" : "filter Brackets Combat (-wrecks)",
                "columns" : "columns combat npc",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ✜ </fontsize>",
                "color" : [1.0, 0.9333, 0.0],
                "filter" : "filter Drones Drones and Fighters (red+neutral)",
                "bracket" : "filter Brackets Combat (+drones)",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ➔ </fontsize>",
                "color" : [1.0, 0.3333, 0.0],
                "filter" : "filter Warp Warp out!",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns navigation",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ❒ </fontsize>",
                "color" : [1.0, 1.0, 1.0],
                "filter" : "filter Loot Loot and salvage",
                "bracket" : "filter Brackets Combat (+drones)",
                "columns" : "columns combat npc",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ⌘ </fontsize>",
                "color" : [1.0, 1.0, 1.0],
                "filter" : "filter All All",
                "bracket" : "_BracketFilterShowAll",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ❤ </fontsize>",
                "color" : [0.9333, 0.1333, 0.9333],
                "filter" : "filter Ships Fleet",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ❤ </fontsize>",
                "color" : [0.098, 0.6, 0.098],
                "filter" : "filter Ships Friendly",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ✇ </fontsize>",
                "color" : [1.0, 1.0, 1.0],
                "filter" : "filter System Mining",
                "bracket" : "filter Brackets Combat (+drones)",
                "columns" : "columns navigation",
                "columns_order" : "columns all ordered",
            }
        ],
        "carbon": [
            {
                "title" : "<b> SYSTEM </b>",
                "color" : [1.0, 1.0, 1.0],
                "filter" : "filter System System",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns navigation",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b> MAIN </b>",
                "color" : [0.0784, 0.6901, 0.8235],
                "filter" : "filter Main System & PVX (+extra)",
                "bracket" : "filter Brackets Combat (+drones)",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b> SHIPS </b>",
                "color" : [1.0, 0.6, 0.0],
                "filter" : "filter Ships Enemy All (red+neutral)",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b> NPC </b>",
                "color" : [1.0, 0.6, 0.0],
                "filter" : "filter Ships NPCs (+turrets)",
                "bracket" : "filter Brackets Combat (-wrecks)",
                "columns" : "columns combat npc",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<b> DRONES </b>",
                "color" : [1.0, 0.9333, 0.0],
                "filter" : "filter Drones Drones and Fighters (red+neutral)",
                "bracket" : "filter Brackets Combat (+drones)",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ➔ </fontsize>",
                "color" : [1.0, 0.3333, 0.0],
                "filter" : "filter Warp Warp out!",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns navigation",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ❒ </fontsize>",
                "color" : [1.0, 1.0, 1.0],
                "filter" : "filter Loot Loot and salvage",
                "bracket" : "filter Brackets Combat (+drones)",
                "columns" : "columns combat npc",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ⌘ </fontsize>",
                "color" : [1.0, 1.0, 1.0],
                "filter" : "filter All All",
                "bracket" : "_BracketFilterShowAll",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            },
            {
                "title" : "<fontsize=16> ❤ </fontsize>",
                "color" : [0.098, 0.6, 0.098],
                "filter" : "filter Ships Friendly",
                "bracket" : "filter Brackets Combat",
                "columns" : "columns combat",
                "columns_order" : "columns all ordered",
            }
        ]
    }
}


def main():
    # optional step, adds comments to part files with groupNames for GroupIDs
    for filter_file_path in dir_paths.parts_dir.glob("part*.yaml"):
        utils.yaml_comment(Path(filter_file_path).stem)

    # build yaml file(s), one for each tab type
    print("Generating all files...")
    for tab_type, tab_data in parts["tabs"].items():
        # combine yaml parts, starting with general
        yaml_content = utils.yaml_load_part(parts["general"])
        
        # add all filters defined in parts["filters"]
        for filter_name, filter_parts in parts["filters"].items():                      

            # get filter
            filter_content = utils.yaml_load_part(filter_name)

            # build combined GroupIDs list for filter from parts
            filter_groups = []
            for part_name in filter_parts:
                part_content = utils.yaml_load_part(part_name)
                filter_groups = sorted(list(set(filter_groups + part_content)))
            filter_content[0][1].append(["groups", filter_groups])

            # add filter to presets
            yaml_content["presets"].extend(filter_content)

        yaml_content.update(utils.yaml_load_part(parts["labels"]))
        yaml_content.update(utils.yaml_load_part(parts["states"]))

        # tab settings
        yaml_tabs = []
        for i, tab in enumerate(tab_data):
            # get exact filter and bracket name from their yaml files, handle ShowAll option
            if tab["bracket"] == "_BracketFilterShowAll":
                bracket_filter = "_BracketFilterShowAll"
            else:
                bracket_filter = utils.yaml_load_part(tab["bracket"])[0][0]
            overview_filter = utils.yaml_load_part(tab["filter"])[0][0]

            # add each tab in required yaml format
            yaml_tabs.append([i, [
                ["bracket", bracket_filter],
                ["color", tab["color"]],
                ["name", tab["title"]],
                ["overview", overview_filter],
                ["tabColumnOrder", utils.yaml_load_part(tab["columns_order"])],
                ["tabColumns", utils.yaml_load_part(tab["columns"])]
            ]])
        yaml_content.update({"tabSetup" : yaml_tabs})

        # user settings
        yaml_content.update({"userSettings" : []})

        # save to file
        date_now = date.today().strftime("%Y%m%d")
        time_now = datetime.now().strftime("%H%M%S")
        output_name = "iridium_overview_" + date_now + "-" + time_now + "_" + tab_type + ".yaml"
        output_path = utils.yaml_save_to_output(yaml_content, output_name)
        print(f" - saved to file: {output_path}")

    print("Done")


if __name__ == '__main__':
    main()
