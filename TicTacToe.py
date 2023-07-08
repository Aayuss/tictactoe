def print_guidegrid():
    print(" " + str(game_elements[0]) + " | " + str(game_elements[1]) + " | " + str(game_elements[2]))
    print("----------");
    print(" " + str(game_elements[3]) + " | " + str(game_elements[4]) + " | " + str(game_elements[5]))
    print("----------");
    print(" " + str(game_elements[6]) + " | " + str(game_elements[7]) + " | " + str(game_elements[8]))

def print_pattern():
    print(" " + str(ge[0]) + " | " + str(ge[1]) + " | " + str(ge[2]))
    print("----------");
    print(" " + str(ge[3]) + " | " + str(ge[4]) + " | " + str(ge[5]))
    print("----------");
    print(" " + str(ge[6]) + " | " + str(ge[7]) + " | " + str(ge[8]))

def turn_of_x():
    while(1):
        print("Turn of 'X'\n")
        x_input = int(input("Enter where you want to put X: "));
        
        if (str(ge[x_input-1]) == "X" or 
            str(ge[x_input-1]) == 'O' or
            x_input < 1 or x_input > 9):
            print("Invalid input value. Re-enter: \n")
        
        
        else:
            ge[x_input-1] = "X"
            print(print_pattern())
            break
        
def turn_of_o():
    while(1):
        print("Turn of 'O'\n")
        x_input = int(input("Enter where you want to put O: "));
        
        if (str(ge[x_input-1]) == "X" or 
            str(ge[x_input-1]) == 'O' or
            x_input < 1 or x_input > 9):
            print("Invalid input value. Re-enter: \n")
        
        
        else:
            ge[x_input-1] = "O"
            print(print_pattern())
            break
             
def check_win():
    if (ge[0] == ge[1] == ge[2] == "X" or
            ge[0] == ge[3] == ge[6] == "X"  or
            ge[0] == ge[4] == ge[8] == "X"  or
            ge[1] == ge[4] == ge[7] == "X"  or
            ge[2] == ge[5] == ge[8] == "X"  or
            ge[3] == ge[4] == ge[5] == "X"  or
            ge[6] == ge[7] == ge[8] == "X"  or
            ge[6] == ge[4] == ge[2] == "X"):
        print("X wonnnnnnnnnnn")
        
        return 1
    
    elif (ge[0] == ge[1] == ge[2] == "O" or
            ge[0] == ge[3] == ge[6] == "O"  or
            ge[0] == ge[4] == ge[8] == "O"  or
            ge[1] == ge[4] == ge[7] == "O"  or
            ge[2] == ge[5] == ge[8] == "O"  or
            ge[3] == ge[4] == ge[5] == "O"  or
            ge[6] == ge[7] == ge[8] == "O"  or
            ge[6] == ge[4] == ge[2] == "O"):
        print("O wonnnnnnnnnnn")
        
        return 1
    
    return 0
    
#---------------------------------------------------------------#

game_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ge = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

print("\nWelcome to this game. Please remember the code numbers to put the number in\n")
print(print_guidegrid())
print(print_pattern())

while(1):
    
    turn_of_x()
    if (check_win()):
        print("Game Over")
        break
    
    turn_of_o()
    if (check_win()):
        print("Game Over")
        break
   
    
    
    
    








