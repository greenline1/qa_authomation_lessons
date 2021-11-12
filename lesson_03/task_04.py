def is_triangle(a: float, b: float, c: float) -> bool:
    """Check if numbers a, b, c are sides of a triangle"""
    if not verify_triangle_sides(a, b, c):
        return False
    else:
        print("ok")
        a, b, c = float(a), float(b), float(c)
        if a + b > c and a + c > b and c + b > a:
            return True
        else:
            return False


def verify_triangle_sides(a: float, b: float, c: float) -> bool:
    """Verify if triangle sides are floats"""
    try:
        a, b, c = float(side_1), float(side_2), float(side_3)
        return True
    except ValueError:
        print("Incorrect input of the triangle sides\n", sep="")
    return False


def find_triangle_type(a, b, c):
    """Make additional checks of triangle type"""
    if not is_triangle(a, b, c):
        return "Not a triangle"
    elif a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a==c:
        return "Isosceles triangle"
    else:
        return "Versatile triangle"


if __name__ == '__main__':
    print("Enter sides of a triangle one by one:")
    side_1 = input("a=")
    side_2 = input("b=")
    side_3 = input("c=")

    sides = [side_1, side_2, side_3]

    if is_triangle(*sides):
        print("Yes")
    else:
        print("No")

    print(find_triangle_type(*sides))
