import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Shiny's Ultimate Mod Manager")
        self.geometry("1280x720")
        self.grid_columnconfigure((0, 1, 2, 3), weight=2, pad=10)
        self.grid_rowconfigure(0, weight=1, pad=10)

        self.button = ctk.CTkButton(self, text="Select SD Card", command=self.button_callback)
        self.button.grid(column=2, row=0, padx=20, pady=20, sticky="se", columnspan=2)

    def button_callback(self):
        print("Button clicked")

app = App()
app.mainloop()

