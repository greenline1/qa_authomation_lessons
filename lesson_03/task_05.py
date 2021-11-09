user_input = print("Enter three numbers:")
a = input("a=")
b = input("b=")
c = input("c=")
try:
    a, b, c = float(a), float(b), float(c)
except ValueError as e:
    print("These are not numbers")

if min(a, b, c) == a:
    if min(b, c) == c:
        b, c = c, b
elif min(a, b, c) == b:
    if min(a, c) == a:
        a, b, c = b, a, c
    else:
        a, b, c = b, c, a
elif min(a, b, c) == c:
    if min(a, b) == a:
        a, b, c = c, a, b
    else:
        a, b, c = c, b, a
print(a, b, c)
