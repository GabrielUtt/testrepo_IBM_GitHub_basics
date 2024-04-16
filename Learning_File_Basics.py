
# This would be a single line comment in Python

""" This would be a
multiline comment in Python """


# A variable is initialized the first time a value is stored in it

x = 15
y = 4


# -------- ARITHMETIC OPERATORS ----------
print(' ')
print(' -------- Arihmetic Operators ------')

""" print() is a funtion. It can take multiple arguments to be printed.
See for more: https://www.programiz.com/python-programming/methods/built-in/print
or other sources... """

""" String literals in python are surrounded by either single quotation marks,
or double quotation marks """

print('the following statments hold for x = ' + str(x) + ' and y = ' + str(y) + ':')

# Addition: +
# x + y = 19
print('x + y =',x+y)

# Subtraction: -
# Output: x - y = 11
print('x - y =',x-y)

# Multiplication: *
# Output: x * y = 60
print('x * y =',x*y)

# Division: /
# Output: x / y = 3.75
print('x / y =',x/y)

# Floored Division: Result of division is rounded down
# Output: x // y = 3
print('x // y =',x//y)
# Carefull with negative results:
# Output: -x // y = -4
print('-x // y =',-x//y)

# Exponent: **
# Output: x ** y = 50625
print('x ** y =',x**y)

# Modulus/Remainder: %
# Output: x % y = 3
print('x % y =',x%y)

# Order of Operations: **, *, /, //, %, +, -

# -------- DATA TYPES ----------
print(' ')
print(' -------- Data Types ------')

# Integers: -2, -1, 0, 1, 2, 3
# Floating-point numbers: -1.25, -1.0, 3.4
# Strings: 'a','aa','Hello',' '

# convert to string: str()
# Output: 15 minus 4 euqals 11
print(str(x) + ' minus ' + str(y) + ' equals ' + str(x-y))

# convert to integer or float: int(), float()
# Output: x * y = 60
a = '5'
b = '6'
# Output: 5 * 6 = 30
print('5 * 6 =',int(a)*int(b))
# int() can be used to round floating-point numbers down, e.g. int(7.7) yield 7
# int() cuts of decimals and thus differs from // operator for negative numbers!
# Output: -x // y = -4
print('-x // y =',-x//y)
# Output: int(-x/y) = -3
print('int(-x / y) =',int(-x/y))

# -------- VARIABLES ----------

# Naming Rules: Only letters, numbers, underscore character (_), can't begin with a number
# variable names are case sensitive
# pyhton convention: start with lowercase letter


# ----------- COMPARISON OPERATORS -----------------
print(' ')
print(' -------- Comparison Operators ------')
x = 10
y = 12
print('the following statments hold for x = ' + str(x) + ' and y = ' + str(y) + ':')

# Boolean values: True, false

# Equal to: ==
# Output: x == y is False
print('x == y is',x==y)

# Greater than: >
# Output: x > y is False
print('x > y  is',x>y)

# Less than: <
# Output: x < y is True
print('x < y  is',x<y)

# Not equal to:
# Output: x != y is True
print('x != y is',x!=y)

# Greater than or equal to:
# Output: x >= y is False
print('x >= y is',x>=y)

# Less than or equal to:
# Output: x <= y is True
print('x <= y is',x<=y)

print(' ') #print() ends with newline by default

# Comparison of data types:
# Operators can actually work with values of any data type:
# Output: 'hello' == 'hello' is True
print("'hello' == 'hello' is ",'hello' == 'hello')
# Remark: python does not distinguish between integer and floating-point
# numbers when comparing
# Output: 10 == 10.0 is True
print('10 == 10.0 is',10==10.0)
# Strings cannot be compared to numbers:
# Output: 10 == '10' is False
print("10 == '10' is",10=='10')

# -------------- BOOLEAN OPERATORS (and, or, not) ---------------
print(' ')
print(' -------- Boolean Operators ------')
x = True
y = False
print('the following statments hold for x = ' + str(x) + ' and y = ' + str(y) + ':')

# Output: x and y is False
print('x and y is',x and y)

# Output: x or y is True
print('x or y is',x or y)

# Output: not x is False
print('not x is',not x)

# Important Note:
# Python interprets any non-zero value as True. None and 0 are interpreted as False.

# -------------- FLOW CONTROL STATEMENTS ---------------
# ----------------------- IF STATEMENTS ---------------
""" Python code is grouped together in blocks. A block begins when indentation
increases and ends when indentation decreases """
x = 10
y = 12

# if statements:
""" In Python, an if statement consists of the following:
 The if keyword, a condition, a colon:
     an intended block of code"""
if x != y:
    print("If-Condition is True")

# else statement:
""" an if statement can optionally be followed by an else statement. The
else keywords starts on the same intendation level as the if statement.
it does not contain a condition and is followed by a colon: """
if x == y:
    print("If-Condition is True")
else:
    print("Else-Condition is True")

# elif statement:
""" elif statements allow to check for multiple conditions. elif statemenst
are only executed if all of the previous conditions were false, so the
order of elif statements is important"""

if x == y:
    print("If-Condition is True")
elif x > y:
    print("First Elif-Condition is True")
elif x < y:
    print("Second Elif-Condition is True")
else:
    print("cannot happen")

# ----------------------- WHILE LOOP STATEMENTS ---------------
""" in Pyhton, a while statement consists of the following:
The while keyword, a condition, a colon:
    an intended block of code
In a while loop, the condition is always checked at the start of each iteration"""

# Example while loop: Add integers up to n:
n = 10
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter
print("The sum is", sum)

# Example while loop: demand correct user input
magicword = 'please'
userinput = '' #variable needs to be initialized befor being used in flow control statement
while userinput != magicword:
    userinput = input('Please say please:')
print('Thank you')

# break, continue statements
""" break statements can be used to break out of a while loop's clause early,
continue statements can be used to jump back to the beginning of the loop
and reevaluate the loop's condition
break and continue statements can also be used in for loops """

# example: break statement
while True: # creates an infinity loop
    print('Please input a valid name')
    name=input()
    if name !='':
        break
print('Thank you!')

# Important note: if you get stuck in an infinity loop, press CTRL+C

# example: continue statement
while True:
    print('Who are you? (Hint: Joe)')
    name = input()
    if name != 'Joe':
        continue # jumps back to beginning of loop
    print('Hello Joe. What is the password (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')



# ----------------------- FOR LOOPs and the range() function ---------------
""" The for loop in Python is used to iterate over a sequence (list, tuple, string)
or other iterable objects (e.g. the output of the range() function
IN Python, a foor loop statement consists of the following:
The for keyword, a variable name, the in keyword,  a sequence, a colon:
    an intended block of code"""
# the range function:
"""The range() function generates a sequence of numbers and can take up
to three arguments: range(start, stop, step size). For efficiency reasons, the
range function does not store the generates values in memory. To
output the values, we can use the function list():"""
# examples range function:

# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))

# Important note: In Python, an index starts with zero and ends with n-1

# Output: [2, 3, 4, 5, 6, 7]
print(list(range(2, 8)))

# Output: [2, 5, 8, 11, 14, 17]
print(list(range(2, 20, 3)))

for i in range(5):
    print(str(i) + '^2 equals ' + str(i**2))

# ---------- The pass statement

# The pass statement is used as a placeholder for future implementations of
# loops, functions, etc. It results in NOP (no operation)

# examples:
for counter in range(10):
    pass

def emptyfunction(*args):
    pass

emptyfunction()

# ------------------ IMPORTING MODULES ------------------
""" Python comes with a set of modules called the 'standard library'.
Each module is a Python program that contains a related group of functions
that can be embedded in your programs. Before you can use the functions
in a module, you must import the module with an import statement
The synthax of accessing functions and objects from imported modules
depeons on the type of import statement"""

import random
print("Your lotto numbers are:")
for i in range(6):
    print(random.randint(1,45))


""" In the previous example, if you use the import syntax
            from random import *
    you don't need to access the random. prefix to access
    functions from the random module. This might make the
    code less readable and traceable, however """ 

# You can import multiple modules with one statement
import random, math

# ---------------- FUNCTIONS ------------------------

""" In Python, a function is a group of related statements that perform a specific
task. Functions help to avoid repetition and make code reusable. The syntax to
define a function contains the following:
keyword def, function name, (parameters)
    docstring (optional)
    intended block of code
    return statement (optional) """
def hello(name):
    """This function greets with name"""
    print('hello ' + str(name))
        
# Calling a function - type in the function name with appropriate parameters
hello('Joe')

# docstring
""" A docstring is a string literal that occurs as the first
statement in a function (or module, object, method definition).
Always use triple quotes for docstrings. A docstring should summarize
the purpose of the function (module, class,..) it is describing"""

# docstrings can be accessed using the help function
help(hello)
help(len)
# The return statement
""" Each function evaluates to a value. By default, a function
evaluates to None (None is a data type representing the absence
of a value). The return statement is used to exit a function and
return a specific value/expression"""

import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Sure'
    elif answerNumber == 2:
        return 'Maybe'
    else:
        return 'Nope'

r = random.randint(1,2)
answer = getAnswer(r)
print(answer)

# Function Arguments
""" Usually arguments are identified by their position in the
function call (example: range() function). However, so called
'keyword arguments' are identified by the keyword put befor them
in the function call. For example, the print function has the
keyword argument end: """

for i in range(10):
    print(i,end=' ') #using blank instead of newline as end character
print(" ")

# *args, **kwargs
""" In Python, we can create functions accepting a variable number of
arguments using special the special symbols
*args (non keyword arguments)
**kwargs (keyword arguments)"""

# examples *args:
""" use an asterisk * before the parameter name to pass  a non-keyworded variable
length argument list to the function. The argument list makes a tuple inside the
function with the same name as the parameter excluding the asterisk *."""

def addnumbers(*nums): 
    sum = 0
    for i in nums:
        sum = sum +i
    return sum

total = addnumbers(2,3,5)
# Output: total: 10
print("total: "+str(total))
total = addnumbers(1,7,9,11,3,5)
# Output: total: 36
print("total: "+str(total))

def multOfSum(multiplicator,*numbs):
    sum = 0
    for i in numbs:
        sum = sum + i
    sum = sum * multiplicator
    return sum

total = multOfSum(2,3,5)
# Output: total: 16
print("total: "+str(total))

# example **kwargs
""" use a double asterisk * before the parameter name to pass keyworded variable
length argument list to the function. The argument list makes a dictionary inside the
function with the same name as the parameter excluding the double asterisk **."""

def personalData(**data):
    for key, value in data.items():
        print("{} is {}".format(key, value))

personalData(name="John",email="John@gmx.at")
personalData(name="Alice",phone=4312345,country="Austria")


# later: unpacking arguments (ObOrP, p 212)

# --------------------NAMESPACE AND SCOPE --------------------

# Names
""" A name (or identifier) in Python is simply a name given to an object
(Everything in Python is an object). A name is a way to access the underlying
object. For example, if we do the assignment:"""
a = 2
""" then 2 is an object stored in memory and a is the name we associate with it"""

b = print("Hello") # names can even be used for functions
# Output: Hello
b

# Namespaces

""" a namespace is a collection of names. It can be imagined as a mapping of every
name you have defined to corresponding objects. A namespace containing all the
built-in names is created every time we start Python. Each module creates its own
global namespace. Namespaces can co-exist but are completely isolated, so that
the same names that may exist in different modules do not collide. When functions
are called they create a local namespace (similarly, with classes)."""

# Scope

""" The various unique namespaces defined can usually not be accessed from
every part of the program. Scope refers to the portion of the program from where
a namespace can be accessed directly without any prefix. Think of a scope as a
container for variables. When a scope is destroyed (e.g. a function is exited),
the scope and all variables in the scope/container are destroyed.

At any moment, there are
at least three nested scopes:
1. Scope of the current function which has local names
2. Scope of the module which has global names
3. Outermost scope which has built-in names
When a reference is made inside a function, the name is first searched at the
lowest level (local namespace), then in the global namespace and finally, in the
built-in namespace. (Consequence?)

The advantage of a local scope is that, for example, when variables are modified
by the code in a particular call to a function, the function interacts with
the rest of the program only through its parameters and the return value. This
narrows down the number of code lines that may be causing a bug (e.g. a
variable being set to a bad value). It's a bad habit to rely on global variables,
it is encouraged to write functions without global variables. """

# Example of scope and Namespace in Python

""" The following functions illustrate the behavior of local and global variables
To simplify your life, avoid using local variables with the same name as a global
variable (as opposed to these examples)"""

def outer_function():
    # global a
    a = 20
    def inner_function():
        # global a
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)
     
a = 10
# Output:
# a = 30
# a = 20
# a = 10
outer_function()
print('a =',a)

def outer_function():
    global a # the global statement allows to initiate/modify a global variable
    # from within a function
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)
     
a = 10
# Output:
# a = 30
# a = 30
# a = 30
outer_function()
print('a =',a)

def outer_function():
    global a
    a = 20
    def inner_function():
       # global a
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)
     
