import os

temp_dir = "./temp"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

output_dir = "./output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

parts_dir = "./parts"

releases_dir = "./releases"