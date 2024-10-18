from os import scandir
from tkinter.filedialog import askdirectory
import os

def main():
    switch_sd = get_directory('Please input the root of your SD card.')

    mods_folder = os.path.normpath(os.path.join(switch_sd, 'ultimate', 'mods'))
    skyline_plugins_folder = os.path.normpath(os.path.join(switch_sd, "atmosphere", "contents", "01006A800016E000", "romfs", "skyline", "plugins"))

    ensure_directory_exists(mods_folder)
    ensure_directory_exists(skyline_plugins_folder)

    print('Mods folder: ' + mods_folder)
    print('Skyline plugins folder: ' + skyline_plugins_folder)

    mods_list = build_mod_hierarchy(mods_folder)
    if mods_list:
        print("Mods found:")
        for mod in mods_list:
            print(mod.name)
            list(scandir(mod))
    else:
        print("No Mods found")

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Directory '" + directory + "' created")
    else:
        print("Directory '" + directory + "' already exists")

def get_directory(prompt):
    print(prompt)
    directory = askdirectory()
    print("selected directory: " + directory)
    return directory

def build_mod_hierarchy(mods_folder):
    mod_hierarchy = {}
    for root, dirs, files in os.walk(mods_folder):
        current_level = mod_hierarchy
        path_parts = root.split(os.sep)

        for part in path_parts:
            if part not in current_level:
                current_level[part] = {}
                current_level = current_level[part]

        for file in files:
            if parse_mod_filename(file):
                current_level[file] = None

    return mod_hierarchy

def parse_mod_filename(filename):
    if filename =

def list_directory_contents(path):
    try:
        return list(scandir(path))
    except FileNotFoundError:
        print(f"Directory {path} not found")
        return []

if __name__ == '__main__':
    main()