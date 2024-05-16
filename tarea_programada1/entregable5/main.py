# Copyright [2024] <Maria Fernanda Andres, Fabian Calvo & Andres Quesada Gonzalez>

import tkinter as tk
from tkinter import filedialog
import os
import pandas as pd
from tkinter import ttk
from JTparser import JTAnalysis
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

font = ("Arial", 16)

filename = "Ningun archivo seleccionado"
questions_columns = ['Category', 'Air Date', 'Question', 'Value', 'Answer', 'Round', 'Show Number']
categories = pd.DataFrame()
questions = pd.DataFrame(columns=questions_columns)
passed_questions = pd.DataFrame(columns=questions_columns)
failed_questions = pd.DataFrame(columns=questions_columns)

def on_close(JT):
    passed_questions.to_csv("passed_questions.csv", index=False)
    failed_questions.to_csv("failed_questions.csv", index=False)
    JT.destroy()
    exit()

class Game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Que empiece el juego!", font=font)
        self.label.pack(pady=5)

        self.category = tk.Label(self, text="", font=font)
        self.category.pack()
        self.question = tk.Label(self, text="", font=font)
        self.question.pack()

        self.contador = 0
        self.seconds = 10
        self.timer = tk.Label(self, text=str(self.seconds), font=font)
        self.timer.pack(pady=5)

        self.current_question = ""

        self.user_question = tk.Label(self, text="Acertó la pregunta?", font=font)
        self.correct_button = tk.Button(self,
            text="Sí",
            command=lambda: self.correct(self.current_question),
            font=font
        )
        self.incorrect_button = tk.Button(self,
            text="No",
            command=lambda: self.incorrect(self.current_question),
            font=font
        )

        self.answer = tk.Label(self, text="", font=font)
        
        self.back_button = tk.Button(
            self,
            text="Volver",
            command=lambda: self.cancel_game(),
            font=font
        )
    
    def start_game(self, contador):
        self.seconds = 10
        self.current_question = self.controller.selected_questions.iloc[contador]
        self.show_question(self.current_question)
    
    def show_question(self, question):
        self.category.config(text=f"{question.Category}")
        self.question.config(text=f"{question.Question}")
        self.answer.config(text=f"RESPUESTA: {question.Answer}")

        self.set_timer()
        
        self.user_question.pack_forget()
        self.correct_button.pack_forget()
        self.incorrect_button.pack_forget()
        self.answer.pack_forget()

    def set_timer(self):
        if self.seconds > 0:
            self.timer.config(text=f"Temporizador: {self.seconds}")
            self.seconds -= 1
            self.controller.after(1000, self.set_timer)
        else:
            self.seconds = 10
            self.answer.pack()
            self.user_question.pack()
            self.correct_button.pack()
            self.incorrect_button.pack()
            self.contador += 1

    def correct(self, question):
        global passed_questions, failed_questions
        passed_questions = pd.concat([passed_questions, pd.DataFrame([question])], ignore_index=True)
        passed_questions = passed_questions.drop_duplicates()
        if (failed_questions == question).all(axis=1).any():
            failed_questions = failed_questions[~(failed_questions == question).all(axis=1)]            
        if self.contador < self.controller.amount_questions:
            self.start_game(self.contador)
        else:
            self.contador = 0
            self.back_button.pack(padx=10, pady=10)

    def incorrect(self, question):
        global passed_questions, failed_questions
        failed_questions = pd.concat([failed_questions, pd.DataFrame([question])], ignore_index=True)
        failed_questions = failed_questions.drop_duplicates()
        if self.contador < self.controller.amount_questions:
            self.start_game(self.contador)
        else:
            self.contador = 0
            self.back_button.pack(padx=10, pady=10)

    def cancel_game(self):
        self.second = 10
        self.category.config(text="")
        self.question.config(text="")
        self.contador = 0
        self.user_question.pack_forget()
        self.correct_button.pack_forget()
        self.incorrect_button.pack_forget()
        self.back_button.pack_forget()
        self.controller.amount_question = 0
        self.controller.show_frame(HomePage)        

