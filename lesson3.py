Python 3.14.8 (tags/v3.14.8:8e6e75d, Sep 30 2026, 18:19:33) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = "alex"
age = 25
score = 100

print(name)
alex
print(age)
25
print(score)
100

name = "sarah"
age = 22
score = 90


print(name)
sarah
print(age)
22
print()score)
SyntaxError: unmatched ')'
print(score)
90

a, b, c = 5, 3.2, 'Hello'

print (a)  # prints 5
print (b)  # prints 3.2
print (c)  # prints Hello
SyntaxError: multiple statements found while compiling a single statement

score = 100
score = score + 10
print(score)
SyntaxError: multiple statements found while compiling a single statement

name = "Alex"
age = 25
print(name + ", you are " + str(age) + " years old")
SyntaxError: multiple statements found while compiling a single statement
print(name + ", you are " + str(age) + " years old")
sarah, you are 22 years old


name = "Emily"
age = 20
print(f"{name}, you are {age} years old")
SyntaxError: multiple statements found while compiling a single statement
name = "emily"
age = 20
print(f"{name}, you are {age} years old")
emily, you are 20 years old

name = "jane"
age= 25

print(" hello, {}! you're {} years old.".formate(name, age))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(" hello, {}! you're {} years old.".formate(name, age))
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
print(" hello, {}! you're {} years old.".format(name, age))
 hello, jane! you're 25 years old.

name = "peter"
age = 55
print("hello {1} you are{0} years old".format(age, name))
hello peter you are55 years old



print("hi whats you're name" input)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("hi whats you're name", input)
hi whats you're name <built-in function input>
name= input("what is you're name: ")
what is you're name: craig
colour= input("whats you're favourite colour: ")
whats you're favourite colour: blue
food= input("what is you're favourite food: ")
what is you're favourite food: pizza
age= input("how old are you, ")
how old are you, 40
print(name, colour, food, age)
craig blue pizza 40
print("hi {0}, you're favourite colour is {1}, you're food is {2}, and {3} is getting a big number now")
hi {0}, you're favourite colour is {1}, you're food is {2}, and {3} is getting a big number now
print("hi "{0}", you're favourite colour is "{1}", you're food is "{2}", and "{3}" is getting a big number now")
SyntaxError: invalid syntax. Is this intended to be part of the string?
print("hi {0}, you're favourite colour is {1}, you're food is {2}, and {3} is getting a big number now".format(name, colour, food, age))
hi craig, you're favourite colour is blue, you're food is pizza, and 40 is getting a big number now



name= input("what is you're name ")
what is you're name craig
adult_tickets= input("how many adult tickets would you like ")
how many adult tickets would you like 2
child_tickets= input("how many child tickets would you like ")
how many child tickets would you like 2
total_cost = (adult_tickets * 10) + (child_tickets * 6)
print(f"hello{name}, your total cost is £{total_cost}.")
hellocraig, your total cost is £2222222222222222.
adult_tickets= int(input("how many adult tickets would you like "))
how many adult tickets would you like 2
child_tickets= int(input("how many child tickets would you like "))
how many child tickets would you like 2
>>> total_cost = (adult_tickets * 10) + (child_tickets * 6)
>>> print(f"hello {name}, your total cost is £{total_cost}.")
hello craig, your total cost is £32.
>>> 
>>> 
>>> name= "py thon"
>>> age = 101
>>> course= learn python from beginner to advanced
SyntaxError: invalid syntax
>>> course= "learn python from beginner to advanced"
>>> current_course_attendance= 100%
SyntaxError: invalid syntax
>>> current_course_attendance= 100
>>> no_of_assignments_completed= 5
>>> whether_the_student_has_completed_the_course= "yes"
>>> 
>>> 
>>> name= "sam"
>>> age=19
>>> attendance= 85.5
>>> assignments= 7
>>> 
>>> age = age+ 1
>>> attendance = attendance + 5
>>> assignments = assignments + 1
>>> 
>>> print(name)
sam
>>> print(age)
20
>>> print(attendance)
90.5
>>> print(assignments)
8
>>> 
