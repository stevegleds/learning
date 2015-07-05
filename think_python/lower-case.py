"""The following functions are all intended to check whether a string contains any
lowercase letters, but at least some of them are wrong. For each function, describe what the function
actually does (assuming that the parameter is a string)."""
def any_lowercase1(s): # This works
    for c in s:
        if c.islower():
            return True
    else:
        return False
    
def any_lowercase2(s): # returns true but only because 'c' is lower case
    for c in s:
        if 'c'.islower():
            return 'True'
    else:
        return 'False'
    
def any_lowercase3(s): # only checks first letter
    for c in s:
        flag = c.islower()
        return flag
    
def any_lowercase4(s): # only checks first letter
    flag = False
    for c in s:
        flag = flag or c.islower()
        return flag
    
def any_lowercase5(s): # stops if first letter is capital. Only works if first is lower case
    for c in s:
        if not c.islower():
            return False
        return True

text = "AbCDE"
print any_lowercase1(text)
print any_lowercase2(text)
print any_lowercase3(text)
print any_lowercase4(text)
print any_lowercase5(text)
