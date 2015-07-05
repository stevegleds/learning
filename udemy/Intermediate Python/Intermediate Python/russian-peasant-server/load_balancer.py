## Server names
import computer1
import computer2
import computer3

SERVERS = [computer1, computer2, computer3]

# Solution 1 : using global variable (not ideal)
#number_of_servers = len(SERVERS)
#current_server = SERVERS[-1]

#def get_server():
#    # Input: none
#    # Output: Return the server name
#    # Use a loop to return the app to be used in order
#    global current_server
#    if current_server == SERVERS[-1]: #reached the end of the list
#       current_server = SERVERS[0] #loop back to the beginning
#    else:
#       current_server = SERVERS[SERVERS.index(current_server) + 1] # move on to the next server in the list
#    return current_server
#    pass

# Solution 2 using cycle in itertools module. still using global variable
#import itertools
##infinite loop iterator
#cycle = itertools.cycle(SERVERS)
#def get_server():
#    global cycle
#    return cycle.__next__()

# solution 3 Uses a generator function, yields an answer and uses 'next' to get the next result
n = -1
def get_server():
    global n
    n += 1 #
    return SERVERS[n % len(SERVERS)]
    
## Testing the function
if __name__ == '__main__' : 
    from random import randint
    for i in range(10):
        ## Generate some 'requested' numbers
        a = randint(5, 99) # min 5 max 99
        b = randint(5, 99)
        server = get_server()
        print("next is printname")
        print(server.printName) # should get App1, 2, 3 looping
        print("next is multiply handler")
        print(server.multiplyHandler(a,b))
        print(server.lastMultipliedHandler())