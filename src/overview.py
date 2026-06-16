from dataclasses import dataclass
from typing import List, Dict
from copy import copy, deepcopy
import utils


@dataclass
class Filter:
    name: str                   # filter name (allows formatting)
    always_shown_states: list   # states that will be always displayed
    filtered_states: list       # states that will be always hidden
    groups: list                # list of group ids displayed by the filter

    def __init__(
        self, 
        name: str, 
        always_shown_states: str, 
        filtered_states: str, 
        parts: List[str]
    ):
        # validation
        utils.yaml_part_exists(always_shown_states)
        utils.yaml_part_exists(filtered_states)
        for part_name in parts:
            utils.yaml_part_exists(part_name)

        # set values
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
    title: str          # tab title (allows formatting), truncated ingame to 16 characters!
    color: List[float]  # color of the tab title
    filter: str         # full overview filter name
    bracket: str        # full overview filter name that is used for brackets
    columns: list       # visible columns
    columns_order: list # column order

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
        utils.yaml_part_exists(columns)
        utils.yaml_part_exists(columns_order)
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
    name: str             # overview pack name
    variant: str          # variant name
    version: str          # version number
    general: dict         # general section (mostly legacy definitions and common default settings)
    filters: List[Filter] # Filter objects
    labels: dict          # ship and bracket label configuration
    states: dict          # visual representation for different states
    tabs: List[Tab]       # Tab objects

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
        utils.yaml_part_exists(general)
        utils.yaml_part_exists(labels)
        utils.yaml_part_exists(states)

        # assign values
        self.name = name
        self.variant = variant
        self.version = version

        self.filters = list(filters.values())
        self.tabs = tabs

        # load config sections from part files
        self.general = utils.yaml_load_part(general)
        self.labels = utils.yaml_load_part(labels)
        self.states = utils.yaml_load_part(states)

    def new_variant(self, variant_name: str):
        variant = deepcopy(self)
        variant.variant = variant_name
        return variant
