"""
Lesson #1
Variables and Data Types
"""

'''
A variable is a block of computer memory that
stores some data.
'''

variable = 42

'''
Different data types such as
integer, string, floating point, and boolean
define how that data is used throughout the program.
These are usually called primitive data types.
'''

counter = 0
message = "eat your vegetables"
pi = 3.14159
happy = True
nothing = None

'''
You can perform various operations with data such as ...
multiply: *
divide: /
'''

counter = counter + 9
new_message = message + "sometimes"
pi_squared = pi * pi
happy = not happy

number = 8 + 8 * 4 # what does this evalute to?

'''
Built in python functions give you simple ways to 
perform useful tasks.
input(prompt) -> inputted value
print(message) -> None
int(value) -> integer
str(value) -> string
'''

value = input("give me a value!")
print(value)
value_size = len(value)
string_value = str(91)
integer_value = int("91")