def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
n = int(input("Enter n: "))
fib_series = []
for i in range(n):
    fib_series.append(fibonacci(i))

print("The first", n, "terms of the Fibonacci series are:", fib_series)
