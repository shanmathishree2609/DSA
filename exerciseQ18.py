# Secret number
secret = 7
# Keep asking until the user guesses correctly
while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Congratulations! You guessed it.")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")
