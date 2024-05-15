import tkinter as tk
from main import HomePage
from game import Game

class Pregame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        questions_label = tk.Label(self, text="Cantidad de preguntas:")
        questions_label.pack(pady=5)
        entry_questions = tk.Entry(self)
        entry_questions.pack(pady=5)
        next_button = tk.Button(
            self,
            text="Siguiente",
            command=lambda: controller.show_frame(Game),
        )
        next_button.pack(padx=10, pady=10)
        back_button = tk.Button(
            self,
            text="Volver",
            command=lambda: controller.show_frame(HomePage),
        )
        back_button.pack(padx=10, pady=10)