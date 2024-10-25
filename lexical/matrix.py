# We should first import ply.lex in order to use the lex generator
import ply.lex as lex

# naming the tokens
# tokens' names should correspond to valid Python names
tokens=(
    "OP_BRACK",
    "CL_BRACK",
    "INT",
    "COMMA"
)

# Regular expressions of each token
t_OP_BRACK=r"\["
t_CL_BRACK=r"\]"
t_COMMA=","

# If the token is somehow complex, we define a function to process it. 
# The regular expression is defined in the docstring
def t_INT(t):
    "[0-9]+"
    t.value=int(t.value)
    return t

# The characters to be ignored
t_ignore=" \t"

# The function to call when no rule applies to a text
def t_error(t):
    raise ValueError(f"Lexical error  {t}")

# This generation the lexer if it not generated yet, otherwise it is just instanciated
lexer=lex.lex()

# This function specifies the input flow of the lexer
lexer.input("[1 2 3,2 4 5 125,,]")

# This is just a loop to display the tokens
while token:=lexer.token():
    print(token)

