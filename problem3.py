# What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well.
def concat(x):
    cat=""
    for i in x:
        cat+=i
    return cat

greetings=["hello", "world",'i','am','python']
a=concat(greetings)
print(a)#output='helloworldiampython'