from django.test import TestCase

# Create your tests here.
"""
unordered_list = ["I>E", "M>I", "A>M", "D>A", "E>N"]

def findWord(array):
    list = [n.replace('>', "") for n in array ]
    return list

def sorter(unordered_array):
    new_list = []
    for n in unordered_array:
        new_list.extend(n.split(">"))
    return list(set(new_list))

un_list = findWord(unordered_list)
alphabets = sorter(unordered_list)
new = []
word = [new.append(char) for char in alphabets for two in un_list if char == two[0] if char != two[1] ]
print("".join(new))
"""