""" Suppose you are given a string and you want to count howmany times each letter appears.
Dictionaries have a method called get that takes a key and a default value.
If the key appears in the dictionary,
get returns the corresponding value; otherwise it returns the default
value"""

def histogram(s):
    d = dict() # create empty dictionary
    for c in s: # loop for all characters in the string
        d[c] = d.get(c,0) + 1 # sets the value of dictionary entry c to the current value + 1
    return d

def print_hist(h): # prints the keys and the corresponding values
    for c in h:
        print c, h[c] #prints the character and the corresponding value
    l = h.keys()
    print l
    return

h = histogram("brontosaurus")
print h
print_hist(h)
