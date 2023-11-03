#This code is an implementation of the abstract syntax of arithmetic expressions containing
#of + and * operators. It is an OOP code that the visitor design pattern.

#The main advantage of this implementation is that it is possible any kind of processing 
#over the nodes of the AST without modifying the source code of the AST. We just have to add
#a new visitor.


class Node:
    """This class is abstract (but Python allows its instanciation). It is the super class of all kinds of nodes
    in the abstract tree. Python has a way to define real abstract classes but this is beyond the scope of this program.
    """

    def accept(self,visitor,*args,**kwargs):
        """For the protocol of the Visitor design pattern. args and kwargs are  respectively the
        optional parameters and keyword parameters of the visitor

        Args:
            visitor (Visitor): the visitor has a method called visit_... that visit each kind of nodes
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
    
    def accept(self,visitor,*args,**kwargs):
        """For a Constant node, visiting just expose the object to the visitor

        Args:
            visitor (Visitor): the visitor

        Returns:
            Any: the return value if any
        """
        return visitor.visit_constant(self,*args,**kwargs)

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
    
    def accept(self,visitor,*args,**kwargs):
        """For a Mul node, the visit consists of visiting the children, then the node is exposed to the visitor

        Args:
            visitor (Visitor): the visitor

        Returns:
            Any: the return value if any
        """
        self.ch1.accept(visitor,*args,**kwargs)
        self.ch2.accept(visitor,*args,**kwargs)
        return visitor.visit_mul(self,*args,**kwargs)
    


class Add(Operator):
    """This class represents an Add operator
    """
    
    def accept(self,visitor,*args,**kwargs):
        """For a Add node, the visit consists of visiting the children, then the node is exposed to the visitor

        Args:
            visitor (Visitor): the visitor

        Returns:
            Any: the return value if any
        """
        self.ch1.accept(visitor,*args,**kwargs)
        self.ch2.accept(visitor,*args,**kwargs)
        return visitor.visit_add(self,*args,**kwargs)


# this represents the expression (1+7)*(2+3*6)
# the indentation is used just to make things easier to understand
ast=Mul(
        Add(Constant(1),Constant(7)),
        Add(Constant(2),Mul(
            Constant(3),Constant(6))
        )
    )


class Visitor:
    """The is an abstract class for all visitors of the nodes. All visitors should
    extend this class in order to add a new kind of visitor.
    """
    
    def dispath(self,node,*args,**kwargs):
        """Remind that unlike Java, Python does not have method overloading since it is not
        strong typed. Instead, we need a dispath function to redirect the call to the right type

        Args:
            node (Node): the nod to visit

        Raises:
            TypeError: if the node is supported

        Returns:
            Any: the return value if any
        """
        if type(node)==Constant:
            return self.visit_constant(node,*args,**kwargs)
        elif type(node)==Mul:
            return self.visit_mul(node,*args,**kwargs)
        elif type(node)==Add:
            return self.visit_add(node,*args,**kwargs)
        else:
            raise TypeError("Unsupported node type")

    
    def visit_constant(self, constant,**kwargs):
        """visiting a Constant node.

        Args:
            constant (Constant): the constant to visit
        """
        pass
    
    def visit_add(self,add,*args,**kwargs):
        """visiting an Add node.

        Args:
            constant (Add): the node to visit
        """
        pass
        
    def visit_mul(self,mul,*args,**kwargs):
        """visiting a Mul node.

        Args:
            constant (Mul): the node to visit
        """
        pass


class EvalVisitor(Visitor):
    """This class represents a visitor that computes the value of the expression
    """
    
    def visit_constant(self, constant,*args,**kwargs):
        """For a constant, just return its value

        Args:
            constant (Constant): the constant to visit

        Returns:
            int: the value of the constant
        """
        return constant.value
    
    def visit_add(self, add,*args,**kwargs):
        """For an Add node, just add the values of children

        Args:
            add (Add): the Add node to visit

        Returns:
            int: the sum of the values of the children
        """
        return self.dispath(add.ch1,**kwargs) + self.dispath(add.ch2,*args,**kwargs)
    
    
    def visit_mul(self, mul,*args,**kwargs):
        """For a Mul node, just multiply the values of children

        Args:
            add (Mul): the Mul node to visit

        Returns:
            int: the product of the values of the children
        """
        return self.dispath(mul.ch1,**kwargs) * self.dispath(mul.ch2,*args,**kwargs)


class PrettyPrinterVisitor(Visitor):
    """A visitor that pretty prints the expression. For all the methods of this class,
    a parameter n defines the depth of the node.
    """
    
    def visit_constant(self, constant,*args,**kwargs):
        """For a constant, return a string representation of the constant with regard to its depth

        Args:
            constant (Constant): the constant to visit

        Returns:
            string: a string representation of the constant
        """
        if kwargs["n"]:return f'{"  "*(kwargs["n"]-1)}|_{constant.value}'
        else:f"{constant.value}"
    
    def visit_add(self, add,*args,**kwargs):
        """For an Add node, return a string representation of the constant with regard to its depth. The function
        first starts by visiting the children that it visits the Add node

        Args:
            constant (Add): the node to visit

        Returns:
            string: a string representation of the node
        """
        s=self.dispath(add.ch1,n=kwargs["n"]+1)
        t=self.dispath(add.ch2,n=kwargs["n"]+1)
        if kwargs["n"]:return f'{"  "*(kwargs["n"]-1)}|_+\n{s}\n{t}'
        else:return(f"+\n{s}\n{t}")
    
    def visit_mul(self, mul,*args,**kwargs):
        """For an Mul node, return a string representation of the constant with regard to its depth. The function
        first starts by visiting the children that it visits the Mul node

        Args:
            constant (Mul): the node to visit

        Returns:
            string: a string representation of the node
        """
        s=self.dispath(mul.ch1,n=kwargs["n"]+1)
        t=self.dispath(mul.ch2,n=kwargs["n"]+1)
        if kwargs["n"]:return f'{"  "*(kwargs["n"]-1)}|_*\n{s}\n{t}'
        else:return(f"+\n{s}\n{t}")
        
#Create the evaluation visitor
print("Value =",ast.accept(EvalVisitor()))

#Create the pretty-printing visitor
print(ast.accept(PrettyPrinterVisitor(),n=0))
