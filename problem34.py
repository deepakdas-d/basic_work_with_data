# def fre(word):
#     f={}
#     for w in word:
#         f[w]=f.get(w,0)+1
#     return f
# print(fre('hello'))
#{'h': 1, 'e': 1, 'l': 2, 'o': 1}

#Improve the above program to print the words in the descending order of the number of occurrences in a file .
import sys

def read_word(file):
    with open(file, 'r') as f:
        txt = f.read().split()  # Read entire file and split into words
        return txt 
def freq(txt):        
    fre = {}
    for j in txt:
        fre[j] = fre.get(j, 0) + 1
    return fre

def main(filename):
    words=read_word(filename)
    frequency={}
    frequency = freq(words)
    for word, count in frequency.items():
        print(word, count)

if __name__ == "__main__":
    main(sys.argv[1])

