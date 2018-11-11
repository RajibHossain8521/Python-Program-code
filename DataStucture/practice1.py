"""
n = int(input())

if n == 0:
    print('None')

factorial = 1
for i in range(1, n+1):
    factorial = factorial * i
    print(factorial)
"""


'''def power(base, exp):
    if exp == 1:
        return base
    if exp != 1:
        return base*power(base, exp-1)
'''
'''
base = int(input('Enter base:'))
exp = int(input('Enter exponential value:'))
result = base**exp
print('Result:', result)
'''
'''
def factorial(n):
    if n < 0:
        return None
    if n in [0, 1]:
        return 1
    return n * factorial(n-1)

def test_factorial():
    assert factorial(1) == 1
    assert factorial(0) == 1
    assert factorial(-1) == None
    assert factorial(5) == 120
'''
'''
def fnc():
    fnc()

if __name__ == '__main__':
    fnc()
'''
'''
def fibonacci(n):
    if n in [1, 2]:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

def test_fibonacci():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
'''
'''
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

def test_fibonacci():
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for n, f in enumerate(fib):
        assert fibonacci(n+1) == f
'''
'''
def fibonacci(n):
    print('Trying to find fibonacci for', n)
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == "__main__":
    print('5th fibonacci number is', fibonacci(5))
'''

def print_number(n):
    if n == 0:
        return

    print_number(n-1)
    print(n)

if __name__ == '__main__':
    print_number(5)



















