#Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.
import textwrap

def wrap(filename, n=20):
    with open(filename, 'r') as f:
        for line in f:
            wrapped = textwrap.wrap(line.strip(), n)
            for i in wrapped:
                print(i)  

wrap('She .txt')  
#She sells seashells
# on the seashore;
# The shells that she
# sells are seashells
# I'm sure.
# So if she sells
# seashells on the
# seashore,
# I'm sure that the
# shells are seashore
# shells.
