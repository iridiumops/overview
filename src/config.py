from overview import Overview, Filter, Tab

# rgb floats
color_theme = {
    "white": [1.0, 1.0, 1.0],
    "blue": [0.0784, 0.6901, 0.8235],
    "red": [1.0, 0.2705, 0.2705],
    "yellow": [1.0, 0.9333, 0.0],
    "orange_light": [1.0, 0.6, 0.0],
    "orange_dark": [1.0, 0.3333, 0.0],
    "fleet_purple": [0.9333, 0.1333, 0.9333],
    "friendly_green": [0.098, 0.6, 0.098],
}

# all filter definitions and their modular sub-parts
all_filters = {
    "filter Brackets Combat": Filter(
        name = '<color=0xFFCCCCCC>/ Brackets: Combat</color>',
        always_shown_states = "states_none",
        filtered_states = "states_none",
        parts = [
            "part_ships", 
            "part_wrecks", 
            "part_npcs", 
            "part_brackets"
        ]
    ),
    "filter Brackets Combat (+drones)": Filter(
        name = '<color=0xFFCCCCCC>/ Brackets: Combat (+drones)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_none",
        parts = [
            "part_ships", 
            "part_drones", 
            "part_fighters", 
            "part_wrecks", 
            "part_npcs", 
            "part_brackets"
        ]
    ),
    "filter Brackets Combat (-wrecks)": Filter(
        name = '<color=0xFFCCCCCC>/ Brackets: Combat (-wrecks)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_none",
        parts = [
            "part_ships", 
            "part_npcs", 
            "part_brackets"
        ]
    ),
    "filter DSCAN Ships": Filter(
        name = '<color=0xFFCCCCCC>? DSCAN: Ships</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue",
        parts = [
            "part_ships", 
            "part_capsule"
        ]
    ),
    "filter DSCAN Basic": Filter(
        name = '<color=0xFFCCCCCC>? DSCAN: Basic</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue",
        parts = [
            "part_dscan_basic", 
            "part_ships", 
            "part_capsule"
        ]
    ),
    "filter DSCAN Extra": Filter(
        name = '<color=0xFFCCCCCC>? DSCAN: Extra</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue",
        parts = [
            "part_dscan_extra", 
            "part_dscan_basic", 
            "part_ships", 
            "part_capsule"
        ]
    ),
    "filter All All": Filter(
        name = '<color=0xFFCCCCCC>⌘ All: All</color>',
        always_shown_states = "states_none",
        filtered_states = "states_none",
        parts = [
            "part_all"
        ]
    ),
    "filter System System": Filter(
        name = '<color=0xFFFFFFFF>✪ System: System</color>',
        always_shown_states = "states_none",
        filtered_states = "states_none",
        parts = [
            "part_system", 
            "part_structures", 
            "part_citadels"
        ]
    ),
    "filter System System (-citadels)": Filter(
        name = '<color=0xFFFFFFFF>✪ System: System (-citadels)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_none",
        parts = [
            "part_system"
        ]
    ),
    "filter System System (+belts)": Filter(
        name = '<color=0xFFFFFFFF>✪ System: System (+belts)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_none",
        parts = [
            "part_system", 
            "part_structures", 
            "part_citadels", 
            "part_belts"
        ]
    ),
    "filter System Mining": Filter(
        name = '<color=0xFFFFFFFF>✪ System: Mining</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue",
        parts = [
            "part_belts", 
            "part_mining"
        ]
    ),
    "filter System Beacons": Filter(
        name = '<color=0xFFFFFFFF>✪ System: Beacons</color>',
        always_shown_states = "states_none",
        filtered_states = "states_none",
        parts = [
            "part_beacons"
        ]
    ),
    "filter Warp Warp out!": Filter(
        name = '<color=0xFFFF5500>➔ Warp: Warp out!</color>',
        always_shown_states = "states_none",
        filtered_states = "states_none",
        parts = [
            "part_warp"
        ]
    ),
    "filter Warp Travel (-citadels)": Filter(
        name = '<color=0xFFFF5500>➔ Warp: Travel (-citadels)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue_ally_militia_agent",
        parts = [
            "part_travel"
        ]
    ),
    "filter Warp Travel": Filter(
        name = '<color=0xFFFF5500>➔ Warp: Travel</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue_ally_militia_agent",
        parts = [
            "part_citadels", 
            "part_travel"
        ]
    ),
    "filter Loot Loot and salvage": Filter(
        name = '<color=0xFFCCCCCC>❒ Loot: Loot and salvage</color>',
        always_shown_states = "states_none",
        filtered_states = "states_none",
        parts = [
            "part_loot"
        ]
    ),
    "filter Drones Drones and Fighters (all)": Filter(
        name = '<color=0xFFFFEE00>✜ Drones: Drones and Fighters (all)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_none",
        parts = [
            "part_drones", 
            "part_fighters"
        ]
    ),
    "filter Drones Drones and Fighters (red+neutral)": Filter(
        name = '<color=0xFFFFEE00>✜ Drones: Drones and Fighters (red+neutral)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue",
        parts = [
            "part_drones", 
            "part_fighters"
        ]
    ),
    "filter Drones Fighters (red+neutral)": Filter(
        name = '<color=0xFFFFEE00>✜ Drones: Fighters (red+neutral)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue",
        parts = [
            "part_fighters"
        ]
    ),
    "filter Ships NPCs (+turrets)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: NPCs (+turrets)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue",
        parts = [
            "part_npcs", 
            "part_police", 
            "part_turrets"
        ]
    ),
    "filter Ships Friendly": Filter(
        name = '<color=0xFF199919>❖ Ships: Friendly</color>',
        always_shown_states = "states_blue_ally_militia",
        filtered_states = "states_not_blue_ally_militia",
        parts = [
            "part_ships", 
            "part_capsule"
        ]
    ),
    "filter Ships Fleet": Filter(
        name = '<color=0xFFEE22EE>❖ Ships: Fleet</color>',
        always_shown_states = "states_fleet",
        filtered_states = "states_not_fleet",
        parts = [
            "part_ships", 
            "part_capsule"
        ]
    ),
    "filter Ships Enemy All (red)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy All (red)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_not_red_war_engagement",
        parts = [
            "part_ships", 
            "part_capsule"
        ]
    ),
    "filter Ships Enemy All (red -capsules)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy All (red -capsules)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_not_red_war_engagement",
        parts = [
            "part_ships"
        ]
    ),
    "filter Ships Enemy All (red+neutral)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy All (red+neutral)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue_agent",
        parts = [
            "part_ships", 
            "part_capsule"
        ]
    ),
    "filter Ships Enemy All (red+neutral -capsules)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy All (red+neutral -capsules)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue_agent",
        parts = [
            "part_ships"
        ]
    ),
    "filter Ships Enemy All (war targets)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy All (war targets)</color>',
        always_shown_states = "states_war",
        filtered_states = "states_not_war",
        parts = [
            "part_ships", 
            "part_capsule"
        ]
    ),
    "filter Ships Enemy All (hisec criminals)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy All (hisec criminals)</color>',
        always_shown_states = "states_war_criminal",
        filtered_states = "states_not_war_criminal",
        parts = [
            "part_ships", 
            "part_capsule"
        ]
    ),
    "filter Ships Enemy Logi (red+neutral)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy Logi (red+neutral)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue_agent",
        parts = [
            "part_ships_logi"
        ]
    ),
    "filter Ships Enemy Utility (red+neutral)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy Utility (red+neutral)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue_agent",
        parts = [
            "part_ships_utility"
        ]
    ),
    "filter Ships Enemy Capitals (red+neutral)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy Capitals (red+neutral)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue_agent",
        parts = [
            "part_ships_capitals"
        ]
    ),
    "filter Main PVX (+friendly +extra)": Filter(
        name = '<color=0xFF14B0D2>✱ Main: PVX (+friendly +extra)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_empty-wreck",
        parts = [
            "part_npcs", 
            "part_main_pvx", 
            "part_main_extra", 
            "part_capsule", 
            "part_ships"
        ]
    ),
    "filter Main PVX (+extra)": Filter(
        name = '<color=0xFF14B0D2>✱ Main: PVX (+extra)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue_empty-wreck",
        parts = [
            "part_npcs", 
            "part_main_pvx", 
            "part_main_extra", 
            "part_capsule", 
            "part_ships"
        ]
    ),
    "filter Main PVX": Filter(
        name = '<color=0xFF14B0D2>✱ Main: PVX</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue",
        parts = [
            "part_npcs", 
            "part_main_pvx", 
            "part_capsule", 
            "part_ships"
        ]
    ),
    "filter Main PVX (-npc)": Filter(
        name = '<color=0xFF14B0D2>✱ Main: PVX (-npc)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue_agent",
        parts = [
            "part_main_pvx", 
            "part_capsule", 
            "part_ships"
        ]
    ),
    "filter Main PVX (+mining)": Filter(
        name = '<color=0xFF14B0D2>✱ Main: PVX (+mining)</color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue",
        parts = [
            "part_npcs", 
            "part_main_pvx", 
            "part_capsule", 
            "part_ships", 
            "part_mining"
        ]
    ),
    "filter Main System & PVX (+extra)": Filter(
        name = '<color=0xFF88DDEE>✕ Main: <color=0xFFFFFFFF>System</color> & <color=0xFF14B0D2>PVX (+extra)</color></color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue_empty-wreck",
        parts = [
            "part_npcs", 
            "part_main_pvx", 
            "part_main_extra", 
            "part_capsule", 
            "part_ships", 
            "part_structures", 
            "part_citadels", 
            "part_system"
        ]
    ),
    "filter Main System & PVX (-npc)": Filter(
        name = '<color=0xFF88DDEE>✕ Main: <color=0xFFFFFFFF>System</color> & <color=0xFF14B0D2>PVX (-npc)</color></color>',
        always_shown_states = "states_none",
        filtered_states = "states_blue_empty-wreck",
        parts = [
            "part_main_pvx", 
            "part_capsule", 
            "part_ships", 
            "part_structures", 
            "part_citadels", 
            "part_system"
        ]
    )
}

