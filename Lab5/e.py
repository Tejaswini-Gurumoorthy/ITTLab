def sum_of_naturals(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_naturals(n-1)

# Example usage
n = int(input("Enter n: "))
sum_n = sum_of_naturals(n)
print("The sum of the first", n, "natural numbers is", sum_n)
