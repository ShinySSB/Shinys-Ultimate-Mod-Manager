from tkinter.filedialog import askdirectory
from commands import *
import get_modslots

FIGHTER_INFO = dict(info.FIGHTER_INFO)
STAGE_INFO = dict(info.STAGE_INFO)

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
                slots = get_modslots.get_modslots(os.path.normpath(current_path), command[1:])
                for slot in slots:
                    print(f'''
                Mod name: {slot.name}
                Character: {slot.fighter.name}
                Fighter number: {slot.fighter.fighter_number}
                Skin slot: {slot.slot}
                Series: {str(slot.fighter.series).split('.')[-1].title()}
                Mod types: {", ".join(slot.mod_type)}
                    ''')
                print(slots)

            case 'help':
                display_help()

            case 'exit':
                break

            case _:
                print("Unknown command: ", cmd)

        update_mod_tree(mod_tree, current_path)

if __name__ == '__main__':
    main()
