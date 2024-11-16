from commands import *

FIGHTER_INFO = info.FIGHTER_INFO
STAGE_INFO = info.STAGE_INFO

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
                                                                        skin = 'c' + f
                                                    else:
                                                        print(f"d6 {d6} is not a file or does not start with 'chara'.")
                                            else:
                                                print(f"d5 {d5} does not start with 'chara'.")
                                    else:
                                        print(f"d4 {d4} is not named 'chara'.")
                            else:
                                print(f"d3 {d3} does not start with 'replace'.")
                        if character == '' or skin == '':
                            print(f'Error! UI mod: <{d1}> does not exist. Please check inside ui folder.')
                        else:
                            ui_mod = FighterMod(d1, character, skin, ['ui'])
                            fighter_slot.append(ui_mod)
                            if not check_for_duplicates(ui_mod, fighter_slot):
                                print(f'{d1} added.')
                                fighter_slot.append(ui_mod)
                                slots += fighter_slot
                                fighter_slot.clear()


    slots = merge_duplicates(slots)

    return slots