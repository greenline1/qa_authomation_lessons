def is_triangle(a: float, b: float, c: float) -> bool:
    """Check if numbers a, b, c are sides of a triangle"""
    verify_triangle_sides(a, b, c)
    if a + b > c and a + c > b and c + b > a:
        return True
    else:
        return False


def verify_triangle_sides(a: float, b: float, c: float) -> None:
    """Verify if triangle sides are floats"""
    try:
        a, b, c = float(side_1), float(side_2), float(side_3)
    except ValueError as e:
        print("Incorrect input of the triangle sides\n", e, sep="")
        exit(-1)


if __name__ == '__main__':
    print("Enter sides of a triangle one by one:")
    side_1 = input("a=")
    side_2 = input("b=")
    side_3 = input("c=")

    if is_triangle(side_1, side_2, side_3):
        print("Yes")
    else:
        print("No")
