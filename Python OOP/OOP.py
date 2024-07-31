from datetime import date


# Class with static methods for mathematical operations
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod    
    def PI():
        return 3.14

# -----------------------------------------------------
# Class to represent a pizza
class Pizza:
    def __init__(self, radius, ingredients):
        self.__radius = radius
        self.__ingredients = ingredients 

    @classmethod 
    def veg(cls):
        return cls(6, ["mushroom", "olives", "onions"])
    
    @classmethod 
    def margherita(cls):
        return cls(6, ["mozzarella", "sauce"])

    def __str__(self):
        return f"Pizza ingredients are {', '.join(self.__ingredients)}"

    def area(self):
        return Pizza.circle_area(self.__radius)
    
    @staticmethod 
    def circle_area(r):
        return r ** 2 * Math.PI()

# Creating pizza instances
pizza1 = Pizza(6, ["tomato", "olives"])
pizza2 = Pizza.margherita()
pizza3 = Pizza.veg()

print(pizza1)
print(pizza2)
print(pizza3)
print(pizza1.area())

# -----------------------------------------------------
# Class to represent a person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"My name is {self.name} and I am {self.age} years old\n"

# Class to represent a man, extending from Person
class Man(Person):
    gender = 'Male'
    no_of_men = 0

    # Constructor method to initialize a man with a name, age, and voice
    def __init__(self, name, age, voice):
        super().__init__(name, age)
        self.voice = voice
        Man.no_of_men += 1

    # Method to describe the man, including voice
    def describe(self):
        string = super().describe()
        return string + f"I have a {self.voice} voice.\n"

# Creating instances of Person and Man
person_1 = Person("John", 40)
print(person_1.describe())

man_1 = Man("Mike", 35, "deep")
print(man_1.describe())

# -----------------------------------------------------
# Class to represent a student
class Student:
    no_of_students = 0

    def __init__(self, name, age=0, courses='none'):
        self.__name = name 
        self.__age = age 
        self.__courses = courses
        Student.no_of_students += 1

    def describe(self):
        print(f"My name is {self.__name} and my age is {self.__age}")

    def is_old(self, num):
        if self.__age <= num:
            print("Student is not old")
        else:
            print("Student is not young")

    def get_name(self):
        return self.__name 

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age 

    def set_age(self, new_age):
        self.__age = new_age

    @classmethod   
    def init_from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

# Creating student instances
student_1 = Student("Islam", 30, ['CS', 'IT'])
student_2 = Student("Ahmed", 25, ['CS', 'IT'])

# Modifying student_1 details
student_1.set_name("Reham")
student_1.set_age(50)
student_1.describe()

# Creating student_3 and student_4 using class method
student_3 = Student("Islam", 20)
student_4 = Student.init_from_birth_year("Ahmed", 1993)
student_4.describe()

# -----------------------------------------------------
# Using Math class methods
x = Math.add(5, 10)
print(x)
