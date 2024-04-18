# Jeopardy! Trainer

## User Manual

Go to the folder ```tareas-programadas-pous/tarea_programada1/entregable3```.

Run the following commands on the console of the folder "entregable3" to create a virtual enviroment and install the dependecies of the project on it:

```
python -m venv ./env/
Windows: \env\Scripts\activate.bat
Linux: source env/bin/activate
pip install ply
```

Execute the biggest file with ```python JTparser.py .\datos\JEO3.json > output.txt```.

On the `output.txt` file you'll find all the tokens read, and on the `parser.out` file you can check all the details about the parser process.

## Requirements

The only requirement for this cycle is the library ```ply```, run the previous commands to install it.

## Authors

### Team name: Pous

* Maria Fernanda Andrés

* Fabián Calvo

* Andrés Quesada