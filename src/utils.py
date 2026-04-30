import os, yaml, re, shutil
from api import api_get_group
from dir_paths import *


def yaml_load_part(file_name):
    """
    Load content of yaml file that is located in parts directory

    :param file_name: file name
    """
    part_file_path = parts_dir / (file_name + ".yaml")
    with open(part_file_path, 'r', encoding="utf8") as part_file:
        return yaml.safe_load(part_file)
    

def yaml_comment(name):
    """
    Add groupName (descriptive string name) as yaml comment for each groupID number

    :param name: file name part
    """
    part_file_path = parts_dir / (name + ".yaml")
    part_file_path_temp = temp_dir / (name + ".yaml")

    # append group names for IDs, write to temp file
    with open(part_file_path, 'r', encoding="utf8") as in_file, open(part_file_path_temp, 'w', encoding="utf8") as out_file:
        for line in in_file:
            match_id = re.search(r'- (\d+)', line)
            match_comment = re.search(r' # ', line)
            if match_id and not match_comment:
                group_id = int(match_id.group(1))

                # fetch group name from api
                group = api_get_group(group_id)

                if group:
                    line = line.rstrip() + ' # ' + group["name"] + '\n'

            out_file.write(line)

    # replace old file
    os.remove(part_file_path)
    shutil.move(part_file_path_temp, part_file_path)


def yaml_get_all_unique_group_ids(yaml_path):
    """Extract all unique group IDs from a YAML file."""

    if not yaml_path.is_file():
        print(f"Error: File not found: {yaml_path}")
        return set()

    group_ids = set()
    try:
        with open(yaml_path, 'r', encoding='utf8') as f:
            yaml_data = yaml.safe_load(f)
        
        # Traverse YAML, find group IDs from yaml_data['presets'][filter][2][1]
        if 'presets' in yaml_data:
            for preset_def in yaml_data['presets']:
                group_ids.update(preset_def[1][2][1])
    except Exception as e:
        print(f"Error parsing YAML: {e}")
    
    return group_ids


def yaml_save_to_output(yaml_content, output_name):
    output_path = output_dir / output_name
    try:
        with open(output_path, 'w', encoding="utf8") as outfile:
            yaml.safe_dump(yaml_content, outfile, sort_keys=False, encoding="utf8", allow_unicode=True)
            return output_path
    except Exception as e:
        print(f"Error saving YAML file: {output_path} {e}")
    
    return None    


def yaml_save_to_temp(data, filename):
    temp_path = temp_dir / filename
    try:
        with open(temp_path, 'w', encoding='utf8') as f:
            yaml.safe_dump(data, f, sort_keys=False, encoding='utf8', allow_unicode=True)
            return temp_path
    except Exception as e:
        print(f"Error saving YAML file: {temp_path} {e}")
    
    return None