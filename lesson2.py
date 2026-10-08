Python 3.14.8 (tags/v3.14.8:8e6e75d, Sep 30 2026, 18:19:33) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print(25)
25
print("this is another line") #this is also a comment
this is another line

name="alex"
age=25
price=19.99
passed=True

print(type(name))
<class 'str'>
print(type(age))
<class 'int'>
print(type(price))
<class 'float'>
print(type(passed))
<class 'bool'>

age="25"
print(age) #this will print the age
25
print(type(age)) #this will display the data type
<class 'str'>


num=inout('enter a number: ')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    num=inout('enter a number: ')
NameError: name 'inout' is not defined. Did you mean: 'input'?
num=input('enter a number: ')
enter a number: 55
print('you entered:', num)
you entered: 55
print('data type of num:', type(num))
data type of num: <class 'str'>
num = int(input("Enter a number: ")) #convert the input into an integer

print("You Entered:", num)
print("Data type of num:", type(num))
SyntaxError: multiple statements found while compiling a single statement
num = int(input("Enter a number: ")) #convert the input into an integer
Enter a number: 55
print~("you entered:", num)
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("you entered:", num)
you entered: 55
print("data type of num:" type(num))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("data type of num:", type(num))
data type of num: <class 'int'>

name= input("what is your name?") #expects a string
what is your name?
name= input("what is your name?") #expects a string
what is your name?craig
print("hello", name)
hello craig
age=int(input("how old are you?")) #expects a integer
how old are you?40
print("you are", age, "years old\n") #\n adds new line
you are 40 years old

print("data type of name:", type(name))
data type of name: <class 'str'>
print("data type of age:", type(age))
data type of age: <class 'int'>


# print with end whitespace
print('Good Morning!', end= ' ')
Good Morning! 
print('it is rainy today')
it is rainy today


player_one="scooby doo"
level= 2
health=65.5
scared=True

print("data type of player_one:", type(player_one))
data type of player_one: <class 'str'>
print("data type of level:", type(level))
data type of level: <class 'int'>
print("data type of health:", type(health))
data type of health: <class 'float'>
print("data type of scared:", type(scared))
data type of scared: <class 'bool'>


name = "Jordan"
age = "19"
mark = 67.5
passed = "True"

print("Name: " + name)
print("Age next year: " + age + 1)
print("Mark: " + mark)
print("Passed: " + passed)
SyntaxError: multiple statements found while compiling a single statement

name="jordan"
age="19"
mark="67.5"
passed=True
>>> 
>>> print("Name: " + name)
... print("Age next year: " + age + 1)
... print("Mark: " + mark)
... print("Passed: " + passed)
SyntaxError: multiple statements found while compiling a single statement
>>> print("name: " + name)
name: jordan
>>> print("age next year: " +age +1)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print("age next year: " +age +1)
TypeError: can only concatenate str (not "int") to str
>>> print("age next year: " age + 1)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("age next year: ", age + 1)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print("age next year: ", age + 1)
TypeError: can only concatenate str (not "int") to str
>>> age=19
>>> print("age next year: ", age + 1)
age next year:  20
>>> print("mark: ", + mark)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print("mark: ", + mark)
TypeError: bad operand type for unary +: 'str'
>>> print("mark: ", mark)
mark:  67.5
>>> print("passed: ", passed)
passed:  True
>>> 
>>> 
>>> 
