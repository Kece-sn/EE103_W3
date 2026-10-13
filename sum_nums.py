
num = int(input("Enter a number: "))

total = 0
for i in range(1, num + 1):
    total += i

print("The sum is:", total)

sum_gauss=num * (num + 1) / 2
print(f"The sum using Gauss formula is: {sum_gauss}")

if sum_gauss == total:
    print("The sum using Gauss formula is equal to the sum calculated using for loop")
else:
    print("The sums are not equal")
