# ------------------------------------------------------------
# Copyright [2024] <Maria Fernanda Andres, Fabian Calvo & Andres Quesada Gonzalez>
# ------------------------------------------------------------
from pathlib import Path
import ply.yacc as yacc
import sys
from JTlexer import tokens


def get_file_content(path):
    file_path = Path(__file__).parent / path
    try:
        return open(file_path, "r", encoding="utf8").read()
    except FileNotFoundError:
        return f"'{file_path}' not found."
    
def write_to_file(path, content):
    file_path = Path(__file__).parent / path
    file = open(file_path, "a", encoding="utf8")
    file.write(content)
    file.close()

def p_file(t):
    'file : LBRACE CATEGORIESLABEL COLON LBRACKET categories RBRACKET COMMA QUESTIONSLABEL COLON  LBRACKET questions RBRACKET RBRACE'
    t[0] = t[1] + t[2] + t[3] + t[4] + t[5] + t[6] + t[7] + t[8] + t[9] + t[10] + t[11] + t[12] + t[13] 

def p_categories(t):
    '''categories : TEXT
    | NUMBER
    | TEXT COMMA categories
    | NUMBER COMMA categories'''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = t[1] + t[2]

def p_questions(t):
    '''questions : question
                | question COMMA questions'''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = t[1] + t[2] + t[3]

def p_question(t):
    '''question : LBRACE category COMMA AIRDATELABEL COLON AIRDATE COMMA QUESTIONLABEL COLON TEXT COMMA VALUELABEL COLON VALUE COMMA answer COMMA ROUNDLABEL COLON ROUND COMMA SHOWNUMLABEL COLON NUMBER RBRACE'''
    if t[0] is None:
        t[0] = ""
    for i in range(1, 25):
        # print(t[i])
        t[0] += t[i]

def p_category(t):
    '''category : CATEGORYLABEL COLON TEXT
             | CATEGORYLABEL COLON NUMBER
             | CATEGORYLABEL COLON VALUE'''
    t[0] = t[1] + t[2] + t[3]

def p_answer(t):
    '''answer : ANSWERLABEL COLON TEXT
           | ANSWERLABEL COLON NUMBER
           | ANSWERLABEL COLON VALUE'''
    t[0] = t[1] + t[2] + t[3]


def p_error(p):
    print(f'Syntax error at line {p.lineno}: {p.value}')

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_path> <output_path>")
        return

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    parser = yacc.yacc()

    data = get_file_content(input_path)

    result = parser.parse(data)
    write_to_file(output_path, result)

if __name__ == "__main__":
    main()
