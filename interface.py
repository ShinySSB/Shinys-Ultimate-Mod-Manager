import customtkinter as ctk
from sys import platform
from pygame import mixer

class ModManager(ctk.CTk):
    def __init__(self, ask_user_for_sd_func):
        super().__init__()
        self.title("Shiny's Ultimate Mod Manager")
        self.iconbitmap(r"images\icon.ico")
        self.geometry("1280x720")
        ctk.set_appearance_mode("System")

        self.grid_columnconfigure(0, weight=80, pad=10)
        self.grid_columnconfigure(1, weight=1, pad=0)
        self.grid_rowconfigure(0, weight=2, pad=10)

        self.ask_user_for_sd_func = ask_user_for_sd_func
        self.create_buttons()
        self.create_tabs()
        self.create_optionmenu()

    def create_tabs(self):
        self.tabview = Tabview(self)

    def create_buttons(self):
        self.sd_card_button = SDCardButton(self, self.ask_user_for_sd_func)

    def create_optionmenu(self):
        self.theme_select = ThemeSelect(self)

class SDCardButton(ctk.CTkButton):
    def __init__(self, root, ask_user_for_sd_func):
        super().__init__(root)

        self.ask_user_for_sd_func = ask_user_for_sd_func
        self.sd_card_button = ctk.CTkButton(root,
            text="Select SD Card",
            command=self.sd_card_button_pressed,
            height=50,
            corner_radius=50,
            font=("Arial", 15))
        self.sd_card_button.grid(column=2, row=0, padx=25, pady=20, sticky="sew")

    def sd_card_button_pressed(self):
        self.switch_sd = self.ask_user_for_sd_func("Invalid directory, please try again.",
                                                   'Cannot find mods folder in directory.\n'
                                                   'Make sure you select the root of your SD card.\n'
                'If you have no mods folder on your SD card,\n' r"create 'SD:\ultimate\mods\'")

class Notification(ctk.CTkToplevel):
    def __init__(self, root, prompt):
        super().__init__(root)
        self.prompt = prompt
        self.title("Notification")
        self.geometry("400x200")
        self.grab_set()
        mixer.init()
        self.sound = mixer.Sound("sounds/notification.wav")
        self.sound.set_volume(float(0.5))
        self.sound.play()
        self.resizable(False, False)
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.label = ctk.CTkLabel(self, text=prompt, font=("Arial", 15))
        self.label.grid(padx=5, pady=10, row=0, column=0)
        self.button = ctk.CTkButton(self, text="Close", command=self.destroy, font=("Arial", 15))
        self.button.grid(padx=5, pady=10, row=1, column=0)
        if platform.startswith("win"):
            # noinspection PyTypeChecker
            self.after(200, lambda: self.iconbitmap(r"images\notif.ico"))


class Tabview(ctk.CTkTabview):
    def __init__(self, root):
        super().__init__(root)

        self.tabview = ctk.CTkTabview(root)
        self.tabview.grid(row=0, column=0, columnspan=1, sticky="nsew")

        self.tabview.add("Explorer")
        self.tabview.add("Characters")
        self.tabview.add("Stages")
        self.tabview.add("Edit Mod")

        self.label = ctk.CTkLabel(master=self.tabview.tab("Explorer"), text="")
        self.label.pack(padx=20, pady=20)

class ThemeSelect(ctk.CTkOptionMenu):
    def __init__(self, root):
        super().__init__(root)

        self.label = ctk.CTkLabel(master=root, text="Theme", font=("Arial", 12))
        self.label.grid(row=0, column=2, padx=75, pady=0, sticky="new")
        self.theme_select = ctk.CTkOptionMenu(root,
                                              font=("Arial", 15, ),
                                              dropdown_font=("Arial", 15),
                                              values=["System", "Light", "Dark"],
                                              corner_radius=70,
                                              width=153,
                                              anchor="center",
                                              command=self.change_theme,
                                              )
        self.theme_select.grid(column=2, row=0, padx=25, pady=30, sticky="new")

    def change_theme(self, choice):
        ctk.set_appearance_mode(choice)
