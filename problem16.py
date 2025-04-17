#Write a function extsort to sort a list of files based on extension.
def extsort(x):
    return sorted(x, key=lambda s: s.split('.')[-1])#we use split to seperate the filename into two by using '.' then accessing the extention using [-1]the we sort by that.
ls = ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']
print(extsort(ls))


