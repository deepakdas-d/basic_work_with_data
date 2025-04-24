#Write a program to count frequency of characters in a given file. Can you use character frequency to tell whether the given file is a Python program file, C program file or a text file?
import sys

def read_word(file):
    with open(file, 'r') as f:
        txt = f.read()  # Read entire file and make characters
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
    for word, count in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
        print(word, count)
    a=filename.split('.')[-1]
    print('extention=',a)

    if(a=='py'):
        print("Python")
    elif(a=='c'):
        print('C Program')
    elif(a=='txt'):
        print('Text File')
    else:
        print('other')


    

n=sys.argv[1]
main(n)


    




