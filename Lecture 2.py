'''python lists
* A dynamic collection of data(heterogenous types)
that can be indexed(index starts at 0)

* List Slicing
[i:j] syntax starts (includes) element at index i up to (not including) element at index J

* Strings are very similar to Lists ) but not exactly !)

* Lists in Python are MUTABLE ( can change the existing list)

* Strings in Python are IMMUTABLE ( can not change the existing string)
'''

''' Function
'''
x = "CS1"

# Function Definition

def double(n):  #function need a ":"
    return 2 * n

print(double(3)) # Have to add print function in order to observe the output in py file

'''
* When IMMUTABLE types are passed into a function, a COPY of that variable is made and used within the function
* When MUTABLE types are passed into a function, the actual parameter variable is used within the function
(no copy is made0
'''
def changeListParameter(x):
    x[0] = "!"
    return x
a = ["C", "S" ,"9"]
b = "CS9"
print(changeListParameter(a)) # [!, S, 9]
print(a)# [!, S, 9]

def changeStringParameter(x):
    x = x.replace("C", "!")
    return x
b = "CS9"
print(changeStringParameter(b)) # "!s9" is change because it changed it's copy
print(b) # original doesn't change because string is immutable

x = False

if x:
    print("Shouldn't print") # True default
else:
    print("Should print") # else, so if False then print

'''
While Loop
'''

while True:
    print("Weeee!") # NEVER STOP
    break # stop

'''For Loops
'''

l = [1,2,3]
for i in l:
    print(i) # print out each item in list l
'''
* We can also use range() function to create a number list
* range(x) returns a collection of numbers from 0 up to (but not including) x
* range(x,y) returns a collection of numbers starting at x up to (but not including) y
* Example : range(4) -> [0,1,2,3]
'''

for x in range(4):
    print(x, "Hello!" * x) # print given time of "Hello!"
    print("---") # after finish range(4) the funciton stops

''' Sets
* Sets are like a mathematical set
    * A collection of items
        * No duplicates
        * Order doesn't matter
'''
s1 = set([2,4,4,6]) # type only keepts unique stuff in the set
print(s1)
print(type(s1))

''' Dictionaries
    * Works where a unique KEY maps to a VALUE
    * Use dictionaries mainly for:
    * D['someString'] - allows us to access elements based
    on key values
        * Keys MUST be IMMUTABLE
'''

D = {}
print(D)
print(len(D))
print(type(D))

D = {"Jane":18, "Jen":19, "Joe":20, "John":21}
print(D)

for x in D:
    print(x) # Key
    print(D[x]) # Value

print("---")

value = D.pop("Joe") # it also removed the value for "Joe"
print(value) # only shows the value that poped out, but it actually removed the whole thing from dictionaries
print(D)
D["Jem"] = 50
print(D)
D["Jem"] = 21 # Jem is still there and only on Jem , we just updated the value for Jem
print(D)


''' Python Errors
'''
print("Start")
 # Syntax Error becasue the ! mark is not allowed for the name of a variable
# Python first check if there is a error in syntax instead of run it first
 # NameError (Runtime error) becasue syntax is correct, but when it checked PYTHON is a good variable name, but python is not defined

''' Exceptions are errors that occur DURING
program execution
'''

print("Start")
 # ZeroDivisionError: division by zero
# TypeError Python doesn't know what to do to sum string and integer, but python knows string times integer

''' Handling Exceptions
* General rule of exception handling is:
    * If an exception was raised in a program and nobody cathes and exception, then the program 
    will terminate
* But we can handle the exception messages
 with a general structure reffered to as try / except
'''


while True:
    try:
        x = int(input("Enter an int: "))
        break
    except Exception:
        print("Input was not an int type")
    print("Let's try again")
'''Flow of execution
* Everything within a try block is executed normally
* If an exception occurs in the try block, execution halts and an 
exception message is passed to a corresponding except block
* The except block tries to catch a certain exception type( not that exception catches 
ALL types of exceptions)
* If there is a matching type then the first-matching except block is executed.
* Once done, program execution resumes past the except block.
'''
try:
    for i in range(5):
        x = i / (i-5)
except:
    print("EXCEPTION CAUGHT")
print("RESUMING EXECUTION")

cs9 = "CS9"
try:
    for s in cs9:
        x = len(cs9) + s
    print("DONE LOOPING")
except:
    print("EXCEPTION CAUGHT")
for x in "h00":
    print(x[0])
    print(None)
print("out of for loop")




