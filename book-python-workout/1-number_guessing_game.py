from random import randint

def guessing_game():
    """Takes an input from the user and compares against the randomly generated number to 
    determine if they match"""

    number = randint(1, 30)
    guess_counter = 2
    while guess_counter > -1:
        guess_greeting = f'You have {guess_counter} attempts remaining.'
        if guess_counter == 1:
            guess_greeting = f'You have {guess_counter} attempt remaining.'
        user_guess = int(input('The random number is between 1 and 30. What is the random number? '))
        if user_guess == number:
            print('You win!')
            break
        elif user_guess < number:
            print(f'{user_guess} is too low.')
            guess_counter -= 1
            print(guess_greeting)
        else:
            print(f'{user_guess} is too high.')
            guess_counter -= 1
            print(guess_greeting)
    
    if guess_counter == -1:
        print('You are out of attempts. Game over.')

guessing_game()