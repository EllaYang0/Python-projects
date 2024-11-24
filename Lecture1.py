# floating point
#e.g. 2 + 2 ( two integers return a integer)
# e.g. 2 + 2.0 ( if there is one floating point or more ,the result return a floating point)

# variable
#e.g.
x = 10.0
x = int(x)# revert to integer or from other types to a floating point
print(x)
x = float(x)
print(x)# from integer or other type to floating point
y = "10.0" # y is a string
z = type(y)
print(z) # str means "string"
print(y) # after print " " quote disapper
float(y)# transer str to numerical floating point
#int(y) wrong!!!! because int has no points, transfer to the numerical, int doesn't konw how to deal with the point "."
x = float(x)
type(x)

# True or False is type: " bool "

# True "or" anything is going to be True
# False "and" anything else is False


# Python lists
# A dynamic collection of data ( heterogenous types) that can be indexed (index starts at 0 ).

x = [] # x is a list
type(x)

x.append(4.5) # the output of x would add an 4.5 at the end, and the output would be [4.5]
x.append(4) # the output of x would be [4.5,4]
x[2] == "4.5" # list can contain diffferent kinds of data.
x.count(2) # count the total number that number 2 exists in the list x
 3 in x # false because there is no 3 in the list
"3" in x # True because

x.insert(3, 2.5) # it means i wanna insert 2.5 in the list in poistion 3
print(x)
x.pop() # default pop out the end element
x.pop(3) # pop out the third elements, ( list starts at 0 )
# after pop, the number is no longer in the list




