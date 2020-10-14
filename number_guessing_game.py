from random import randint

def guessing_game():
    """Takes input from the user and compares against the randomly generated number to 
    determine if they match"""
    number = randint(10, 30)
    while True:
        user_guess = int(input('What is the random number? '))
        if user_guess == number:
            print('You win!')
            break
        elif user_guess < number:
            print(f'{user_guess} is too low, try again: ')
        else:
            print(f'{user_guess} is too high, try again: ')

guessing_game()