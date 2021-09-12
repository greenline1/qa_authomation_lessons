'''
Hometask for lesson2 of QA Automation course
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

my_string = "123"
print("Task 1")
print("Checking if the string is digit...")
print(my_string.isdigit())
print("\n")

print("Task 2")
my_string = "Hi there. How are you?"
print("Counting spaces in the string...")
print(my_string.count(" "))
print("\n")

print("Task 3")
print("Counting dots in the string...")
print(my_string.count("."))
print("\n")

print("Task 4")
print("Padding 'Homework' string with spaces, length = 100")
task_4 = "Homework"
task_4_updated = task_4.center(100, " ")
print("updated string:\n" + task_4_updated)
print("The length of updated string is " + str(len(task_4_updated)))

print("Task 5")
print("Modifying string to UPPERCASE")
print(my_string.upper())
print("\n")

print("Task 6")
print("Checking if the string ends with 'ing'...")
print(my_string.endswith("ing"))
print("\n")

print("Task 7")
print("Searching the index of first occurrence of \"a\" character in the string \"" + my_string + "\"...")
print(my_string.find("a"))
print("\n")

print("Task 8")
print("Dividing string on the two subsrings by space symbol...")
print(my_string.split(" "))
print("\n")

print("Task 9")
print("New string for this task: \"" + " "*10 + my_string + " "*8 + "\"")
print("Removing spaces on the beginning and and of the string...")
print(my_string.strip(" "))
print("\n")


