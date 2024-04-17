# ------------------------------------------------------------
# Copyright [2024] <Maria Fernanda Andres, Fabian Calvo & Andres Quesada Gonzalez>
# ------------------------------------------------------------
from pathlib import Path
import ply.yacc as yacc
import sys
from JTlexer import tokens


def p_file(t):
    'file : LBRACE CATEGORIESLABEL COLON LBRACKET categories RBRACKET COMMA QUESTIONSLABEL COLON  LBRACKET question RBRACKET RBRACE'
    t[0] = t[1] + t[2] + t[3] + t[4] + t[5] + t[6] + t[7] + t[8] + t[9] + t[10] + t[11] + t[12] + t[13] 

def p_categories(t):
    '''categories : TEXT
    | SHOWNUMBER
    | TEXT COMMA categories
    | SHOWNUMBER COMMA categories'''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = t[1] + t[2]


def p_question(t):
    '''
    question : LBRACE CATEGORYLABEL COLON TEXT COMMA AIRDATELABEL COLON AIRDATE COMMA QUESTIONLABEL COLON TEXT COMMA VALUELABEL COLON VALUE COMMA ANSWERLABEL COLON TEXT COMMA ROUNDLABEL COLON ROUND COMMA SHOWNUMLABEL COLON SHOWNUMBER RBRACE
             | LBRACE CATEGORYLABEL COLON TEXT COMMA AIRDATELABEL COLON AIRDATE COMMA QUESTIONLABEL COLON TEXT COMMA VALUELABEL COLON VALUE COMMA ANSWERLABEL COLON TEXT COMMA ROUNDLABEL COLON ROUND COMMA SHOWNUMLABEL COLON SHOWNUMBER RBRACE COMMA question
             | LBRACE CATEGORYLABEL COLON SHOWNUMBER COMMA AIRDATELABEL COLON AIRDATE COMMA QUESTIONLABEL COLON TEXT COMMA VALUELABEL COLON VALUE COMMA ANSWERLABEL COLON SHOWNUMBER COMMA ROUNDLABEL COLON ROUND COMMA SHOWNUMLABEL COLON SHOWNUMBER RBRACE
             | LBRACE CATEGORYLABEL COLON SHOWNUMBER COMMA AIRDATELABEL COLON AIRDATE COMMA QUESTIONLABEL COLON TEXT COMMA VALUELABEL COLON VALUE COMMA ANSWERLABEL COLON SHOWNUMBER COMMA ROUNDLABEL COLON ROUND COMMA SHOWNUMLABEL COLON SHOWNUMBER RBRACE COMMA question
    '''
    if t[0] is None:
        t[0] = ""
        
    if len(t) == 30:
        for i in range(1, 30):
            t[0]  += t[i]
    elif len(t) == 32:
        for i in range(1, 32):
            t[0]  += t[i]



def p_error(p):
    print(f'Syntax error at line {p.lineno}: {p.value}')


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
    parser = yacc.yacc()

    data = get_file_content(path)

    result = parser.parse(data)
    print(result)

if __name__ == "__main__":
    main()
