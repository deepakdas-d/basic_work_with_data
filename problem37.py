#Write a function valuesort to sort values of a dictionary based on the key.
def valuesort(x):
    return sorted(x,reverse=True)
d={'x': 1, 'y': 2, 'a': 3}
print(valuesort(d.values()))
#Output

# [3, 2, 1]