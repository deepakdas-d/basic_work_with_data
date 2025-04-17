 #Write a program to print each line of a file in reverse order.
def charcount(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
    return ' '.join(words[::-1])
p=charcount('She .txt')

print(p)
#shells seashore are shells the that sure I'm seashore,
#the on seashells sells she if So sure. 
#I'm seashells are sells she that shells The seashore;
#  the on seashells sells She