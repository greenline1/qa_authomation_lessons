def is_year_leap(year: int) -> bool:
    """Check if year is leap"""
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False


if __name__ == '__main__':
    try:
        year = int(input("Enter a year to check if it is leap:\n"))
        if is_year_leap(year):
            print("Yes")
        else:
            print("No")
    except ValueError as e:
        print("Year should be an integer\n", e, sep="")