class Pregame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.questions_label = tk.Label(self, text="Cantidad de preguntas:", font=font)
        self.questions_label.pack(pady=5)
        self.entry_questions = tk.Entry(self, font=font)
        self.entry_questions.pack(pady=5)
        self.next_button = tk.Button(
            self,
            text="Siguiente",
            command=lambda: self.start_game(controller),
            font=font
        )
        self.next_button.pack(padx=10, pady=10)
        back_button = tk.Button(
            self,
            text="Volver",
            command=lambda: controller.show_frame(HomePage),
            font=font
        )
        back_button.pack(padx=10, pady=10)
    
    def start_game(self, controller):
        controller.amount_questions = int(self.entry_questions.get())
        controller.selected_questions = questions.sample(controller.amount_questions)
        controller.show_frame(Game)
        controller.start_game()
        
class QuestionSearch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.search_label = tk.Label(self, text="Search", width=5, font=14)  
        self.search_label.grid(row=1, column=0, padx=2, pady=10)

        self.entry_box = tk.Entry(self, width=80, bg="white", font=14)
        self.entry_box.grid(row=1, column=2, padx=1)

        self.search_button = tk.Button(self, text="Search", width=10, font=14, command=lambda: user_search())
        self.search_button.grid(row=1, column=3, padx=2)

        self.back_button = tk.Button(self, text="Volver", width=10, font=14, command=lambda: controller.show_frame(DataHub))
        self.back_button.grid(row=1, column=4, padx=2)

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
            mask = questions.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)
            matched_questions = questions[mask]
            
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
        
class PlotDisplay(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        back_button = tk.Button(self, text="Generar Gráficos", command= self.generate_plots)
        back_button.pack(padx=10, pady=10)
        
        back_button = tk.Button(self, text="Volver", command=lambda: controller.show_frame(DataHub))
        back_button.pack(padx=10, pady=10)

    def generate_plots(self):
        fig1 = Figure(figsize=(5, 4), dpi=100)
        plot1 = fig1.add_subplot(111)
        # Conteo de la frecuencia de cada categoría
        category_counts = categories.value_counts()
        plot1.bar(category_counts.index, category_counts.values)
        plot1.set_title('Frecuencia de Categorías')
        plot1.set_xlabel('Categoría')
        plot1.set_ylabel('Frecuencia')

        fig2 = Figure(figsize=(5, 4), dpi=100)
        plot2 = fig2.add_subplot(111)
        # Conversión de la columna 'Value' a valores numéricos
        questions['Value'] = questions['Value'].replace('[\$,]', '', regex=True).astype(float)
        # Agrupación por categoría y cálculo del valor promedio
        category_values = questions.groupby('Category')['Value'].mean()
        plot2.bar(category_values.index, category_values.values)
        plot2.set_title('Valor Promedio de Preguntas por Categoría')
        plot2.set_xlabel('Categoría')
        plot2.set_ylabel('Valor Promedio ($)')
        
        canvas1 = FigureCanvasTkAgg(fig1, self)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        canvas2 = FigureCanvasTkAgg(fig2, self)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)       

