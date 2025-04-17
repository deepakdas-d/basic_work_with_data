#Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.
def unique(z):
    return set(z)
sr=["python", "java", "Python", "Java"]
lsr=list(map(str.lower,sr))
print(list(unique(lsr)))#output=['java', 'python']



''''''''
# def unique(seq, key=lambda x: x):
#     seen = set()
#     result = []
#     for item in seq:
#         val = key(item)
#         if val not in seen:
#             seen.add(val)
#             result.append(item)
#     return result
# sr = ["python", "java", "Python", "Java"]
# print(unique(sr, key=str.lower))
