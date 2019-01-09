"""
List Homework
Defining a function adding elements to the list
"""

myUniqueList = []
myLeftovers = []
#Here are my empty lists

def addtolist(x):
    if x not in myUniqueList:
        myUniqueList.append(x)
        return True
    else:
        myLeftovers.append(x)
        return False

a, b, c, d, e, f, g= 10, 12, 13, 10, 11, 14, 12
#here are the variables that I used with this function

print("a is added to the unqua list: ", addtolist(a))
print("b is added to the unqua list: ",addtolist(b))
print("c is added to the unqua list: ",addtolist(c))
print("d is added to the unqua list: ",addtolist(d))
print("e is added to the unqua list: ",addtolist(e))
print("f is added to the unqua list: ",addtolist(f))
print("g is added to the unqua list: ",addtolist(g))

print("The unique list contains: ",myUniqueList)
print("The leftover list containes: ",myLeftovers)
#Here we print the two lists

