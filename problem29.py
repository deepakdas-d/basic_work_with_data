# Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:
def array(m,n):
    return [[None for i in range(m)] for j in range(n)]
a=array(3,4)
a[0][0]=5
for r in a:
    print(r)
    #[5, None, None, None]
# [None, None, None, None]
# [None, None, None, None]