a = 10
# Output:
# a = 30
# a = 20
# a = 20
outer_function()
print('a =',a)

def outer_function():
    # global a
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)
     
a = 10
# Output:
# a = 30
# a = 20
# a = 30
outer_function()
print('a =',a)

# --------------------------- DATA TYPES IN PYTHON -------------------------

# The LIST Data Type

""" In Python, a list is a value that contains multiple values in an ordered
sequence. A list can hold any number of items. A list is created by placing
items inside a square bracket. The different items are separated by commas."""

# example, creating a list

intList = [3,5,7,10]
# Output: intList: [3, 5, 7, 10]
print("intList:",intList)

"""One list may hold different types (integer, strings, floats, lists,
tuples, dictionarie, (self-defined) objects,..."""

mixedList = [3,'five',7.0,[10,20,30],[],(1,2,3),{'name':'Joe','age':45},print('hello')]
# Output: mixedList: [3, 'five', 7.0, [10, 20, 30],[],(1, 2, 3), {'name': 'Joe', 'age': 45}, None]
print("mixedList:",mixedList) # The item [] represents an empty list

# Accessing individual items of a list using indices

# output: mixedList[0]: 3
print("mixedList[0]:", mixedList[0]) # The first value in the list is at index 0 !!!

# output: mixedList[0]: 3
print("mixedList[0]:", mixedList[0])

