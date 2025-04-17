x = [0, 1, [2]]
x[2][0] = 3 # Here the value of the inner list is changed in the zeroth position to 3.
print(x) #output=[0, 1, [3]].
x[2].append(4)#to add 4 to the inner list to the last position.
print(x) #output=[0, 1, [3, 4]].
x[2] = 2 #it will completely change the inner list to a single number.
print(x) #output=[0, 1, 2].