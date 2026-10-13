n = int(input("Enter a number to calculate its factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}")

m = int(input("Enter another number to calculate its factorial: "))
s=m
factorial_m = 1
while m > 1:
    factorial_m *= m
    m -= 1
print(f"The factorial of {s} is {factorial_m}") 