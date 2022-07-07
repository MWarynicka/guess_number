print("Welcome to the Number Guessing Game!")
print("I'am thinking of a number between 1 and 100")
dificulty=input("Choose the dificulty. Type 'easy' or 'hard': ")

import random
number_to_guess= random.randint(0, 100)
lives1 =5
lives2 =10
finish= False
while not finish:
  guess=int(input("Make a guess: "))
  if guess > number_to_guess:
    print("too high")
  elif guess < number_to_guess:
    print("Too low")
  elif guess == number_to_guess:
    finish= True
    print(f"The number is {number_to_guess}")
  if dificulty== "easy":
    if  not number_to_guess==guess:
      lives2 -= 1
      if lives2 == 0:
        finish = True
        print("game over")
    print(f"You have {lives2} attemps ramaining to guess the number.")
  elif dificulty== "hard":
    if  not number_to_guess==guess:
      lives1 -= 1
      if lives1 == 0:
        finish = True
        print("game over")
    print(f"You have {lives1} attemps ramaining to guess the number.")
