#builtins
import json
import os
import ctypes
import pathlib

#self-made
from data import info

#Function attached to the SD card button.
def ask_for_sd(root):
    from tkinter.filedialog import askdirectory
    from interface import Notification

    result = askdirectory()
    result = os.path.normpath(result)

    mods = os.path.normpath(os.path.join(result, 'ultimate', 'mods'))
    skyline = os.path.normpath(os.path.join(
        result, "atmosphere", "contents", "01006A800016E000", "romfs", "skyline", "plugins"
    ))

    if not os.path.exists(result) or not os.path.isdir(result):
        Notification(prompt="Invalid directory, please try again.", root=root)
        return
    elif not os.path.isdir(mods):
        Notification(prompt='Cannot find mods folder in directory.\n'
                            'Make sure you select the root of your SD card.\n'
                            'If you have no mods folder on your SD card,\n' r"create 'SD:\ultimate\mods\'",
                     root=root)
        if not (info.switch_sd is None or info.switch_sd == ''):
            return
    elif not os.path.isdir(skyline):
        Notification(prompt="Cannot find skyline plugins folder. Ignoring...", root=root)

    info.switch_sd = result
    info.mods_folder = mods
    info.skyline_plugins_folder = skyline

#Executed on closing.
def save_settings():
    save_path = os.path.normpath(os.path.join('user_config', 'settings.json'))
    settings = {
        'switch_sd': info.switch_sd,
        'mods_folder': info.mods_folder,
        'skyline_plugins_folder': info.skyline_plugins_folder,
        'theme': info.theme,
    }

    save_dir = os.path.dirname(save_path)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    try:
        with open(save_path, 'w') as f:
            json.dump(settings, f)
    except Exception as e:
        print(f"Error saving settings: {e}")

#Executed on start.
def load_settings():
    save_path = os.path.normpath(os.path.join('user_config', 'settings.json'))
    if not os.path.isfile(save_path):
        info.get_defaults()
        return info

    try:
        with open(save_path, 'r') as f:
            settings = json.load(f)
            info.switch_sd = settings.get('switch_sd')
            info.mods_folder = settings.get('mods_folder')
            info.skyline_plugins_folder = settings.get('skyline_plugins_folder')
            info.theme = settings.get('theme')
            return settings

    except FileNotFoundError:
        print('Could not load settings, using defaults.')
        return None
    except json.JSONDecodeError:
        print("Error parsing settings file.")
        return None
    except Exception as e:
        print(f"Error loading settings: {e}")
        return None