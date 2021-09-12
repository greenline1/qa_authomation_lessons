#!/usr/bin/env python3
'''
Hometask for lesson2 of QA Automation course.

>>> usage = 'python3 task_01.py "Some input string for experiments"'
Part 1
Tip: use strings methods
1. Check if a string is number
2. Count the number of spaces in a string
3. Count the number of dots in a string
4. Create string with text "Homework". Modify it in a string with  100 character length with "Homework" in the middle
and pad it with spaces from the both sides. Display the length of new string.
5. Modify string to UPPERCASE
6. Check if string ends with "ing"
7. Find the index of first occurrence of "a" character in the string
8. Divide string on the list of subsrings by space symbol
9. Let string start and end with spaces. Find method that removes that spaces from the beginning and the end,
but not in the middle of the phrase
'''


def main(argv):
    input_string = str(argv[1])

    print("Input string is: " + "\"" + input_string + "\"")
    print("Task 1")
    print("Checking if the string is digit...")
    print(input_string.isdigit())
    print("\n")

    print("Task 2")
    print("Counting spaces in the string...")
    print(input_string.count(" "))
    print("\n")

    print("Task 3")
    print("Counting dots in the string...")
    print(input_string.count("."))
    print("\n")

    print("Task 4")
    print("Padding 'Homework' string with spaces, length = 100")
    task_4 = "Homework"
    task_4_updated = task_4.center(100, " ")
    print("updated string:\n" + task_4_updated)
    print("The length of updated string is " + str(len(task_4_updated)))
    print("\n")

    print("Task 5")
    print("Modifying string to UPPERCASE")
    print(input_string.upper())
    print("\n")

    print("Task 6")
    print("Checking if the string ends with 'ing'...")
    print(input_string.endswith("ing"))
    print("\n")

    print("Task 7")
    print("Searching the index of first occurrence of \"a\" character in the string \"" + input_string + "\"...")
    print(input_string.find("a"))
    print("\n")

    print("Task 8")
    print("Dividing string on the list of subsrings by space symbol...")
    print(input_string.split(" "))
    print("\n")

    print("Task 9")
    print("New string for this task: \"" + " " * 10 + input_string + " " * 8 + "\"")
    print("Removing spaces on the beginning and and of the string...")
    print(input_string.strip(" "))
    print("\n")


if __name__ == '__main__':
    def _script_io():
        from sys import argv

        main(argv)

    _script_io()
