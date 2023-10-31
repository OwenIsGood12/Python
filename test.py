import random

number = random.randint(1, 100)
guessing = True
while guessing:
  guess = input('Guess the number')
  if int(guess) > number:
    print('The number is less than', guess)
  if int(guess) < number:
    print('The number is greater than', guess)
  if int(guess) = number:
    print('Correct!'
    guessing = False
