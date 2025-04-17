#Write a function reverse to reverse a list. Can you do this without using list slicing?
def reverse(x):
    ls=[]
    n=len(x)
    while(n>0):
        ls.append(n)
        n-=1
    return ls
list1=[1,2,3,4,5]
print(reverse(list1))# Output: [5, 4, 3, 2, 1]
