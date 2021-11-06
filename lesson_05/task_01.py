from datetime import datetime


class Person:
    """
    Creates Person object
    """

    def __init__(self, fullname, year_of_birth):
        """
        Constructor for Person class

        :param fullname: str
        :param year_of_birth: str
        """
        self.fullname = fullname

        if 1900 < year_of_birth < datetime.now().year:
            self.year_of_birth = year_of_birth
        else:
            raise ValueError('Year of birth is not between 1900 and current year')

    def get_name(self):
        """Return name from full name"""

        return self.fullname.split()[0]

    def get_lastname(self):
        """Return last name from full name"""

        return self.fullname.split()[1]

    def age_in(self, year=None): # pay attention on place where datetime.now().year is calculated. Here it is calculated when class is created
        if year is None:
            year = datetime.now().year # Calculated when this method is called
        return year - self.year_of_birth


if __name__ == '__main__':
    p1 = Person("John Smith", 1970)
    print(p1.fullname)
    print(p1.year_of_birth)
    print(p1.age_in(2012))
    print(p1.age_in())
    print(p1.get_name())
    print(p1.get_lastname())
