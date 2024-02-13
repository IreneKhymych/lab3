def factorial(n): return 1 if n == 0 else n * factorial(n-1)

def ncd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input())
num2 = int(input())
