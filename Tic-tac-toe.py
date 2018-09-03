
def naughts_and_crosses():

    #Game board
    def game_board():
        print(f" {pos_7} | {pos_8} | {pos_9} ")
        print("------------")
        print(f" {pos_4} | {pos_5} | {pos_6} ")
        print("------------")
        print(f" {pos_1} | {pos_2} | {pos_3} ")

    #Win statement
    def win_statement():
        if player1go == "FALSE":
            winning_player = player1
        else:
            winning_player = player2
        print(f"Congratulations {winning_player}, you have won!")
        new_game()

    #New game
    def new_game():
        new_game_input = str(input("Do you want to play again?"))
        if new_game_input.lower() == "yes":
            naughts_and_crosses()
        else:
            print("OK. Thanks for playing!")
            global player1go
            global player2go
            player1go = "FALSE"
            player2go = "FALSE"

    #Invalid input
    def invalid_input():
        print("That's not a valid input, try again!")

    #Win checking
    def win_checking():
        if move_d["position_7"]==move_d["position_8"]==move_d["position_9"]:
            win_statement()

        elif move_d["position_4"]==move_d["position_5"]==move_d["position_6"]:
            win_statement()

        elif move_d["position_1"]==move_d["position_2"]==move_d["position_3"]:
            win_statement()

        elif move_d["position_7"]==move_d["position_4"]==move_d["position_1"]:
            win_statement()

        elif move_d["position_8"]==move_d["position_5"]==move_d["position_2"]:
            win_statement()

        elif move_d["position_9"]==move_d["position_6"]==move_d["position_3"]:
            win_statement()

        elif move_d["position_7"]==move_d["position_5"]==move_d["position_3"]:
            win_statement()

        elif move_d["position_9"]==move_d["position_5"]==move_d["position_1"]:
            win_statement()

        elif move_d["position_4"]==move_d["position_5"]==move_d["position_6"]:
            win_statement()

        elif move_d["position_8"]==move_d["position_5"]==move_d["position_2"]:
            win_statement()

        elif set(move_d.values()) == set(comparison_d.values()):
            print("Game over - no more moves left!")
            new_game()

    #Declaring the values for the board positions
    pos_1=" "
    pos_2=" "
    pos_3=" "
    pos_4=" "
    pos_5=" "
    pos_6=" "
    pos_7=" "
    pos_8=" "
    pos_9=" "

    #Position dictionary
    pos_d = {"1":pos_1,"2":pos_2,"3":pos_3,"4":pos_4,"5":pos_5,"6":pos_6,"7":pos_7,"8":pos_8,"9":pos_9}
    move_d = {"position_1":"1","position_2":"2","position_3":"3","position_4":"4","position_5":"5","position_6":"6","position_7":"7","position_8":"8","position_9":"9"}
    comparison_d = {"k1":"X","k2":"O"}

    #Introduction
    print("Welcome to naughts and crosses! \nWhen asked for your move, type in the number corresponding to the position on the board below.")
    print(f" 7 | 8 | 9 ")
    print("------------")
    print(f" 4 | 5 | 6 ")
    print("------------")
    print(f" 1 | 2 | 3 ")

    #Preparing game state
    game_state = "TRUE"
    global player1go
    global player2go
    player1go = "TRUE"

    #Selecting character
    while game_state is "TRUE":
        player1 = str(input("Player 1: Do you want to be X or O?")).upper()
        if player1 not in set(comparison_d.values()):
            invalid_input()
            continue

        if player1 == "X":
            player2 = "O"
        else:
            player1 = "O"
            player2 = "X"


        game_board()
        break

    #Game logic
    while game_state is "TRUE":
        while player1go is "TRUE":
            player1_moveinput = str(input(f"Player 1 - {player1} - what is your move?"))
            if player1_moveinput == "1":
                if pos_1 != " ":
                    invalid_input()
                    continue
                pos_1 = player1
                move_d["position_1"] = player1
            elif player1_moveinput == "2":
                if pos_2 != " ":
                    invalid_input()
                    continue
                pos_2 = player1
                move_d["position_2"] = player1
            elif player1_moveinput == "3":
                if pos_3 != " ":
                    invalid_input()
                    continue
                pos_3 = player1
                move_d["position_3"] = player1
            elif player1_moveinput == "4":
                if pos_4 != " ":
                    invalid_input()
                    continue
                pos_4 = player1
                move_d["position_4"] = player1
            elif player1_moveinput == "5":
                if pos_5 != " ":
                    invalid_input()
                    continue
                pos_5 = player1
                move_d["position_5"] = player1
            elif player1_moveinput == "6":
                if pos_6 != " ":
                    invalid_input()
                    continue
                pos_6 = player1
                move_d["position_6"] = player1
            elif player1_moveinput == "7":
                if pos_7 != " ":
                    invalid_input()
                    continue
                pos_7 = player1
                move_d["position_7"] = player1
            elif player1_moveinput == "8":
                if pos_8 != " ":
                    invalid_input()
                    continue
                pos_8 = player1
                move_d["position_8"] = player1
            elif player1_moveinput == "9":
                if pos_9 != " ":
                    invalid_input()
                    continue
                pos_9 = player1
                move_d["position_9"] = player1
            else:
                invalid_input()
                continue

            #Swapping turns
            player1go = "FALSE"
            player2go = "TRUE"

            #Game board
            game_board()

            #Win checking
            win_checking()

            break

        while player2go is "TRUE":
            player2_moveinput = str(input(f"Player 2 - {player2} - what is your move?"))
            if player2_moveinput == "1":
                if pos_1 != " ":
                    invalid_input()
                    continue
                pos_1 = player2
                move_d["position_1"] = player2
            elif player2_moveinput == "2":
                if pos_2 != " ":
                    invalid_input()
                    continue
                pos_2 = player2
                move_d["position_2"] = player2
            elif player2_moveinput == "3":
                if pos_3 != " ":
                    invalid_input()
                    continue
                pos_3 = player2
                move_d["position_3"] = player2
            elif player2_moveinput == "4":
                if pos_4 != " ":
                    invalid_input()
                    continue
                pos_4 = player2
                move_d["position_4"] = player2
            elif player2_moveinput == "5":
                if pos_5 != " ":
                    invalid_input()
                    continue
                pos_5 = player2
                move_d["position_5"] = player2
            elif player2_moveinput == "6":
                if pos_6 != " ":
                    invalid_input()
                    continue
                pos_6 = player2
                move_d["position_6"] = player2
            elif player2_moveinput == "7":
                if pos_7 != " ":
                    invalid_input()
                    continue
                pos_7 = player2
                move_d["position_7"] = player2
            elif player2_moveinput == "8":
                if pos_8 != " ":
                    invalid_input()
                    continue
                pos_8 = player2
                move_d["position_8"] = player2
            elif player2_moveinput == "9":
                if pos_9 != " ":
                    invalid_input()
                    continue
                pos_9 = player2
                move_d["position_9"] = player2
            else:
                invalid_input()
                continue

            #Swapping turns
            player2go = "FALSE"
            player1go = "TRUE"

            #Game board
            game_board()

            #Win checking
            win_checking()

            break

naughts_and_crosses()
