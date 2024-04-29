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
    # General labels
    "CATEGORIESLABEL", 
    "QUESTIONSLABEL", 
    # Data
    "AIRDATE", 
    "VALUE",  
    "NUMBER",
    "ROUND", 
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
    t.value = t.value[1:-1]
    return t

def t_ROUNDLABEL(t):
    r'"round"'
    return t

def t_SHOWNUMLABEL(t):
    r'"show_number"'
    t.value = t.value[1:-1]
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
    r'\"(20[012]\d|19[89]\d)-(0[1-9]|1[0-2])-(0[1-9]|[1-2]\d|3[01])\"'
    t.value = t.value[1:-1]
    return t

def t_VALUE(t):
    r'\"\$(\d+|\,)+\"|null'
    if t.value == 'null':
        t.value = "$0"
    else:
        t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r'\"\d+\"'
    t.value = t.value[1:-1]
    return t

def t_ROUND(t):
    r'"((Double\s|Final\s)?Jeopardy!|Tiebreaker)"'
    t.value = t.value[1:-1]
    return  t

def t_TEXT(t):
    r'\".+?(?=(?<!\\)")\"'
    t.value = t.value[1:-1]
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

lexer = lex.lex()
