# ------------------------------------------------------------
# Copyright [2024] <Maria Fernanda Andres, Fabian Calvo & Andres Quesada Gonzalez>
# ------------------------------------------------------------
from pathlib import Path
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    # Symbols
    "LBRACKET", # [
    "RBRACKET", # ]
    "LBRACE", # {
    "RBRACE", # }
    "QUOTES", # "
    "COLON", # :
    "COMMA",
    # Big labels
    "CATEGORIESLABEL", 
    "QUESTIONSLABEL", 
    # Elements
    "TEXT",  # ['":!?,\.\;\[\]\{\}\(\)\- \\\/&%#\w]+
    "AIRDATE", # (20[01]\d|19[89]\d)-(0[1-9]|1[0-2])-([0-2]\d|3[01])
    "VALUE", # ^\$\d+$
    "SHOWNUMBER", #^\d+$
    # "Tiny labels"
    "CATEGORYLABEL",
    "AIRDATELABEL",
    "QUESTIONLABEL",
    "VALUELABEL",
    "ANSWERLABEL",
    "ROUNDLABEL", #^round$
    "SHOWNUMLABEL",
)

# Regular expression rules for simple tokens
t_LBRACKET = r'^\[$'
t_RBRACKET = r'^\]$'
t_LBRACE = r'^\{$'
t_RBRACE = r'^\}$'
t_QUOTES = r'^\"$' # Check
t_COLON = r'^\:$'
t_COMMA = r'^\,$'

t_CATEGORIESLABEL = r'^categories$'
t_QUESTIONSLABEL = r'^questions$'

t_TEXT = r'[\'\"\:\!\?\,\.\;\[\]\{\}\(\)\- \\\/&%#\w]+' # Check
t_AIRDATE = r'(20[01]\d|19[89]\d)-(0[1-9]|1[0-2])-([0-2]\d|3[01])'
t_VALUE = r'^\$\d+$'
t_SHOWNUMBER = r'^\d+$'

t_CATEGORYLABEL = r'^category$'
t_AIRDATELABEL = r'^air_date$'
t_QUESTIONLABEL = r'^question$'
t_VALUELABEL = r'^value$'
t_ANSWERLABEL = r'^answer$'
t_ROUNDLABEL = r'^round$'
t_SHOWNUMLABEL = r'^show_number$'

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


def get_file_content():
    # Get the parent directory of the current script and add the data file name
    file_path = Path(__file__).parent / "data.json"
    # Get content from the file and return it as a string
    try:
        return open(file_path, "r", encoding="utf8").read()
    except FileNotFoundError:
        return f"'{file_path}' not found."


# Build the lexer
lexer = lex.lex()

# Input extracted from the file
data = get_file_content()

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
