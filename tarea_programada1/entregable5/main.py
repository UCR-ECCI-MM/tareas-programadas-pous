import tkinter as tk
from tkinter import filedialog
import csv
import os
import pandas as pd
from tkinter import ttk
from JTparser import JTAnalysis

filename = "Ningun archivo seleccionado"

# TODO(Andres): Quitar
categories = pd.DataFrame()
questions = pd.DataFrame()

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


class QuestionSearch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        

        self.search_label = tk.Label(self, text="Search", width=5, font=18)  
        self.search_label.grid(row=1, column=0, padx=2, pady=10)

        self.entry_box = tk.Entry(self, width=80, bg="white", font=18)
        self.entry_box.grid(row=1, column=2, padx=1)

        self.search_button = tk.Button(self, text="Search", width=10, font=18, command=lambda: user_search())
        self.search_button.grid(row=1, column=3, padx=2)

        # Adapted from: https://stackoverflow.com/questions/48057591/cant-resize-treeview-with-grid-on-tkinter
        self.table_scrollbar = tk.Scrollbar(self)
        self.table_scrollbar.grid(row=2, column=5, sticky=tk.NS)
        
        self.table_tree = ttk.Treeview(self)

        def refresh_table(self):
            self.table_tree.delete(*self.table_tree.get_children())

        def user_search():
            # Reset TreeView Table
            refresh_table(self)
            query = self.entry_box.get().strip()
            # Create a boolean mask for each row where any column contains the query
            mask = questions.questions.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)
            matched_questions = questions.questions[mask]
            
            self.table_tree["columns"] = list(matched_questions.columns)
            self.table_tree['show'] = 'headings'
            # Configure the columns and headings
            for col in matched_questions.columns:
                self.table_tree.column(col, width=100, anchor='c')
                self.table_tree.heading(col, text=col)
            # Insert the DataFrame rows into the Treeview
            for _, row in matched_questions.iterrows():
                self.table_tree.insert('', 'end', values=list(row))

            # Place the Treeview on the grid
            self.table_tree.grid(row=2, column=0, columnspan=5, sticky='nsew')
            self.table_tree.configure(yscrollcommand=self.table_scrollbar.set)

            self.columnconfigure(0, weight=1) # column with treeview
            self.rowconfigure(2, weight=1) # row with treeview 

        back_button = tk.Button(
            self,
            text="Volver",
            command=lambda: controller.show_frame(DataHub),
        )
        back_button.grid(row=2, column=1, padx=5, pady=10)
        
class DataHub(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        question_search_button = tk.Button(
            self,
            text="Buscador de preguntas",
            command=lambda: controller.show_frame(QuestionSearch)
        )
        question_search_button.pack(padx=10, pady=5)
        
        category_histogram_button = tk.Button(
            self,
            text="Histograma de categorías",
            command=lambda: print("Funcionalidad del histograma de categorías"),
        )
        category_histogram_button.pack(padx=10, pady=5)
        
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

        datahub_button = tk.Button(
            self,
            text="Centro de datos",
            command=lambda: controller.show_frame(DataHub),
        )
        datahub_button.pack(padx=10, pady=10)
        
    def read_file(self):
        global categories, questions
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r', encoding="utf8") as file:
                file_content = file.read()
                analysis = JTAnalysis()
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
        for F in (HomePage, Pregame, Game, DataHub, QuestionSearch):
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