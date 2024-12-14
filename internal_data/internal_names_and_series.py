from enum import Enum, auto

class Series(Enum):
    SMASH = auto()
    MARIO = auto()
    MARIO_KART = auto()
    DONKEY_KONG = auto()
    ZELDA = auto()
    METROID = auto()
    YOSHI = auto()
    KIRBY = auto()
    STAR_FOX = auto()
    POKEMON = auto()
    F_ZERO = auto()
    ICE_CLIMBER = auto()
    MOTHER = auto()
    FIRE_EMBLEM = auto()
    GAME_AND_WATCH = auto()
    KID_ICARUS = auto()
    WARIO = auto()
    PIKMIN = auto()
    FAMICOM = auto()
    ELECTROPLANKTON = auto()
    BALLOON_FIGHT = auto()
    NINTENDOGS = auto()
    MII = auto()
    MII_PLAZA = auto()
    TOMODACHI = auto()
    WUHU_ISLAND = auto()
    PILOTWINGS = auto()
    PICTOCHAT = auto()
    WRECKING_CREW = auto()
    ANIMAL_CROSSING = auto()
    WII_FIT = auto()
    PUNCH_OUT = auto()
    XENOBLADE_CHRONICLES = auto()
    DUCK_HUNT = auto()
    SPLATOON = auto()
    METAL_GEAR = auto()
    SONIC = auto()
    MEGA_MAN = auto()
    PACMAN = auto()
    STREET_FIGHTER = auto()
    FINAL_FANTASY = auto()
    BAYONETTA = auto()
    CASTLEVANIA = auto()
    PERSONA = auto()
    DRAGON_QUEST = auto()
    BANJO_KAZOOIE = auto()
    FATAL_FURY = auto()
    ARMS = auto()
    MINECRAFT = auto()
    TEKKEN = auto()
    KINGDOM_HEARTS = auto()
    OTHER = auto()
    NONE = auto()

