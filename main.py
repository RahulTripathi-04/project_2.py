import random
n = random.randint(1, 100)
a = -1
guesses = 0

while (a!=n):
    guesses += 1
   

    a = int(input("Guess a number between 1 and 100 (or -1 to quit):"))

    if a == -1:
        print("Game over.")
        break
    elif a > n:
        print("Too high!")
    elif a < n:
        print("Too low!")

print(f"You have guessed the number {n} correctly in {guesses} attempts.")        