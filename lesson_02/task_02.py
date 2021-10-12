#!/usr/bin/env python3
import math
'''
Hometask for lesson2 of QA Automation course.
Part 2
Calculate the length of hypotenuse of right triangle with sides 367 and 127
A two-digit number is given. Find the number of tens in it.
A three-digit number is given. Find the sum of its digits.
An integer n is given. Print the next even number after it.
Given a positive float number X. Print its fractional part.
Given a positive float number X. Print its first digit after the decimal point.


'''
print("Task 1".center(50, '-'))
print("Calculating the length of hypotenuse of right triangle with sides 367 and 127...")
side_1 = 367
side_2 = 127
side_3 = round(math.sqrt(side_1 ** 2 + side_2 ** 2), 2)
print(side_3)
print("\n")

print("Task 2".center(50, '-'))
print("Finding the number of tens in two-digit number...")
try:
    a = int(input("Enter two-digit number: "))
except ValueError:
    print("[x] Value error!")
    exit(1)
b = a // 10
print(b)
print("\n")

print("Task 3".center(50, '-'))
print("Finding the sum of numbers of three-digit number...")
try:
    c = int(input("Enter three-digit number: "))
except ValueError:
    print("[x] Value error!")
    exit(1)
digit_sum = 0
for i in str(c):
    digit_sum += int(i)
print(digit_sum)
print("\n")

print("Task 4".center(50, '-'))
print("Printing the next even number after given integer...")
try:
    d = int(input("Enter an integer: "))
except ValueError:
    print("[x] Value error!")
    exit(1)
print(d+1 if d % 2 else d+2)
print("\n")

print("Task 5".center(50, '-'))
print("Printing the fractional part of given float...")
try:
    f = float(input("Enter a float: "))
except ValueError:
    print("[x] Value error!")
    exit(1)
print(f % 1)
print("\n")

print("Task 6".center(50, '-'))
print("Printing the first digit after the decimal point of given float...")
try:
    f = float(input("Enter a float: "))
except ValueError:
    print("[x] Value error!")
    exit(1)
print(int(str(f).split(".")[1][0]))
print("\n")
