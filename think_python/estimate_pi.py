"""Write a function called estimate_pi that uses this formula to compute and return an estimate of
p. It should use a while loop to compute terms of the summation until the last term is smaller than
1e-15 (which is Python notation for 10
15
). You can check the result by comparing it to math.pi.
solution http://thinkpython.com/code/pi.py 
"""
import math
def estimate_pi():
    k=0
    precision = 0.000000000000001
    term = 1.1
    cumulative_term = 0
    while term >= precision:
        term = math.factorial(4*k)*(1103+(26390 * k))
        term = term / ((math.factorial(k) ** 4) * (396 ** (4 * k)))
        k += 1
        cumulative_term = cumulative_term + term
    answer = 1/((2* math.sqrt(2)) * cumulative_term / 9801)
    return answer

print estimate_pi()
print "the difference is ", estimate_pi() - math.pi
print math.pi
