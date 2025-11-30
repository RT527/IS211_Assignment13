# Rafi Talukder Assignment_13

"""---------------------------------------------------------------------------------"""

def fibonnaci(n): #This returns the nth Fibonacci number using recursion.The sequence starts with 1, 1 for n = 1 and n = 2.
    if n == 1 or n == 2:
        return 1
    return fibonnaci(n - 1) + fibonnaci(n - 2)
"""---------------------------------------------------------------------------------"""
def gcd(a, b): #This computes the greatest common divisor (GCD) of two integers using Euclid's recursive algorithm.
    if b == 0:
        return a
    return gcd(b, a % b)
