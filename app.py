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

    parse_mods(mods_folder)

def parse_mods(mods):
    for mod in os.listdir(mods):
        mod_path = os.path.join(mods, mod)
        if os.path.isdir(mod_path):
            for folder in os.listdir(mod_path):
                if not os.path.isdir(os.path.join(mod_path, folder)):
                    continue

                match folder:
                    case 'fighter':
                        print(f'{mod} affects a fighter.')
                    case 'ui':
                        print(f'{mod} affects UI.')
                    case 'stage':
                        print(f'{mod} affects a stage.')
                    case 'effect':
                        print(f'{mod} affects vfx.')
                    case 'sound':
                        print(f'{mod} affects sound.')
                    case _:
                        print(f"Error: Folder '{os.path.join(mod_path, folder)}' is incompatible. "
                              "Note it is unmodifiable in this manager currently.")

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Directory '" + directory + "' created")
    else:
        print("Directory '" + directory + "' already exists")

def get_directory(prompt):
    print(prompt)
    directory = askdirectory()
    print("Selected directory: " + directory)
    return directory

def is_skin_slot(folder_name):
    """Checks if the folder name matches a skin slot in smash ultimate."""
    if folder_name.startswith('c') and len(folder_name) > 1 and folder_name[1:].isdigit():
        # Convert to integer to check the range
        slot_number = int(folder_name[1:])
        return 0 <= slot_number <= 50
    return False

def list_directory_contents(path):
    try:
        return list(scandir(path))
    except FileNotFoundError:
        print(f"Directory {path} not found")
        return []

if __name__ == '__main__':
    main()