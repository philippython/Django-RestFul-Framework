from django.test import TestCase

# Create your tests here.
# unordered_list = ["I>E", "M>I", "A>M", "D>A", "E>N"]

# def findWord(array):
#     list = [n.replace('>', "") for n in array ]
#     return list

# def sorter(unordered_array):
#     new_list = []
#     for n in unordered_array:
#         new_list.extend(n.split(">"))
#     return list(set(new_list))


# word = findWord(unordered_list)
# print(word)
# letters = sorter(unordered_list)
# print(letters)
# #
# final_word = []

# for alphabet in letters:
#     for n in word:
#         if alphabet == n[0]:
#             for fr in word:
#                if alphabet != fr[1]:
#                    print(n)
#                    word.pop()
#                    final_word.append(alphabet)
#     print(final_word)
# 🚨 Don't change the code below 👇
# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆
# print(position)
# # Write your code below this row
#  # 👇
# horizontal = int(position[0])
# # horizontal = 32[0] = 3
# vertical = int(position[1])
# #  vertical = 32[1] = 2
#
# # selected_row = map[ 2 - 1]
# # map[1]
# selected_row = map[vertical-1]
# # selected_row[3 - 1]
# # selected_row[2]
# selected_row[horizontal-1] = 'x'
#
#
# print(f"{row1}\n{row2}\n{row3}")
# #Write your code above this row 👆
#
# # 🚨 Don't change the code below
