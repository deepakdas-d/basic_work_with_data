#Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a, b, c) and (b, a, c) represent same triplet.
def triplets(n):
    ls=[]
    for i in range(1,n):
        for j in range(i,n):#avoid duplicates a+b b+a
            c=i+j
            if(c<n):
                ls.append((i,j,c))
    print(ls)
triplets(5)
#Output [(1, 1, 2), (1, 2, 3), (1, 3, 4), (2, 2, 4)]