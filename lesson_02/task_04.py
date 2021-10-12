#!/usr/bin/env python3
'''
Hometask for lesson2 of QA Automation course.

Part 4
1. Create a product specification dictionary with keys "title" (value of str data type),
"price" (value of numeric data type), "ingredients" (value is a list of strings).
2. Add one more key-value pair - "description": some text
3. Increase the price by 100.
4. Add one more ingredient to the list of ingredients.
5. Display the number of ingredients in the product.
6. Remove the value with the "description" key from the dictionary
'''

print("Task 1".center(50, '-'))
print("[-] Creating a product specification dictionary")
d = {'title': 'mint jelly', 'price': 3, 'ingredients': ['corn syrup', 'water', 'natural mint flavor']}

print("Created dictionary: \n", d)

print("Task 2".center(50, '-'))
print("[-] Adding one more key-value pair - \"description\"...")

d['description'] = 'Naturally flavored mint jelly'
print("Updated dictionary: \n", d)

print("Task 3".center(50, '-'))
print("[-] Increasing price on 100...")
d['price'] += 100
print("Updated dictionary: \n", d)

print("Task 4".center(50, '-'))
print("[-] Adding one more ingredient to the list of ingredients...")
d['ingredients'].append('fruit pectin')
print("Updated dictionary: \n", d)

print("Task 5".center(50, '-'))
print("[-] Displaying the number of ingredients in the product...")
print(len(d['ingredients']))

print("Task 6".center(50, '-'))
print("[-] Removing the value with the \"description\" key from the dictionary...")
d.pop('description')
print("Updated dictionary: \n", d)
