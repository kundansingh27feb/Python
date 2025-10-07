"""
_____________________________________________________________________________________________

It is time to get you to put together all your skills to start building usable projects!
Before you jump into our full milestone project, we will go through some warm-up component
exercises, to get you comfortable with a few key ideas we use in the milestone projectand
larger projects in general, specifically:
------------------
Getting User Input
Creating Functions that edit variables based on user input
Generating output
Joining User Inputs and Logic Flow
_____________________________________________________________________________________________

"""
#Create a small game where a user can choose a "position" in an existing list and replace it
# with a value of their choice.

# Example:

# PS C:\Users\v-kundsingh\Projects\AI\Python\Milestone-Project-1\Warm Up Project> python
# .\Solution.py
# Here is the current list
# [0, 1, 2]

# Pick a position to replace (0,1,2): 0
# Type a string to place at the position10
# Here is the current list
# ['10', 1, 2]

# Would you like to keep playing? Y or N Y
# Here is the current list
# ['10', 1, 2]

# Pick a position to replace (0,1,2): 2
# Type a string to place at the position5
# Here is the current list
# ['10', 1, '5']

# Would you like to keep playing? Y or N N

def display_list(list1):
    '''

    '''

    print("Here is the Current List:")
    print(list1)

def choice_position():
    '''

    '''
    choice = ''
    while choice not in ['0','1','2']:
        choice = input("Pick a position where you want to replace(0, 1, 2): ")
        if choice not in ['0','1','2']:
            print("Sorry! Worng Choice!! Please enter from (0, 1, 2).")
    return int(choice)

def replace_choice(list1,choice):
    '''

    '''
    user_input = input("Please enter the string to replace: ")
    list1[choice] = user_input
    return list1

def game_on_choice():
    '''

    '''
    choice = ''
    while choice not in ['Y','N']:
        choice = input("Would You like to keep playing? Y or N: ")
        if choice not in ['Y','N']:
            print("Wrong Input. Please select Y or N.")

    if choice == 'Y':
        return True
    else:
        return False

GAME_ON = True
list1 = [0,0,0]
while GAME_ON:
    display_list(list1)
    choice = choice_position()
    list1 = replace_choice(list1,choice)
    display_list(list1)
    GAME_ON = game_on_choice()
