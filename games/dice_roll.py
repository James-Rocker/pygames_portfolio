import random
import time
import sys


def _roll_validate(roll):
    try:
        int(roll)
        return True
    except ValueError:
        print("Please enter a number for the number of rolls")
        return False


def _roll_dice(dice_roll, die_type):
    if _roll_validate(roll=dice_roll) is True and _dice_type(die_type) is True:
        for i in range(int(dice_roll)):
            print(random.choice(_die(die_type)))


def _die(die_type):
    die_list = list(range(1, int(die_type) + 1))
    return die_list


def _dice_type(die_type):
    valid_dice = [2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 24, 30, 34, 48, 50, 60, 100, 120]
    try:
        int(die_type)
        if int(die_type) in valid_dice:
            return True
        elif die_type not in valid_dice:
            print("This is not a valid dice")
            return False
    except ValueError:
        print("That's not a dice number!")


class Game:
    def __init__(self):
        self.re_roll = True
        self.run_true = ['yes', 'y']
        self.run_false = ['no', 'n']

    def play(self):
        print("Welcome to the dice roll application")
        time.sleep(1)
        roll_confirm = input("Would you like to roll a dice? ")

        while roll_confirm in self.run_true:
            time.sleep(1)
            if self.re_roll is True:
                dice_roll = input("How many times do you want to roll a dice? ")
                dice_type = input("What kind of die do you want to roll? D")
                _roll_dice(dice_roll, dice_type)
                time.sleep(1)
                rerun = input("Do you want another roll? ").lower()
                if rerun in self.run_true:
                    print("Okay")
                elif rerun in self.run_false:
                    print("Okay, thank you for using the dice program.")
                    time.sleep(1)
                    sys.exit()
                else:
                    print("Sorry, I don't understand what you said. The dice program is shutting down.")
                    time.sleep(3)
                    sys.exit()
        else:
            print("Okay, have a nice day.")
            time.sleep(3)
            sys.exit()

