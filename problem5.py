# #Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?
# def fact(x):
#     pro=x
#     if pro== 1:
#         return 1
#     else:
#         return pro*fact(pro-1) #recursive function.
# x=4
# print(fact(x)) # output 24
def product(x):
    pro=x
    fact=1
    while(pro>0): 
        fact*=pro
        pro-=1
    return fact
x=0
print(product(x))#output=12