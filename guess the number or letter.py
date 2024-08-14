print("Hello men and women and any othe gender. WELCOME TO MY SHOW- I mean welcome to my")
import random

def guess_the_number():

  sigma = "abcdefghijklmnopqrstuvwxyz"
  number = random.randint(1, 26)
  letter = sigma[number - 1]
  funny = 0

  while True:
    guess = input("Guess a letter (a-z): ").lower()
    funny += 1

    if len(guess) != 1 or not guess.isalpha():
      print("Invalid input. Please enter a single letter.")
      continue

    funny = ord(guess) - ord('a') + 1

    if funny == number:
      print(f"Congratulations! You guessed the letter '{letter}' in {funny} tries. Get better next time! (or fail miserably)")
      break
    else:
      print("You are wrong. Get out or do it again")

guess_the_number()
