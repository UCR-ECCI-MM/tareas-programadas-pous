# ------------------------------------------------------------
# Copyright [2024] <Maria Fernanda Andres, Fabian Calvo & Andres Quesada Gonzalez>
# ------------------------------------------------------------
from pathlib import Path
import ply.yacc as yacc
import sys
from JTlexer import tokens
from JTcategories import Categories
from JTquestions import Questions

categories = Categories()
questions = Questions()

def get_file_content(path):
    file_path = Path(__file__).parent / path
    try:
        return open(file_path, "r", encoding="utf8").read()
    except FileNotFoundError:
        return f"'{file_path}' not found."
    
def p_file(t):
    'file : LBRACE CATEGORIESLABEL COLON LBRACKET categories RBRACKET COMMA QUESTIONSLABEL COLON  LBRACKET questions RBRACKET RBRACE'

def p_categories(t):
    '''categories : TEXT
    | NUMBER
    | TEXT COMMA categories
    | NUMBER COMMA categories'''
    if len(t) == 2:
        clean_string = t[1]
        categories.add_value(clean_string)
    else:
        clean_string = t[1]
        categories.add_value(clean_string)

def p_questions(t):
    '''questions : question
                | question COMMA questions'''

def p_question(t):
    '''question : LBRACE category COMMA AIRDATELABEL COLON AIRDATE COMMA QUESTIONLABEL COLON TEXT COMMA VALUELABEL COLON VALUE COMMA answer COMMA ROUNDLABEL COLON ROUND COMMA SHOWNUMLABEL COLON NUMBER RBRACE'''
    questions.add_air_date(t[6])
    questions.add_question(t[10])
    questions.add_value(t[14])
    questions.add_round(t[20])
    questions.add_show_number(t[24])

def p_category(t):
    '''category : CATEGORYLABEL COLON TEXT
             | CATEGORYLABEL COLON NUMBER
             | CATEGORYLABEL COLON VALUE'''
    questions.add_category(t[3])

def p_answer(t):
    '''answer : ANSWERLABEL COLON TEXT
           | ANSWERLABEL COLON NUMBER
           | ANSWERLABEL COLON VALUE'''
    questions.add_answer(t[3])


def p_error(p):
    print(f'Syntax error at line {p.lineno}: {p.value}')

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_path> <output_path")
        return

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    parser = yacc.yacc()
    data = get_file_content(input_path)
    parser.parse(data)
    
    categories.create_series()
    categories.save_csv()
    
    questions.create_dataframe()
    questions.save_csv()

if __name__ == "__main__":
    main()
