import random
from playsound import playsound

def play_game(dice):
    roll = ""
    
    for i in range(dice):
        choice_1 = random.randint(1,4)
        if choice_1 == 1: roll += '[L] '
        if choice_1 == 2: roll += '[*] '
        if choice_1 == 3: roll += '[R] '
        if choice_1 == 4: roll += '[C] '
    print(roll)
        

while True:
    my_input = input('How many dollarie-doos: ')
    if my_input.isdigit():
        my_input = int(my_input)
        playsound('roll_dice.mp3')
        if my_input >= 3:
            play_game(3)
        if my_input == 2:
            play_game(2)
        if my_input == 1:
            play_game(1)
