from dataclasses import dataclass
from typing import List, Dict
from copy import copy, deepcopy
import dir_paths
import utils


@dataclass
class Filter:
    name: str
    always_shown_states: list
    filtered_states: list
    groups: list

    def __init__(
        self, 
        name: str, 
        always_shown_states: str, 
        filtered_states: str, 
        parts: List[str]
    ):
        # validation
        always_shown_states_path = dir_paths.parts_dir / (always_shown_states + ".yaml")
        if not always_shown_states_path.is_file():
            raise Exception("overview filter always_shown_states must be valid yaml file in the parts directory")
        
        filtered_states_path = dir_paths.parts_dir / (filtered_states + ".yaml")
        if not filtered_states_path.is_file():
            raise Exception("overview filter filtered_states must be valid yaml file in the parts directory")
        
        for part_name in parts:
            part_file_path = dir_paths.parts_dir / (part_name + ".yaml")
            if not part_file_path.is_file():
                raise Exception("overview filter part must be valid yaml file in the parts directory")

        self.name = name

        # load states from specified parts
        self.always_shown_states = list(utils.yaml_load_part(always_shown_states))
        self.filtered_states = list(utils.yaml_load_part(filtered_states))

        # build combined list of GroupIDs from declared parts
        self.groups = []
        for part_name in parts:
            part_content = utils.yaml_load_part(part_name)
            # ensure uniqueness and consistent order
            self.groups = sorted(list(set(self.groups + part_content)))


@dataclass
class Tab:
    title: str
    color: List[float]
    filter: str
    bracket: str
    columns: list
    columns_order: list

    def __init__(
        self, 
        title: str, 
        color: List[float], 
        filter: str, 
        bracket: str, 
        columns: str, 
        columns_order: str
    ):
        # validation
        columns_path = dir_paths.parts_dir / (columns + ".yaml")
        if not columns_path.is_file():
            raise Exception("overview filter always_shown_states must be valid yaml file in the parts directory")
        
        columns_order_path = dir_paths.parts_dir / (columns_order + ".yaml")
        if not columns_order_path.is_file():
            raise Exception("overview filter filtered_states must be valid yaml file in the parts directory")

        if len(color) != 3:
            raise Exception("overview tab color must be a list with exactly 3 float values")
        for c in color:
            if c<0 or c>1:
                raise Exception("overview tab color must be a float between 0 and 1")
        
        # init simple values
        self.title = title
        self.color = copy(color)
        self.filter = filter
        self.bracket = bracket

        # load column config from part files
        self.columns = list(utils.yaml_load_part(columns))
        self.columns_order = list(utils.yaml_load_part(columns_order))


@dataclass
class Overview:
    name: str
    variant: str
    version: str
    general: dict # general section (mostly legacy definitions and common default settings)
    filters: List[Filter]
    labels: dict # ship and bracket label configuration
    states: dict # visual representation for different states
    tabs: List[Tab]

    def __init__(
        self, 
        name: str, 
        variant: str, 
        version: str, 
        general: str, 
        filters: Dict[str, Filter], 
        labels: str, 
        states: str,
        tabs: List[Tab]
    ):
        # validate
        general_path = dir_paths.parts_dir / (general + ".yaml")
        if not general_path.is_file():
            raise Exception("general must be valid yaml file in the parts directory")
        
        labels_path = dir_paths.parts_dir / (labels + ".yaml")
        if not labels_path.is_file():
            raise Exception("genlabelseral must be valid yaml file in the parts directory")
        
        states_path = dir_paths.parts_dir / (states + ".yaml")
        if not states_path.is_file():
            raise Exception("states must be valid yaml file in the parts directory")

        # assign values
        self.name = name
        self.variant = variant
        self.version = version

        self.filters = list(filters.values())
        self.tabs = tabs

        # load config from parts
        self.general = utils.yaml_load_part(general)
        self.labels = utils.yaml_load_part(labels)
        self.states = utils.yaml_load_part(states)


