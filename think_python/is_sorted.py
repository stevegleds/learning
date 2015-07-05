"""
Write a function called is_sorted that takes a list as a
parameter and returns
True
if the list is sorted in ascending order and
False otherwise. You can assume (as a precondition) that
the elements of the list can be compared with
the relational operators <, >, etc.
For example, is_sorted([1,2,2]) should return True and
is_sorted(['b','a']) should re-turn False.
"""

def is_sorted(t):
    if len(t) < 2: #only 1 item or empty list
        print "less than 2"
        return True # if only 1 item must be sorted
    if t[0] > t[1]: # not sorted
        return False
    del t[0] # remove first element
    is_sorted(t) # call is_sorted recursively on smaller list
    return True

print is_sorted([1,2,2])
print "next test: ",
print is_sorted(['b','a'])
print "final test: ",
print is_sorted([1,2])
print "test empty list: ", is_sorted([])
print "test one item", is_sorted([2])

