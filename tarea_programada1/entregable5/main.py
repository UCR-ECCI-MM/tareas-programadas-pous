from JTparser import JTAnalysis
import tkinter as tk
from tkinter import filedialog

def read_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding="utf8") as file:
            file_content = file.read()
            analysis = JTAnalysis()
            analysis.run(file_content)

root = tk.Tk()
 
root.title("Jeopardy Trainer!")
root.geometry('1280x720')

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

open_button = tk.Button(frame, text="Open File", command=read_file)
open_button.pack(padx=10, pady=10)

root.mainloop()