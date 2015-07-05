# Using assert to test code

def adding(a, b):
    return a + b

def test_adding():
    assert adding(3,4) == 7 # True
    assert adding(3,2) == 5 # True
    assert adding(99, 49) == 148 # True

    return "All Tests pass for function adding()"

print(test_adding())
# end
