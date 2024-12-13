import os
from tkinter.filedialog import askdirectory
import customtkinter as ctk
import interface

app = interface.ModManager

def main():
    app.mainloop()


def ask_for_sd(no_input, no_mods):
    result = askdirectory()
    if result == '':
        print(no_input)
    elif not os.path.isdir(os.path.join(result, "ultimate", "mods")):
        print(no_mods)
    return result


if __name__ == '__main__':
    main()
