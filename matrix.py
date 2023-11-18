import ply.lex as lex
import ply.yacc as yacc

tokens=("OB","CB","COMMA","CST")

t_OB=r"\["
t_CB=r"\]"
t_COMMA=","

def t_CST(t):
    "[0-9]+"
    t.value=int(t.value)
    return t

t_ignore=" \t"
def t_error(t):
    print(f"Lexical error {t}")
lexer=lex.lex()


#In this solution, we first build the matrix (this is actually the AST of the word).
#Because parsing and semantic analysis are done separately, this technique is both better and simpler.
def p_s(p):
    """s : OB rows CB
    """
    p[0]=p[2]

def p_lignes(p):
    """rows : one_row COMMA rows
    | one_row
    """
    if len(p)==2:
        p[0]=[p[1]]
    else:
        p[0]=[p[1]] + p[3]

def p_une_ligne(p):
    """one_row : CST
    | CST one_row
    """
    if len(p)==2:
        p[0]=[p[1]]
    else:
        p[0]=[p[1]] + p[2]

def p_error(p):
    raise ValueError(f"Syntax error {p}")

parser=yacc.yacc()

try:
    mat=parser.parse("[1 34,4 6]")
    l=len(mat[0])
    for ligne in mat[1:]:
        if len(ligne)!=l:raise ValueError("Wrong matrix format")
except ValueError as e:
    print(e)
