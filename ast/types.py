import ply.lex as lex
import ply.yacc as yacc


tokens=(
    "PLUS",
    "INT",
    "FLOAT"
)

t_PLUS=r"\+"

def t_FLOAT(t):
    "[0-9]+\.[0-9]+"
    t.value="FLOAT"
    return t

def t_INT(t):
    "[0-9]+"
    t.value="INT"
    return t
    


t_ignore=" \t"

def t_error(t):
    raise ValueError(f"Wrong char {t}")

precedence=(
    ("left","PLUS"),
)

def p_e(p):
    """e : e PLUS e
    | val
    """
    if len(p)==4:
        if p[1]=="INT" and p[3]=="INT":
            p[0]="INT"
        else:
            p[0]="FLOAT"
    else:
        p[0]=p[1]

def p_val(p):
    """val : INT
    | FLOAT
    """
    p[0]=p[1]

def p_error(p):
    raise ValueError("Syntax error")

lexer=lex.lex()
parser=yacc.yacc()

lexer.input("1+2+5.0")
print(parser.parse())
