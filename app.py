import os
import shutil
from os import scandir
from tkinter.filedialog import askdirectory
import data.internal_names_and_series as info

Series = info.Series
FIGHTER_INFO = dict(info.FIGHTER_INFO)
STAGE_INFO = dict(info.STAGE_INFO)

class Character:
    def __init__(self, name: str):
        self.name = name

class Fighter(Character):
    def __init__(self, fighter_number: int, name: str, series: Series):
        self.fighter_number = fighter_number
        super().__init__(name)
        self.series = series

class Stage(Character):
    def __init__(self, name: str, series: Series):
        super().__init__(name)
        self.series = series

class Mod:
    instances = []
    def __init__(self, name: str):
        self.name = name


class FighterMod(Mod):
    def __init__(self, name: str, fighter: Fighter, slot: str, mod_type: list[str]):
        super().__init__(name)
        self.fighter = fighter
        self.slot = slot
        self.mod_type = mod_type

class StageMod(Mod):
    def __init__(self, name: str):
        super().__init__(name)

def main():

    switch_sd = ask_user_for_path('Please input the root of your SD card.')
    mods_folder = os.path.normpath(os.path.join(switch_sd, 'ultimate', 'mods'))

    skyline_plugins_folder = os.path.normpath(os.path.join(
        switch_sd, "atmosphere", "contents", "01006A800016E000", "romfs", "skyline", "plugins"
    ))

    print('Mods folder: ' + mods_folder)
    print('Skyline plugins folder: ' + skyline_plugins_folder)

    mod_tree = build_mod_tree(mods_folder)
    run_file_manager(mod_tree, mods_folder)

def ask_user_for_path(prompt):
    while True:
        print(prompt)
        result = askdirectory()
        print("Selected directory: " + result)
        mods_folder = os.path.normpath(os.path.join(result, 'ultimate', 'mods'))
        if not os.path.exists(result) or not os.path.isdir(result):
            print("Not a valid directory. Please try again.")
        elif not os.path.isdir(mods_folder):
            print('Cannot find mods folder in directory. Make sure you select the root of your SD card. '
              r'If you have no mods folder on your SD card, create SD:\ultimate\mods\'')
        else:
            return result

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

def print_mod_tree(tree, indent=0):
    for key, value in tree.items():
        if key == '_files':
            for file in value:
                print(' ' * indent + f'-{file}')
        else:
            print(' ' * indent + f'/{key}')
            print_mod_tree(value['_subdirs'], indent + 4)
            if value['_files']:
                for file in value['_files']:
                    print(' ' * (indent + 8) + file)

def run_file_manager(mod_tree, current_path):
    mods_folder = current_path
    while True:
        command = input(f"{current_path}> ").strip().split()
        if not command:
            continue
        cmd = command[0].lower()

        match cmd:
            case 'ls':
                list_contents(current_path)

            case 'cd':
                current_path = change_directory(command, current_path)

            case 'up':
                current_path = move_up_directory(current_path, mods_folder)

            case 'mkdir':
                create_directory(command, current_path)

            case 'rmdir':
                remove_directory(command, current_path)

            case 'get_modslots': #WIP
                slots = get_modslots(os.path.normpath(current_path), command[1:])
                for slot in slots:
                    print(f'''
                Mod name: {slot.name}
                Character: {slot.fighter.name}
                Fighter number: {slot.fighter.fighter_number}
                Skin slot: {slot.slot}
                Series: {str(slot.fighter.series).split('.')[-1].title()}
                Mod type: {slot.mod_type}
                    ''')
                print(slots)

            case 'help':
                display_help()

            case 'exit':
                break

            case _:
                print("Unknown command: ", cmd)

        update_mod_tree(mod_tree, current_path)

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

