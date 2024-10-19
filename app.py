import sys
from os import scandir
from tkinter.filedialog import askdirectory
import os

# Dictionary mapping internal names to (fighter number, character name)
FIGHTER_INFO = {
    'mario': ('1', 'Mario'),
    'donkey': ('2', 'Donkey Kong'),
    'link': ('3', 'Link'),
    'samus': ('4', 'Samus'),
    'samusd': ('4E', 'Dark Samus'),
    'yoshi': ('5', 'Yoshi'),
    'kirby': ('6', 'Kirby'),
    'fox': ('7', 'Fox'),
    'pikachu': ('8', 'Pikachu'),
    'luigi': ('9', 'Luigi'),
    'ness': ('10', 'Ness'),
    'captain': ('11', 'Captain Falcon'),
    'purin': ('12', 'Jigglypuff'),
    'peach': ('13', 'Peach'),
    'daisy': ('13E', 'Daisy'),
    'koopa': ('14', 'Bowser'),
    'koopag': ('14B', 'Giga Bowser'),
    'nana': ('15', 'Ice Climbers (Nana)'),
    'popo': ('15', 'Ice Climbers (Popo)'),
    'sheik': ('16', 'Sheik'),
    'zelda': ('17', 'Zelda'),
    'mariod': ('18', 'Dr. Mario'),
    'pichu': ('19', 'Pichu'),
    'falco': ('20', 'Falco'),
    'marth': ('21', 'Marth'),
    'lucina': ('21E', 'Lucina'),
    'younglink': ('22', 'Young Link'),
    'ganon': ('23', 'Ganondorf'),
    'mewtwo': ('24', 'Mewtwo'),
    'roy': ('25', 'Roy'),
    'chrom': ('25E', 'Chrom'),
    'gamewatch': ('26', 'Mr. Game & Watch'),
    'metaknight': ('27', 'Meta Knight'),
    'pit': ('28', 'Pit'),
    'pitb': ('28E', 'Dark Pit'),
    'szerosuit': ('29', 'Zero Suit Samus'),
    'wario': ('30', 'Wario'),
    'snake': ('31', 'Snake'),
    'ike': ('32', 'Ike'),
    'ptrainer': ('33T', 'Pokémon Trainer'),
    'pzenigame': ('33', 'Squirtle'),
    'pfushigisou': ('34', 'Ivysaur'),
    'plizardon': ('35', 'Charizard'),
    'diddy': ('36', 'Diddy Kong'),
    'lucas': ('37', 'Lucas'),
    'sonic': ('38', 'Sonic'),
    'dedede': ('39', 'King Dedede'),
    'pikmin': ('40', 'Olimar'),
    'lucario': ('41', 'Lucario'),
    'robot': ('42', 'R.O.B.'),
    'toonlink': ('43', 'Toon Link'),
    'wolf': ('44', 'Wolf'),
    'murabito': ('45', 'Villager'),
    'rockman': ('46', 'Mega Man'),
    'wiifit': ('47', 'Wii Fit Trainer'),
    'rosetta': ('48', 'Rosalina & Luma'),
    'littlemac': ('49', 'Little Mac'),
    'gekkouga': ('50', 'Greninja'),
    'miifighter': ('51', 'Mii Brawler'),
    'miiswordsman': ('52', 'Mii Swordfighter'),
    'miigunner': ('53', 'Mii Gunner'),
    'palutena': ('54', 'Palutena'),
    'pacman': ('55', 'Pac-Man'),
    'reflet': ('56', 'Robin'),
    'shulk': ('57', 'Shulk'),
    'koopajr': ('58', 'Bowser Jr.'),
    'duckhunt': ('59', 'Duck Hunt'),
    'ryu': ('60', 'Ryu'),
    'ken': ('60E', 'Ken'),
    'cloud': ('61', 'Cloud'),
    'kamui': ('62', 'Corrin'),
    'bayonetta': ('63', 'Bayonetta'),
    'inkling': ('64', 'Inkling'),
    'ridley': ('65', 'Ridley'),
    'simon': ('66', 'Simon'),
    'richter': ('66E', 'Richter'),
    'krool': ('67', 'King K. Rool'),
    'shizue': ('68', 'Isabelle'),
    'gaogaen': ('69', 'Incineroar'),
    'packun': ('70', 'Piranha Plant'),
    'jack': ('71', 'Joker'),
    'brave': ('72', 'Hero'),
    'buddy': ('73', 'Banjo & Kazooie'),
    'dolly': ('74', 'Terry'),
    'master': ('75', 'Byleth'),
    'tantan': ('76', 'Min Min'),
    'pickel': ('77', 'Steve'),
    'edge': ('78', 'Sephiroth'),
    'eflame': ('79', 'Pyra'),
    'element': ('79B', 'Rex'),
    'elight': ('80', 'Mythra'),
    'demon': ('81', 'Kazuya'),
    'trail': ('82', 'Sora'),
}

