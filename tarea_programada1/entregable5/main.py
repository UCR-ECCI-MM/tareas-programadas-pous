from JTparser import JTAnalysis
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def read_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding="utf8") as file:
            file_content = file.read()
            analysis = JTAnalysis()
            analysis.run(file_content)
            show_main_menu()

def show_main_menu():
    root.withdraw()  # Hide the initial root window
    menu_window = tk.Toplevel()
    menu_window.title("Main Menu")
    menu_window.geometry("1280x720")

    # Load the logo
    image = Image.open("assets/logo.png") 
    photo = ImageTk.PhotoImage(image)

    # Display logo
    image_label = tk.Label(menu_window, image=photo)
    image_label.image = photo 
    image_label.pack(pady=0)

    button_style = {'font': ('Arial', 14), 'width': 25, 'height': 1}

    play_button = tk.Button(menu_window, text="Play", command=lambda: print("Play!"), **button_style)
    play_button.pack(pady=0)

    stats_button = tk.Button(menu_window, text="Player Stats", command=lambda: print("Player Stats!"), **button_style)
    stats_button.pack(pady=0)

    data_hub_button = tk.Button(menu_window, text="Data Hub", command=lambda: print("Data Hub!"), **button_style)
    data_hub_button.pack(pady=0)

    change_input_button = tk.Button(menu_window, text="Change input data", command=lambda: go_back(menu_window), **button_style)
    change_input_button.pack(pady=0)

    about_button = tk.Button(menu_window, text="About", command=lambda: print("About!"), **button_style)
    about_button.pack(pady=0)


    menu_window.protocol("WM_DELETE_WINDOW", lambda: on_close(menu_window))



def on_close(window):
    window.destroy()
    root.quit()

def go_back(window):
    window.destroy()
    root.deiconify()

root = tk.Tk()
 
root.title("Jeopardy Trainer!")
root.geometry('1280x720')

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

open_button = tk.Button(frame, text="Open File", command=read_file)
open_button.pack(padx=10, pady=10)

root.protocol("WM_DELETE_WINDOW", lambda: on_close(root))

root.mainloop()