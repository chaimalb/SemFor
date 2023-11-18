import ply.lex as lex
import ply.yacc as yacc

tokens=("PLUS","INT","REAL")

t_PLUS=r"\+"

def t_REAL(t):
    "[0-9]+\.[0-9]+"
    t.value=float(t.value)
    return t

def t_INT(t):
    "[0-9]+"
    # The value type is used to distinguish between integer constants and float constants
    t.value = int(t.value)
    return t



def t_error(t):
    print("Erreur lexicale")
    
lexer=lex.lex()

# This is used to tell PLY that PLUS has a left associativity
precedence = (
    ('left', 'PLUS'),
)

def p_Expr(p):
    """E : E PLUS E
    | INT
    | REAL
    """
    if len(p) == 2:
        if type(p[1]) == int:
            p[0]="INT"
        else:
            p[0]="FLOAT"
    else:
        if p[1]==p[3]=="INT":
            p[0]="INT"
        else:
            p[0]="FLOAT"

def p_error(p):
    print("Erreur syntaxique")

parser=yacc.yacc()

print(parser.parse("2+5+3+5+10.6"))
