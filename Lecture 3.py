'''
Handling Exceptions
* General rule of exception handling is:
    *If an exception was raised in a program and nobody catches
     the exception, then the program will terminate
* But we can handle the exception messages with a general
structure refered to as try / except
'''

while True:
    try:
        x = int(input("Enter an int: "))
        break
    except Exception:
        print("Input was not an int type")
    print("Let's try again")


def divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError()
    return numerator / denominator

try:
    print(divide(1,1)) # OK
    print(divide(1,0)) # ZeroDivisionError
    print(divide(2,2)) # OK
except ZeroDivisionError:
    print("Error: cannot divide by zero")
print("Resuming execution")

''' Flow of execution
* Everything within a try block is executed
normally
* If an exception occurs in the try block,
passed to a corresponding except block
* The except block tries to catch a certain
exception type (note that Exception catches ALL
types of exceptions)
* If there is a matching type then the first-matching except block is executed.
* Once done, program execution resumes past the except block.
* Once done, program execution resumes past the except block.
'''

l = [1,2,3]
l[10] # IndexError, it is out of boundary, so

''' Python Objects
* Objects are a way for programmers to define
their own Python types and create abstractions of things with the programming language
* Each object may have a certain state that gets modified throughout program execution
* Object oriented programming is a way programs
use and manipulate objects to solve problems and model real-world properties
    * Object oriented programming is NOT REQUIRED
    * It's more of a way to organize, read,
    maintain, test, and debug software in a 
    manageable way
    
'''

# Student.py

class Student:
    ''' Student class type that contains student values '''

    def setName(self, name): # we can also use def __init__(self,name,perm): more convient
        self.name = name

    def setPerm(self, perm):
        self.perm = perm

    def printAttributes(self):
        print("Student name: {}, perm: {}")\
            .format(self.name,self.perm)

s = Student() # set the class and define it # by using __init__ we can use Student(name, perm)
print(type(s))
s.setName("Chris Gaucho")
s.setPerm("1111111")
s.printAttributes()

s1 = Student("Jane", 1234567)
s2 = Student("Joe", 7654321)
s3 = Student("Jill", 5555555)

studentList = [s1,s2,s3]
for s in studentList:
    s.printAttributes() # print all of them




# Courses.py

# From [filename withour .py] import [ component]

class Courses:
    '''Class representing a collection of courses.
    Courses are oranized by a dictionary where the key is the course number and the
    value is a list of Students in a course'''
    def __init__(self):
        self.courses == {}

    def addStudent(self, student, courseNum):
        '''Method that adds a student to a courseNum
        If courseNum doesn't exist, create the course
        '''
        if self.courses.get(courseNum) == None:
            self.courses[courseNum] = [student]
        elif not student in self.courses.get(courseNum):
            self.courses[courseNum].append(student)
    def printCourses(self):
        for courseNum in self.courses:
            print("CourseNum: ", courseNum)
            for student in self.courses[courseNum]:
                student.printAttributes()
            print("---")

UCSB = Courses()
UCSB.addStudent(s1, "CS8")
UCSB.addStudent(s2,  "CS9")
UCSB.addStudent(s3, "CS16")

UCSB.addStudent(s1, "CS9") # s1 student can appear several times

UCSB.printCourses()


