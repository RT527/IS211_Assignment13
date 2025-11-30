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
"""---------------------------------------------------------------------------------"""
def compareTo(s1, s2): #This compares two strings recursively

    if s1 == "" and s2 == "":
        return 0 #If both strings are empty, they are equal

    if s1 == "" and s2 != "":
        return -1
    if s1 != "" and s2 == "":
        return 1 #If one string is empty, the shorter one is considered smaller

    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0]) #This compares the first characters of each string

    return compareTo(s1[1:], s2[1:])#This compare the rest of the strings