# define main overview variant
overview_main = Overview(
    name = "iridium overview",
    variant = "main",
    version = "3.11.1",
    general = "general",
    filters = all_filters,
    labels = "labels",
    states = "states",
    tabs = [
        Tab(
            title = "<b> SYSTEM </b>",
            color = color_theme["white"],
            filter = all_filters["filter System System"].name,
            bracket = all_filters["filter Brackets Combat"].name,
            columns = "columns_navigation",
            columns_order = "columns_all_ordered",
        ),
        Tab(
            title = "<b> PVE </b>",
            color = color_theme["blue"],
            filter = all_filters["filter Main PVX (+friendly +extra)"].name,
            bracket = all_filters["filter Brackets Combat (+drones)"].name,
            columns = "columns_combat",
            columns_order = "columns_all_ordered",
        ),
        Tab(
            title = "<b> PVP </b>",
            color = color_theme["red"],
            filter = all_filters["filter Main PVX"].name,
            bracket = all_filters["filter Brackets Combat"].name,
            columns = "columns_combat",
            columns_order = "columns_all_ordered",
        ),
        Tab(
            title = "<b> SHIPS </b>",
            color = color_theme["orange_light"],
            filter = all_filters["filter Ships Enemy All (red+neutral)"].name,
            bracket = all_filters["filter Brackets Combat"].name,
            columns = "columns_combat",
            columns_order = "columns_all_ordered",
        ),
        Tab(
            title = "<b> CAPS </b>",
            color = color_theme["orange_light"],
            filter = all_filters["filter Ships Enemy Capitals (red+neutral)"].name,
            bracket = all_filters["filter Brackets Combat"].name,
            columns = "columns_combat",
            columns_order = "columns_all_ordered",
        ),
        Tab(
            title = "<b> NPC </b>",
            color = color_theme["orange_light"],
            filter = all_filters["filter Ships NPCs (+turrets)"].name,
            bracket = all_filters["filter Brackets Combat (-wrecks)"].name,
            columns = "columns_combat_npc",
            columns_order = "columns_all_ordered",
        ),
        Tab(
            title = "<b> DRONES </b>",
            color = color_theme["yellow"],
            filter = all_filters["filter Drones Drones and Fighters (red+neutral)"].name,
            bracket = all_filters["filter Brackets Combat (+drones)"].name,
            columns = "columns_combat",
            columns_order = "columns_all_ordered",
        ),
        Tab(
            title = "<b> WARP </b>",
            color = color_theme["orange_dark"],
            filter = all_filters["filter Warp Warp out!"].name,
            bracket = all_filters["filter Brackets Combat"].name,
            columns = "columns_navigation",
            columns_order = "columns_all_ordered",
        ),
        Tab(
            title = "<b> LOOT </b>",
            color = color_theme["white"],
            filter = all_filters["filter Loot Loot and salvage"].name,
            bracket = all_filters["filter Brackets Combat (+drones)"].name,
            columns = "columns_combat_npc",
            columns_order = "columns_all_ordered",
        ),
        Tab(
            title = "<b> ALL </b>",
            color = color_theme["white"],
            filter = all_filters["filter All All"].name,
            bracket = "_BracketFilterShowAll",
            columns = "columns_combat",
            columns_order = "columns_all_ordered",
        ),
        Tab(
            title = "<b> FLEET </b>",
            color = color_theme["fleet_purple"],
            filter = all_filters["filter Ships Fleet"].name,
            bracket = all_filters["filter Brackets Combat"].name,
            columns = "columns_combat",
            columns_order = "columns_all_ordered",
        ),
        Tab(
            title = "<b>FRIENDLY</b>",
            color = color_theme["friendly_green"],
            filter = all_filters["filter Ships Friendly"].name,
            bracket = all_filters["filter Brackets Combat"].name,
            columns = "columns_combat",
            columns_order = "columns_all_ordered",
        ),
        Tab(
            title = "<b> MINING </b>",
            color = color_theme["white"],
            filter = all_filters["filter System Mining"].name,
            bracket = all_filters["filter Brackets Combat (+drones)"].name,
            columns = "columns_navigation",
            columns_order = "columns_all_ordered",
        )
    ]
)

