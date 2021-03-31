import random

def number_guess():
    num = random.randint(0,10)
    user_num = int(input('Please guess a number between 1-10: '))
    while(user_num != num):
        if user_num < num:
            user_num = int(input(f'The number is higher than {user_num} try again: '))
        else:
            user_num = int(input(f'The number is lower than {user_num} try again: '))
    print(f'Congratulations!  The number was {user_num}')

number_guess()