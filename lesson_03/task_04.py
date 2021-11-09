def is_triangle(a: float, b: float, c: float) -> bool:
    """Check if numbers a, b, c are sides of a triangle"""
    if a + b > c and a + c > b and c + b > a:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Enter sides of a triangle one by one:")
    side_1 = input("a=")
    side_2 = input("b=")
    side_3 = input("c=")
    try:
        a, b, c = float(side_1), float(side_2), float(side_3)
    except ValueError as e:
        print("Incorrect input of the triangle sides\n", e, sep="")

    if is_triangle(a, b, c):
        print("Yes")
    else:
        print("No")
