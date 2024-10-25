
from abc import ABC, abstractmethod
from functools import reduce

# This is the base class of all kinds of expressions. It is abstract since we don't know
# how the compute its value
class Expression(ABC):
    @abstractmethod
    def eval(self) -> int:
        ...

# This class is a number node
class Number(Expression):
    def __init__(self,value:int) -> None:
        self.value=value
    
    def eval(self) -> int:
        return self.value

# Since addition and multiplication differ in just how to compute the value, so we use
# this class to unify creation
class BinaryOperation(Expression):
    def __init__(self,*children) -> None:
        assert len(children)>1
        self.children=children

class Addition(BinaryOperation):
    def eval(self) -> int:
        return sum([c.eval() for c in self.children])

class Multiplication(BinaryOperation):
    def eval(self) -> int:
        return reduce(lambda x,y:x*y,[c.eval() for c in self.children])


# It is always a good idea to declare data type in Python even if this is not mandatory
expr:Expression
expr=Addition(Number(1),Multiplication(Number(2),Number(3)))
print(expr.eval())
