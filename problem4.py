#Implement a function product, to compute product of a list of numbers.
def product(x):
    pro=1
    for i in x: 
        pro*=i
    return pro
x=[4,3,1]
print(product(x))#output=12