#Reimplement the unique function implemented in the earlier examples using sets.
def unique(x):
   return set(x)
ls=[1,2,3,1,5,4,3,5,2]
print(list(unique(ls)))#output=[1, 2, 3, 4, 5]