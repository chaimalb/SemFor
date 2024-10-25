from __future__ import annotations
from abc import ABC, abstractmethod
from functools import reduce


# This class implements the visitor protocol (the visitor design pattern). The advantage of this protocol
# is to define as many visitor as we want without modifying the code of the base system (class expression and its subclasses).
class Visitor(ABC):
    @abstractmethod
    def visit(self,expr:Expression,*args):
        ...

# A visitor that computes the value of expressions
class EvalVisitor(Visitor):
    # Here we use a dictionary to store associate each type to its visit behavior
    def __init__(self):
        self.__visit_functions={
            Number:lambda e:e.value,
            Addition:lambda _,*args:sum(args),
            Multiplication:lambda _,*args:reduce(lambda x,y:x*y,args)
        }
    
    # Just call the right function
    def visit(self, expr: Expression,*args):
        return self.__visit_functions[type(expr)](expr,*args)


    
# This is the base class of all kinds of expressions. It is abstract since we don't know
# how the compute its value
class Expression(ABC):
    
    # This method belongs to the Visitor protocol. It establishes rules which are accepted.
    @abstractmethod
    def accept(self,v:Visitor):
        ...

# This class is a number node
class Number(Expression):
    def __init__(self,value:int) -> None:
        self.value=value
    
    # For a number, just let the visitor visit the nod
    def accept(self,v:Visitor):
        return v.visit(self)

# Since addition and multiplication differ in just how to compute the value, so we use
# this class to unify creation
class BinaryOperation(Expression):
    def __init__(self,*children) -> None:
        assert len(children)>1
        self.children=children
    
    # For the other operations, first let the visitor be accepted by all the children, then let him
    # visit the node. This method collects the result of children visit, then passes that to the visit of the current node
    def accept(self,v:Visitor):
        values=[e.accept(v) for e in self.children]
        return v.visit(self,*values)

class Addition(BinaryOperation):
    pass

class Multiplication(BinaryOperation):
    pass


# It is always a good idea to declare data type in Python even if this is not mandatory
expr:Expression
expr=Addition(Number(1),Multiplication(Number(2),Number(3)))
print(expr.accept(EvalVisitor()))
