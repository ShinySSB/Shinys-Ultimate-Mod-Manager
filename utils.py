from tkinter.filedialog import askdirectory
import os

def ask_user_for_sd(prompt):
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