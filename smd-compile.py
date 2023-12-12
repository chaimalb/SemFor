import ply.lex as lex


#Lexical specification starts here
tokens=("TEXT","STAR","LBK","RBK","LP","RP",
        "LB","RB","VAR","PARAGRAPH","FUNC","DEF","SEP","UNDER"
        )

#This is to define states of the scanner, since some tokens have special signification in some context
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

with open("sample1.smd") as f:
    text=f.read()

lexer.input(text)
    
#This code is just a test for the scanner. It should not be used in the next steps

for t in iter(lexer.token,None):print(t)


