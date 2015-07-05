def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]



        
def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

def is_palindrome2(word):
    """ Returns True if word is a palindrome.
    the third parameter steps backwards! Normally used to select every 2nd, 3rd etc."""
    return word == word[::-1] 

print is_palindrome('allen')
print is_palindrome('bob')
print is_palindrome('otto')
print is_palindrome('redivider')
print "One-line alternative"
print is_palindrome2('allen')
print is_palindrome2('bob')
print is_palindrome2('otto')
print is_palindrome2('redivider')

