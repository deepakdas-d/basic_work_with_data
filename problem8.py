# Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?
def cumulativesum(x):
    ls=[]
    temp=0
    for i in x:
        temp+=i
        ls.append(temp)
    return ls
lst=[1,3,5,7,9]
print(cumulativesum(lst))#output=[1, 4, 9, 16, 25]