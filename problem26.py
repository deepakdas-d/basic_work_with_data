#Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true. Provide an implementation for filter using list comprehensions.
def isodd(n):
    return n%2!=0
num=filter(isodd,range(10))
print(list(num))
#output [1, 3, 5, 7, 9]