from os import scandir
from tkinter.filedialog import askdirectory
import os

def main():
    switch_sd = get_directory('Please input the root of your SD card.')

    switch_sd = switch_sd.rstrip("/\\")

    mods_folder = os.path.normpath(os.path.join(switch_sd, 'ultimate', 'mods'))
    skyline_plugins_folder = os.path.normpath(os.path.join(switch_sd, "atmosphere", "contents", "01006A800016E000", "romfs", "skyline", "plugins"))

    ensure_directory_exists(mods_folder)
    ensure_directory_exists(skyline_plugins_folder)

    print('Mods folder: ' + mods_folder)
    print('Skyline plugins folder: ' + skyline_plugins_folder)

    mods_list = list_directory_contents(mods_folder)
    if mods_list:
        print("Mods found:")
        for mod in mods_list:
            print(mod.name)
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

def list_directory_contents(path):
    try:
        return list(scandir(path))
    except FileNotFoundError:
        print(f"Directory {path} not found")
        return []

if __name__ == '__main__':
    main()