# all filter definitions and their modular sub-parts
all_filters = {
    "filter Brackets Combat": Filter(
        name = '<color=0xFFCCCCCC>/ Brackets: Combat</color>',
        always_shown_states = "states none",
        filtered_states = "states none",
        parts = [
            "part ships", 
            "part wrecks", 
            "part npcs", 
            "part brackets"
        ]
    ),
    "filter Brackets Combat (+drones)": Filter(
        name = '<color=0xFFCCCCCC>/ Brackets: Combat (+drones)</color>',
        always_shown_states = "states none",
        filtered_states = "states none",
        parts = [
            "part ships", 
            "part drones", 
            "part fighters", 
            "part wrecks", 
            "part npcs", 
            "part brackets"
        ]
    ),
    "filter Brackets Combat (-wrecks)": Filter(
        name = '<color=0xFFCCCCCC>/ Brackets: Combat (-wrecks)</color>',
        always_shown_states = "states none",
        filtered_states = "states none",
        parts = [
            "part ships", 
            "part npcs", 
            "part brackets"
        ]
    ),
    "filter DSCAN Ships": Filter(
        name = '<color=0xFFCCCCCC>? DSCAN: Ships</color>',
        always_shown_states = "states none",
        filtered_states = "states blue",
        parts = [
            "part ships", 
            "part capsule"
        ]
    ),
    "filter DSCAN Basic": Filter(
        name = '<color=0xFFCCCCCC>? DSCAN: Basic</color>',
        always_shown_states = "states none",
        filtered_states = "states blue",
        parts = [
            "part dscan basic", 
            "part ships", 
            "part capsule"
        ]
    ),
    "filter DSCAN Extra": Filter(
        name = '<color=0xFFCCCCCC>? DSCAN: Extra</color>',
        always_shown_states = "states none",
        filtered_states = "states blue",
        parts = [
            "part dscan extra", 
            "part dscan basic", 
            "part ships", 
            "part capsule"
        ]
    ),
    "filter All All": Filter(
        name = '<color=0xFFCCCCCC>⌘ All: All</color>',
        always_shown_states = "states none",
        filtered_states = "states none",
        parts = [
            "part all"
        ]
    ),
    "filter System System": Filter(
        name = '<color=0xFFFFFFFF>✪ System: System</color>',
        always_shown_states = "states none",
        filtered_states = "states none",
        parts = [
            "part system", 
            "part structures", 
            "part citadels"
        ]
    ),
    "filter System System (-citadels)": Filter(
        name = '<color=0xFFFFFFFF>✪ System: System (-citadels)</color>',
        always_shown_states = "states none",
        filtered_states = "states none",
        parts = [
            "part system"
        ]
    ),
    "filter System System (+belts)": Filter(
        name = '<color=0xFFFFFFFF>✪ System: System (+belts)</color>',
        always_shown_states = "states none",
        filtered_states = "states none",
        parts = [
            "part system", 
            "part structures", 
            "part citadels", 
            "part belts"
        ]
    ),
    "filter System Mining": Filter(
        name = '<color=0xFFFFFFFF>✪ System: Mining</color>',
        always_shown_states = "states none",
        filtered_states = "states blue",
        parts = [
            "part belts", 
            "part mining"
        ]
    ),
    "filter System Beacons": Filter(
        name = '<color=0xFFFFFFFF>✪ System: Beacons</color>',
        always_shown_states = "states none",
        filtered_states = "states none",
        parts = [
            "part beacons"
        ]
    ),
    "filter Warp Warp out!": Filter(
        name = '<color=0xFFFF5500>➔ Warp: Warp out!</color>',
        always_shown_states = "states none",
        filtered_states = "states none",
        parts = [
            "part warp"
        ]
    ),
    "filter Warp Travel (-citadels)": Filter(
        name = '<color=0xFFFF5500>➔ Warp: Travel (-citadels)</color>',
        always_shown_states = "states none",
        filtered_states = "states blue ally militia agent",
        parts = [
            "part travel"
        ]
    ),
    "filter Warp Travel": Filter(
        name = '<color=0xFFFF5500>➔ Warp: Travel</color>',
        always_shown_states = "states none",
        filtered_states = "states blue ally militia agent",
        parts = [
            "part citadels", 
            "part travel"
        ]
    ),
    "filter Loot Loot and salvage": Filter(
        name = '<color=0xFFCCCCCC>❒ Loot: Loot and salvage</color>',
        always_shown_states = "states none",
        filtered_states = "states none",
        parts = [
            "part loot"
        ]
    ),
    "filter Drones Drones and Fighters (all)": Filter(
        name = '<color=0xFFFFEE00>✜ Drones: Drones and Fighters (all)</color>',
        always_shown_states = "states none",
        filtered_states = "states none",
        parts = [
            "part drones", 
            "part fighters"
        ]
    ),
    "filter Drones Drones and Fighters (red+neutral)": Filter(
        name = '<color=0xFFFFEE00>✜ Drones: Drones and Fighters (red+neutral)</color>',
        always_shown_states = "states none",
        filtered_states = "states blue",
        parts = [
            "part drones", 
            "part fighters"
        ]
    ),
    "filter Drones Fighters (red+neutral)": Filter(
        name = '<color=0xFFFFEE00>✜ Drones: Fighters (red+neutral)</color>',
        always_shown_states = "states none",
        filtered_states = "states blue",
        parts = [
            "part fighters"
        ]
    ),
    "filter Ships NPCs (+turrets)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: NPCs (+turrets)</color>',
        always_shown_states = "states none",
        filtered_states = "states blue",
        parts = [
            "part npcs", 
            "part police", 
            "part turrets"
        ]
    ),
    "filter Ships Friendly": Filter(
        name = '<color=0xFF199919>❖ Ships: Friendly</color>',
        always_shown_states = "states blue ally militia",
        filtered_states = "states not blue ally militia",
        parts = [
            "part ships", 
            "part capsule"
        ]
    ),
    "filter Ships Fleet": Filter(
        name = '<color=0xFFEE22EE>❖ Ships: Fleet</color>',
        always_shown_states = "states fleet",
        filtered_states = "states not fleet",
        parts = [
            "part ships", 
            "part capsule"
        ]
    ),
    "filter Ships Enemy All (red)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy All (red)</color>',
        always_shown_states = "states none",
        filtered_states = "states not red war engagement",
        parts = [
            "part ships", 
            "part capsule"
        ]
    ),
    "filter Ships Enemy All (red -capsules)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy All (red -capsules)</color>',
        always_shown_states = "states none",
        filtered_states = "states not red war engagement",
        parts = [
            "part ships"
        ]
    ),
    "filter Ships Enemy All (red+neutral)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy All (red+neutral)</color>',
        always_shown_states = "states none",
        filtered_states = "states blue agent",
        parts = [
            "part ships", 
            "part capsule"
        ]
    ),
    "filter Ships Enemy All (red+neutral -capsules)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy All (red+neutral -capsules)</color>',
        always_shown_states = "states none",
        filtered_states = "states blue agent",
        parts = [
            "part ships"
        ]
    ),
    "filter Ships Enemy All (war targets)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy All (war targets)</color>',
        always_shown_states = "states war",
        filtered_states = "states not war",
        parts = [
            "part ships", 
            "part capsule"
        ]
    ),
    "filter Ships Enemy All (hisec criminals)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy All (hisec criminals)</color>',
        always_shown_states = "states war criminal",
        filtered_states = "states not war criminal",
        parts = [
            "part ships", 
            "part capsule"
        ]
    ),
    "filter Ships Enemy Logi (red+neutral)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy Logi (red+neutral)</color>',
        always_shown_states = "states none",
        filtered_states = "states blue agent",
            parts = [
            "part ships logi"
        ]
    ),
    "filter Ships Enemy Utility (red+neutral)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy Utility (red+neutral)</color>',
        always_shown_states = "states none",
        filtered_states = "states blue agent",
        parts = [
            "part ships utility"
        ]
    ),
    "filter Ships Enemy Capitals (red+neutral)": Filter(
        name = '<color=0xFFFF9900>❖ Ships: Enemy Capitals (red+neutral)</color>',
        always_shown_states = "states none",
        filtered_states = "states blue agent",
        parts = [
            "part ships capitals"
        ]
    ),
    "filter Main PVX (+friendly +extra)": Filter(
        name = '<color=0xFF14B0D2>✱ Main: PVX (+friendly +extra)</color>',
        always_shown_states = "states none",
        filtered_states = "states empty-wreck",
        parts = [
            "part npcs", 
            "part main pvx", 
            "part main extra", 
            "part capsule", 
            "part ships"
        ]
    ),
    "filter Main PVX (+extra)": Filter(
        name = '<color=0xFF14B0D2>✱ Main: PVX (+extra)</color>',
        always_shown_states = "states none",
        filtered_states = "states blue empty-wreck",
        parts = [
            "part npcs", 
            "part main pvx", 
            "part main extra", 
            "part capsule", 
            "part ships"
        ]
    ),
    "filter Main PVX": Filter(
        name = '<color=0xFF14B0D2>✱ Main: PVX</color>',
        always_shown_states = "states none",
        filtered_states = "states blue",
        parts = [
            "part npcs", 
            "part main pvx", 
            "part capsule", 
            "part ships"
        ]
    ),
    "filter Main PVX (-npc)": Filter(
        name = '<color=0xFF14B0D2>✱ Main: PVX (-npc)</color>',
        always_shown_states = "states none",
        filtered_states = "states blue agent",
        parts = [
            "part main pvx", 
            "part capsule", 
            "part ships"
        ]
    ),
    "filter Main PVX (+mining)": Filter(
        name = '<color=0xFF14B0D2>✱ Main: PVX (+mining)</color>',
        always_shown_states = "states none",
        filtered_states = "states blue",
        parts = [
            "part npcs", 
            "part main pvx", 
            "part capsule", 
            "part ships", 
            "part mining"
        ]
    ),
    "filter Main System & PVX (+extra)": Filter(
        name = '<color=0xFF88DDEE>✕ Main: <color=0xFFFFFFFF>System</color> & <color=0xFF14B0D2>PVX (+extra)</color></color>',
        always_shown_states = "states none",
        filtered_states = "states blue empty-wreck",
        parts = [
            "part npcs", 
            "part main pvx", 
            "part main extra", 
            "part capsule", 
            "part ships", 
            "part structures", 
            "part citadels", 
            "part system"
        ]
    ),
    "filter Main System & PVX (-npc)": Filter(
        name = '<color=0xFF88DDEE>✕ Main: <color=0xFFFFFFFF>System</color> & <color=0xFF14B0D2>PVX (-npc)</color></color>',
        always_shown_states = "states none",
        filtered_states = "states blue empty-wreck",
        parts = [
            "part main pvx", 
            "part capsule", 
            "part ships", 
            "part structures", 
            "part citadels", 
            "part system"
        ]
    )
}

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

