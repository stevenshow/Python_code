import random
import numpy as np
from numpy import random
import time
from playsound import playsound
def square_num(num):
    square = num*num
    return square

#Make a dice rolling game that stores your 5 rolls and adds them up and saves a hi-score



def user_input():
    play = input('Would you like to play the dice game? [Y/N]:').upper()
    if play == 'Y':
        name = input('Please enter your name: ')
        new_game = input('Would you like to read the rules? [Y/N]: ').upper()
        if new_game == 'Y':
            print(name + ' you will roll the dice 5 times and have your score added up at the end.  If you are in the top 3 scorers you will be placed on the wall of fame.  Good luck!')

def dice_roll():    
    sum = 0
    dice_rolled = 0
    diceDict={
    1 : ('|   |\n| * |\n|   |'),
    2 : ('|*  |\n|   |\n|  *|'),
    3 : ('|  *|\n| * |\n|*  |'),
    4 : ('|* *|\n|   |\n|* *|'),
    5 : ('|* *|\n| * |\n|* *|'),
    6 : ('|* *|\n|* *|\n|* *|')}
    roll_again = True
    while(roll_again):
        roll = random.choice([1, 2, 3, 4, 5, 6])
        playsound('roll_dice.mp3')
        print(diceDict[roll])
        roll_again = ('y' or 'yes') in input('Would you like to roll again? [Y/N]: ').lower()
        sum = sum + roll
        dice_rolled = dice_rolled + 1
    print('Your total after rolling '+ str(dice_rolled) + ' dice was [' + str(sum) + ']')

   

dice_roll()