import ply.lex as lex
import ply.yacc as yacc

# Lexical specifications start here
tokens=["OP","CP","C"]

t_OP=r"\("
t_CP=r"\)"
t_C="[^()]"

## Function to call when a token is not recognized
def t_error(t):
    print(f"Lexical error {t}")
## Generate the scanner
lexer=lex.lex()


# Syntactic and semantic specifications start here
## Function associated to non-terminal s
def p_s(p):
    """s : s t
    | t
    """
    ## First find out which rule has been used (len(p) gives how many symbols are defined in a given rule
    ## For instance, in a rule A: B C D, len(p)=4 such that p[0] refers to A, p[1] refers to B and so one.
    ## Here, there is on integer attribute (maximal depth). Si p[...] is treated as an integer.
    if len(p) == 2:
        p[0]=p[1]
    else:
        p[0]=max(p[1],p[2])

## Function associated to non-terminal t
def p_t(p):
    """t : OP s CP
    | C
    """
    ## Please refer to the solution of tutorial exercise n°3 for the semantic rules.
    if len(p)==2:
        p[0]=0
    else:
        p[0]=p[2]+1

## Function to call when a syntactic error is encountered
def p_error(p):
    print("Syntax error")

## Generate the parser
parser=yacc.yacc()

lexer.input("a(b)((c))")

pf=parser.parse()
print(f"Max depth={pf}")

