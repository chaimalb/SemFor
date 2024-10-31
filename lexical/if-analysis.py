import ply.lex as lex
import ply.yacc as yacc

########Les noms des unités lexicales
tokens=(
    "A1",
    "A2",
    "A3",
    "IF",
    "ELSE",
    "INST"
)

########Leurs expressions régulières
t_A1="a1"
t_A2="a2"
t_A3="a3"
t_IF="if"
t_ELSE="else"
t_INST="inst"



t_ignore  = " \t"

def t_error(t):
    print(f"Incorrect char {t.value[0]}")
    

lexer = lex.lex()

def p_s(p):
    """s : IF cdt s
    | IF cdt s ELSE s
    | INST
    """
    pass

def p_cdt(p):
    """cdt : A1
    | A2
    | A3
    """
    pass

def p_error(p):
    raise ValueError("Syntax Error")

parser=yacc.yacc()

lexer.input("if a1 if a2 inst else inst")

parser.parse()
