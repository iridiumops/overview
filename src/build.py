# import libs
from datetime import date, datetime
from pathlib import Path
import utils
import dir_paths
from overview import config


def main():
    # optional step, adds comments to part files with groupNames for GroupIDs
    for filter_file_path in dir_paths.parts_dir.glob("part*.yaml"):
        utils.yaml_comment(Path(filter_file_path).stem)

    # build yaml file(s), one for each tab type
    print("Generating all files...")
    for tab_type, tab_data in config["tabs"].items():
        # combine yaml parts, starting with general section
        yaml_content = utils.yaml_load_part(config["general"])
        
        # filters
        for filter in config["filters"].values():
            # get states for filter
            always_shown_states = utils.yaml_load_part(filter["always_shown_states"])
            filtered_states = utils.yaml_load_part(filter["filtered_states"])
            
            # build combined GroupIDs list for filter from defined parts
            filter_groups = []
            for part_name in filter["parts"]:
                part_content = utils.yaml_load_part(part_name)
                # ensure uniqueness and consistent order
                filter_groups = sorted(list(set(filter_groups + part_content)))
            
            filter_content = [[
                filter["name"],
                [
                    ["alwaysShownStates", always_shown_states],
                    ["filteredStates", filtered_states],
                    ["groups", filter_groups],
                ]
            ]]

            # add filter to presets
            yaml_content["presets"].extend(filter_content)

        # ship labels
        yaml_content.update(utils.yaml_load_part(config["labels"]))
        # visual representation of states
        yaml_content.update(utils.yaml_load_part(config["states"]))

        # tab settings
        yaml_tabs = []
        for i, tab in enumerate(tab_data):
            # get exact filter and bracket name from their yaml files, handle ShowAll option
            if tab["bracket"] == "_BracketFilterShowAll":
                bracket_filter = "_BracketFilterShowAll"
            else:
                bracket_filter = config["filters"][tab["bracket"]]["name"]
            overview_filter = config["filters"][tab["filter"]]["name"]

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
