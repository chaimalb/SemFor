#This code is an implementation of the abstract syntax of arithmetic expressions containing
#of + and * operators. It is an OOP code that use inheritance and polymorphism
#to define the abstract syntax

#Notice how the function are added to all classes. The recusion is done naturally by redefining
#the functions as needed


class Node:
    """This class is abstract (but Python allows its instanciation). It is the super class of all kinds of nodes
    in the abstract tree. Python has a way to define real abstract classes but this is beyond the scope of this program.
    """
    
    def eval(self):
        """ This is an abstract function whose goal is to compute the value of the expression.
        It should be redefined in each subclass"""
        pass

    def pprint(self,prefix):
        """ This is an abstract function whose goal to pretty print the expression (as a tree). The parameter
        prefix defines the depth of the node. This function should be redefined in each subclass
        """
        pass

class Constant(Node):
    """This class corresponds to a constant in the tree. It only represents the value of the constant
    """
    
    def __init__(self,value) -> None:
        """Initialize a constant node

        Args:
            value (int): the value of the node
        """
        self.value=value
    
    def eval(self):
        return self.value
    
    def pprint(self,prefix):
        if prefix:print(f'{"  "*(prefix-1)}|_{self.value}')
        else:print(self.value)

class Operator(Node):
    """This is an abstract class representing a generic operator. It should be
    subclassed to have an Add node and Mul Note
    """
    def __init__(self,ch1,ch2) -> None:
        """Every node has two children. This constructor sets the children of the nod.

        Args:
            ch1 (Node): the first child
            ch2 (Node): the second child
        """
        self.ch1=ch1
        self.ch2=ch2

class Mul(Operator):
    """This class represents a Mul operator
    """
    def eval(self):
        return self.ch1.eval()*self.ch2.eval()
    
    def pprint(self,prefix):
        if prefix:print(f'{"  "*(prefix-1)}|_*')
        else:print("*")
        self.ch1.pprint(prefix+1)
        self.ch2.pprint(prefix+1)

class Add(Operator):
    """This class represents an Add operator
    """
    def eval(self):
        return self.ch1.eval()+self.ch2.eval()
    
    def pprint(self,prefix):
        if prefix:print(f'{"  "*(prefix-1)}|_+')
        else:print("*")
        self.ch1.pprint(prefix+1)
        self.ch2.pprint(prefix+1)

#this represents the expression (1+7)*(2+3*6)
#the indentation is used just to make things easier to understand
ast=Mul(
        Add(Constant(1),Constant(7)),
        Add(Constant(2),Mul(
            Constant(3),Constant(6))
        )
    )

#evaluate the expression
print(ast.eval())

#pretty print the expression
ast.pprint(0)

