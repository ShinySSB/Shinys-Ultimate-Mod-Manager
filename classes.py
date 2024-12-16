import internal_data.internal_names_and_series as internal

Series = internal.Series

class UserData:
    def __init__(self):
        self.switch_sd = None
        self.mods_folder = None
        self.skyline_plugins_folder = None
        self.theme = "System"

    def get_defaults(self):
        self.switch_sd = None
        self.mods_folder = None
        self.skyline_plugins_folder = None
        self.theme = "System"

class Character:
    def __init__(self, name: str):
        self.name = name
        self.internal_name = (internal.FIGHTER_INFO.get(name)
                              or internal.FIGHTER_INFO.get(name)
                              or None)
        if self.internal_name is None:
            print(f"Error, internal name of {self} does not exist.")

class Fighter(Character):
    def __init__(self, fighter_number: int, name: str, series: Series):
        super().__init__(name)
        self.fighter_number = fighter_number
        self.series = series

class Stage(Character):
    def __init__(self, name: str, series: Series):
        super().__init__(name)
        self.series = series

class Mod:
    def __init__(self, name: str):
        self.name = name

class FighterMod(Mod):
    def __init__(self, name: str, fighter: Fighter, slot: str, mod_type: list[str]):
        super().__init__(name)
        self.fighter = fighter
        self.slot = slot
        self.mod_type = mod_type

class StageMod(Mod):
    def __init__(self, name: str, stage: Stage, mod_type: list[str]):
        super().__init__(name)
        self.stage = stage
        self.mod_type = mod_type