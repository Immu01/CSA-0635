def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=2
print(f"\nThe Fibonacci number for n = {n} is {fibonacci(n)}")