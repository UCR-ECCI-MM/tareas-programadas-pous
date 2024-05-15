import tkinter as tk
from tkinter import filedialog
import csv
import os
from JTparser import JTAnalysis

filename = "Ningun archivo seleccionado"

def open_file(file_name):
    result = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for item in reader:
            result.append(item)
    return result

class Game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        back_button = tk.Button(
            self,
            text="Volver",
            command=lambda: controller.show_frame(HomePage),
        )
        back_button.pack(padx=10, pady=10)

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

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.filename_var = tk.StringVar()
        self.filename_var.set(f'Archivo seleccionado: {filename}')
        open_button = tk.Button(self, text="Open File", command=self.read_file)
        open_button.pack(padx=10, pady=10)
        filename_label = tk.Label(self, 
                        textvariable=self.filename_var, 
                        anchor=tk.CENTER,                       
                        justify=tk.CENTER,    
                        )
        filename_label.pack(pady=20)
        play_button = tk.Button(
            self,
            text="Jugar",
            command=lambda: controller.show_frame(Pregame),
        )
        play_button.pack(padx=10, pady=10)
        
    def read_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r', encoding="utf8") as file:
                file_content = file.read()
                analysis = JTAnalysis()
                global categories, questions
                categories, questions = analysis.run(file_content)
                filename = os.path.basename(file_path)
                self.filename_var.set(f'Archivo seleccionado: {filename}')
                
class JT(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title("Jeopardy Trainer!")
        self.geometry('1280x720')
        container = tk.Frame(self, height=720, width=1280)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, Pregame, Game):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
if __name__ == "__main__":
    jt = JT()
    jt.mainloop()