# define main overview variation
overview_main = Overview(
    name = "iridium overview",
    variant = "main",
    version = "3.10.1",
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
            columns = "columns navigation",
            columns_order = "columns all ordered",
        ),
        Tab(
            title = "<b> PVE </b>",
            color = color_theme["blue"],
            filter = all_filters["filter Main PVX (+friendly +extra)"].name,
            bracket = all_filters["filter Brackets Combat (+drones)"].name,
            columns = "columns combat",
            columns_order = "columns all ordered",
        ),
        Tab(
            title = "<b> PVP </b>",
            color = color_theme["red"],
            filter = all_filters["filter Main PVX"].name,
            bracket = all_filters["filter Brackets Combat"].name,
            columns = "columns combat",
            columns_order = "columns all ordered",
        ),
        Tab(
            title = "<b> SHIPS </b>",
            color = color_theme["orange_light"],
            filter = all_filters["filter Ships Enemy All (red+neutral)"].name,
            bracket = all_filters["filter Brackets Combat"].name,
            columns = "columns combat",
            columns_order = "columns all ordered",
        ),
        Tab(
            title = "<b> CAPS </b>",
            color = color_theme["orange_light"],
            filter = all_filters["filter Ships Enemy Capitals (red+neutral)"].name,
            bracket = all_filters["filter Brackets Combat"].name,
            columns = "columns combat",
            columns_order = "columns all ordered",
        ),
        Tab(
            title = "<b> NPC </b>",
            color = color_theme["orange_light"],
            filter = all_filters["filter Ships NPCs (+turrets)"].name,
            bracket = all_filters["filter Brackets Combat (-wrecks)"].name,
            columns = "columns combat npc",
            columns_order = "columns all ordered",
        ),
        Tab(
            title = "<b> DRONES </b>",
            color = color_theme["yellow"],
            filter = all_filters["filter Drones Drones and Fighters (red+neutral)"].name,
            bracket = all_filters["filter Brackets Combat (+drones)"].name,
            columns = "columns combat",
            columns_order = "columns all ordered",
        ),
        Tab(
            title = "<b> WARP </b>",
            color = color_theme["orange_dark"],
            filter = all_filters["filter Warp Warp out!"].name,
            bracket = all_filters["filter Brackets Combat"].name,
            columns = "columns navigation",
            columns_order = "columns all ordered",
        ),
        Tab(
            title = "<b> LOOT </b>",
            color = color_theme["white"],
            filter = all_filters["filter Loot Loot and salvage"].name,
            bracket = all_filters["filter Brackets Combat (+drones)"].name,
            columns = "columns combat npc",
            columns_order = "columns all ordered",
        ),
        Tab(
            title = "<b> ALL </b>",
            color = color_theme["white"],
            filter = all_filters["filter All All"].name,
            bracket = "_BracketFilterShowAll",
            columns = "columns combat",
            columns_order = "columns all ordered",
        ),
        Tab(
            title = "<b> FLEET </b>",
            color = color_theme["fleet_purple"],
            filter = all_filters["filter Ships Fleet"].name,
            bracket = all_filters["filter Brackets Combat"].name,
            columns = "columns combat",
            columns_order = "columns all ordered",
        ),
        Tab(
            title = "<b>FRIENDLY</b>",
            color = color_theme["friendly_green"],
            filter = all_filters["filter Ships Friendly"].name,
            bracket = all_filters["filter Brackets Combat"].name,
            columns = "columns combat",
            columns_order = "columns all ordered",
        ),
        Tab(
            title = "<b> MINING </b>",
            color = color_theme["white"],
            filter = all_filters["filter System Mining"].name,
            bracket = all_filters["filter Brackets Combat (+drones)"].name,
            columns = "columns navigation",
            columns_order = "columns all ordered",
        )
    ]
)

