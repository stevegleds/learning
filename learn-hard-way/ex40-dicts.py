cities = {'CA' : 'San Francisco', 'MI' : 'Detroit', 'FL' : 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state) :
    if state in themap:
        return themap[state]
    else:
        return "Not found"
        
# ok pay attention!
# this puts the function find_city in the dict with label _find
cities['_find'] = find_city

while True:
    print("State? (Enter to quit)")
    state = input("> ")
    
    if not state: break
    
    # this line is the most important ever! study!
    # uses the find_city function that is included in the cities dict and passes arguments
    city_found = cities['_find'](cities, state)
    print(city_found)