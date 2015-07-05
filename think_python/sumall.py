""" Many of the built-in functions use variable-length argument tuples. For example,
max and min can take any number of arguments:
116 Chapter 12. Tuples
>>> max(1,2,3)
3
But sum does not.
>>> sum(1,2,3)
TypeError: sum expected at most 2 arguments, got 3
Write a function called sumall that takes any number of arguments and returns their sum.
"""

def sumall(*args): # The * takes the arguments and stores them in a tuple
    if len(args) == 0: # No values were entered when the function was called
        print "your list is empty. I have decided to give you an answer of 0"
        return 0
    a = args[0] # first element of tuple
    res = a
    while len(args) >= 2: # have more to values to add
        res = res + sumall(*args[1:]) # adds res to call of sumall on all but the first element
        return res 
    return res

answer = sumall(1,2,3,4,12)
print answer
print sumall(1,4)
print sumall(3)
print sumall()
