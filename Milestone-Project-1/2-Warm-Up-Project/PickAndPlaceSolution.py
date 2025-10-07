'''


'''
import os
def clear_console():
    '''

    '''

    os.system('cls' if os.name == 'nt' else 'clear')
#________________________________________________________________________
def display_game(game_list):
    '''

    '''

    print("Here is the current list")
    print(game_list)
#________________________________________________________________________

def podition_choice():
    '''

    '''

    # This original choice value can be anything that isn't an integer
    choice = 'wrong'
    # While the choice is not a digit, keep asking for input.
    while choice not in ['0','1','2']:
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Pick a POSITION to replace (0,1,2): ")

        if choice not in ['0','1','2']:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            clear_console()

            print("Sorry, but you did not choose a valid POSITION (0,1,2)")


    # Optionally you can clear everything after running the function
    # clear_output()

    # We can convert once the while loop above has confirmed we have a digit.
    return int(choice)

#________________________________________________________________________

def replacement_choice(game_list,POSITION):
    '''

    '''

    user_placement = input("Type a string to place at the POSITION")
    game_list[POSITION] = user_placement
    return game_list
#________________________________________________________________________

def game_on_choice():
    '''

    '''

    # This original choice value can be anything that isn't a Y or N
    choice = 'wrong'
    # While the choice is not a digit, keep asking for input.
    while choice not in ['Y','N']:
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Would you like to keep playing? Y or N ")
        if choice not in ['Y','N']:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            clear_console()
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
    # Optionally you can clear everything after running the function
    # clear_console()
    if choice == "Y":
        # Game is still on
        return True
    else:
        # Game is over
        return False
#________________________________________________________________________


GAME_ON = True
# First Game List
game_list = [0,1,2]
while GAME_ON:

    # Clear any historical output and show the game list
    clear_console()
    display_game(game_list)

    # Have player choose POSITION
    POSITION = podition_choice()

    # Rewrite that POSITION and update game_list
    game_list = replacement_choice(game_list,POSITION)

    # Clear Screen and show the updated game list
    clear_console()
    display_game(game_list)

    # Ask if you want to keep playing
    GAME_ON = game_on_choice()
