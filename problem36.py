#Write a program to find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. For example 'eat', 'ate' and 'tea' are anagrams
from collections import defaultdict
def find_anagrams(word_list):
    anagrams = defaultdict(list)

    for word in word_list:
        key = ''.join(sorted(word))
        anagrams[key].append(word)

    return [group for group in anagrams.values() if len(group) >= 1]#group the anagrams as per the condition .

anagrams=['eat', 'ate', 'done', 'tea', 'soup', 'node']
result = find_anagrams(anagrams)
for group in result:
    print(group)
#output

# ['eat', 'ate', 'tea']
# ['done', 'node']
# ['soup']