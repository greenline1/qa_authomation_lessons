#!/usr/bin/env python3
'''
Hometask for lesson2 of QA Automation course.

Part 3
Create list of the words:
1. Print the third word from the end from the list.
2. Print the 1st character of the second word of the list.
3. Print the last character of the last word of the list.
4. Add one more word to the end of the list
5. Insert another word in the middle of the list.
6. Remove the first word from the list.
7. Remove the word "world" from the list if any
'''

user_string = str(input("Enter list of the words separated by spaces: "))
word_list = user_string.split(" ")
print(word_list)

print("Task 1".center(50, '-'))
print("[-] Printing the third word from the end of the list...")
try:
    print(word_list[-3])
except IndexError:
    print("[x] A list index out of range. There are not enough words in a phrase")

print("Task 2".center(50, '-'))
print("[-] Printing the 1st character of the second word of the list...")
try:
    print(word_list[1][0])
except IndexError:
    print("[x] list index out of range. There are not enough words in a phrase")

print("Task 3".center(50, '-'))
print("[-] Printing the last character of the last word of the list...")
try:
    print(word_list[-1][-1])
except IndexError:
    print("[x] list index out of range")

print("Task 4".center(50, '-'))
print("[-] Adding one word ('OK') to the end of the list...")
word_list.append('OK')
print("Updated word list: \n", word_list)

print("Task 5".center(50, '-'))
print("[-] Insert another word ('Hello') in the middle of the list...")
word_list.insert(len(word_list)//2, 'Hello')
print("Updated word list: \n", word_list)

print("Task 6".center(50, '-'))
print("[-] Remove first word of the list...")
word_list = word_list.pop(0)
print("Updated word list: \n", word_list)

print("Task 7".center(50, '-'))
print("[-] Removing the word \"world\" from the list if any...")
try:
    word_list.remove('world')
    print("Updated word list: \n", word_list)
except ValueError:
    print('[x] There is no word "world" to remove!')
