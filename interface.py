#builtins
from sys import platform

#external
import customtkinter as ctk
from pygame import mixer

#self-made
import internal_data.internal_names_and_series as internal

class ModManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Shiny's Ultimate Mod Manager")
        self.iconbitmap(r"images\icon.ico")
        self.geometry("1280x720")
        self.load_settings()

        self.grid_columnconfigure(0, weight=80, pad=10)
        self.grid_columnconfigure(1, weight=1, pad=0)
        self.grid_rowconfigure(0, weight=2, pad=10)

        self.create_buttons()
        self.create_tabs()
        self.create_optionmenu()

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_tabs(self):
        self.tabview = Tabview(self)

    def create_buttons(self):
        self.sd_card_button = SDCardButton(self)

    def create_optionmenu(self):
        self.theme_select = ThemeSelect(self)

    def load_settings(self):
        from functions import load_settings
        settings = load_settings()
        try:
            ctk.set_appearance_mode(settings.get("theme"))
        except AttributeError:
            ctk.set_appearance_mode("System")

    def save_settings(self):
        from functions import save_settings
        save_settings()

    def on_closing(self):
        self.save_settings()
        self.destroy()

class SDCardButton(ctk.CTkButton):
    def __init__(self, root):
        super().__init__(root)

        self.sd_card_button = ctk.CTkButton(root,
            text="Select SD Card",
            command=self.sd_card_button_pressed,
            height=50,
            corner_radius=50,
            font=("Arial", 15))
        self.sd_card_button.grid(column=2, row=0, padx=25, pady=20, sticky="sew")

    def sd_card_button_pressed(self):
        from functions import ask_for_sd
        ask_for_sd(self)

class Notification(ctk.CTkToplevel):
    def __init__(self, root, prompt):
        super().__init__(root)
        self.prompt = prompt
        self.title("Notification")
        self.geometry("400x200")
        self.iconbitmap(r"images\notif.ico")
        self.grab_set()
        mixer.init()
        self.sound = mixer.Sound("sounds/notification.wav")
        self.sound.set_volume(float(0.3))
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
        self.tabview.grid(row=0, column=0, columnspan=1, sticky="nsew", padx=5, pady=5)


        self.tabview.add("Explorer")
        self.tabview.add("Characters")
        self.tabview.add("Stages")
        self.tabview.add("Edit Mod")
        self.tabview.set("Characters")

        self.tabview.tab("Characters").columnconfigure((0,1,2), weight=1, pad=0)
        self.tabview.tab("Characters").rowconfigure(tuple(range(31)), weight=1, pad=0)


        self.character_frame = ctk.CTkScrollableFrame(master=self.tabview.tab("Characters"),)
        self.character_frame.grid(columnspan=3, rowspan=31, sticky="nsew")
        self.character_frame.columnconfigure((0,1,2), weight=1, pad=0)
        self.character_frame.rowconfigure(tuple(range(31)), weight=1, pad=0)
        self.characters = []

        self.character_index = 0
        for key,val in internal.FIGHTER_INFO.items():
            self.button = CharacterButton(self, text=val[1], master=self.character_frame)
            col = self.character_index % 3
            row = self.character_index // 3
            self.button.grid(column=col, row=row, padx=5, pady=5, sticky="new")
            self.characters.append(self.button)
            self.character_index += 1

        self.tabview.tab("Stages").columnconfigure(0, weight=1, pad=10)
        self.tabview.tab("Stages").rowconfigure(0, weight=1, pad=10)

class CharacterButton(ctk.CTkButton):
    def __init__(self, root, **kwargs):
        super().__init__(root)
        self.master = kwargs.get("master")
        self.text = kwargs.get("text")
        self.character_button = ctk.CTkButton(master=self.master,
                text=self.text,
                font=("Arial", 15),
                fg_color="transparent",
                border_spacing=20,
                height=75,
                width=200,
                command=self.button_pressed,
                )

    def button_pressed(self):
        self.grid(pady=(5, 500))

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
        from data import info
        ctk.set_appearance_mode(choice)
        info.theme = choice
