from os import scandir
from tkinter.filedialog import askdirectory
import os

def main():
    switch_sd = get_directory('Please input the root of your SD card.')
    mods_folder = os.path.normpath(os.path.join(switch_sd, 'ultimate', 'mods'))
    skyline_plugins_folder = os.path.normpath(os.path.join(switch_sd, "atmosphere", "contents", "01006A800016E000", "romfs", "skyline", "plugins"))

    print('Mods folder: ' + mods_folder)
    print('Skyline plugins folder: ' + skyline_plugins_folder)

    mods_list = list_directory_contents(mods_folder)
    if mods_list:
        print("Mods found:")
        for mod in mods_list:
            print(mod.name)
    else:
        print("No Mods found")

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