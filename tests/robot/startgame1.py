####################################################################
#                            MODULES                               #
####################################################################
import os, sys

####################################################################
#                           VARIABLES                              #
####################################################################
max_y_coordinates = 9
min_y_coordinates = 0
max_x_coordinates = 9
min_y_coordinates = 0

current_y_position = 0
current_x_position = 0
total_move_count = 0

global action_choice
action_choice =""

####################################################################
#                       _welcome_screen                            #
####################################################################
def _welcome_screen():
   print("""
#############################################
        Welcome to the world of Atari.
Adventure awaits the ones brave enought to
enter this world of crazy.
#############################################\n\n
""")
####################################################################
#                       _clear_screen                              #
####################################################################
def _clear_screen():
    os.system('clear')

####################################################################
#                      _validate_move                              #
####################################################################
def _validate_move():
    global current_y_position, current_x_position, total_move_count
    total_move_count = total_move_count + 1

    if action_choice == "W":
        new_x_position = current_x_position - 1
        if new_x_position >= 0 and new_x_position <= 9:
            current_x_position =  new_x_position

    if action_choice == "E":
        new_x_position = current_x_position + 1
        if new_x_position >= 0 and new_x_position <= 9:
            current_x_position = new_x_position

    if action_choice == "N":
        new_y_position = current_y_position + 1
        if new_y_position >= 0 and new_y_position <= 9:
            current_y_position = new_y_position

    if action_choice == "S":
        new_y_position = current_y_position - 1
        if new_y_position >= 0 and new_y_position <= 9:
            current_y_position = new_y_position
####################################################################
#                      _exit_function                              #
####################################################################
def _exit_function():
    _clear_screen()
    print ("############################################")
    print ("               Game Summary                #")
    print ("############################################")
    print ("Character: "+name)
    print ("Last Position: "+str(current_y_position)+" , "+str(current_x_position))
    print ("Total Moves: "+str(total_move_count))
    sys.exit()

####################################################################
#                               MAIN                               #
####################################################################
_clear_screen()
_welcome_screen()
name = input('What is your name?\n')     # \n --->
play_choice = input("\nWelcome "+name+" , would you like to play?").upper() 

if  play_choice == "Y" :
   print ("Great, Lets go!")
else:
   print ("\nYour cowardice is a discrace")
   exit()

while play_choice == "Y":
    _clear_screen()
    print("\nCharacter: "+name)
    print("Position: "+str(current_y_position)+" , "+str(current_x_position))
    action_choice = input("Move direction? N, S, E, W, or Q to quit: ").upper()
    if action_choice == "N" or action_choice == "S" or action_choice == "E" or action_choice == "W":
       _validate_move()
    elif action_choice == "Q":
        _exit_function()
