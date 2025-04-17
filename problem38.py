#Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.
def invertdict(x):
    invert={v: k for k, v in x.items()}
    return invert
print(invertdict({'x': 1, 'y': 2, 'z': 3}))

