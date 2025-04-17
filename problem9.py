# Write a function cumulative_product to compute cumulative product of a list of numbers.
def cumulativeproduct(x):
    ls=[]
    temp=1
    for i in x:
        temp*=i
        ls.append(temp)
    return ls
lst=[1,3,5,7,9]
print(cumulativeproduct(lst))#output=[1, 3, 15, 105, 945]