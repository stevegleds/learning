# computer 2
import fake_database as db

CACHE = {} # used to speed up code if run before

def printName():
    print(str(__name__)) # prints name of module

def updateLastMultiplied(left, right, answer):
    key = 'lastFive' # this key has been used to store latest results
    lastFiveList = CACHE.get(key) #creates list from the entries in CACHE[key]
    if lastFiveList: # there are some previous reusults
        if len(lastFiveList) >= 5: # need to remove first item
            newList = lastFiveList[1:] # remove first item
            newList.append('{}x{}={}' .format(left, right, answer)) # add new result to end
            CACHE[key] = newList # update CACHE with latest last 5 results
        else: # the list is less than 5 - just add new result
            lastFiveList.append('{}x{}={}' .format(left, right, answer)) # add new result to end
            CACHE[key] = lastFiveList # update CACHE with latest latest results
    else: # create new first result
        print("this is the first calc")
        CACHE[key] = ['{}x{}={}' .format(left, right, answer)]

def lastMultipliedHandler():
    #Write this function
    #Inputs : none
    #Outputs : The last multiplied result
    #This is the last 5 multiplied questions and answers
    key = 'lastFive' # we will store last 5 results as a string in key 'key'
    if key in CACHE: # runs after there is at least one result and we can print previous results
        print("Last 5 = {}" .format(CACHE[key])) # print string stored in CACHE
        print("-" * 8) 
        print(" ")
    else: # no results yet
        print("This is the first multiplication")
        print("-" * 8) 
        print(" ")
    return

def multiplyHandler(left, right):
    #Inputs: a, b representing Numbers as arguments from the request
    #Outputs: The result of those two numbers being sent through
    #    The Russian Peasant's Algorithm.
    key = (left, right) # tuple to check if already know answer
    if key in CACHE: # already calculated. Return answer without calculating
        print("been there, done that")
        answer = CACHE[key]
        print(lastMultipliedHandler())
    else: # Not done this before, Need to calculate answer
        print("this is new")
        answer = db.russian(left, right)
        updateLastMultiplied(left, right, answer)
        CACHE[key] = answer # store answer in case we are asked again
        print("Latest Result: {} " .format(answer))
        lastMultipliedHandler() # this produces the latest results - maximum of 5
    return answer
    
if __name__ == '__main__':
    multiplyHandler(13, 13)
    multiplyHandler(31, 31)
    multiplyHandler(12, 12)
    multiplyHandler(14, 19)
    multiplyHandler(13, 13)
    multiplyHandler(131, 113)
    multiplyHandler(123, 113)

