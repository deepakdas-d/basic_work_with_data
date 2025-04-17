#Write a function group(list, size) that take a list and splits into smaller lists of given size
def group(x,s):
    n=len(x)
    ls=list()
    for i in range(0,n,s):
        ls.append(x[i:i+s])
    return ls

print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))#output=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
