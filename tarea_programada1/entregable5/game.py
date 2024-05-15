import tkinter as tk

class Game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        back_button = tk.Button(
            self,
            text="Volver",
            command=lambda: controller.show_frame(HomePage),
        )
        back_button.pack(padx=10, pady=10)