class Review(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        play_button = tk.Button(
            self,
            text="Jugar",
            command=lambda: controller.show_frame(PreReviewGame),
            font=font
        )
        play_button.pack(padx=10, pady=10)
        graphs = tk.Button(
            self,
            text="Grafico",
            command=lambda: controller.show_frame(ReviewGraph),
            font=font
        )
        graphs.pack(padx=10, pady=10)
        back_button = tk.Button(
            self,
            text="Volver",
            command=lambda: controller.show_frame(HomePage),
            font=font
        )
        back_button.pack(padx=10, pady=10)
        
class PreReviewGame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.questions_label = tk.Label(self, text="Cantidad de preguntas:", font=font)
        self.questions_label.pack(pady=5)
        self.entry_questions = tk.Entry(self)
        self.entry_questions.pack(pady=5)
        self.next_button = tk.Button(
            self,
            text="Siguiente",
            command=lambda: self.start_game(controller),
            font=font
        )
        self.next_button.pack(padx=10, pady=10)
        back_button = tk.Button(
            self,
            text="Volver",
            command=lambda: controller.show_frame(HomePage),
            font=font
        )
        back_button.pack(padx=10, pady=10)
    
    def start_game(self, controller):
        controller.amount_questions = int(self.entry_questions.get())
        controller.selected_questions = failed_questions.sample(controller.amount_questions)
        controller.show_frame(Game)
        controller.start_game()
        
class ReviewGraph(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        plot_button = tk.Button(
            self,
            text="Generar gráfico",
            command=self.plot_circular_graph,
            font=font
        )
        plot_button.pack(padx=10, pady=10)
        back_button = tk.Button(
            self,
            text="Volver",
            command=lambda: controller.show_frame(HomePage),
            font=font
        )
        back_button.pack(padx=10, pady=10)
        
    def plot_circular_graph(self):
        labels = ['Preguntas falladas', 'Preguntas acertadas']
        size_failed_questions = int(len(failed_questions) * 100 / 2)
        size_passed_questions = int(len(passed_questions) * 100 / 2)
        if size_failed_questions == 0:
            size_failed_questions = 1
        if size_passed_questions == 0:
            size_passed_questions = 1
        sizes = [size_failed_questions, size_passed_questions]  # Sizes as percentages
        colors = ['purple', 'red']

        fig, ax = plt.subplots()
        
        ax.pie(sizes, labels=labels, colors=colors)
        ax.set_title('Preguntas acertadas vs preguntas falladas')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
class ReviewGame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        back_button = tk.Button(
            self,
            text="Terminar Juego",
            command=lambda: controller.show_frame(HomePage),
            font=font
        )
        back_button.pack(padx=10, pady=10)

class DataHub(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        question_search_button = tk.Button(
            self,
            text="Buscador de preguntas",
            command=lambda: controller.show_frame(QuestionSearch),
            font=font
        )
        question_search_button.pack(padx=10, pady=5)
        
        category_histogram_button = tk.Button(
            self,
            text="Gráficos sobre los datos",
            command=lambda: controller.show_frame(PlotDisplay),
            font=font
        )
        category_histogram_button.pack(padx=10, pady=5)
        
        back_button = tk.Button(
            self,
            text="Volver",
            command=lambda: controller.show_frame(HomePage),
            font=font
        )
        back_button.pack(padx=10, pady=10)

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.filename_var = tk.StringVar()
        self.filename_var.set(f'Archivo seleccionado: {filename}')
        open_button = tk.Button(self, text="Open File", command=self.read_file, font=font)
        open_button.pack(padx=10, pady=10)
        filename_label = tk.Label(self, 
                        textvariable=self.filename_var, 
                        anchor=tk.CENTER,                       
                        justify=tk.CENTER,
                        font=font    
                        )
        filename_label.pack(pady=20)
        play_button = tk.Button(
            self,
            text="Jugar",
            command=lambda: controller.show_frame(Pregame),
            font=font
        )
        play_button.pack(padx=10, pady=10)
        review_button = tk.Button(
            self,
            text="Review",
            command=lambda: controller.show_frame(Review),
            font=font
        )
        review_button.pack(padx=10, pady=10)
        datahub_button = tk.Button(
            self,
            text="Centro de datos",
            command=lambda: controller.show_frame(DataHub),
            font=font
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
        self.amount_questions = 0
        self.selected_questions = pd.DataFrame
        
        global passed_questions, failed_questions
        try:
            passed_questions = pd.read_csv("passed_questions.csv")
            failed_questions = pd.read_csv("failed_questions.csv")
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
        except FileNotFoundError:
            with open("passed_questions.csv", 'w'):
                pass
            with open("failed_questions.csv", 'w'):
                pass
            print("Error: File not found. Please check the file path and try again.")
                                        
        container = tk.Frame(self, height=720, width=1280)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, Pregame, Game, DataHub, QuestionSearch, PlotDisplay, Review, PreReviewGame, ReviewGraph):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def start_game(self):
        self.frames[Game].start_game(0)
        
if __name__ == "__main__":
    jt = JT()
    jt.protocol("WM_DELETE_WINDOW", lambda: on_close(jt))
    jt.mainloop()