def main():
    switch_sd = get_directory('Please input the root of your SD card.')

    mods_folder = os.path.normpath(os.path.join(switch_sd, 'ultimate', 'mods'))

    if switch_sd and mods_folder:
        os.chdir(mods_folder)

    skyline_plugins_folder = os.path.normpath(os.path.join(switch_sd, "atmosphere", "contents", "01006A800016E000", "romfs", "skyline", "plugins"))

    ensure_directory_exists(mods_folder)
    ensure_directory_exists(skyline_plugins_folder)

    print('Mods folder: ' + mods_folder)
    print('Skyline plugins folder: ' + skyline_plugins_folder)

    parse_mods(mods_folder)

def parse_mods(mods_folder):
    for mod in os.listdir(mods_folder):
        mod_path = os.path.join(mods_folder, mod)
        if os.path.isdir(mod_path):
            parse_mod(mod, mod_path)

def parse_mod(mod, mod_path):
    for folder in os.listdir(mod_path):
        folder_path = os.path.join(mod_path, folder)

        if not os.path.isdir(folder_path):
            continue

        match folder:
            case 'fighter':
                parse_fighter_mod(folder_path)
            case 'ui':
                #print(f'{mod} affects UI.')
                continue
            case 'stage':
                print(f'{mod} affects a stage.')
            case 'effect':
                print(f'{mod} affects VFX.')
            case 'sound':
                print(f'{mod} affects sound.')
            case _:
                print(f"Error: Folder '{folder_path}' is incompatible. "
                      f"Note it is unmodifiable in this manager currently.")

def parse_fighter_mod(folder_path):
    for fighter in os.listdir(folder_path):
        fighter_path = os.path.join(folder_path, fighter)
        if fighter in FIGHTER_INFO:
            fighter_number, fighter_name = FIGHTER_INFO[fighter]
            print(f"Found fighter mod for {fighter_name} (Internal name: {fighter}, Fighter number: {fighter_number})")
            try:
                parse_skin_slots(fighter_path)
            except FileNotFoundError:
                print(f"File not found: {os.path.join(fighter_path, 'model', 'body')}")

def parse_skin_slots(fighter_path):
    model_path = os.path.join(fighter_path, 'model', 'body')
    if os.path.exists(model_path):
        for folder in os.listdir(model_path):
            if is_skin_slot(folder):
                print(f"  Slot: {folder}")
            else:
                print(f"Invalid folder: {os.path.join(model_path, folder)}")

def is_skin_slot(folder_name):
    """Checks if the folder name matches a skin slot in smash ultimate ranging from c00 to c49."""
    if folder_name.startswith('c') and len(folder_name) == 3 and folder_name[1:].isdigit():
        slot_number = int(folder_name[1:])
        return 0 <= slot_number <= 49
    else:
        print("Invalid skin slot name")
        return False

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


def list_directory_contents(path):
    try:
        return list(scandir(path))
    except FileNotFoundError:
        print(f"Directory {path} not found")
        return []

if __name__ == '__main__':
    main()
