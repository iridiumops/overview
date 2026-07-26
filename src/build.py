# import libs
from datetime import date, datetime
from pathlib import Path
import utils
import dir_paths
from config import config


def main():
    # adds missing comments to part files with groupNames for GroupIDs
    for filter_file_path in dir_paths.parts_dir.glob("part*.yaml"):
        utils.yaml_comment(Path(filter_file_path).stem)

    print("Generating all files...")
    # build yaml file in required format for each overview variation
    for overview in config: 
        # combine yaml parts, starting with general section
        yaml_content = overview.general
        
        # filters
        for filter in overview.filters:  # warning: variable filter shadows inbuilt python function!
            filter_content = [[
                filter.name,
                [
                    ["alwaysShownStates", filter.always_shown_states],
                    ["filteredStates", filter.filtered_states],
                    ["groups", filter.groups],
                ]
            ]]
            # add filter to presets
            yaml_content["presets"].extend(filter_content)

        # ship labels
        yaml_content.update(overview.labels)
        # visual representation of states
        yaml_content.update(overview.states)

        # tab settings
        yaml_tabs = []
        for i, tab in enumerate(overview.tabs):
            # add each tab in required yaml format
            yaml_tabs.append([i, [
                ["bracket", tab.bracket],
                ["color", tab.color],
                ["name", tab.title],
                ["overview", tab.filter],
                ["tabColumnOrder", tab.columns_order],
                ["tabColumns", tab.columns]
            ]])
        yaml_content.update({"tabSetup" : yaml_tabs})

        # user settings
        yaml_content.update({"userSettings" : []})

        # save to file
        date_now = date.today().strftime("%Y%m%d")
        time_now = datetime.now().strftime("%H%M%S")
        output_name = overview.name + "_" + date_now + "_" + time_now + "-v" + overview.version.replace(".", "") + "_" + overview.variant + ".yaml"
        output_name = output_name.replace(" ", "_")
        output_path = utils.yaml_save_to_output(yaml_content, output_name)
        print(f" - saved to file: {output_path}")

    print("Done")


if __name__ == '__main__':
    main()
