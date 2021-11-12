from datetime import datetime


class Person:
    """Create a Person object"""

    def __init__(self, fullname='', year_of_birth=None):
        """Constructor for a Person class"""
        self.year_of_birth = year_of_birth
        self.fullname = fullname
        if year_of_birth < 1900 or year_of_birth > datetime.now().year:
            raise ValueError('Year of birth is not between 1900 and current year')
        if len(self.fullname.strip().split()) != 2:
            raise ValueError('Fullname should consist of Firstname and Lastname')

    def __str__(self):
        """Print information about a Person object"""
        return f"name: {self.fullname},\nyear of birth: {self.year_of_birth}"

    def get_name(self):
        """Return name from full name"""
        return self.fullname.split()[0]

    def get_lastname(self):
        """Return last name from full name"""
        return self.fullname.split()[1]

    def age_in(self,
               year=None):  # Pay attention on place where datetime.now().year is calculated. Here it is calculated when class is created
        """Calculate difference between given year and year of birth. Default value - current year"""
        if year is None:
            year = datetime.now().year  # Calculated when this method is called
        return year - self.year_of_birth


class Employee(Person):
    """Create an Employee object"""

    def __init__(self, fullname='', year_of_birth=None, position='', experience=0, salary=0):
        Person.__init__(self, fullname, year_of_birth)
        self.position = position
        self.experience = experience
        self.salary = salary

        if experience < 0:
            raise ValueError("Experience should not be negative number")
        if salary < 0:
            raise ValueError("Salary should be not a negative value")

    def __str__(self):
        return f"name: {self.fullname},\n" \
               f"year of birth: {self.year_of_birth},\n" \
               f"position: {self.position},\n" \
               f"salary: ${self.salary}\n" \
               f"experience: {self.experience} year(s)\n"

    def extend_position(self):
        """Return Junior/Middle/Senior extension to a position based on an experience"""
        if self.experience > 6:
            return "Senior " + self.position
        elif 3 <= self.experience <= 6:
            return "Middle " + self.position
        else:
            return "Junior " + self.position

    def increase_salary(self, amount):
        """Increase salary on specified amount"""
        if amount >= 0:
            self.salary += amount
        else:
            raise ValueError('Amount for salary increasing is incorrect')


class ITEmployee(Employee):
    """Create an IT Employee object"""

    def __init__(self, fullname='', year_of_birth=None, position='', experience=0, salary=0, skills=None):
        Employee.__init__(self, fullname, year_of_birth, position, experience, salary)
        self.skills = skills

    def __str__(self):
        return f"name: {self.fullname},\n" \
               f"year of birth: {self.year_of_birth},\n" \
               f"position: {self.position},\n" \
               f"salary: ${self.salary}\n" \
               f"experience: {self.experience} year(s)\n" \
               f"skills: {self.skills}\n"

    def add_skill(self, *skills):
        if self.skills is None:
            self.skills = []
        else:
            for skill in skills:
                self.skills.append(skill)


if __name__ == '__main__':
    p1 = Person("John Smith", 1970)
    print(p1.fullname)
    print(p1.year_of_birth)
    print(p1.age_in(2012))
    print(p1.age_in())
    print(p1.get_name())
    print(p1.get_lastname())
    print(p1.__str__())

    e1 = Employee("Jane Smith", 1972, "HR", 2, 75000)
    print(e1.fullname)
    print(e1.year_of_birth)
    print(e1.age_in(2012))
    print(e1.age_in())
    print(e1.get_name())
    print(e1.get_lastname())
    e1.increase_salary(7000)
    print(e1.__str__())

    i1 = ITEmployee("Jacob Smith", 1992, "developer", 7, 150000, skills=['java', '.net'])
    print(i1.fullname)
    print(i1.year_of_birth)
    print(i1.age_in(2012))
    print(i1.age_in())
    print(i1.get_name())
    print(i1.get_lastname())
    i1.add_skill('python')
    i1.increase_salary(5000)
    print(i1.__str__())
