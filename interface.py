from doctest import master

import customtkinter as ctk

import main


class ModManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Shiny's Ultimate Mod Manager")
        self.iconbitmap(r"images\icon.ico")
        self.geometry("1280x720")
        self._set_appearance_mode("System")

        self.grid_columnconfigure(0, weight=80, pad=10)
        self.grid_columnconfigure(1, weight=1, pad=0)
        self.grid_rowconfigure(0, weight=2, pad=10)

        self.create_tabs()
        self.create_buttons()
        self.create_optionmenu()

    def create_tabs(self):
        self.tabview = Tabview(self)

    def create_buttons(self):
        self.sd_card_button = SDCardButton(self)

    def create_optionmenu(self):
        self.theme_select = ThemeSelect(self)

class SDCardButton(ctk.CTkButton):
    def __init__(self, root):
        super().__init__(root)

        self.sd_card_button = ctk.CTkButton(root,
            text="Select SD Card",
            command=self.sd_card_button_pressed,
            height=50,
            corner_radius=50,
            font=("Arial", 15))
        self.sd_card_button.grid(column=2, row=0, padx=20, pady=20, sticky="se")

    def sd_card_button_pressed(self):
        switch_sd = main.ask_user_for_sd('Please input the root of your SD card.')

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
        self.label.grid(row=0, column=2, padx=75, pady=0, sticky="ne")
        self.theme_select = ctk.CTkOptionMenu(root,
                                              font=("Arial", 15, ),
                                              dropdown_font=("Arial", 15),
                                              values=["System", "Light", "Dark"],
                                              corner_radius=70,
                                              anchor="center",
                                              width=153,
                                              command=self.change_theme,
                                              )
        self.theme_select.grid(column=2, row=0, padx=20, pady=30, sticky="ne")

    def change_theme(self, choice):
        pass

app = ModManager()
app.mainloop()
