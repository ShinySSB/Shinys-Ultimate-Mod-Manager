import shutil
import sys
from os import scandir
import os
from tkinter.filedialog import askdirectory

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
    'ptrainer_low': ('33T', 'Pokémon Trainer (Low)'),
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
    #'common': '',
    #'miienemyf': '',
    #'miienemyg': '',
    #'miienemys': '',
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
    #'bonusgame': '',
    'bossstage_dracula': "Dracula's Boss Stage",
    #'bossstage_final1': '',
    #'bossstage_final2': '',
    #'bossstage_final3': '',
    'bossstage_galleom': "Galleom's Boss Stage",
    'bossstage_ganonboss': "Ganon's Boss Stage",
    'bossstage_marx': "Marx's Boss Stage",
    'bossstage_rathalos': "Rathalos' Boss Stage",
    'brave_altar': "Yggdrasil's altar",
    'buddy_spiral': 'Spiral Mountain',
    'campaignmap': 'The Map of World of Light',
    #'common': '',
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
    'homeruncontest': 'Home-Run Contest',
    'icarus_angeland': "Palutena's Temple",
    'icarus_skyworld': 'Skyworld',
    'icarus_uprising': 'Reset Bomb Forest',
    'ice_top': 'Summit',
    'jack_mementoes': 'Mementos',
    'kart_circuitfor': 'Mario Circuit',
    'kart_circuitx': 'Figure-8 Circuit',
    'kirby_cave': 'The Great Cave Offensive',
    'kirby_fountain': 'Fountain of Dreams',
    'kirby_gameboy': 'Dream Land GB',
    'kirby_greens': 'Green Greens',
    'kirby_halberd': 'Halberd',
    'kirby_pupupu64': 'Dream Land',
    'luigimansion': "Luigi's Mansion",
    'mario_3dland': '3D Land',
    'mario_castle64': "Peach's Castle",
    'mario_castledx': "Princess Peach's Castle",
    'mario_dolpic': 'Delfino Plaza',
    'mario_galaxy': 'Mario Galaxy',
    'mario_newbros2': 'Golden Plains',
    'mario_odyssey': 'New Donk City Hall',
    'mario_paper': 'Paper Mario',
    'mario_past64': 'Mushroom Kingdom',
    'mario_pastusa': 'Mushroom Kingdom II',
    'mario_pastx': 'Mushroomy Kingdom',
    'mario_rainbow': 'Rainbow Cruise',
    'mario_uworld': 'Mushroom Kingdom U',
    'mariobros': 'Mario Bros.',
    'metroid_kraid': 'Brinstar Depths',
    'metroid_norfair': 'Norfair',
    'metroid_orpheon': 'Frigate Orpheon',
    'metroid_zebesdx': 'Brinstar',
    'mg_shadowmoses': 'Shadow Moses Island',
    'mother_fourside': 'Fourside',
    'mother_magicant': 'Magicant',
    'mother_newpork': 'New Pork City',
    'mother_onett': 'Onett',
    'nintendogs': 'Living Room',
    'pac_land': 'PAC-LAND',
    'photostage': 'Mii Photo Stage',
    'pickel_world': 'Minecraft World',
    'pictochat2': 'PictoChat 2',
    'pikmin_garden': 'Garden of Hope',
    'pikmin_planet': 'Distant Planet',
    'pilotwings': 'Pilotwings',
    'plankton': 'Hanenbow',
    'poke_kalos': 'Kalos Pokémon League',
    'poke_stadium': 'Pokémon Stadium',
    'poke_stadium2': 'Pokémon Stadium 2',
    'poke_tengam': 'Spear Tower',
    'poke_tower': 'Prism Tower',
    'poke_unova': 'Unova Pokémon League',
    'poke_yamabuki': 'Saffron City',
    'punchoutsb': 'Boxing Ring',
    #'punchoutw': '',
    'resultstage': 'Results Stage',
    'resultstage_edge': "Sephiroth's Results Stage",
    'resultstage_jack': "Joker's Results Stage",
    'rock_wily': 'Wily Castle',
    'settingstage': 'Controller Setting Stage',
    'sf_suzaku': 'Suzaku Castle',
    #'shamfight': '',
    'sonic_greenhill': 'Green Hill Zone',
    'sonic_windyhill': 'Windy Hill Zone',
    #'sp_edit': '',
    #'spiritsroulette': '',
    'spla_parking': 'Moray Towers',
    #'staffroll': '',
    'streetpass': 'Find Mii',
    'tantan_spring': 'Spring Stadium',
    'tomodachi': 'Tomodachi Life',
    'trail_castle': 'Hollow Bastion',
    'training': 'Training Mode Stage',
    'wario_gamer': 'Gamer',
    'wario_madein': 'WarioWare, Inc.',
    'wiifit': 'Wii Fit Studio',
    'wreckingcrew': 'Wrecking Crew',
    'wufuisland': 'Wuhu Island',
    'xeno_alst': 'Cloud Sea of Alrest',
    'xeno_gaur': 'Gaur Plain',
    'yoshi_cartboard': "Yoshi's Story",
    'yoshi_island': "Yoshi's Island",
    'yoshi_story': 'Super Happy Tree',
    'yoshi_yoster': "Yoshi's Island (Melee)",
    'zelda_gerudo': 'Gerudo Valley',
    'zelda_greatbay': 'Great Bay',
    'zelda_hyrule': "Hyrule Castle",
    'zelda_oldin': "Bridge of Eldin",
    'zelda_pirates': 'Pirate Ship',
    'zelda_skyward': 'Skyloft',
    'zelda_temple': 'Temple',
    'zelda_tower': 'Great Plateau Tower',
    'zelda_train': 'Spirit Train',
}

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
    result = ""
    while True:
        print(prompt)
        result = askdirectory()
        print("Selected directory: " + result)
        mods_folder = os.path.normpath(os.path.join(result, 'ultimate', 'mods'))
        if not os.path.exists(result) or not os.path.isdir(result):
            print("Not a valid directory. Please try again")
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
                if len(command) > 1:
                    args = ' '.join(command[1:])
                    new_path = os.path.join(current_path, args)
                    if os.path.isdir(new_path):
                        current_path = new_path
                        list_contents(current_path)
                    else:
                        print(f'{current_path} {args} does not exist')
                else:
                    print("Usage: cd <path>")

            case 'up':
                new_path = os.path.dirname(current_path)
                if os.path.commonpath([new_path, mods_folder]) == mods_folder:
                    current_path = new_path
                    list_contents(current_path)
                else:
                    print(f'Cannot move up. {new_path} is outside of the mods folder.')

            case 'mkdir':
                if len(command) > 1:
                    os.mkdir(os.path.join(current_path, command[1]))
                else:
                    print("Usage: mkdir <path>")

            case 'rmdir':
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

            case 'get modslot': #WIP
                continue

            case 'help':
                print(f'    ')
                print(f'Commands: ')
                print(f'    ls           - lists contents of current directory.')
                print(f'    cd <path>    - changes directory.')
                print(f'    up           - goes up a level in the tree hierarchy.')
                print(f'    mkdir <name> - creates directory in current directory.')
                print(f'    rmdir <name> - deletes directory in current directory.')
                print(f'    get modslot  - WIP.')
                print(f'    exit         - exit the program.')
                print(f'    ')

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