# tab icons variant
overview_icons = overview_main.new_variant("icons")
overview_icons.tabs[0].title = "<fontsize=16> ✪ </fontsize>"
overview_icons.tabs[1].title = "<fontsize=16> ✱ </fontsize>"
overview_icons.tabs[2].title = "<fontsize=16> ✱ </fontsize>"
overview_icons.tabs[3].title = "<fontsize=16> ❖ </fontsize>"
overview_icons.tabs[4].title = "<fontsize=16> ♦ </fontsize>"
overview_icons.tabs[5].title = "<fontsize=16> ✿ </fontsize>"
overview_icons.tabs[6].title = "<fontsize=16> ✜ </fontsize>"
overview_icons.tabs[7].title = "<fontsize=16> ➔ </fontsize>"
overview_icons.tabs[8].title = "<fontsize=16> ❒ </fontsize>"
overview_icons.tabs[9].title = "<fontsize=16> ⌘ </fontsize>"
overview_icons.tabs[10].title = "<fontsize=16> ❤ </fontsize>"
overview_icons.tabs[11].title = "<fontsize=16> ❤ </fontsize>"
overview_icons.tabs[12].title = "<fontsize=16> ✇ </fontsize>"

# carbon variant 
overview_carbon = overview_main.new_variant("carbon")
overview_carbon.tabs = [
    Tab(
        title = "<b> SYSTEM </b>",
        color = color_theme["white"],
        filter = all_filters["filter System System"].name,
        bracket = all_filters["filter Brackets Combat"].name,
        columns = "columns_navigation",
        columns_order = "columns_all_ordered",
    ),
    Tab(
        title = "<b> MAIN </b>",
        color = color_theme["blue"],
        filter = all_filters["filter Main System & PVX (+extra)"].name,
        bracket = all_filters["filter Brackets Combat (+drones)"].name,
        columns = "columns_combat",
        columns_order = "columns_all_ordered",
    ),
    Tab(
        title = "<b> SHIPS </b>",
        color = color_theme["orange_light"],
        filter = all_filters["filter Ships Enemy All (red+neutral)"].name,
        bracket = all_filters["filter Brackets Combat"].name,
        columns = "columns_combat",
        columns_order = "columns_all_ordered",
    ),
    Tab(
        title = "<b> NPC </b>",
        color = color_theme["orange_light"],
        filter = all_filters["filter Ships NPCs (+turrets)"].name,
        bracket = all_filters["filter Brackets Combat (-wrecks)"].name,
        columns = "columns_combat_npc",
        columns_order = "columns_all_ordered",
    ),
    Tab(
        title = "<b> DRONES </b>",
        color = color_theme["yellow"],
        filter = all_filters["filter Drones Drones and Fighters (red+neutral)"].name,
        bracket = all_filters["filter Brackets Combat (+drones)"].name,
        columns = "columns_combat",
        columns_order = "columns_all_ordered",
    ),
    Tab(
        title = "<fontsize=16> ➔ </fontsize>",
        color = color_theme["orange_dark"],
        filter = all_filters["filter Warp Warp out!"].name,
        bracket = all_filters["filter Brackets Combat"].name,
        columns = "columns_navigation",
        columns_order = "columns_all_ordered",
    ),
    Tab(
        title = "<fontsize=16> ❒ </fontsize>",
        color = color_theme["white"],
        filter = all_filters["filter Loot Loot and salvage"].name,
        bracket = all_filters["filter Brackets Combat (+drones)"].name,
        columns = "columns_combat_npc",
        columns_order = "columns_all_ordered",
    ),
    Tab(
        title = "<fontsize=16> ⌘ </fontsize>",
        color = color_theme["white"],
        filter = all_filters["filter All All"].name,
        bracket = "_BracketFilterShowAll",
        columns = "columns_combat",
        columns_order = "columns_all_ordered",
    ),
    Tab(
        title = "<fontsize=16> ❤ </fontsize>",
        color = color_theme["friendly_green"],
        filter = all_filters["filter Ships Friendly"].name,
        bracket = all_filters["filter Brackets Combat"].name,
        columns = "columns_combat",
        columns_order = "columns_all_ordered",
    )
]

# all overview variants
config = [
    overview_main,
    overview_icons,
    overview_carbon
]
