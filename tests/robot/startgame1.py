#!/bin/python3
####################################################################
#                            MODULES                               #
####################################################################
import os, sys, time

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

global action_choice, life_count
action_choice = ""
life_count = 3
game_end_status = ""
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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
####################################################################
#                        _draw_map_func                            #
####################################################################
def _draw_map_func():
    print("""
    #################################
    #         Atari World           #
    #################################
-----------------------------------------
|0,9|1,9|2,9|3,9|4,9|5,9|6,9|7,9|8,9|9,9|
-----------------------------------------
|0,8|1,8|2,8|3,8|4,8|5,8|6,8|7,8|8,8|9,8|
-----------------------------------------
|0,7|1,7|2,7|3,7|4,7|5,7|6,7|7,7|8,7|9,7|
-----------------------------------------
|0,6|1,6|2,6|3,6|4,6|5,6|6,6|7,6|8,6|9,6|
-----------------------------------------
|0,5|1,5|2,5|3,5|4,5|5,5|6,5|7,5|8,5|9,5|
-----------------------------------------
|0,4|1,4|2,4|3,4|4,4|5,4|6,4|7,4|8,4|9,4|
-----------------------------------------
|0,3|1,3|2,3|3,3|4,3|5,3|6,3|7,3|8,3|9,3|
-----------------------------------------
|0,2|1,2|2,2|3,2|4,2|5,2|6,2|7,2|8,2|9,2|
-----------------------------------------
|0,1|1,1|2,1|3,1|4,1|5,1|6,1|7,1|8,1|9,1|
-----------------------------------------
|0,0|1,0|2,0|3,0|4,0|5,0|6,0|7,0|8,0|9,0|
-----------------------------------------
STARTING POINT is 0,0
END POINT is 9,9
Watch out for hidden mines, and GO!!
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
#                      _mine_hit_function                          #
####################################################################
def _mine_hit_function():
    global life_count, game_end_status
    mine_list = ["40", "70", "13", "17", "03", "05", "07", "19", "39", "98"]
    target = str(current_x_position) + str(current_y_position)
    if target in mine_list:
        life_count = life_count - 1
        print ("\nOH NO, YOU STEPPED ON A MINE")
        print ("You lost one life")
        time.sleep(3)
    if target == "99":
        print ("\n CONGRATULATIONS, YOU MADE IT")
        game_end_status = "YOU WON"
        time.sleep(3)
        _exit_function()
    
####################################################################
#                      _exit_function                              #
####################################################################
def _exit_function():
    _clear_screen()
    print ("############################################")
    print ("               Game Summary                #")
    print ("############################################")
    print ("Character: "+name)
    print ("Game Status: "+game_end_status)
    print ("Last Position: "+str(current_y_position)+","+str(current_x_position))
    print ("Total Moves: "+str(total_move_count)+"\n\n")
    sys.exit()

####################################################################
#                               MAIN                               #
####################################################################
_clear_screen()
_welcome_screen()
name = input('What is your name?\n')     # \n --->
play_choice = input("\nWelcome "+name+" , would you like to play? Y/N ").upper() 

if  play_choice == "Y" :
   print ("Great, Lets go!")
elif play_choice == "N":
   print ("\nYour cowardice is a disgrace.")
   print ("Jennifer is very disappointed in you.\n\n")
   sys.exit()
else:
   print("Invalid Option Entered.  Exiting Game.\n\n")  

while play_choice == "Y":
    _clear_screen()
    _draw_map_func()
    print("\nCharacter: "+name)
    print("Life count: "+str(life_count))
    print("Position: "+str(current_x_position)+" , "+str(current_y_position))
    action_choice = input("Move direction? N, S, E, W, or Q to quit: ").upper()
    if action_choice == "N" or action_choice == "S" or action_choice == "E" or action_choice == "W":
       _validate_move()
       _mine_hit_function()
       if life_count == 0:
           game_end_status = "YOU LOST"
           print("GAME OVER")
           time.sleep(3)
           _exit_function()
    elif action_choice == "Q":
        _exit_function()
