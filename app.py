import shutil
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

STAGE_INFO = {
    '75m': '75 m',
    'animal_city': 'Town and City',
    'animal_island': 'Tortimer Island',
    'animal_village': 'Smashville',
    'balloonfight': 'Balloon Fight',
    'battlefield': 'Battlefield',
    'battlefield_l': 'Big Battlefield',
    'battlefield_s': 'Small Battlefield',
    'bayo_clock': 'Umbra Clock Tower',
    'brave_altar': "Yggdrasil's altar",
    'buddy_spiral': 'Spiral Mountain',
    'demon_dojo': 'Mishima Dojo',
    'dk_jungle': 'Kongo Jungle',
    'dk_lodge': 'Jungle Japes',
    'dk_waterfall': 'Kongo Falls',
    'dolly_stadium': 'King of Fighters Stadium',
    'dracula_castle': "Dracula's Castle",
    'duckhunt': 'Duck Hunt',
    'end': 'Final Destination',
    'fe_arena': 'Arena Ferox',
    'fe_colloseum': 'Coliseum',
    'fe_shrine': 'Garreg Mach Monastery',
    'fe_siege': 'Castle Siege',
    'ff_cave': 'Northern Cave',
    'ff_midgar': 'Midgar',
    'flatzonex': 'Flat Zone X',
    'fox_corneria': 'Corneria',
    'fox_lylatcruise': 'Lylat Cruise',
    'fox_venom': 'Venom',
    'fzero_bigblue': 'Big Blue',
    'fzero_mutecity3ds': 'Mute City SNES', #What the actual fuck nintendo
    'fzero_porttown': 'Port Town Aero Drive',
    'homeruncontest': ''
}

def main():

    switch_sd = ''
    while not os.path.exists(switch_sd):
        print('Please input the root of your SD card.')
        switch_sd = askdirectory()
        print("Selected directory: " + switch_sd)
        if os.path.exists(switch_sd) and os.path.isdir(switch_sd):
            break
        else:
            continue

    mods_folder = os.path.normpath(os.path.join(switch_sd, 'ultimate', 'mods'))
    if not os.path.isdir(mods_folder):
        print('Cannot find mods folder in directory. Make sure you select the root of your SD card. '
              r'If you have no mods folder on your SD card, create SD:\ultimate\mods\'')


    skyline_plugins_folder = os.path.normpath(os.path.join(switch_sd, "atmosphere", "contents", "01006A800016E000", "romfs", "skyline", "plugins"))

    print('Mods folder: ' + mods_folder)
    print('Skyline plugins folder: ' + skyline_plugins_folder)

    mod_tree = build_mod_tree(mods_folder)
    print_mod_tree(mod_tree)
    run_file_manager(mod_tree, mods_folder)

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
    while True:
        command = input(f"{current_path}> ").strip().split()
        if not command:
            continue
        cmd = command[0].lower()
        if cmd == 'ls':
            list_contents(current_path)
        elif cmd == 'cd':
            if len(command) > 1:
                args = ' '.join(command[1:])
                new_path = os.path.join(current_path, args)
                if os.path.isdir(new_path):
                    current_path = new_path
                else:
                    print(f'{current_path} {args} does not exist')
            else:
                print("Usage: cd <path>")
        elif cmd == 'mkdir':
            if len(command) > 1:
                os.mkdir(os.path.join(current_path, command[1]))
            else:
                print("Usage: mkdir <path>")
        elif cmd == 'rmdir':
            if len(command) > 1:
                target_path = os.path.join(current_path, command[1])
                if os.path.isdir(target_path):
                    shutil.rmtree(target_path)
                elif os.path.isfile(target_path):
                    os.remove(target_path)
                else:
                    print(f"{target_path} does not exist")
            else:
                print("Usage: rmdir <path>")
        elif cmd == 'exit':
            break
        else:
            print("Unknown command: ", cmd)
        update_mod_tree(mod_tree, current_path)

def list_contents(path):
    entries = list_directory_contents(path)
    for entry in entries:
        if entry.is_dir():
            print(f'DIR: {entry.name}')
        else:
            print(f'FILE: {entry.name}')

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
