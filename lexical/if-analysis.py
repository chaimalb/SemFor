from __future__ import annotations

from abc import ABC
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


############# Abstract Tree Structures ###############
class Stmt(ABC):
    pass

class Inst(Stmt):
    def __str__(self) -> str:
        return "Inst()"

class If(Stmt):
    def __init__(self,cdt:Cdt,child1:Stmt,child2:Stmt=None) -> None:
        self.cdt=cdt
        self.child1=child1
        self.child2=child2
        
    def __str__(self) -> str:
        if self.child2:
            return f"If({self.cdt},{self.child1},{self.child2})"
        else:
            return f"If({self.cdt},{self.child1})"

class Cdt:
    def __init__(self,name:str) -> None:
        self.name=name
    
    def __str__(self) ->str:
        return f"Cdt({self.name})"
        
    

def p_s(p):
    """s : IF cdt s
    | IF cdt s ELSE s
    | INST
    """
    if len(p)==4:# this is the first rule
        p[0]=If(p[2],p[3])
    elif len(p)==6:
        p[0]=If(p[2],p[3],p[5])
    else:
        p[0]=Inst()

def p_cdt(p):
    """cdt : A1
    | A2
    | A3
    """
    p[0]=Cdt(p[1])

def p_error(p):
    raise ValueError("Syntax Error")

parser=yacc.yacc()

lexer.input("if a1 if a2 inst else inst")

print(parser.parse())


