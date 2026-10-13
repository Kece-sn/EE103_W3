
given_number = int(input("Enter a number: "))

if given_number < 0:
    print("Square root of negative numbers is not a real number.")
else:
    guess = 0

    while guess * guess < given_number:
        guess += 1

    if guess * guess == given_number:
        print("The square root is", guess)
    else:
        print("The number is not a perfect square.")