# output: mixedList[3]: [10, 20, 30]
print("mixedList[3]:", mixedList[3])

# accessing individual items of lists/sequences in lists

# output: mixedList[3][1]: 20
print("mixedList[3][1]:", mixedList[3][1])

# output: mixedList[5][2]: 3
print("mixedList[5][2]:", mixedList[5][2])

# output: mixedList[6]['name']: Joe
print("mixedList[6]['name']:", mixedList[6]['name'])

# negative indices: The integer value of -1 refers to the last item of a list a.s.o

# output: mixedList[-1]: None
print("mixedList[-1]:", mixedList[-1])

# Getting sublists with slices
""" A slice can cet several values from a list in the form of a new list. The old list
remains unchanged. A slice is typed between square brackets, but is has up to to
integers plus a colon. A slice goes up to, but will not include the value at the
second index:"""

# output: mixedList[3:5]: [[10, 20, 30], []]
print("mixedList[3:5]:", mixedList[3:5])

# output: mixedList[:3]: [3, 'five', 7.0]
print("mixedList[:3]:", mixedList[:3]) # Leaving out the first index = starting with 0

# output: mixedList[5:]: [(1, 2, 3), {'name': 'Joe', 'age': 45}, None]
print("mixedList[5:]:", mixedList[5:]) # Leaving out the second index = until end of list

