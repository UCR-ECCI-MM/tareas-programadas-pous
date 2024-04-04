# ------------------------------------------------------------
# Copyright [2024] <Maria Fernanda Andres, Fabian Calvo & Andres Quesada Gonzalez>
# ------------------------------------------------------------
from pathlib import Path
import ply.lex as lex
import sys


tokens = (
    # Symbols
    "LBRACKET", # [
    "RBRACKET", # ]
    "LBRACE", # {
    "RBRACE", # }
    "COLON", # :
    "COMMA", # ,
    "QUOTES", # "
    # General labels
    "CATEGORIESLABEL", 
    "QUESTIONSLABEL", 
    # Data
    "AIRDATE", 
    "VALUE",  
    "SHOWNUMBER", 
    # Specific labels
    "CATEGORYLABEL",
    "AIRDATELABEL",
    "QUESTIONLABEL",
    "VALUELABEL",
    "ANSWERLABEL",
    "ROUNDLABEL",
    "SHOWNUMLABEL",
    "TEXT",
)

def t_CATEGORIESLABEL(t):
    r'"categories"'
    return t

def t_QUESTIONSLABEL(t):
    r'"questions"'
    return t

def t_CATEGORYLABEL(t):
    r'"category"'
    return t

def t_AIRDATELABEL(t):
    r'"air_date"'
    return t

def t_QUESTIONLABEL(t):
    r'"question"'
    return t

def t_VALUELABEL(t):
    r'"value"'
    return t

def t_ANSWERLABEL(t):
    r'"answer"'
    return t

def t_ROUNDLABEL(t):
    r'"round"'
    return t

def t_SHOWNUMLABEL(t):
    r'"show_number"'
    return t

def t_QUOTES(t):
    r'\"'
    return t

def t_COMMA(t):
    r'\,'
    return t

def t_COLON(t):
    r'\:'
    return t

def t_LBRACKET(t):
    r'\['
    return t

def t_RBRACKET(t):
    r'\]'
    return t

def t_LBRACE(t):
    r'\{'
    return t

def t_RBRACE(t):
    r'\}'
    return t

def t_AIRDATE(t):
    r'(20[01]\d|19[89]\d)-(0[1-9]|1[0-2])-(0[1-9]|[1-2]\d|3[01])'
    return t

def t_VALUE(t):
    r'\$\d+'
    return t

def t_SHOWNUMBER(t):
    r'\d+'
    return t

def t_TEXT(t):
    r'.+?(?=(?<!\\)")'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def get_file_content(path):
    # Get the parent directory of the current script and add the data file name
    file_path = Path(__file__).parent / path
    # Get content from the file and return it as a string
    try:
        return open(file_path, "r", encoding="utf8").read()
    except FileNotFoundError:
        return f"'{file_path}' not found."


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path>")
        return

    path = sys.argv[1]
    # Build the lexer
    lexer = lex.lex()

    data = get_file_content(path)

    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

if __name__ == "__main__":
    main()
