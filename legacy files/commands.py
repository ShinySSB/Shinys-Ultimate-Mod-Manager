import os
import shutil
from classes import *
import internal_data.internal_names_and_series as info

FIGHTER_INFO = info.FIGHTER_INFO
STAGE_INFO = info.STAGE_INFO

def build_mod_tree(path):
    tree = {}

    for root, dirs, files in os.walk(path):
        path_parts = root.split(os.sep)

        current_level = tree
        for part in path_parts:
            if part not in current_level:
                current_level[part] = {'_subdirs': {}, '_files': []}
                current_level = current_level[part]['_subdirs']

        current_level['_files'] = files
        for dirname in dirs:
            if dirname not in current_level:
                current_level[dirname] = {'_subdirs': {}, '_files': []}

    return tree

def list_contents(path):
    entries = list_directory_contents(path)
    for entry in entries:
        if entry.is_dir():
            print(f'DIR: {entry.name}')
        else:
            print(f'FILE: {entry.name}')

def change_directory(command, current_path):
    if len(command) > 1:
        args = ' '.join(command[1:])
        new_path = os.path.join(current_path, args)
        if os.path.isdir(new_path):
            return new_path
        else:
            print(f'{new_path} {args} does not exist')
    else:
        print("Usage: cd <path>")

def move_up_directory(current_path, mods_folder):
    new_path = os.path.dirname(current_path)
    if os.path.commonpath([new_path, mods_folder]) == mods_folder:
        current_path = new_path
        list_contents(current_path)
    else:
        print(f'Cannot move up. {new_path} is outside of the mods folder.')
    return current_path

def create_directory(command, current_path):
    if len(command) > 1:
        directory_name = ' '.join(command[1:])
        os.mkdir(os.path.join(current_path, directory_name))
    else:
        print("Usage: mkdir <path>")

def remove_directory(command, current_path):
    if len(command) > 1:
        directory_name = ' '.join(command[1:])
        target_path = os.path.join(current_path, directory_name)
        if os.path.isdir(target_path):
            shutil.rmtree(target_path)
        elif os.path.isfile(target_path):
            os.remove(target_path)
        else:
            print(f"{target_path} does not exist")
    else:
        print("Usage: rmdir <path>")

def check_for_duplicates(new: FighterMod, array: list[FighterMod]) -> bool:
    for i in array:
        if new.name == i.name and new.fighter.name == i.fighter.name and new.slot == i.slot and new.mod_type == i.mod_type:
            return True
        else:
            continue
    return False

def merge_duplicates(mods: list[FighterMod]) -> list[FighterMod]:
    # Dictionary to hold unique FighterMod objects by a tuple key
    unique_mods = {}

    # Helper function to create a unique key based on FighterMod attributes
    def mod_key(mod: FighterMod):
        return (mod.name, mod.fighter.name, mod.slot)

    # Iterate through the list of mods
    for mod in mods:
        key = mod_key(mod)
        if key in unique_mods:
            # Merge mod_types for duplicate entries
            unique_mods[key].mod_type = list(set(unique_mods[key].mod_type + mod.mod_type))
        else:
            # Add new mod if no duplicate found
            unique_mods[key] = mod

    # Return the list of merged FighterMod objects
    return list(unique_mods.values())

def get_fighter_directories(paths):
    result = []
    for path in paths:
        if os.path.isdir(path):
            for directory in os.listdir(path):
                if os.path.isdir(directory) and directory in FIGHTER_INFO.keys():
                    result.append(directory)
                else:
                    print(f"{directory} is not valid.")
    return result

def display_help():
    print(f'    ')
    print(f'Commands: ')
    print(f'    ls           - lists contents of current directory.')
    print(f'    cd <path>    - changes directory.')
    print(f'    up           - goes up a level in the tree hierarchy.')
    print(f'    mkdir <name> - creates directory in current directory.')
    print(f'    rmdir <name> - deletes directory in current directory.')
    print(f'    get_modslots  - WIP.')
    print(f'    exit         - exit the program.')
    print(f'    ')

def update_mod_tree(tree, path):
    new_tree = build_mod_tree(path)
    tree.clear()
    tree.update(new_tree)

def list_directory_contents(path):
    try:
        return list(os.scandir(path))
    except FileNotFoundError:
        print(f"Directory {path} not found")
        return []