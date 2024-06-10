# In OOP we are working with objects that have certain class 
# (they are an instance of a specific class) like for example:
def hello():
	print("hello")
print(type(hello))
# Class defines the way an object is interacting with other object in a program. 


# Functions or methods define what we are doing with objects. 
# Like making the string all capital letters 
# so working on object with class string with built in method of `upper()`:
string = "hello"
print(string.upper())


def func_new():
    print("one, two")
output = func_new()
# This function returns no value
print(output)


# Running functions:
def main():
	func1()
	func2()
	func1()
	
def func1():
    print('One')

def func2():
    print('Two')

if __name__ == "__main__": main()


# Running functions with default values:
def main():
	func1(3)
	func1(a)
	
def func1(a=1):
    print(a)
if __name__ == "__main__": main()


# New class in Python:
class Cat:
    def miau(self):
        print("miau")


# If we assign a parameter 'c' to a class it become an instance of a class Cat. 
# So when we want to check what type the object is (what class) 
# we will get the the information that it belong to class Cat:
c = Cat()
print(type(c))


# "Main" with underscored is the default module. 
# The output shows where the class was defined. 
# If we use this method on an object we will execute the 'miau' function:
c.miau()


# If we expand this class and add a new function like 'minus_one' 
# we can perform operations on the 'c' object:
class Cat:
    def miau(self):
        print("miau")
    def minus_one(self, x):
        return x - 1
c = Cat()
print(type(c))
print(c.minus_one(3))


# Adding attributes like 'name' to a class is through 'init' method (the constructor) 
# allows to reference them after the parameter:
class New_class:
	# Constructor
	def __init__(self, person_name = "Tim"):
		self.person_name = person_name
		
	def whatName(self):
		return self.person_name

def main():
    new_person = New_class()
    old_person = New_class("Oldie")
    print(new_person.whatName())
    print(old_person.whatName())

if __name__ == "__main__": main()


# Adding attributes like 'name' to a class is through 'init' method 
# allows to reference them after the parameter:
class Cat:
    def __init__(self, name):
        self.name = name
        print(name)
    def miau(self):
        print("miau")
    def minus_one(self, x):
        return x - 1
c = Cat('Bad')
print(c.name)


''' 'Self' serves as a reference to the current instance of the class 
and is used to access variables and methods that belong to the class. 
It is a refence to instantiated object. 
This mechanism allows each object to keep track of its own data and behavior, 
enabling the creation of multiple instances of a class, each with its own distinct state.
We use 'self' because we need to pass 'c' object itself so that we know which we are accessing: '''
class Cat:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
c = Cat('Bad')
print(c.get_name())
c2 = Cat('Very Bad')
print(c2.get_name())


# We can use methods to change values assigned to a class:
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
c = Cat('Bad',3)
c.set_age(2)
print(c.get_name())
print(c.get_age())

c2 = Cat('Very Bad',1)
c2.set_age(2)
print(c2.get_name())
print(c2.get_age())


# We create classes so that we can have multiple instances of them 
# instead of assigning them one by one:
# Basic way of assigning parameters
cat1_name = "Bad"
cat1_age = 3
cat2_name = "Very Bad"
cat2_age = 1
# Not scalable way of assigning parameters
cats_name = ["Bad", "Very Bad"]
cats_age = [3,1]


# Classes introduction with simple Fibonacci series:
# the sum of two elements defines the next set
class Fibonacci():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b

f = Fibonacci(0, 1)
for r in f.series():
    if r > 100: break    
    print(r, end=' ')


# Let's create a more useful example of a class with parameters:
class Employee:
    def __init__(self, name, age, level) -> None:
        self.name = name
        self.age = age
        self.level = level # 0 - 100

    def get_level(self):
        return self.level
    
class Job:
    def __init__(self, name, max_employees) -> None:
        self.name = name
        self.max_employees = max_employees
        self.employees = []
    def add_employee(self, employee):
        if len(self.employees) < self.max_employees:
            self.employees.append(employee)
            return True
        return False
    def get_avg_level(self):
        value = 0
        for employee in self.employees:
            value += employee.get_level()
        return value / len(self.employees)

e1 = Employee("Mark", 33, 20)
e2 = Employee("Bob", 33, 25)
e3 = Employee("Bill", 33, 32)

job = Job("OpenAI",2)
job.add_employee(e1)
job.add_employee(e2)
print(job.employees)
# Show the name of the first employee in "OpenAI"
print(job.employees[0].name)
# Show average level
print(job.get_avg_level())


# Variable number of arguments in a function
def new_func(*args):
    total = sum(args)
    return total

new_func(2,1)


# Variable number of keyword arguments in a function:
def variable_length(**kwargs):
    print(f"{len(kwargs)} keyword arguments passed:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

variable_length(days=1, day="Wednesday", users=3)




