FIGHTER_INFO = {
    'mario': ('1', 'Mario', Series.MARIO),
    'donkey': ('2', 'Donkey Kong', Series.DONKEY_KONG),
    'link': ('3', 'Link', Series.ZELDA),
    'samus': ('4', 'Samus', Series.METROID),
    'samusd': ('4E', 'Dark Samus', Series.METROID),
    'yoshi': ('5', 'Yoshi', Series.YOSHI),
    'kirby': ('6', 'Kirby', Series.KIRBY),
    'fox': ('7', 'Fox', Series.STAR_FOX),
    'pikachu': ('8', 'Pikachu', Series.POKEMON),
    'luigi': ('9', 'Luigi', Series.MARIO),
    'ness': ('10', 'Ness', Series.MOTHER),
    'captain': ('11', 'Captain Falcon', Series.F_ZERO),
    'purin': ('12', 'Jigglypuff', Series.POKEMON),
    'peach': ('13', 'Peach', Series.MARIO),
    'daisy': ('13E', 'Daisy', Series.MARIO),
    'koopa': ('14', 'Bowser', Series.MARIO),
    'koopag': ('14B', 'Giga Bowser', Series.MARIO),
    'nana': ('15', 'Ice Climbers (Nana)', Series.ICE_CLIMBER),
    'popo': ('15', 'Ice Climbers (Popo)', Series.ICE_CLIMBER),
    'sheik': ('16', 'Sheik', Series.ZELDA),
    'zelda': ('17', 'Zelda', Series.ZELDA),
    'mariod': ('18', 'Dr. Mario', Series.MARIO),
    'pichu': ('19', 'Pichu', Series.POKEMON),
    'falco': ('20', 'Falco', Series.STAR_FOX),
    'marth': ('21', 'Marth', Series.FIRE_EMBLEM),
    'lucina': ('21E', 'Lucina', Series.FIRE_EMBLEM),
    'younglink': ('22', 'Young Link', Series.ZELDA),
    'ganon': ('23', 'Ganondorf', Series.ZELDA),
    'mewtwo': ('24', 'Mewtwo', Series.POKEMON),
    'roy': ('25', 'Roy', Series.FIRE_EMBLEM),
    'chrom': ('25E', 'Chrom', Series.FIRE_EMBLEM),
    'gamewatch': ('26', 'Mr. Game & Watch', Series.GAME_AND_WATCH),
    'metaknight': ('27', 'Meta Knight', Series.KIRBY),
    'pit': ('28', 'Pit', Series.KID_ICARUS),
    'pitb': ('28E', 'Dark Pit', Series.KID_ICARUS),
    'szerosuit': ('29', 'Zero Suit Samus', Series.METROID),
    'wario': ('30', 'Wario', Series.WARIO),
    'snake': ('31', 'Snake', Series.METAL_GEAR),
    'ike': ('32', 'Ike', Series.FIRE_EMBLEM),
    'ptrainer': ('33T', 'Pokémon Trainer', Series.POKEMON),
    'ptrainer_low': ('33T', 'Pokémon Trainer (Low)', Series.POKEMON),
    'pzenigame': ('33', 'Squirtle', Series.POKEMON),
    'pfushigisou': ('34', 'Ivysaur', Series.POKEMON),
    'plizardon': ('35', 'Charizard', Series.POKEMON),
    'diddy': ('36', 'Diddy Kong', Series.DONKEY_KONG),
    'lucas': ('37', 'Lucas', Series.MOTHER),
    'sonic': ('38', 'Sonic', Series.SONIC),
    'dedede': ('39', 'King Dedede', Series.KIRBY),
    'pikmin': ('40', 'Olimar', Series.PIKMIN),
    'lucario': ('41', 'Lucario', Series.POKEMON),
    'robot': ('42', 'R.O.B.', Series.FAMICOM),
    'toonlink': ('43', 'Toon Link', Series.ZELDA),
    'wolf': ('44', 'Wolf', Series.STAR_FOX),
    'murabito': ('45', 'Villager', Series.ANIMAL_CROSSING),
    'rockman': ('46', 'Mega Man', Series.MEGA_MAN),
    'wiifit': ('47', 'Wii Fit Trainer', Series.WII_FIT),
    'rosetta': ('48', 'Rosalina & Luma', Series.MARIO),
    'littlemac': ('49', 'Little Mac', Series.PUNCH_OUT),
    'gekkouga': ('50', 'Greninja', Series.POKEMON),
    'miifighter': ('51', 'Mii Brawler', Series.SMASH),
    'miiswordsman': ('52', 'Mii Swordfighter', Series.SMASH),
    'miigunner': ('53', 'Mii Gunner', Series.SMASH),
    'palutena': ('54', 'Palutena', Series.KID_ICARUS),
    'pacman': ('55', 'Pac-Man', Series.PACMAN),
    'reflet': ('56', 'Robin', Series.FIRE_EMBLEM),
    'shulk': ('57', 'Shulk', Series.XENOBLADE_CHRONICLES),
    'koopajr': ('58', 'Bowser Jr.', Series.MARIO),
    'duckhunt': ('59', 'Duck Hunt', Series.DUCK_HUNT),
    'ryu': ('60', 'Ryu', Series.STREET_FIGHTER),
    'ken': ('60E', 'Ken', Series.STREET_FIGHTER),
    'cloud': ('61', 'Cloud', Series.FINAL_FANTASY),
    'kamui': ('62', 'Corrin', Series.FIRE_EMBLEM),
    'bayonetta': ('63', 'Bayonetta', Series.BAYONETTA),
    'inkling': ('64', 'Inkling', Series.SPLATOON),
    'ridley': ('65', 'Ridley', Series.METROID),
    'simon': ('66', 'Simon', Series.CASTLEVANIA),
    'richter': ('66E', 'Richter', Series.CASTLEVANIA),
    'krool': ('67', 'King K. Rool', Series.DONKEY_KONG),
    'shizue': ('68', 'Isabelle', Series.ANIMAL_CROSSING),
    'gaogaen': ('69', 'Incineroar', Series.POKEMON),
    'packun': ('70', 'Piranha Plant', Series.MARIO),
    'jack': ('71', 'Joker', Series.PERSONA),
    'brave': ('72', 'Hero', Series.DRAGON_QUEST),
    'buddy': ('73', 'Banjo & Kazooie', Series.BANJO_KAZOOIE),
    'dolly': ('74', 'Terry', Series.FATAL_FURY),
    'master': ('75', 'Byleth', Series.FIRE_EMBLEM),
    'tantan': ('76', 'Min Min', Series.ARMS),
    'pickel': ('77', 'Steve', Series.MINECRAFT),
    'edge': ('78', 'Sephiroth', Series.FINAL_FANTASY),
    'eflame': ('79', 'Pyra', Series.XENOBLADE_CHRONICLES),
    'element': ('79B', 'Rex', Series.XENOBLADE_CHRONICLES),
    'elight': ('80', 'Mythra', Series.XENOBLADE_CHRONICLES),
    'demon': ('81', 'Kazuya', Series.TEKKEN),
    'trail': ('82', 'Sora', Series.KINGDOM_HEARTS),
    #'common': '',
    #'miienemyf': '',
    #'miienemyg': '',
    #'miienemys': '',
}

