import random
guesses=1
low=int(input("Enter the lower limit: "))
high=int(input("Enter the higher limit: "))
num=random.randint(low,high)
guess=int(input("Enter Your Guess: "))
while num!=guess:
    if guess<num:
        guesses+=1
        print("Too Low!")
        guess=int(input("Enter Your Guess: "))
    elif guess>num:
        guesses+=1
        print("Too High!")
        guess=int(input("Enter Your Guess: "))
print("Yes! You Guessed it Correct!") 
print(f"The no.of Guesses = {guesses}")  