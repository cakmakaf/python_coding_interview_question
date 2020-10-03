"""
Write a iterative and recursive function that implements the factorial
of a number.
5! = 5 * 4 * 3 * 2 * 1
   = 120
n! = n * n - 1 * ... * 1
"""

n = 5
def fact_iter(n):
    x = 1
    for i in range(n, 0, -1):
        x *= i 
    return x

def fact_recur(n):
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n-1)


print(fact_iter(n))

print(fact_recur(n))