# changing values in a list with indices

a = ['old','old','old']
a[1] = 'new'
# Output: ['old','new','old']
print(a)

# removing values of a list using the del statement

del a[1]
# Output: ['old','old']
print(a)

# ------- List Methods ----------
"""An object is characterized by its attributes (data) and behaviors. Behaviors are
actions that can occur on an object. The behaviors that can be performed on a specific
class of objects (like lists) are called methods. Methods are like functions, but
the have automatically access to all the data associated with this object. Like
functions, methods can accept parameters and return values"""



""" Lists are objects that have a number of methods that can be invoked upon them, e.g.:
- append(element)
- insert(index, element)
- count(element)
- index(element)
- find(element)
- reverse()
- sort()

To look up information about list methods, use:

"""

dir(list) # getting all methods of a list
help(list.append) # getting info about append method of list

""" A good overview of available list methods can be found here:
https://www.programiz.com/python-programming/methods/list """

# adding elements to lists:

a.append('new')
# Output: ['old','old','new']
print(a)
# -------sorting values in a list

"""without any parameters, sort will generally do the expected things. Strings
will be placed in alphabetical order (case sensitive!), numbers will be sorted
in numerical order, a list of tupels is sorted by the first element in each tuple.
If a mixture containing unsortable items is supplied, the sort will raise a
TypeError exception"""


a = [3,2,1]
a.sort()
# output: [1,2,3]
print(a)

a = ['c','a','A','C']
a.sort()
# output: ['A', 'C', 'a', 'c']
print(a)
a.sort(key=str.lower) # use str.lower as keyword argument to perform a case-insensitive order
# output: ['A', 'a', 'C', 'c']
print(a)

""" for more information on the list.sort() method, look up
https://www.programiz.com/python-programming/methods/list/sort
or other internet sources"""

# the IN and NOT IN operators / List membership tests
""" Like other operators, in and not in are used in expressions and connect
two values. These expressions will evaluate to a boolean value (True, False)"""

animals = ['cat','dog','tiger']
animal = 'cat'
if animal in animals:
    print("There's a "+animal+" in the list")
elif animal not in animals:
    print("There's no "+animal+" in the list")
else:
    print('cannot happen')

# Multiple Assignement using lists
cat = ['fat','white','aggressie']
size,color, disposition = cat #assigning 3 variables at the same time
#Output: The cat's color is white
print("The cat's color is "+color)



# Using for loops with list

"""Using a for loop, we can iterate through each item in a list. Technically, a for
loop repeats the code block for each value in a list or list-like value. The output
of the range function is a list like value. The output of range(3) is considered
to be similar to [0,1,2] by Python

Python doesn't actally have for loops. Pythons for loops are foreach loops. A foreach
loop is a control flow statement for traversing items in a collection. Unlike standard
for loops, foreach loops usually maintain no explicit counter
"""

