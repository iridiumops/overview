from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent

temp_dir = root_dir / "temp"
temp_dir.mkdir(parents=True, exist_ok=True)

output_dir = root_dir / "output"
output_dir.mkdir(parents=True, exist_ok=True)

parts_dir = root_dir / "parts"
parts_dir.mkdir(parents=True, exist_ok=True)

releases_dir = root_dir / "releases"
releases_dir.mkdir(parents=True, exist_ok=True)