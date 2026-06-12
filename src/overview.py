# configuration dictionary
# contains all filter definitions and their modular sub-parts, tab settings, other sections of overview configuration
config = {
    # general section (mostly legacy definitions and common default settings)
    "general": "general",
    # filters
    "filters": {
        "filter Brackets Combat": {
            "name" : '<color=0xFFCCCCCC>/ Brackets: Combat</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states none",
            "parts" : [
                "part ships", 
                "part wrecks", 
                "part npcs", 
                "part brackets"
            ]
        },
        "filter Brackets Combat (+drones)": {
            "name" : '<color=0xFFCCCCCC>/ Brackets: Combat (+drones)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states none",
            "parts" : [
                "part ships", 
                "part drones", 
                "part fighters", 
                "part wrecks", 
                "part npcs", 
                "part brackets"
            ]
        },
        "filter Brackets Combat (-wrecks)": {
            "name" : '<color=0xFFCCCCCC>/ Brackets: Combat (-wrecks)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states none",
            "parts" : [
                "part ships", 
                "part npcs", 
                "part brackets"
            ]
        },
        "filter DSCAN Ships": {
            "name" : '<color=0xFFCCCCCC>? DSCAN: Ships</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue",
            "parts" : [
                "part ships", 
                "part capsule"
            ]
        },
        "filter DSCAN Basic": {
            "name" : '<color=0xFFCCCCCC>? DSCAN: Basic</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue",
            "parts" : [
                "part dscan basic", 
                "part ships", 
                "part capsule"
            ]
        },
        "filter DSCAN Extra": {
            "name" : '<color=0xFFCCCCCC>? DSCAN: Extra</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue",
            "parts" : [
                "part dscan extra", 
                "part dscan basic", 
                "part ships", 
                "part capsule"
            ]
        },
        "filter All All": {
            "name" : '<color=0xFFCCCCCC>⌘ All: All</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states none",
            "parts" : [
                "part all"
            ]
        },
        "filter System System": {
            "name" : '<color=0xFFFFFFFF>✪ System: System</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states none",
            "parts" : [
                "part system", 
                "part structures", 
                "part citadels"
            ]
        },
        "filter System System (-citadels)": {
            "name" : '<color=0xFFFFFFFF>✪ System: System (-citadels)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states none",
            "parts" : [
                "part system"
            ]
        },
        "filter System System (+belts)": {
            "name" : '<color=0xFFFFFFFF>✪ System: System (+belts)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states none",
            "parts" : [
                "part system", 
                "part structures", 
                "part citadels", 
                "part belts"
            ]
        },
        "filter System Mining": {
            "name" : '<color=0xFFFFFFFF>✪ System: Mining</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue",
            "parts" : [
                "part belts", 
                "part mining"
            ]
        },
        "filter System Beacons": {
            "name" : '<color=0xFFFFFFFF>✪ System: Beacons</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states none",
            "parts" : [
                "part beacons"
            ]
        },
        "filter Warp Warp out!": {
            "name" : '<color=0xFFFF5500>➔ Warp: Warp out!</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states none",
            "parts" : [
                "part warp"
            ]
        },
        "filter Warp Travel (-citadels)": {
            "name" : '<color=0xFFFF5500>➔ Warp: Travel (-citadels)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue ally militia agent",
            "parts" : [
                "part travel"
            ]
        },
        "filter Warp Travel": {
            "name" : '<color=0xFFFF5500>➔ Warp: Travel</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue ally militia agent",
            "parts" : [
                "part citadels", 
                "part travel"
            ]
        },
        "filter Loot Loot and salvage": {
            "name" : '<color=0xFFCCCCCC>❒ Loot: Loot and salvage</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states none",
            "parts" : [
                "part loot"
            ]
        },
        "filter Drones Drones and Fighters (all)": {
            "name" : '<color=0xFFFFEE00>✜ Drones: Drones and Fighters (all)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states none",
            "parts" : [
                "part drones", 
                "part fighters"
            ]
        },
        "filter Drones Drones and Fighters (red+neutral)": {
            "name" : '<color=0xFFFFEE00>✜ Drones: Drones and Fighters (red+neutral)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue",
            "parts" : [
                "part drones", 
                "part fighters"
            ]
        },
        "filter Drones Fighters (red+neutral)": {
            "name" : '<color=0xFFFFEE00>✜ Drones: Fighters (red+neutral)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue",
            "parts" : [
                "part fighters"
            ]
        },
        "filter Ships NPCs (+turrets)": {
            "name" : '<color=0xFFFF9900>❖ Ships: NPCs (+turrets)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue",
            "parts" : [
                "part npcs", 
                "part police", 
                "part turrets"
            ]
        },
        "filter Ships Friendly": {
            "name" : '<color=0xFF199919>❖ Ships: Friendly</color>',
            "always_shown_states" : "states blue ally militia",
            "filtered_states" : "states not blue ally militia",
            "parts" : [
                "part ships", 
                "part capsule"
            ]
        },
        "filter Ships Fleet": {
            "name" : '<color=0xFFEE22EE>❖ Ships: Fleet</color>',
            "always_shown_states" : "states fleet",
            "filtered_states" : "states not fleet",
            "parts" : [
                "part ships", 
                "part capsule"
            ]
        },
        "filter Ships Enemy All (red)": {
            "name" : '<color=0xFFFF9900>❖ Ships: Enemy All (red)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states not red war engagement",
            "parts" : [
                "part ships", 
                "part capsule"
            ]
        },
        "filter Ships Enemy All (red -capsules)": {
            "name" : '<color=0xFFFF9900>❖ Ships: Enemy All (red -capsules)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states not red war engagement",
            "parts" : [
                "part ships"
            ]
        },
        "filter Ships Enemy All (red+neutral)": {
            "name" : '<color=0xFFFF9900>❖ Ships: Enemy All (red+neutral)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue agent",
            "parts" : [
                "part ships", 
                "part capsule"
            ]
        },
        "filter Ships Enemy All (red+neutral -capsules)": {
            "name" : '<color=0xFFFF9900>❖ Ships: Enemy All (red+neutral -capsules)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue agent",
            "parts" : [
                "part ships"
            ]
        },
        "filter Ships Enemy All (war targets)": {
            "name" : '<color=0xFFFF9900>❖ Ships: Enemy All (war targets)</color>',
            "always_shown_states" : "states war",
            "filtered_states" : "states not war",
            "parts" : [
                "part ships", 
                "part capsule"
            ]
        },
        "filter Ships Enemy All (hisec criminals)": {
            "name" : '<color=0xFFFF9900>❖ Ships: Enemy All (hisec criminals)</color>',
            "always_shown_states" : "states war criminal",
            "filtered_states" : "states not war criminal",
            "parts" : [
                "part ships", 
                "part capsule"
            ]
        },
        "filter Ships Enemy Logi (red+neutral)": {
            "name" : '<color=0xFFFF9900>❖ Ships: Enemy Logi (red+neutral)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue agent",
                "parts" : [
                "part ships logi"
            ]
        },
        "filter Ships Enemy Utility (red+neutral)": {
            "name" : '<color=0xFFFF9900>❖ Ships: Enemy Utility (red+neutral)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue agent",
            "parts" : [
                "part ships utility"
            ]
        },
        "filter Ships Enemy Capitals (red+neutral)": {
            "name" : '<color=0xFFFF9900>❖ Ships: Enemy Capitals (red+neutral)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue agent",
            "parts" : [
                "part ships capitals"
            ]
        },
        "filter Main PVX (+friendly +extra)": {
            "name" : '<color=0xFF14B0D2>✱ Main: PVX (+friendly +extra)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states empty-wreck",
            "parts" : [
                "part npcs", 
                "part main pvx", 
                "part main extra", 
                "part capsule", 
                "part ships"
            ]
        },
        "filter Main PVX (+extra)": {
            "name" : '<color=0xFF14B0D2>✱ Main: PVX (+extra)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue empty-wreck",
            "parts" : [
                "part npcs", 
                "part main pvx", 
                "part main extra", 
                "part capsule", 
                "part ships"
            ]
        },
        "filter Main PVX": {
            "name" : '<color=0xFF14B0D2>✱ Main: PVX</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue",
            "parts" : [
                "part npcs", 
                "part main pvx", 
                "part capsule", 
                "part ships"
            ]
        },
        "filter Main PVX (-npc)": {
            "name" : '<color=0xFF14B0D2>✱ Main: PVX (-npc)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue agent",
            "parts" : [
                "part main pvx", 
                "part capsule", 
                "part ships"
            ]
        },
        "filter Main PVX (+mining)": {
            "name" : '<color=0xFF14B0D2>✱ Main: PVX (+mining)</color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue",
            "parts" : [
                "part npcs", 
                "part main pvx", 
                "part capsule", 
                "part ships", 
                "part mining"
            ]
        },
        "filter Main System & PVX (+extra)": {
            "name" : '<color=0xFF88DDEE>✕ Main: <color=0xFFFFFFFF>System</color> & <color=0xFF14B0D2>PVX (+extra)</color></color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue empty-wreck",
            "parts" : [
                "part npcs", 
                "part main pvx", 
                "part main extra", 
                "part capsule", 
                "part ships", 
                "part structures", 
                "part citadels", 
                "part system"
            ]
        },
        "filter Main System & PVX (-npc)": {
            "name" : '<color=0xFF88DDEE>✕ Main: <color=0xFFFFFFFF>System</color> & <color=0xFF14B0D2>PVX (-npc)</color></color>',
            "always_shown_states" : "states none",
            "filtered_states" : "states blue empty-wreck",
            "parts" : [
                "part main pvx", 
                "part capsule", 
                "part ships", 
                "part structures", 
                "part citadels", 
                "part system"
            ]
        }
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