bases = [3,2,5,1,7,11]
for num in bases:
    print(str(num)+'^2 equals ',num**2)

# enumerate function

"""if you need the index of a loop, you can use the enumerate function. This function
allows to loop over a list and retrieve bothe the index and the value of each item in
the list"""

items = ['apple','orange','banana','cucumber','cherries']
for n, item in enumerate(items, start=1):
    print("Item {}: {}".format(n, item))

# ------ List comprehension ----------

"""List comprehensions are one of the most powerful tools in Python. They are
trivial, and handle some of the most common operations in software development.
For example, converting a list of items into a list of related items"""

# example - convertings strings to integers, standard loop

input_list=['2','4','7','9','15','25']

output_list=[]
for num in input_list:
    output_list.append(int(num))
# output: [2, 4, 7, 9, 15, 25]
print(output_list)

# example - converting strings to integers, using list comprehension

input_list=['2','4','7','9','15','25']
output_list = [int(num) for num in input_list]
# output: [2, 4, 7, 9, 15, 25]
print(output_list)

# syntax eplanation

""" The square brackets indicate that we are creating a list. Inside this list
is a for loop that iterates over each item in the input sequence. The term
between the opening bracket [ and the for loop describes what happens to each
item of the input list"""

# advantages of list comprehension

""" Apart from better readability, list comprehensions are faster than for loops
when looping over a huge number of items."""

# using conditions in list comprehension

input_list=['2','4','7','9','15','25']
oddnumbers = [int(n) for n in input_list if not int(n) % 2]
print(oddnumbers)


# Use of Lists
""" Lists should normally be used when we want to store several instances of the
"same" type of object. Lists should always be used when we want to store items in
some kind of order. Lists are also very useful when we need to modify the contents
(e.g. insert, delete, update at arbitrary locations in a list)"""

# ---- List like types: Typles and Strings --------

""" Like lists, strings and tuples represent ordered sequences of values (Imagine
a string being a list of single text characters). Therefore, many of the things that
can be done with lists can also be done with strings/tuples"""

name = "Joe"
# output: name[0] is the initial is J
print("name[0] is the initial is ",name[0])

# output: name[0] is the initial is J
print("Joe ends with name[1:], that is with ",name[1:])

# output: There's no I in Team True
print("There's no I in Team", 'I' not in 'Team')

for i in 'Loop':
    print(i)

# -------- mutable and immutable data types ------------

"""But lists and strings are different in an important way. A list value is a
mutable data type: It can have values added, removed or changed. A string is
immutable. It cannot be changed. Therefore you cannot

- assign a character in a string, the code

name='Joe a plumber'
name[4] = 'the

does not work.

The proper way to change a string is to use slicing and concatenation to build a
new string by copying parts of the old string:"""

name='Joe a plumber'
newname = name[:4] + 'the' + name[5:] # name = name[:4] + ... also works
# output: Joe the plumber
print(newname)

""" When you assign a list to a variable, you do not assign a value to the variable,
but you assign a list reference to the variable. A list reference is a value that
points to a list. Python uses references whenever a variable must store values of
mutable datatypes like lists or dictionaries. For values of immutable data types such
as strings, integers or tuples, Python variables will store the value itself
The difference can be seen in the following examples:"""

name='Joe a plumber'
name2 = name
name2 = 'Moe a plumber'
# output: Joe a plumber
print(name)
# output: Moe a plumber
print(name2)

nameList=['Joe','a','plumber']
nameList2 = nameList

nameList2[0] = 'Moe'
# output: ['Moe', 'a', 'plumber']
print(nameList)
# output: ['Moe', 'a', 'plumber']
print(nameList2)

""" When a function is called, the values of the arguments are copied to the parameter
variables. For lists (and other mutables datatypes), this means a copy of the reference
is used. Keep this behavior in mind - Forgetting this can lead to confusing bugs """

oldPlumber=['Joe','the','plumber']
def changePlumber(nameList,name):
    newPlumber=nameList
    newPlumber[0]=name
    print(newPlumber)

changePlumber(oldPlumber,'Moe')
# output: ['Moe', 'the', 'plumber']
print(oldPlumber) # The function unintentionally changed the original list !!!

# Passing References

""" if you don't want to pass a reference but copy an object (so that the original
object remains unchanged, Python offers two functions to create copies, a so called
'shallow copy' and 'deep copy'. To make these work, you need the copy module.
"""

import copy

""" A shallow copy creates a new object which stores the reference of the original
object. A shallow copy does not copy nested objects (e.g. lists in lists), it copies
only the references of nested objects"""

