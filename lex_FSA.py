# This is to emulate the head of the tape
head=0

# This is to emulate the tape
word=""

def next_char():
    ''' This function returns the current character on the tape
    then take the pointer to the next position. At the end of the word,
    it return \0
    '''
    # This is to tell that head and word are global variables. This is not a good idea in fact.
    global head
    global word
    if head<len(word):
        c=word[head]
        head+=1
        return c
    else:
        return '\0'

def lex(w):
    ''' This function detects the token in the input (it only detects one token in the
        input). It simulates the FSA (Finite State Automaton) given the slides of chapter 1
    '''
    
    # Again, this is not a good idea
    global head
    global word
    
    # Put the head at the beginning
    head=0
    
    # Define the state as initial
    state=0
    
    # Write the word on the tape
    word=w
    
    # Let's emulate the FSA
    while state>=0:
        c=next_char()
        if c=='\0':
            break
        if state==0:
            if c=='i':state=2
            elif 'a'<=c<='z' or 'A'<=c<='Z':state=1
            else:state=-1
        elif state==1:
            if 'a'<=c<='z' or 'A'<=c<='Z' or '0'<=c<='9':state=1
            else:state=-1
        elif state==2:
            if c=='f':state=3
            elif 'a'<=c<='z' or 'A'<=c<='Z' or '0'<=c<='9':state=1
            else:state=-1
        elif state==3:
            if 'a'<=c<='z' or 'A'<=c<='Z'  or '0'<=c<='9':state=1
            else:state=-1

    # Test whether the state of FSA is final
    if state==1:print("Identifier")
    elif state==3:print("Keyword if")
    else:print("Error")

# The test
lex("if")
