import sys
import random
from time import sleep


class Game:
    def __init__(self):
        self.wins = 0
        self.loses = 0
        self.RPS = ['Rock', 'Paper', 'Scissors']
        self.confirm = ['Yes', 'Y', 'Okay']

    def _game(self):
        player_rps = input("Please select either rock, paper or scissors: ")
        player_clean = player_rps.capitalize()

        def validate(a):
            if player_rps.capitalize() in self.RPS:
                return True
            else:
                return False

        rps_cpu = (random.choice(self.RPS))
        if validate(player_clean) is False:
            sleep(1)
            sys.exit("Hey! You should have chosen either rock, paper or scissors.")

        def win_condition(a, b):
            if (a, b) in (("Rock", "Scissors"), ("Paper", "Scissors"), ("Scissors", "Rock")):
                return True

        def choices():
            sleep(1)
            print("Player chooses - " + player_clean)
            sleep(1)
            print("CPU chooses - " + rps_cpu)

        choices()

        if rps_cpu != player_clean:
            if win_condition(player_clean, rps_cpu):
                sleep(1)
                print("Player wins!")
                self.wins += 1
                self._score()
            else:
                sleep(1)
                print("CPU wins")
                self.loses += 1
                self._score()
        else:
            sleep(1)
            print("Tie!")
            self._score()

    def _score(self):
        print("Wins: " + str(self.wins) + " Loses: " + str(self.loses))
        play_again = input("Do you want to play again? ")
        if play_again.capitalize() in self.confirm:
            self._game()
        else:
            print("Final score is - " + "Wins: " + str(self.wins) + " Loses: " + str(self.loses))
            print("Thanks for playing!")
            sleep(5)

    def play(self):
        print("Welcome to the Rock Paper Scissors application!")
        sleep(1)
        user_input = input("Would you like to play, rock, paper, scissors? ")
        if user_input.capitalize() in self.confirm:
            sleep(1)
            self._game()
        else:
            print("Okay, have a nice day.")
            sleep(5)
