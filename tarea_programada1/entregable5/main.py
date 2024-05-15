from JTparser import JTAnalysis
import tkinter as tk
from tkinter import filedialog
import csv

def read_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding="utf8") as file:
            file_content = file.read()
            analysis = JTAnalysis()
            analysis.run(file_content)

# Method for reading the questions and categories files
def open_file(file_name):
    result = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for item in reader:
            result.append(item)
    return result

# Method to change the current frame for a new one
def change_frame(frame):
    global current_frame
    if current_frame is not None:
        current_frame.pack_forget()
    frame.pack()
    current_frame = frame

# Shows the home page
def show_home():
    change_frame(frame)

# Shows the pregame page
def show_pregame():
    change_frame(pregame)

# Shows the game page
def show_game():
    amount_questions = tk.Label(game, text="Cantidad de preguntas seleccionadas:")
    amount_questions.pack(pady=5)
    aux = tk.Label(game, text=entry_questions.get())
    aux.pack(pady=5)
    change_frame(game)

categories = open_file("categories.csv")
questions = open_file("questions.csv")

root = tk.Tk()
 
root.title("Jeopardy Trainer!")
root.geometry('1280x720')

# Home page
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

open_button = tk.Button(frame, text="Open File", command=read_file)
open_button.pack(padx=10, pady=10)
play_button = tk.Button(frame, text="Jugar", command=show_pregame)
play_button.pack(padx=10, pady=10)

# Variable to control the current frame
current_frame = frame


# Pregame
pregame = tk.Frame(root)

questions_label = tk.Label(pregame, text="Cantidad de preguntas:")
questions_label.pack(pady=5)
entry_questions = tk.Entry(pregame)
entry_questions.pack(pady=5)
back_button = tk.Button(pregame, text="Volver", command=show_home)
back_button.pack(padx=10, pady=10)
next_button = tk.Button(pregame, text="Siguiente", command=show_game)
next_button.pack(padx=10, pady=10)

# Game
game = tk.Frame(root)

back_button = tk.Button(game, text="Volver", command=show_pregame)
back_button.pack(padx=10, pady=10)

root.mainloop()