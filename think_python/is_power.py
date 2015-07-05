"""A number, a, is a power of b if it is divisible by b
and a/b is a power of b. Write a
function called is_power that takes parameters a and b
and returns True if a is a power of b. Note:
you will have to think about the base case."""

def is_power(a, b):
    print "a is " , a , "b is " , b
    if a%b != 0 and a != 1 :
        return False
    if a == 1 :
        return True
    return is_power(a/b, b)

print is_power(4, 2)
print is_power(81, 3)
print is_power(2, 2)
print is_power(5, 2)
