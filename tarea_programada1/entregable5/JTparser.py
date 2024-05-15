# ------------------------------------------------------------
# Copyright [2024] <Maria Fernanda Andres, Fabian Calvo & Andres Quesada Gonzalez>
# ------------------------------------------------------------
from pathlib import Path
import ply.yacc as yacc
import ply.lex as lex
import sys, os
from JTcategories import Categories
from JTquestions import Questions

def clean_text(text):
    cleaned_text = text.replace('\\"', '"')
    cleaned_text = cleaned_text.replace("\\'", "'")
    return cleaned_text
    
class JTParser:
    def __init__(self, **kw):
        self.categories = Categories()
        self.questions = Questions()
        lex.lex(module=self)
        yacc.yacc(module=self)

    def run(self, data):
        yacc.parse(data)
        self.categories.create_series()
        self.questions.create_dataframe()
        self.categories.save_csv()
        self.questions.save_csv()
        
class JTAnalysis(JTParser):
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

    def t_CATEGORIESLABEL(self, t):
        r'"categories"'
        return t

    def t_QUESTIONSLABEL(self, t):
        r'"questions"'
        return t

    def t_CATEGORYLABEL(self, t):
        r'"category"'
        return t

    def t_AIRDATELABEL(self, t):
        r'"air_date"'
        return t

    def t_QUESTIONLABEL(self, t):
        r'"question"'
        return t

    def t_VALUELABEL(self, t):
        r'"value"'
        return t

    def t_ANSWERLABEL(self, t):
        r'"answer"'
        t.value = t.value[1:-1]
        return t

    def t_ROUNDLABEL(self, t):
        r'"round"'
        return t

    def t_SHOWNUMLABEL(self, t):
        r'"show_number"'
        t.value = t.value[1:-1]
        return t

    def t_COMMA(self, t):
        r'\,'
        return t

    def t_COLON(self, t):
        r'\:'
        return t

    def t_LBRACKET(self, t):
        r'\['
        return t

    def t_RBRACKET(self, t):
        r'\]'
        return t

    def t_LBRACE(self, t):
        r'\{'
        return t

    def t_RBRACE(self, t):
        r'\}'
        return t

    def t_AIRDATE(self, t):
        r'\"(20[012]\d|19[89]\d)-(0[1-9]|1[0-2])-(0[1-9]|[1-2]\d|3[01])\"'
        t.value = t.value[1:-1]
        return t

    def t_VALUE(self, t):
        r'\"\$(\d+|\,)+\"|null'
        if t.value == 'null':
            t.value = "$0"
        else:
            t.value = t.value[1:-1]
        return t

    def t_NUMBER(self, t):
        r'\"\d+\"'
        t.value = t.value[1:-1]
        return t

    def t_ROUND(self, t):
        r'"((Double\s|Final\s)?Jeopardy!|Tiebreaker)"'
        t.value = t.value[1:-1]
        return  t

    def t_TEXT(self, t):
        r'\".+?(?=(?<!\\)")\"'
        t.value = t.value[1:-1]
        return t
    
    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)
    
    t_ignore = " \t"

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
    
    def p_file(self, t):
        'file : LBRACE CATEGORIESLABEL COLON LBRACKET categories RBRACKET COMMA QUESTIONSLABEL COLON  LBRACKET questions RBRACKET RBRACE'

    def p_categories(self, t):
        '''categories : TEXT
        | NUMBER
        | TEXT COMMA categories
        | NUMBER COMMA categories'''
        if len(t) == 2:
            self.categories.add_value(clean_text(t[1]))
        else:
            self.categories.add_value(clean_text(t[1]))

    def p_questions(self, t):
        '''questions : question
                    | question COMMA questions'''

    def p_question(self, t):
        '''question : LBRACE category COMMA AIRDATELABEL COLON AIRDATE COMMA QUESTIONLABEL COLON TEXT COMMA VALUELABEL COLON VALUE COMMA answer COMMA ROUNDLABEL COLON ROUND COMMA SHOWNUMLABEL COLON NUMBER RBRACE'''
        self.questions.add_air_date(t[6])
        self.questions.add_question(clean_text(t[10]))
        self.questions.add_value(t[14])
        self.questions.add_round(t[20])
        self.questions.add_show_number(t[24])

    def p_category(self, t):
        '''category : CATEGORYLABEL COLON TEXT
                | CATEGORYLABEL COLON NUMBER
                | CATEGORYLABEL COLON VALUE'''
        self.questions.add_category(clean_text(t[3]))

    def p_answer(self, t):
        '''answer : ANSWERLABEL COLON TEXT
            | ANSWERLABEL COLON NUMBER
            | ANSWERLABEL COLON VALUE'''
        self.questions.add_answer(clean_text(t[3]))


    def p_error(self, p):
        print(f'Syntax error at line {p.lineno}: {p.value}')