list1dim = ['old','old','old']
list_assigned = list1dim # assigning the reference
list_copy = copy.copy(list1dim) # create (shallow) copy of list

list_copy[0] = 'new'
# output: ['old','old','old']
print(list1dim) # changing copy (list_copy) does not change original list (list1dim)

list_assigned[1] = 'new'
# output: ['old','new','old']
print(list1dim) # changing list with reference (list_assigned) changes original list (list1dim)

# copy() only works on the first level. Nested objects are not copied

list1dim = ['old','old',['old','old','old']]
list_copy = copy.copy(list1dim) # create (shallow) copy of list
list_copy[2][1]='new'
# output: ['old','old',['old','new','old']]
print(list1dim) # changing nested (mutable) objects changes original list (list1dim)

""" A shallow copy creates a new object which stores the reference of the original
object. A shallow copy does not copy nested objects (e.g. lists in lists), it copies
only the references of nested objects"""

list1dim = ['old','old',['old','old','old']]
list_copy = copy.deepcopy(list1dim) # creates deep copy of list
list_copy[2][1]='new'
# output: ['old','old',['old','old','old']]
print(list1dim) # changing nested (mutable) objects does not change original list
# when using the deepcopy() function


# -------------- TUPLES --------------

""" Tupels are similar to lists. Like lists, they can store a specific number
of objects in order. The main difference is that that tupels are
immutable objects. Typels are typed with parentheses ( and ) instead of
square brackets [ and ]."""

# empty tuple
# Output: ()
a_tuple = ()
print(a_tuple)

# creating a tuples with one element
# Output: (3,)
a_tuple = (3,) # without the comma, Python wouln't recognize input as tuple
print(a_tuple)

# tuple having integers
# Output: (4, 2, 7)
a_tuple = (4, 2, 7)
print(a_tuple)

# tuple with mixed datatypes
# Output: (7, "Hello", 8.1)
a_tuple = (7, "Hello", 8.1)
print(a_tuple)

# nested tuple
# Output: ('mouse', [8, 4, 6], (1, 2, 3))
nested_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(nested_tuple)

# tuple can be created without parentheses, also called tuple packing
# Output: 3, 4.6, "dog"

a_tuple = 3, 4.6, "dog"
print(a_tuple)

# tuple unpacking is also possible
# Output:
# 3
# 4.6
# dog
a, b, c = a_tuple
print(a)
print(b)
print(c)

""" Because tuples are similar to lists (storing ordered objects), indexing,
slicing notation and loops works just like with lists"""

# accessing elements in a tuple ------------

# Indexing
a_tuple = (7, "Hello", 8.1)
# output: 8.1
print(a_tuple[2])

# Indexing (nested objects)
nested_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# output: 8
print(nested_tuple[1][0])
# output: u
print(nested_tuple[0][2])

# output:
# [8,4,6]
# (1,2,3)
for i in nested_tuple[1:]: # slicing notation, for loop
    print(i)

""" Because tuples are immutalbe data types, assignement of individual elements
does not work """


a_tuple = (1,2,3)
try:
    a_tuple[0]=0
except TypeError:
    print("Elements of a tuple cannot be changed")

""" Assignement works if tuples contain mutable data types """

a_tuple = (1,2,[3,4,5])
a_tuple[2][0] = 0
# output: (1, 2, [0, 4, 5])
print(a_tuple)

""" Like lists, tuples offer a number of built-in methods. An overview of
tuple methods can be found here
https://www.programiz.com/python-programming/methods/tuple
or anywhere else on the internet """

# tuple method examples

a_tuple = (2,2,2,8,9)
# output: 3
print(a_tuple.count(2))
# output: 4
print(a_tuple.index(9))

# converting type with the list() and tuple() functions

a_tuple = (2,3,4,'end')
a_list = list(a_tuple)
print(a_list)
another_tuple = tuple(a_list)
print(another_tuple)

# When to use tuples - Advantages of tupels over lists
"""
- tuples that contain immutable objects can be used as keys in dictionaries
(as opposed to lists)
- since tuples are immutable, iterating through a tuple is faster than with list
- if you have data that does not change, implementing it as tuple will ensure
that it remains write protected

The primary purpose of a tuple is to aggregate different pieces of data together into
one container

"""
# when not to use tuples

"""
- if you need to modify a tuple, you're using the wrong data type
- one of the main disadvantages of tuples is readability. It is difficult to
know what an element of a tuple represents. It is advised against accessing
individual elements of tuples in code. Such so called 'magig numbers' (numbers
that seem to come out of thin air with no apparent meaning within the code) are
the source of many hours of frustrated debugging. Therefore
- try to use tuples only when you know that all the values are going to be useful
at once and it's normally boing to be unpacked when it is accessed (or at
least inclue an explaining comment)

"""

