# Write a function dups to find all duplicates in the list.
def dups(x):
    seen = set()
    duplicates = set()
    for i in x:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
    return list(duplicates)

ls = [1, 2, 3, 1, 5, 4, 3, 5, 2]
print(dups(ls))  # Output: [1, 2, 3, 5]


