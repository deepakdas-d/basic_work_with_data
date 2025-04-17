#Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.
def grep(pattern,filename):
    with open(filename,'r') as f:
        for i in f:
            if pattern in i:
               print(i,end=" ")
grep('sells','She .txt')
#She sells seashells on the seashore;
#  The shells that she sells are seashells I'm sure.
#  So if she sells seashells on the seashore,


