#import the lex and yacc modules from package ply
import ply.lex as lex
import ply.yacc as yacc

################################
#Let's create the scanner first#
################################

#the names of the tokens
tokens=("IF","ELSE","INST","A")

#the regular expression of each token
t_IF="if"
t_ELSE="else"
t_INST="inst"
t_A="a"

#tokens to ignore
t_ignore=" \t"

#generate the scanner
lexer=lex.lex()

################################
#Now, let's create the parser  #
################################

#Each non-terminal has its own function
#whose name is p_name_of_non_terminal
#the first function p_... corresponds to
#the axiom

#The production rules of each non-terminal are defined
#in the docstring. Here, I used capital letters to note
#the terminals, and lower-case letters to note the non-terminals
#(this is not mandatory). For the moment, the function does only
#syntactic analysis, its body is empty
def p_start(p):
    """s : IF cdt s
    | IF cdt s ELSE s
    | INST
    """
    pass

#The production function correponds to the non-terminal cdt
def p_cdt(p):
    """cdt : A
    """
    pass

#Generation of the parser code (this is made once)
parser=yacc.yacc()

#Specify the string to parse. You can test
#other input like "if inst" just to see the behavior of the parser
#with a wrong input
lexer.input("if a if a inst else inst")

#Launch the parser.
parser.parse()
