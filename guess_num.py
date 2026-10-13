
from secret_number import secretNum
guess = None 
n=1
while (n<=5):
    n += 1
    guess = int(input("Guess a number: "))
    if guess < secretNum:
        print("Too low")
    elif guess > secretNum:
        print("Too high")
if guess == secretNum:
    print("Same as the secret number")

