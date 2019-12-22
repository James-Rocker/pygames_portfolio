from games import battleships as bs
from games import dice_roll as dr
from games import rock_paper_scissors as rps

if __name__ == "__main__":
    games_list = ['battleships', 'dice', 'rock paper scissors']
    game_select = False

    while game_select is False:
        selected_game = input("What game would you like to play? ")
        if not [s for s in games_list if selected_game in s]:
            print('Please select either ' + str(games_list))
        else:
            game_select = True
            if selected_game in games_list[0]:
                bs.Game().play()
            elif selected_game in games_list[1]:
                dr.Game().play()
            elif selected_game in games_list[2]:
                rps.Game().play()
