#Write a program reverse.py to print lines of a file in reverse order

def charcount(filename):
    with open(filename, 'r') as f:
     r=f.readlines()
     return ' '.join(r[::-1])

p=charcount('She .txt')

print(p)
#["I'm sure that the shells are seashore shells.\n",
#  'So if she sells seashells on the seashore,\n',
#  "The shells that she sells are seashells I'm sure.\n", 
# 'She sells seashells on the seashore;\n']