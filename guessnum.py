import random

print('Welcome to the number guessing game! You have to guess the number from the range of 0 to 30 in as few tries as possible.')

secret = random.randint(0, 40)
guesses = 0
guess = False

while guess == False:
    attempt = int(input('Guess the number between zero and forty:'))
    if attempt > secret:
        print('That is too high!')
        guesses += 1
    if attempt < secret:
        print('That is too low!')
        guesses += 1
    if attempt == secret:
        print('You did it! Congratulations!')
        print('It took you ' + str(guesses) + ' guesses until you found it!')
        
