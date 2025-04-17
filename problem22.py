#The above wrap program is not so nice because it is breaking the line at middle of any word. Can you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?

import textwrap #To implement the textwrap.wrap function.
def wordwrap(filename, n=20):
    with open(filename, 'r') as f:
        for line in f:
            wrapped = textwrap.wrap(line.strip(),width=n,break_long_words=False,break_on_hyphens=False)
            for i in wrapped:
                print(i)  

wordwrap('alice.txt')
# Alice was beginning
# to get very tired of
# sitting by her
# sister on the bank,
# and of having
# nothing to do.
# Once or twice she
# had peeped into the
# book her sister was
# reading,
# but it had no
# pictures or
# conversations in it,
# "and what is the use
# of a book," thought
# Alice, "without
# pictures or
# conversations?"