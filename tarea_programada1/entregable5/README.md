# Jeopardy! Trainer

## User Manual

Go to the folder ```tareas-programadas-pous/tarea_programada1/entregable5```.

Run the following commands on the console of the folder "entregable5" to create a virtual enviroment and install the dependecies of the project on it:

```
python -m venv ./env/
Windows: env\Scripts\activate.bat
Linux: source env/bin/activate
pip install requirements.txt
```

Execute the main file with ```python ./main.py```.

This will execute the program, in this window what you need to do first is to import a file of questions, for this, you can go to the folder ```datos``` in this same directory.

If you want to see the requirements for the app see ```requirements.txt```

## Features implemented

### Jugar
In this feature the app will ask you to enter how many question you want to play, enter a number and click on "Siguiente", you will play as many questions as you entered in the previous screen, you will have 10 seconds to respond and the answer will be displayed. You can state if you guessed the question or not so we can store your answers for the feature "Repaso"

### Modo repaso
In this mode you will be able to play the questions that you have previously failed, you can replay them so you get better!

### Busqueda de preguntas
Here you can navigate between all the questions asked on the file you imported. You can search based on any column!

### Estadisticas de datos
You can find two types of graphs, one for frequency of categories and other for comparing the media value of each category

### Estadisticas personales
Here you can see your personal scores and graphs based on categories and questions you've played



## Authors

### Team name: Pous

* Maria Fernanda Andrés (C00442)

* Fabián Calvo Alcázar (B91399)

* Andrés Quesada Gonzales (C16105)