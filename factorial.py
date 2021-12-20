
def factorial(n):
    if n <= 0 or type(n) == float:
        return 'n must be positive integer'
    if n == 1:
        return n
    else:
        return factorial(n-1) * n

print(factorial(5))
print(factorial(0.5))
print(factorial(-5))