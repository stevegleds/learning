from math import floor, sqrt
def is_prime(candidate):
    limit = int(floor(sqrt(float(candidate))))
    answer = "prime"
    for i in range (1, limit + 1):
        if float(candidate) % i == 0:
            # print("we are testing ", i)
            answer = "not_prime"
            return answer            
        else:
            pass
    return answer
            
# print(is_prime(raw_input("enter your number ")))
prime_count = 1
candidate = 2
while prime_count < 3: 
    if float(candidate) % 2 == 0:
        candidate += 1
    else:
        answer = is_prime(candidate)
        if answer == 'prime' :
            prime_count += 1
            
print("we have reached ", prime_count, " the final number is : ", candidate)