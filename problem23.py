#Write a program center_align.py to center align all lines in the given file.
import textwrap

def centeralign(filename,n=20):
    with open(filename,'r')as f:
        for line in f:
            wrapped=textwrap.wrap(line.strip(),n,break_long_words=False)
            for i in wrapped:
                print(i.center(n))

centeralign('alice.txt')
#Alice was beginning 
# to get very tired of
#    sitting by her
# sister on the bank,
#    and of having
#    nothing to do.
#  Once or twice she
# had peeped into the
# book her sister was
#       reading,
#    but it had no
#     pictures or
# conversations in it,
# "and what is the use
# of a book," thought
#   Alice, "without
#     pictures or
#   conversations?"