import json
import ply.lex as lex
import ply.yacc as yacc
from smd_ast import *

tokens=("TEXT","STAR","LBK","RBK","LP","RP",
        "LB","RB","VAR","PARAGRAPH","FUNC","DEF","SEP","UNDER"
        )
states = (
    ('def','inclusive'),
)

def t_TSTAR(t):
    r"\\\*"
    t.type="TEXT"
    t.value="*"
    return t

def t_TUNDER(t):
    r"\\_"
    t.type="TEXT"
    t.value="_"
    return t

def t_TLBK(t):
    r"\\\{"
    t.type="TEXT"
    t.value="{"
    return t

def t_TRBK(t):
    r"\\\}"
    t.type="TEXT"
    t.value="}"
    return t

def t_TLP(t):
    r"\\\("
    t.type="TEXT"
    t.value="("
    return t

def t_TRP(t):
    r"\\\)"
    t.type="TEXT"
    t.value=")"
    return t
    
def t_TLB(t):
    r"\\\["
    t.type="TEXT"
    t.value="["
    return t

def t_TRB(t):
    r"\\]"
    t.type="TEXT"
    t.value="]"
    return t
    
def t_TAT(t):
    r"\\@"
    t.type="TEXT"
    t.value="@"
    return t

def t_THASH(t):
    r"\\\#"
    t.type="TEXT"
    t.value="#"
    return t

def t_BACKSLAH(t):
    r"\\"
    t.type="TEXT"
    t.value="\\"
    return t

def t_def_SEP(t):
    r'\"[^"]*\"'
    t.value=t.value[1:-1]
    t.lexer.begin("INITIAL")
    return t

def t_STAR(t):
    "\*"
    return t

def t_UNDER(t):
    "_"
    return t

def t_VAR(t):
    "\$([0-9]+|[a-zA-Z][a-zA-Z_0-9]*)"
    try:
        t.value=int(t.value[1:])
    except:
        t.value=t.value[1:]
    return t

def t_FUNC(t):
    '@[a-zA-Z_][a-zA-Z_0-9]*'
    t.value=t.value[1:]
    return t

def t_DEF(t):
    '\#[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value!="#def":t.type="TEXT"
    else:t.lexer.begin("def")
    return t
    
def t_LB(t):
    "\{"
    return t

def t_RB(t):
    "\}"
    return t

def t_LBK(t):
    "\["
    return t

def t_RBK(t):
    "\]"
    return t

def t_LP(t):
    "\("
    return t

def t_RP(t):
    "\)"
    return t

def t_PARAGRAPH(t):
    r"\n\n"
    t.lexer.lineno+=2
    return t

def t_NEWLINE(t):
    r"\n"
    t.lexer.lineno+=1
    t.type="TEXT"
    return t


def t_TEXT(t):
    r"[^$@()\[\]{}*\n_]+"
    if not t.value.isspace():return t



def t_error(t):
    raise ValueError(f"Lexical error {t}")

lexer=lex.lex()

def p_start(p):
    """start : start one_def
    | start reg_block
    |
    """
    pass

def p_one_def(p):
    """one_def : DEF FUNC LP SEP RP LB smd RB
    """
    pass

def p_smd(p):
    """smd : smd reg_block
    | reg_block
    """
    pass

def p_reg_block(p):
    """reg_block : TEXT
    | STAR in_bold_italic STAR
    | UNDER in_bold_italic UNDER
    | LBK smd RBK LP TEXT RP
    | PARAGRAPH
    | FUNC LB smd RB
    | VAR
    """
    pass

def p_in_bold_italic(p):
    """in_bold_italic : TEXT
    | LBK smd RBK LP TEXT RP
    | PARAGRAPH
    | FUNC LB smd RB
    | VAR
    """
    pass

def p_error(p):
    raise ValueError(f"Syntax error {p}")

parser=yacc.yacc()

with open("sample1.smd") as f:
    smd=f.read()

lex.input(smd)
parser.parse()
