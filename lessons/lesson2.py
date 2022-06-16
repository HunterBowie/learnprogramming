"""
Lesson #2
Conditionals and Control Flow
"""

'''
Conditional statements check their contents to decide
whether to execute the inner block of code.
== checks for identical values
> checks for number greater on left side
< checks for number greater on right side
or evalutes to True if one of the sides is True
and evalutes to True if both sides are True
not evalutes to the inverse of the right side
'''

money = 500

if money == 0:
    print("broke")

if money < 0:
    print("in debt")

if money > 0 and money < 100:
    print("poor")

if money > 100:
    print("rich")


'''
The else and elif statements execute only if the previous
if/elif statement evaluted to False.
'''

if money == 0:
    print("still broke")

elif money < 0:
    print("still in debt")

elif money < 100:
    print("still poor")
    
else:
    print("still rich")