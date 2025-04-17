#Write a function unique to find all the unique elements of a list.
def sort(s):
    exist=list()#two lists to arrnge list item regarding the dulicate and original
    noexist=list()
    for i in s:
        if i in exist:
            noexist.append(i)
        else:
            exist.append(i)
    return exist

ls=[1,2,3,1,5,4,3,5,2]
print(sort(ls))

