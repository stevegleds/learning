## The Russian Peasant's Algorithm with testing 
## I use recursion for fun
## Been around for a long time (1700s)

## Multiply two numbers together
## Requirements: multiply one by two and divide other by two
## Keep going til get to 1 on LHS
## Add up the RHS for all odd values on LHS

## Eg. 24 * 16
## 12 * 32
## 6 * 64
## 3 * 128
## 1 * 256 {round down}
## Add 128 and 256 to get the correct answer 384

## Input 2 numbers
## Calculate product
## Output 1 answer (the product)


import math # Used to use floor function to keep integar values
import time # We will use this to test efficiency


def russian(a, b):
    x = a; y = b
    z = 0 ## accumulator
    while x > 0:
        if x % 2 == 1: z = z + y ## modulo operator
        y = y << 1 ## Shift binary to the left - not sure what this is doing
        x = x >> 1 ## Shift binary to the right
    print("Hit DB")
    return z


def test_russian():
    start_time = time.time()
    print(russian(357, 16))
    print("Russian Algorithm took {} seconds" .format(time.time()-start_time) )
    assert russian(357, 16) == 5712

if __name__ == "__main__": # this is needed to stop the following function call running when this is imported.
    test_russian()

