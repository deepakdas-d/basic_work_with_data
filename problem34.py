def fre(word):
    f={}
    for w in word:
        f[w]=f.get(w,0)+1
    return f
print(fre('hello'))

