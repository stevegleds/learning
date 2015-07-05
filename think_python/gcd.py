# Greatest common divisor
# The greatest common divisor (GCD) of a and b is the
# largest number that divides
# both of them with no remainder
# Euclid: If r is the remainder after a is divided by b.
# then gcd of a,b is same as gcd of b,r
# gcd of a,0 is a
# write gcd that takes a,b and returns the gcd

def gcd(a, b):
    print a, b
    if b == 0:
        return a
    remainder = a % b
    print remainder
    return gcd(b, remainder)

print gcd(252, 105)