def get_modslots(current_path, command):
    folders = [] #stores the folder names for the match case further down
    slots = [] #what we'll return at the end
    fighter_slot = []
    for dirname in os.listdir(current_path):
        if os.path.isdir(os.path.join(current_path, dirname)):
            folders.append(dirname)

    for d1 in folders:
        for d2 in os.listdir(os.path.join(current_path, d1)):
            if os.path.isdir(os.path.join(current_path, d1, d2)):
                match d2:
                    case 'fighter':
                        # if the first subdirectory is called fighter
                        for d3 in os.listdir(os.path.join(current_path, d1, d2)):
                         # if the subdirectory of fighter exists in the keys of FIGHTER_INFO
                            if d3 in FIGHTER_INFO.keys() and os.path.isdir(os.path.join(current_path, d1, d2, d3)):
                                fighter_info = FIGHTER_INFO[d3] #store the data about the fighter from the dictionary
                                # ignore the names of these 2 subdirectories (d4 and d5, typically named model and body)
                                for d4 in os.listdir(os.path.join(current_path, d1, d2, d3)):
                                    for d5 in os.listdir(os.path.join(current_path, d1, d2, d3, d4)):
                                        for d6 in os.listdir(os.path.join(current_path, d1, d2, d3, d4, d5)):
                                            if d6.startswith('c') and os.path.isdir(os.path.join(current_path, d1, d2, d3, d4, d5, d6)) and d6[1:].isdigit():
                                                fighter = Fighter(*fighter_info)
                                                fighter_mod = FighterMod(d1, fighter, d6, ['fighter'])
                                                # if the current mod doesn't have any duplicates
                                                if not check_for_duplicates(fighter_mod, fighter_slot):
                                                    # make a new FighterMod object for each skin slot it finds
                                                    fighter_slot.append(fighter_mod)
                        slots += fighter_slot
                        fighter_slot.clear()
                    case 'ui':
                        skin = ''
                        character  = ''
                        for d3 in os.listdir(os.path.join(current_path, d1, d2)):
                            if d3.startswith('replace') and os.path.isdir(os.path.join(current_path, d1, d2, d3)):
                                for d4 in os.listdir(os.path.join(current_path, d1, d2, d3)):
                                    if d4 == 'chara' and os.path.isdir(os.path.join(current_path, d1, d2, d3, d4)):
                                        for d5 in os.listdir(os.path.join(current_path, d1, d2, d3, d4)):
                                            if d5.startswith('chara'):
                                                for d6 in os.listdir(os.path.join(current_path, d1, d2, d3, d4, d5)):
                                                    if os.path.isfile(os.path.join(current_path, d1, d2, d3, d4, d5, d6
                                                                                   )) and d6.startswith('chara_'):
                                                        file_strings = d6.split('_')
                                                        for file_string in file_strings:
                                                            if file_string in FIGHTER_INFO.keys():
                                                                character = file_string
                                                                character = FIGHTER_INFO[character]
                                                                character = Fighter(*character)
                                                            elif file_string.find('.') != -1:
                                                                file_string = file_string.split('.')
                                                                for f in file_string:
                                                                    if f.isdigit() and len(f) == 2:
                                                                        skin = f
                        if character == '' or skin == '':
                            print(f'Error! UI mod: <{d1}> does not exist. Please check inside ui folder.')
                        else:
                            ui_mod = FighterMod(d1, character, skin, ['ui'])
                            fighter_slot.append(ui_mod)
                            if not check_for_duplicates(ui_mod, fighter_slot):
                                fighter_slot.append(ui_mod)
                                slots += fighter_slot
                                fighter_slot.clear()

    return slots

def check_for_duplicates(new: FighterMod, array: list[FighterMod]) -> bool:
    mod_types = []
    for i in array:
        if new.name == i.name and new.fighter.name == i.fighter.name and new.slot == i.slot and new.mod_type == i.mod_type:
            return True
        elif new.mod_type != i.mod_type:
            mod_types += new.mod_type
            mod_types += i.mod_type
            mod_types = list(dict.fromkeys(mod_types))
            continue
        else:
            continue
    return False

def merge_mod_types(slots):
    checked_mods = []
    for slot in slots:
        if not checked_mods:
            checked_mods.append(slot)
        for mod in checked_mods:
            if slot.mod_type != mod.mod_type and slot.name == mod.name and slot.fighter.name == mod.fighter.name and slot.slot == mod.slot:
                mod.mod_type.append(slot.mod_type)




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
        return list(scandir(path))
    except FileNotFoundError:
        print(f"Directory {path} not found")
        return []

if __name__ == '__main__':
    main()