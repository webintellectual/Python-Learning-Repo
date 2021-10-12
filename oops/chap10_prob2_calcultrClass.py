import math

class Calculator:
    def cube(self,n):
        return n*n*n
    def square(self,n):
        return n*n
    def squreRoot(self,n):
        return math.sqrt(n)

object = Calculator()
print(object.squreRoot(81))
print(object.square(9))
print(object.cube(7))
print(object.squreRoot(20))