# To start REPL which stands for Read-Eval-Print Loop and run Python directly 
# without any files open a terminal or command prompt and type:
python
>>> 


# Clear terminal (console):
> clear


# Code can be executed directly in terminal as script files:
> python main.py


# Or it can be executed as a module when imported to another py file:
import my_module


'''When a py file contains a definition of a function that can be used elsewhere a separation of definitions of functions and classes from the executable code is useful. Test code can be executed only when script file is started directly. 
To avoid execution of the code when imported as module we use (part that follows will execute only when py file is executed directly):'''
if __name__ == "__main__":


# Stating path to the interpreter used to run the script example (this is not obligatory):
#!/usr/bin/python3


# Default code indentation should be 4 spaces:
def main():
    print("Print")


# Check basic venv settings in powershell console:
python --version
pip --version
pip list


# Basic system information:
import sys
print(sys.version)
print(sys.winver)
print(sys.gettrace)
print(sys.argv)


# Help on basic packages:
import pandas as pd
help(pd)


# Data types:
number = 3.4
print(int(number))
print(float(number))
print(str(number))
print(type(number))
print(type(str(number)))
print(type(int(number)))
str(number)


# For reading input from the keyboard, Python provides the `input()` function:
print('What is your name?')
name = input()
print(name)
# input numbers
first_number = int(input('Type the first number: ')) ;\
second_number = int(input('Type the second number: ')) ;\
print("The sum is: ", first_number + second_number)


# Boolean logic:
# equals
a == b
# not equals
a != b
# other
a < b
a > b
a <= b
a >= b


# Assigning value conditionally (conditional expression):
a, b = 0, 1
s = 'less than' if a < b else 'not less than'
print (s)

a, b = 0, 1
print('one' if a < b else 'two')


# Conditional execution - If statement:
a = 1
b = 1
if a > b:
#statement to be run
    print("a")
elif a == b: # else if
    print("c")
else:
    print("b")


# Nested if statement:
a = 3
b = 2
c = 1
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")


# Operator "or":
a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)


# Operator "and":
a = 34
b = 34
if a == 34 and b == 34:
    print(a + b)


# Strings are immutable so changing strings require assigning them to a new variable:
fact = "The Moon has no atmosphere."
two_facts = fact + "No sound can be heard on the Moon."
print(two_facts)

# Dealing with problem of single and double quotation marks in the string with triple quotation marks:
fact = """We only see about 60% of the Moon's surface, this is known as the "near side"."""


# Strings multiline solutions:
# String manipulations
string_example = "Temperatures and facts. \n Data about the moon. "

# Initial capital letters
print(string_example.title())
# Create a list of words out of a sentence
print(string_example.split())
# Create a list of parts based on split character
parts = string_example.split("D")
print(parts)
print(parts[-1])
# Split into sentences
print(string_example.split('. '))
# Create a list of lines out of a sentence
print(string_example.split('\n'))
# Show index of a substring with minus one if not found
print(string_example.find('moon'))
# How many times a substring is present
print(string_example.count('moon'))
# Convert to lower case
print(string_example.lower())
# Convert to upper case
print(string_example.upper())


# String manipulations
string_example = "Temperatures and facts. \n Data about the moon. "

# Initial capital letters
print(string_example.title())
# Create a list of words out of a sentence
print(string_example.split())
# Create a list of parts based on split character
parts = string_example.split("D")
print(parts)
print(parts[-1])
# Split into sentences
print(string_example.split('. '))
# Create a list of lines out of a sentence
print(string_example.split('\n'))
# Show index of a substring with minus one if not found
print(string_example.find('moon'))
# How many times a substring is present
print(string_example.count('moon'))
# Convert to lower case
print(string_example.lower())
# Convert to upper case
print(string_example.upper())


# Extract numbers from string:
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)


# Replace and join string:
# Replacing all occurences of a string with a fixed new string which works like Find and Replace Control + H
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))
# Create a string out of a list with a space between each element
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))


# Show only sentences with a specific word
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
sentences = text.lower().split('. ')
for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)


# Place variable in a string:
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")


# Input multiple variables
print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))


# Place a text manipulation function:
subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)


# While loop as Fibonacci series:
a, b = 0, 1
while b < 50:
    print(b)
    a, b = b, a + b


















