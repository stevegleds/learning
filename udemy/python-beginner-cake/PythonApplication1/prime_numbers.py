from math import floor, sqrt
def is_prime(candidate):
    limit = int(floor(sqrt(float(candidate)))) # must be a better way of doing this but we can speed things up by restricting test to square root of number
    answer = "prime"
    for i in range (3, limit + 1):
        if float(candidate) % i == 0:
            answer = "not_prime"
            break # no point carrying on after we find that candidate is prime
        else:
            pass # keep testing to see if it can be divided
    return answer # if we get here then it must be prime
            
# print(is_prime(raw_input("enter your number ")))
prime_count = 1
candidate = 2
while prime_count < 1000: 
    candidate += 1
    if float(candidate) % 2 == 0: # ignore all even numbers        
        print("this should be odd: ", candidate)
    else:
        answer = is_prime(candidate) # test candidate         
        if answer == 'prime' :
            prime_count += 1
            print("primes found are now: ", prime_count)
        else:
            print("no prime found")
            
print("we have reached ", prime_count, " the final number is : ", candidate)

# finds the value of the 1000th prime number