# ---------------- Named Tuples ----------------

""" If we do noeet to add behavior to the object, and we know in advance what
attributes we need to store, we can use a named tupled. Named tuples are
a great way to group read-only data together """

# example named tuple

from collections import namedtuple
Stock = namedtuple("Stock", "symbol current high low")
stock = Stock("FB", 75.00, high=75.03, low=74.90)

# output: FB
print(stock.symbol)
# output: 75.03
print(stock.high)

# more on name tuples later.....

# ------------------------ DICTIONARIES ------------------------

"""Like a list, a dictionary is a collection of many values. But unlike
indices for lists, indices for dictionaries can use many different data types,
not just integers. Indices for dictionaries are called keys. Each key
is associated with a value. This is called a key: value pair

A Python dictionary is an unordered collection of items. Dictionaries
are optimized to retrieve a value when the key is known

Dictionaries are very powerful containers that allow to map objects directly
to other objects. Dictionaries are extremely efficient at looking up a value.
Dictionaries should always be used when you want to find one object based on
some other object"""

# keys

""" we can used strings, tuples, numbers and even self-defined objects as
dictionary keys. We cannot use lists as keys. Because lists can
change at any time (by adding, removing values), they cannot hash to a
specific value. Objects that are hashable have a defined algorith that
converts the object into a unique integer value for rapid lookup. Any two
objects that are considered equal should have the same hash value, and the
hash value for an object should never change. For the same reason,
dictionaries cannot be used as keys """

# Creating/accessing a dictionary

""" A dictionary is typed using curly brackets {}. Key: value pairs are
separated by comma; keys and values are seperated by colon.

Dictonary uses keys instead of indices to access values. Keys can be either
used in square brackets[] or with the get() method
"""

# Uses of dictionaries

""" There are two major ways that dictionaries can be used: The first is dictionaries
where alle the keys represent different instances of similar objects. For example,
keys are stock names and values are tuples containt data on the stock. This is an
indexing system

The second design is dictionaries where each key represents some aspect of a single
structuree. We'd probably use a different dictionary for each object in this case.
Such situations can often also be solved with named tuples. Tuples should be used
when we know exactly what attributes must be stored and that they are all supplied
at once. But if we need to change or create dictionary keys over time or we don't
know what the keys might be, a dictionary is more suitable"""

# empty dictionary
a_dict = {}

# dictionary with integer keys
a_dict = {1: 'apple', 2: 'banana'}
# output: apple
print(a_dict[1]) # accessing usind square brackets []
print(a_dict.get(1)) # accessing using get() method

# dictionary with mixed keys
a_dict = {'name': 'John', 1: [2, 4, 3]}

# creating a dictionary using the built-in function dict()

""" For more info on dict() see
https://www.programiz.com/python-programming/methods/built-in/dict
"""

# Changing value in dictionaries

""" Like lists, dictionaries are mutable objects. We can add new values
or change existing one using the assignment operator """

my_dict = {'name':'Joe','age': 33}
my_dict['age'] = 34
print(my_dict)
my_dict['sex'] = 'male'
print(my_dict)

""" Unlike lists, dictionaries are unordered objects. Therefore, dictionaries
cannot be sliced """

# keys(), values() and items() methods and for loops

""" These three dictionary methods will return list-like values of the dictionary's
keys, values or key:value pairs. The returned data types (dict_keys, dict_values
and dict_items respectively) are not true lists, but they can be used in for loops:"""

birthdays = {'Joe':'Jan 1', 'John':'Feb 2', 'Jason':'March 3'}
for name in birthdays.keys():
    print(birthdays[name] + ' is the birthday of ' + name)

# alternatively, you can use the multiple assignement trick
# items() provides an iterator over tuples
for name, date in birthdays.items():
    print(date + ' is the birthday of ' + name)

# checking wheter key or value exists in a dictionary using (not) in operator

birthdays = {'Joe':'Jan 1', 'John':'Feb 2', 'Jason':'March 3'}
# output: True
print('Joe' in birthdays)
# output: True
print('Joe' in birthdays.keys())
# output: False
print('Joe' in birthdays.values())
# output: True
print(('Joe','Jan 1') in birthdays.items())

# KeyError, default Methods

""" Trying to access a key that does not exist in a dictionary raises the
KeyError """
birthdays = {'Joe':'Jan 1', 'John':'Feb 2', 'Jason':'March 3'}
# output: no birthday date for this name
try:
    birthdays['Jenny']
except KeyError:
    print('no birthday date for this name')

