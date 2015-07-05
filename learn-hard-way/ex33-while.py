i = 0
numbers = []
def printnumbers(number, increment):
    i = 0
    while i < number:

        print("At the top i is {} " .format(i))
        numbers.append(i)
    
        i = i + increment
        print("Numbers now: ", numbers)
        print("At the bottom i is {} " .format(i))
    
        print("The numbers: ")

printnumbers(10, 2)        
for num in numbers:
    print(num)