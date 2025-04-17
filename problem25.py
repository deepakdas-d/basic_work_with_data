#Python provides a built-in function map that applies a function to each element of a list. Provide an implementation for map using list comprehensions.
def sq(x):
    return x*x
num=map(sq,range(5))
print(list(num))
#output [0, 1, 4, 9, 16]