STAGE_INFO = {
    '75m': ('75 m', Series.DONKEY_KONG),
    'animal_city': ('Town and City', Series.ANIMAL_CROSSING),
    'animal_island': ('Tortimer Island', Series.ANIMAL_CROSSING),
    'animal_village': ('Smashville', Series.ANIMAL_CROSSING),
    'balloonfight': ('Balloon Fight', Series.BALLOON_FIGHT),
    'battlefield': ('Battlefield', Series.SMASH),
    'battlefield_l': ('Big Battlefield', Series.SMASH),
    'battlefield_s': ('Small Battlefield', Series.SMASH),
    'bayo_clock': ('Umbra Clock Tower', Series.BAYONETTA),
    #'bonusgame': '',
    'bossstage_dracula': ("Dracula's Boss Stage", Series.CASTLEVANIA),
    #'bossstage_final1': '',
    #'bossstage_final2': '',
    #'bossstage_final3': '',
    'bossstage_galleom': ("Galleom's Boss Stage", Series.SMASH),
    'bossstage_ganonboss': ("Ganon's Boss Stage", Series.ZELDA),
    'bossstage_marx': ("Marx's Boss Stage", Series.KIRBY),
    'bossstage_rathalos': ("Rathalos' Boss Stage", Series.OTHER),
    'brave_altar': ("Yggdrasil's Altar", Series.DRAGON_QUEST),
    'buddy_spiral': ('Spiral Mountain', Series.BANJO_KAZOOIE),
    #'campaignmap': ('The Map of World of Light', Series.SMASH),
    #'common': '',
    'demon_dojo': ('Mishima Dojo', Series.TEKKEN),
    'dk_jungle': ('Kongo Jungle', Series.DONKEY_KONG),
    'dk_lodge': ('Jungle Japes', Series.DONKEY_KONG),
    'dk_waterfall': ('Kongo Falls', Series.DONKEY_KONG),
    'dolly_stadium': ('King of Fighters Stadium', Series.FATAL_FURY),
    'dracula_castle': ("Dracula's Castle", Series.CASTLEVANIA),
    'duckhunt': ('Duck Hunt', Series.DUCK_HUNT),
    'end': ('Final Destination', Series.SMASH),
    'fe_arena': ('Arena Ferox', Series.FIRE_EMBLEM),
    'fe_colloseum': ('Coliseum', Series.FIRE_EMBLEM),
    'fe_shrine': ('Garreg Mach Monastery', Series.FIRE_EMBLEM),
    'fe_siege': ('Castle Siege', Series.FIRE_EMBLEM),
    'ff_cave': ('Northern Cave', Series.FINAL_FANTASY),
    'ff_midgar': ('Midgar', Series.FINAL_FANTASY),
    'flatzonex': ('Flat Zone X', Series.GAME_AND_WATCH),
    'fox_corneria': ('Corneria', Series.STAR_FOX),
    'fox_lylatcruise': ('Lylat Cruise', Series.STAR_FOX),
    'fox_venom': ('Venom', Series.STAR_FOX),
    'fzero_bigblue': ('Big Blue', Series.F_ZERO),
    'fzero_mutecity3ds': ('Mute City SNES', Series.F_ZERO),
    'fzero_porttown': ('Port Town Aero Drive', Series.F_ZERO),
    'homeruncontest': ('Home-Run Contest', Series.SMASH),
    'icarus_angeland': ("Palutena's Temple", Series.KID_ICARUS),
    'icarus_skyworld': ('Skyworld', Series.KID_ICARUS),
    'icarus_uprising': ('Reset Bomb Forest', Series.KID_ICARUS),
    'ice_top': ('Summit', Series.ICE_CLIMBER),
    'jack_mementoes': ('Mementos', Series.PERSONA),
    'kart_circuitfor': ('Mario Circuit', Series.MARIO_KART),
    'kart_circuitx': ('Figure-8 Circuit', Series.MARIO_KART),
    'kirby_cave': ('The Great Cave Offensive', Series.KIRBY),
    'kirby_fountain': ('Fountain of Dreams', Series.KIRBY),
    'kirby_gameboy': ('Dream Land GB', Series.KIRBY),
    'kirby_greens': ('Green Greens', Series.KIRBY),
    'kirby_halberd': ('Halberd', Series.KIRBY),
    'kirby_pupupu64': ('Dream Land', Series.KIRBY),
    'luigimansion': ("Luigi's Mansion", Series.MARIO),
    'mario_3dland': ('3D Land', Series.MARIO),
    'mario_castle64': ("Peach's Castle", Series.MARIO),
    'mario_castledx': ("Princess Peach's Castle", Series.MARIO),
    'mario_dolpic': ('Delfino Plaza', Series.MARIO),
    'mario_galaxy': ('Mario Galaxy', Series.MARIO),
    'mario_newbros2': ('Golden Plains', Series.MARIO),
    'mario_odyssey': ('New Donk City Hall', Series.MARIO),
    'mario_paper': ('Paper Mario', Series.MARIO),
    'mario_past64': ('Mushroom Kingdom', Series.MARIO),
    'mario_pastusa': ('Mushroom Kingdom II', Series.MARIO),
    'mario_pastx': ('Mushroomy Kingdom', Series.MARIO),
    'mario_rainbow': ('Rainbow Cruise', Series.MARIO),
    'mario_uworld': ('Mushroom Kingdom U', Series.MARIO),
    'mariobros': ('Mario Bros.', Series.MARIO),
    'metroid_kraid': ('Brinstar Depths', Series.METROID),
    'metroid_norfair': ('Norfair', Series.METROID),
    'metroid_orpheon': ('Frigate Orpheon', Series.METROID),
    'metroid_zebesdx': ('Brinstar', Series.METROID),
    'mg_shadowmoses': ('Shadow Moses Island', Series.METAL_GEAR),
    'mother_fourside': ('Fourside', Series.MOTHER),
    'mother_magicant': ('Magicant', Series.MOTHER),
    'mother_newpork': ('New Pork City', Series.MOTHER),
    'mother_onett': ('Onett', Series.MOTHER),
    'nintendogs': ('Living Room', Series.NINTENDOGS),
    'pac_land': ('PAC-LAND', Series.PACMAN),
    'photostage': ('Mii Photo Stage', Series.OTHER),
    'pickel_world': ('Minecraft World', Series.MINECRAFT),
    'pictochat2': ('PictoChat 2', Series.PICTOCHAT),
    'pikmin_garden': ('Garden of Hope', Series.PIKMIN),
    'pikmin_planet': ('Distant Planet', Series.PIKMIN),
    'pilotwings': ('Pilotwings', Series.PILOTWINGS),
    'plankton': ('Hanenbow', Series.ELECTROPLANKTON),
    'poke_kalos': ('Kalos Pokémon League', Series.POKEMON),
    'poke_stadium': ('Pokémon Stadium', Series.POKEMON),
    'poke_stadium2': ('Pokémon Stadium 2', Series.POKEMON),
    'poke_tengam': ('Spear Tower', Series.POKEMON),
    'poke_tower': ('Prism Tower', Series.POKEMON),
    'poke_unova': ('Unova Pokémon League', Series.POKEMON),
    'poke_yamabuki': ('Saffron City', Series.POKEMON),
    'punchoutsb': ('Boxing Ring', Series.PUNCH_OUT),
    #'punchoutw': '',
    'resultstage': ('Results Stage', Series.SMASH),
    'resultstage_edge': ("Sephiroth's Results Stage", Series.FINAL_FANTASY),
    'resultstage_jack': ("Joker's Results Stage", Series.PERSONA),
    'rock_wily': ('Wily Castle', Series.MEGA_MAN),
    'settingstage': ('Controller Setting Stage', Series.SMASH),
    'sf_suzaku': ('Suzaku Castle', Series.STREET_FIGHTER),
    #'shamfight': '',
    'sonic_greenhill': ('Green Hill Zone', Series.SONIC),
    'sonic_windyhill': ('Windy Hill Zone', Series.SONIC),
    #'sp_edit': '',
    #'spiritsroulette': '',
    'spla_parking': ('Moray Towers', Series.SPLATOON),
    #'staffroll': '',
    'streetpass': ('Find Mii', Series.MII_PLAZA),
    'tantan_spring': ('Spring Stadium', Series.ARMS),
    'tomodachi': ('Tomodachi Life', Series.OTHER),
    'trail_castle': ('Hollow Bastion', Series.KINGDOM_HEARTS),
    'training': ('Training Mode Stage', Series.SMASH),
    'wario_gamer': ('Gamer', Series.WARIO),
    'wario_madein': ('WarioWare, Inc.', Series.WARIO),
    'wiifit': ('Wii Fit Studio', Series.WII_FIT),
    'wreckingcrew': ('Wrecking Crew', Series.OTHER),
    'wufuisland': ('Wuhu Island', Series.WUHU_ISLAND),
    'xeno_alst': ('Cloud Sea of Alrest', Series.XENOBLADE_CHRONICLES),
    'xeno_gaur': ('Gaur Plain', Series.XENOBLADE_CHRONICLES),
    'yoshi_cartboard': ("Yoshi's Story", Series.YOSHI),
    'yoshi_island': ("Yoshi's Island", Series.YOSHI),
    'yoshi_story': ('Super Happy Tree', Series.YOSHI),
    'yoshi_yoster': ("Yoshi's Island (Melee)", Series.YOSHI),
    'zelda_gerudo': ('Gerudo Valley', Series.ZELDA),
    'zelda_greatbay': ('Great Bay', Series.ZELDA),
    'zelda_hyrule': ("Hyrule Castle", Series.ZELDA),
    'zelda_oldin': ('Bridge of Eldin', Series.ZELDA),
    'zelda_pirates': ('Pirate Ship', Series.ZELDA),
    'zelda_skyward': ('Skyloft', Series.ZELDA),
    'zelda_temple': ('Temple', Series.ZELDA),
    'zelda_tower': ('Great Plateau Tower', Series.ZELDA),
    'zelda_train': ('Spirit Train', Series.ZELDA),
}
