import random
print("Welcome to the number guessing game!\nYou will have 5 guesses to guess a number between 1 and a 100, and after each guess, I will give you a hint to help you!")
number = random.randint(1, 100)
guesses = 5
while guesses>0:
    user = int(input("What is your guess?\n"))
    if user > number:
        print("Thats too high!")
    elif user < number:
        print("Thats too low!")
    else:
        print("Good Job! You guessed the number!")
        break
    guesses -= 1
if guesses <= 0:
    print(f"You ran out of guesses! The number was {number}!")