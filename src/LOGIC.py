#####################################
# Imports                           #
#####################################
import ply.yacc as yacc
import ply.lex as lex
from operator import (add,  sub, mul, truediv, pow) 
#####################################

#####################################
# List of tokens                    #
#####################################
tokens = (
    # data types
    "NUM",
    "FLOAT",    
    # athemetic operations   
    "PLUS",
    "MINUS",
    "MUL",
    "DIV",
    "POW",
    # brackets
    "LPAREN",
    "RPAREN",
)
#####################################
# Regular expression for the tokens #
#####################################
t_PLUS    =  r"\+"
t_MINUS   =  r"\-"
t_MUL     =  r"\*"
t_DIV     =  r"/"
t_LPAREN  =  r"\("
t_RPAREN  =  r"\)"
t_POW     =  r"\^"
# spaces and tabs will be ignored
t_ignore  =  r"     "

# adding rules with actions
def t_FLOAT(t):
    r"\d+\.\d+"
    t.value = float(t.value)
    return t

def t_NUM(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"keyword not found: {t.value[0]}\nline {t.lineno}")
    t.lexer.skip(1)

def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")

#####################################
# list of operators                 #
#####################################
ops = {
    '+' : add,  '-' : sub,
    '*' : mul,  '/' : truediv,   
    '^' : pow,  
}
#####################################
# Setting precedence of symbols     #
#####################################
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('right', 'UMINUS'),
)
#####################################
# Writing BNF rule                  #
#####################################
def p_expression(p):
    """expression : expression PLUS factor
                | expression MINUS factor
                | expression DIV factor
                | expression MUL factor
                | expression POW factor"""
    if (p[2], p[3]) == ("/",  0):
        # if  division is by 0 puttinf 'inf' as value 
        p[0] = float('INF')
    else:  
        p[0] = ops[p[2]](p[1], p[3])

def p_expression_uminus(p):
    "expression : MINUS expression %prec UMINUS"
    p[0] = -p[2]

def p_expression_factor(p):
    'expression : factor'
    p[0] = p[1]

def p_factor_num(p):
    """factor : NUM
            | FLOAT"""
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

#####################################
# Error rule for syntax errors      #
#####################################
def p_error(p):
    print(f"Syntax error in {p.value}")
#####################################

#####################################
# Variables                         #
#####################################
lexer = lex.lex()
parser = yacc.yacc()
#####################################

#####################################
# This function does calulation     #
#####################################
def evaluate(cmd: str) -> str:
    try:
        result = parser.parse(cmd)
        return str(result)
    except AttributeError:
        return "nan"
#####################################
