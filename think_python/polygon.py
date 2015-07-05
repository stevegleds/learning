import math
def check_fermat():
    global a, b, c, n
    print a, b, c, n
    if n <= 2:
        print "please enter a power greater than 2"
    else:
        if (a ** n) + (b ** n) == (c ** n):
            print "Fermat was wrong"
        else:
            print "sorry"


def get_values():
    global a, b, c, n
    a = int(raw_input("a "))
    b = int(raw_input("b "))
    c = int(raw_input("c "))
    n = int(raw_input("d "))
    print a
    return

a = 1
b = 2
c = 3
n = 4

get_values()
check_fermat()

