#Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.
def enu(x):
    for i,v in enumerate(x):
        print(i,v) 

ls=["a", "b", "c"]
enu(ls)
#output
#0 a
# 1 b
# 2 c