# tab icons variation
overview_icons = deepcopy(overview_main)
overview_icons.variant = "icons"
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

# carbon variation 
overview_carbon = deepcopy(overview_main)
overview_carbon.variant = "carbon"
overview_icons.tabs = [
    Tab(
        title = "<b> SYSTEM </b>",
        color = color_theme["white"],
        filter = all_filters["filter System System"].name,
        bracket = all_filters["filter Brackets Combat"].name,
        columns = "columns navigation",
        columns_order = "columns all ordered",
    ),
    Tab(
        title = "<b> MAIN </b>",
        color = color_theme["blue"],
        filter = all_filters["filter Main System & PVX (+extra)"].name,
        bracket = all_filters["filter Brackets Combat (+drones)"].name,
        columns = "columns combat",
        columns_order = "columns all ordered",
    ),
    Tab(
        title = "<b> SHIPS </b>",
        color = color_theme["orange_light"],
        filter = all_filters["filter Ships Enemy All (red+neutral)"].name,
        bracket = all_filters["filter Brackets Combat"].name,
        columns = "columns combat",
        columns_order = "columns all ordered",
    ),
    Tab(
        title = "<b> NPC </b>",
        color = color_theme["orange_light"],
        filter = all_filters["filter Ships NPCs (+turrets)"].name,
        bracket = all_filters["filter Brackets Combat (-wrecks)"].name,
        columns = "columns combat npc",
        columns_order = "columns all ordered",
    ),
    Tab(
        title = "<b> DRONES </b>",
        color = color_theme["yellow"],
        filter = all_filters["filter Drones Drones and Fighters (red+neutral)"].name,
        bracket = all_filters["filter Brackets Combat (+drones)"].name,
        columns = "columns combat",
        columns_order = "columns all ordered",
    ),
    Tab(
        title = "<fontsize=16> ➔ </fontsize>",
        color = color_theme["orange_dark"],
        filter = all_filters["filter Warp Warp out!"].name,
        bracket = all_filters["filter Brackets Combat"].name,
        columns = "columns navigation",
        columns_order = "columns all ordered",
    ),
    Tab(
        title = "<fontsize=16> ❒ </fontsize>",
        color = color_theme["white"],
        filter = all_filters["filter Loot Loot and salvage"].name,
        bracket = all_filters["filter Brackets Combat (+drones)"].name,
        columns = "columns combat npc",
        columns_order = "columns all ordered",
    ),
    Tab(
        title = "<fontsize=16> ⌘ </fontsize>",
        color = color_theme["white"],
        filter = all_filters["filter All All"].name,
        bracket = "_BracketFilterShowAll",
        columns = "columns combat",
        columns_order = "columns all ordered",
    ),
    Tab(
        title = "<fontsize=16> ❤ </fontsize>",
        color = color_theme["friendly_green"],
        filter = all_filters["filter Ships Friendly"].name,
        bracket = all_filters["filter Brackets Combat"].name,
        columns = "columns combat",
        columns_order = "columns all ordered",
    )
]

# all overview variations
config = [
    overview_main,
    overview_icons,
    overview_carbon
]
