#Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively
from collections import deque
def head(filename,n=10):

    with open(filename,'r') as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            print(line, end='')
def tail(filename,n=10):
    with open(filename,'r')as f:
        lastlines=deque(f,maxlen=n)
        for line in lastlines:
            print(line,end='')
    

head('sun.txt')#The sun was rising gently over the hills.
# Birds chirped softly from the trees nearby.
# Dewdrops sparkled on the grass like tiny gems.
# A cool breeze moved through the tall pines.
# Everything felt fresh and peaceful.
# The small stream flowed steadily past the rocks.
# Its sound was like a quiet song in the distance.
# A rabbit hopped across the clearing without a sound.
# Flowers began to open toward the light.
# Insects buzzed lazily in the warm air.
print()
print()
print()
tail('sun.txt')
# A squirrel darted from one tree to another.
# Clouds drifted slowly across the pale sky.
# The day had only just begun.
# Leaves rustled gently with the wind.
# The earth smelled rich after the nightâ€™s rain.
# Footprints marked the damp trail by the woods.
# No voices could be heardâ€”only nature.
# Time felt slower in this quiet place.
# The moment was calm and perfect.
# It was a peaceful morning, full of promise.