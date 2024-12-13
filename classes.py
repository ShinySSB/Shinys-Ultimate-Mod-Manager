import data.internal_names_and_series as info

Series = info.Series

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