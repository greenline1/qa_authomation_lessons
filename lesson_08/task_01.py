# list comprehension tasks

# Task 01
print("task 01_01".center(30, "-"))
nth = (x ** 2 for x in range(0, 21))

print(type(nth))
for n in nth:
    print(n, end=" ")
print()

# Task 02
print("task 01_02".center(30, "-"))
predefined_list = [3, 5, 8, 11, 24, 2, 8, 11, 14]

reminders = [p % 3 for p in predefined_list]
print(type(reminders))
print(reminders)

# Task 03
print("task 01_03".center(30, "-"))
all_types_list = [True, "Hi there", "Hello 123", "111 or 222", 3.0, 5, 7, [11, 10, 'a'], {'a': 100, 'b': 200}]

int_list = [i for i in all_types_list if isinstance(i, int) or isinstance(i, float)]
print(int_list)

# Task 04
print("task 01_04".center(30, "-"))


def remove_not_alpha(string_with_digits):
    updated_string = ""
    for element in string_with_digits:
        if element.isalpha():
            updated_string += element
    return updated_string


updated_list = [remove_not_alpha(x) for x in all_types_list if isinstance(x, str)]

print(updated_list)

# Task 05
print("task 01_05".center(30, "-"))

person = {
    "name": "John",
    "surname": "Smith",
    "age": 31,
    "position": "developer",
    "address": "1111 New street",
    "skills": ["java", ".net"]
}

person_value_type = {key: type(value) for key, value in person.items()}
print(person_value_type)

person_alpha = {key: remove_not_alpha(value.lower()) for key, value in person.items() if isinstance(value, str)}
print(person_alpha)