# dictionary get() method

""" To avoid KeyErrors, we can use the get method. The get method
optionally allows to specify a default value. The default value
is returned if the key is not found """

birthdays = {'Joe':'Jan 1', 'John':'Feb 2', 'Jason':'March 3'}

#output: Jan 1
print(birthdays.get('Joe','unknown birthday date'))
#output: unknown birthday date
print(birthdays.get('Jenny','unknown birthday date'))

# dictionary setdefault() method

""" For even more control, we can use the setdefault() method. If the key
is in the dictionary, the setdefault() method returns the value for that key.
If the key is not in the dictionary, it will not only return the default value,
but also add it to the dictionary """

birthdays = {'Joe':'Jan 1', 'John':'Feb 2', 'Jason':'March 3'}
#output: unknown birthday date
print(birthdays.setdefault('Jenny','unknown birthday date'))
# output: {'Joe': 'Jan 1', 'John': 'Feb 2', 'Jason': 'March 3',
# 'Jenny': 'unknown birthday date'}
print(birthdays)
#output: unknown birthday date
print(birthdays['Jenny'])



# ---------- Pretty Printing -------------------

"""The pprint() and pformat() functions, contained in the pprint module
allow to 'pretty print' a dictionary's values, when you want to have a
cleaner display of the items in a dictionary"""

# example: counting characters, displaying result in a dictionary using pprint()

import pprint
sentence = """All Gaul is divided into three parts, one of which the Belgae inhabit,
the Aquitani another, those who in their own language are called Celts,
in our Gauls, the third."""

charcount={} # starting with empty dictionary
for char in sentence: # looping over string
    charcount.setdefault(char,0) # First entry, count = 0
    charcount[char] = charcount[char] + 1 # add 1 when character is encountered

# output: try it out ...
pprint.pprint(charcount)

# the pformat() function returns the formated expression of a string (to which
# standard print function can be applied, for example

# output: same as in statement above
print(pprint.pformat(charcount))

# -------- usind default dict, counter (oop, p164 ----------------

""" character count can be made simpler using defaultdict or counter """

# later ......

# Concatanation of lists, tuples, strings   

""" lists, tuples and strings can be concatenated using the + symbol"""

a = 'Hello'
b = 'World'
# output: Hello World
print(a + ' ' + b)

a = (1,2)
b = (3,4)
# output: (1,2,3,4)
print(a + b)


a = [1,2]
b = [3,4,5]
# output: [1,2,3,4,5]
print(a + b)


# -------------- SETS -----------------

"""Lists are not useful when we want to ensure that objects in the list are unique.
Sets come from mathematics and represent an unordered group of unique elements.
In Python, sets can hold any hashable object (the same that can be used as
keys in dictionaries). In other words, sets can only hold immutable objects.
Objects in a set can have different types. Sets can store only one copy of
each object. Sets are created using curly braces {}, separating elements by
comma"""

# creating a set: 

a_set = {1,2,3,2,2,3,1}
# output: {1,2,3}
print(a_set)

# empty set
empty_set = set() # {} creates an empty dictionary

# adding an element
a_set = {1,2,3,2,2,3,1}
a_set.add(5)
# output: {1,2,3,5}
print(a_set)

# Purpose of sets

""" The primary purpose a set is to divide the world in two groups: "things
that are in the set and things that are not in the set. Sets are most useful
when two of them are used in combination. Most of the methods on the set
operate on other sets, allowing to efficiently compare or combine the items
in two or more sets. An overview of methods on sets can be found here

https://www.programiz.com/python-programming/methods/set

"""
# example set methods

set1={2,4,6,8,10,12,14,16,18,20}
set2={3,6,9,12,15,18}

unionset=set1.union(set2) # returns union of two sets
# output: {2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20}
print(unionset)
# output: True
print(unionset == set1 | set2) # | operater also possible

intersectionSet=set2.intersection(set1) # returns intersection of two sets
# output: {18, 12, 6}
print(intersectionSet)
# output: True
print(intersectionSet.issubset(set1)) # tests if subset
# output: True
print(set1 & set2 == intersectionSet) # & operator also possible

differenceSet = set1.difference(set2) # elements in set1 but not set2
# output: {2, 4, 8, 10, 14, 16, 20}
print(differenceSet)

# output: True
print(set1 - set2 == differenceSet) # - operator also possible

# Exception Handling

# later....

# --------------- Important Modules --------------------

# math
# random
# sys


# --------------------- Important built-in functions -----------------------
# print() function
# input() function
userinput = input('Please enter an input and confirm:')

print('you just inputed ',userinput)
# len(), str(), int(), float()
# range()
# format()

print("this print was added using a Git branch")
