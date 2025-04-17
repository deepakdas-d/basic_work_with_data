# Write a function lensort to sort a list of strings based on length.
def lensort(x):
    return sorted(x,key=len)
sr=['python', 'perl', 'java', 'c', 'haskell', 'ruby']
print(lensort(sr))#output=['c', 'perl', 'java', 'ruby', 'python', 'haskell']