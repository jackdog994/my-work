"""Second milestone project of the course - create a game of blackjack. This was quite a long
piece of work, taking me about a week to complete. I enjoyed translating the rules of blackjack in
to the logical rules you can build in Python. There were a lot of steps to complete for this so to help
me keep track I created and worked through the list below."""

#Variable Players: Y
#Player Names Retreived: Y
#Initial Bets Taken: Y
#Initial Card Deal: Y
#Conversion of Cards Dealt to Numerical Value: Y
#Natural Check: Y
#Stand/Hit/Bust: Y
#Calculating Bet Result: Y
#Confirming Whether Player Out of Game: Y
#Option to Leave Table: Y
#Option to Join Table: Y
#New Round: Y
#New Game: Y

#Step 1: Define Player attributes

class Player:
    '''Class for defining attributes'''
    def __init__(self):
        self.attributes = {"name":"","pool":100,"bet_size":0,"hand":[],"hand_value":[],"natural":False,"in_round":True}

    def reset(self):
        self.attributes = {"name":"","pool":100,"bet_size":0,"hand":[],"hand_value":[],"natural":False,"in_round":True}


    def update_name(self,input_name):
        self.input_name = input_name
        self.attributes["name"] = self.input_name

    def update_bet(self,bet_size):
        self.bet_size = bet_size
        self.attributes["bet_size"] = self.bet_size

    def update_hand(self,dealt_card):
        self.dealt_card = dealt_card
        self.attributes["hand"].append(self.dealt_card)

#Step 2: Define each of your players as Player object

#Setting up player variables
DEALER = Player()
PLAYER1 = Player()
PLAYER2 = Player()
PLAYER3 = Player()
PLAYER4 = Player()
PLAYER5 = Player()
PLAYER6 = Player()

PLAYER_LIST = [DEALER, PLAYER1, PLAYER2, PLAYER3, PLAYER4, PLAYER5, PLAYER6]
ORIGINAL_PLAYER_LIST = [DEALER, PLAYER1, PLAYER2, PLAYER3, PLAYER4, PLAYER5, PLAYER6]
GAME_STATE = True
NO_PLAYERS = 0
SHUFFLED_DECK = []
SKIP_JOIN = False

def invalid_answer():
    print("That's not a valid answer!")


#Step 3 - Create a function to define how many players will exist in a round
#This only needs to happen once per game

def defining_players(NO_PLAYERS,PLAYER_LIST):
    '''Defining the number of players in a round'''
    DEALER.update_name("Dealer")
    DEALER.attributes["pool"]:100
    INDEX_POS = -1
    PLAYER_NO = 1

    #Determining how many players
    while GAME_STATE is True:
        try:
            NO_PLAYERS = int(input("How many players are there? "))
            break
        except:
             invalid_answer()
             continue
    for player in range(NO_PLAYERS,(len(ORIGINAL_PLAYER_LIST)+1)):
        try:
            del(PLAYER_LIST[player-INDEX_POS])
            INDEX_POS += 1
        except IndexError:
            break

    #Asking for player.name
    for player in range(1,(NO_PLAYERS+1)):
        input_name = str(input(f"Player {PLAYER_NO} what is your name? "))
        PLAYER_LIST[player].update_name(input_name)
        PLAYER_NO += 1

    return NO_PLAYERS,PLAYER_LIST

# NOTE: NO_PLAYERS,PLAYER_LIST = defining_players(NO_PLAYERS,PLAYER_LIST)

#Step 4 - Create a deck and shuffle it
#This needs to happen every round
def shuffle_deck(SHUFFLED_DECK):
    '''Creating and shuffling a deck of cards'''
    #Defining the deck
    deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","Ace"]*4
    decksize = 13*4
    SHUFFLED_DECK = list(range(0,decksize))

    #Shuffling the deck
    for card in deck:
        while GAME_STATE == True:
            import random
            deck_pos = random.randint(0,decksize)
            if deck_pos in SHUFFLED_DECK:
                SHUFFLED_DECK[deck_pos] = card
                break
            else:
                continue

    return SHUFFLED_DECK

# NOTE: SHUFFLED_DECK = shuffle_deck(SHUFFLED_DECK)

#Step 5 - Print the player pools at the start of each Round
#This needs to happen every round
def print_pool():
    '''Printing the player pools'''
    pool_string = ""
    print("\nThe current player pools:")
    for player in range(1,(NO_PLAYERS+1)):
        pool_string += f"{PLAYER_LIST[player].attributes['name']}:{PLAYER_LIST[player].attributes['pool']} "
    print(f"{pool_string}\n")

# NOTE: print_pool()

#Step 6 - Take the players bets
#This needs to happen every round
def taking_bets():
    '''Asking player bets'''
    for player in range(1,(NO_PLAYERS+1)):
        while GAME_STATE is True:
            try:
                bet_size = int(input(f"{PLAYER_LIST[player].attributes['name']} how much would you like to bet? "))
                if bet_size > PLAYER_LIST[player].attributes['pool']:
                    invalid_answer()
                elif bet_size == 0:
                    invalid_answer()
                else:
                    PLAYER_LIST[player].update_bet(int(bet_size))
                    break
            except:
                invalid_answer()
                continue

# NOTE: taking_bets()

#Step 7 - Deal out 2 cards to each player6
#This needs to happen every Round
class Deal():

    def dealing(self,SHUFFLED_DECK,player):
        """Function to deal a single card"""
        dealt_card = SHUFFLED_DECK.pop(0)
        PLAYER_LIST[player].update_hand(dealt_card)
        try:
            PLAYER_LIST[player].attributes['hand_value'].append(int(PLAYER_LIST[player].attributes['hand'][-1]))
        except:
            if PLAYER_LIST[player].attributes['hand'][-1] == "Ace":
                PLAYER_LIST[player].attributes['hand_value'].append("Ace")
            else:
                PLAYER_LIST[player].attributes['hand_value'].append(10)

    #Dealing the first round of cards
    def first_deal(self):
        """Dealing the first round of cards"""
        for i in range(0,2):
            for player in range(0,(NO_PLAYERS+1)):
                self.dealing(SHUFFLED_DECK,player)

        HAND_STRING = ""
        print("\nThe result after the first deal:\n")
        for player in range(0,(NO_PLAYERS+1)):
            if PLAYER_LIST[player].attributes['name'] == 'Dealer':
                HAND_STRING += f"Dealer: ['{PLAYER_LIST[0].attributes['hand'][0]}','?']\n"
            else:
                HAND_STRING += f"{PLAYER_LIST[player].attributes['name']}:{PLAYER_LIST[player].attributes['hand']} "
        print(f"{HAND_STRING}\n")

# NOTE: Deal().first_deal()

#Step 8 - Logic to either reset the round or take the player out of the round
#Will be called through the round and at the end of every round
class GameReset:
    ''' Class to either reset the round or take the player out of the round '''
    def reset_player(self,player_to_reset):
        '''Remove a player from the round'''
        self.player_to_reset = player_to_reset
        PLAYER_LIST[player_to_reset].attributes['bet_size'] = 0
        PLAYER_LIST[player_to_reset].attributes['natural'] = False
        PLAYER_LIST[player_to_reset].attributes['hand'] = []
        PLAYER_LIST[player_to_reset].attributes['hand_value'] = []
        PLAYER_LIST[player_to_reset].attributes['in_round'] = False

    def reset_game(self):
        '''Reset the round'''
        for player in range(0,(NO_PLAYERS+1)):
            self.reset_player(player)

#Step 9 - Checking for a Natural on the first go
def check_natural():
    '''Checking for a Natural on the first go'''
    for player in range(0,(NO_PLAYERS+1)):
        if 10 in PLAYER_LIST[player].attributes['hand_value']:
            if "Ace" in PLAYER_LIST[player].attributes['hand_value']:
                PLAYER_LIST[player].attributes['natural'] = True
            else:
                continue
        else:
            continue

    #Actions to take upon a Natural occurring
    for player in range(1,(NO_PLAYERS+1)):
        #Checking if any player has 'natural' = True
        if PLAYER_LIST[player].attributes['natural'] == True:
            #Checking if the dealer also 'natural' = True
            #Natural players will retain their pool size, all other players lose their bet
            if PLAYER_LIST[0].attributes['natural'] == True:
                PLAYER_LIST[player].attributes['pool'] += PLAYER_LIST[player].attributes['bet_size']
                for notnaturals in range(0,(NO_PLAYERS+1)):
                    PLAYER_LIST[notnaturals].attributes['pool'] -= PLAYER_LIST[notnaturals].attributes['bet_size']
                print(f"Both the dealer and {PLAYER_LIST[player].attributes['name']} had a natural 21. {PLAYER_LIST[player].attributes['name']} loses nothing, all other players lose their bets.")
                GameReset().reset_game()
            else:
                print(f"Congratulations {PLAYER_LIST[player].attributes['name']} you had a natural 21. You receive your bet x 1.5.\n")
                PLAYER_LIST[player].attributes['pool'] += (1.5 * PLAYER_LIST[player].attributes['bet_size'])
                PLAYER_LIST[player].attributes['pool'] = int(PLAYER_LIST[player].attributes['pool'])
            GameReset().reset_player(player)
            break
            #If only a player has a natural

        elif PLAYER_LIST[0].attributes['natural'] == True:
            print("Unlucky! The dealer had a natural 21, all players lose their bets.")
            for notnaturals in range(1,(NO_PLAYERS+1)):
                PLAYER_LIST[notnaturals].attributes['pool'] -= PLAYER_LIST[notnaturals].attributes['bet_size']
            GameReset().reset_game()

# NOTE: check_natural()

#Step 10 - Create logic to define stand/hit/bust process for dealer and players in round
def round_of_play():
    '''Stand/hit/bust process for dealer and players in round'''
    for player in range(1,(NO_PLAYERS+1)):
        while PLAYER_LIST[player].attributes['in_round'] is True:
            #Checking if Ace is in the playerhand
            INDEX_POS  = -1
            for value in PLAYER_LIST[player].attributes['hand']:
                INDEX_POS += 1
                if value == "Ace":
                    if sum(i for i in (PLAYER_LIST[player].attributes['hand_value']) if not isinstance(i, str)) + 11 > 21:
                        PLAYER_LIST[player].attributes['hand_value'][INDEX_POS] = 1
                    else:
                        PLAYER_LIST[player].attributes['hand_value'][INDEX_POS] = 11

            #Checking for bust
            if sum(PLAYER_LIST[player].attributes["hand_value"]) > 21:
                PLAYER_LIST[player].attributes['pool'] -= PLAYER_LIST[player].attributes['bet_size']
                print(f"Bust! {PLAYER_LIST[player].attributes['hand']} is worth {sum(PLAYER_LIST[player].attributes['hand_value'])} - You lose your bet, your pool is now {PLAYER_LIST[player].attributes['pool']}.\n")
                #Fixed - does not seem to be reducing pool size correctly
                GameReset().reset_player(player)
                break
            #print(f"{PLAYER_LIST[player].attributes['hand']}")
            #print(f"{PLAYER_LIST[player].attributes['hand_value']}")
            STAND_OR_HIT = input(f"{PLAYER_LIST[player].attributes['name']} your current hand is {PLAYER_LIST[player].attributes['hand']} and worth {sum(PLAYER_LIST[player].attributes['hand_value'])}. Do you want to stand or hit? You can use s or h for shorthand. ").lower()
            try:
                if STAND_OR_HIT[0] == "s":
                    print("\n")
                    break
                elif STAND_OR_HIT[0] == "h":
                    Deal().dealing(SHUFFLED_DECK,player)
                    #ValueConverstion().check_value(player)
                    continue
                else:
                    invalid_answer()
                    continue
            except:
                invalid_answer()
                continue

    #Logic to check the value of the dealers hand and take actions based upon StandHitOrBust
    while PLAYER_LIST[0].attributes['in_round'] is True:
        INDEX_POS  = -1
        for value in PLAYER_LIST[0].attributes['hand']:
            INDEX_POS += 1
            if value == "Ace":
                if sum(i for i in (PLAYER_LIST[0].attributes['hand_value']) if not isinstance(i, str)) + 11 > 21:
                    PLAYER_LIST[0].attributes['hand_value'][INDEX_POS] = 1
                else:
                    PLAYER_LIST[0].attributes['hand_value'][INDEX_POS] = 11
        #Checking for dealer bust
        if sum(PLAYER_LIST[0].attributes["hand_value"]) > 21:
            print(f"Dealer is bust! Dealer's hand: {PLAYER_LIST[0].attributes['hand']} - everyone wins their bets!\n")
            for player in range(1,(NO_PLAYERS+1)):
                if PLAYER_LIST[player].attributes['in_round'] is True:
                    PLAYER_LIST[player].attributes['pool'] += PLAYER_LIST[player].attributes['bet_size']
                else:
                    continue
            GameReset().reset_game()
            break
        #Checking for dealer hit
        elif sum(PLAYER_LIST[0].attributes["hand_value"]) <= 16:
            Deal().dealing(SHUFFLED_DECK,0)
            continue
        else:
            print(f"Dealer's hand: {PLAYER_LIST[0].attributes['hand']} worth {sum(PLAYER_LIST[0].attributes['hand_value'])}.\n")
            for player in range(1,(NO_PLAYERS+1)):
                #Checking if the player has more than the dealer
                #Ignoring players who have left the round
                if PLAYER_LIST[player].attributes['in_round'] is True:
                    if sum(PLAYER_LIST[player].attributes["hand_value"]) > sum(PLAYER_LIST[0].attributes["hand_value"]):
                        PLAYER_LIST[player].attributes['pool'] += PLAYER_LIST[player].attributes['bet_size']
                        print(f"Congratulations {PLAYER_LIST[player].attributes['name']} you have more than the dealer, your pool is now {PLAYER_LIST[player].attributes['pool']}.")
                        GameReset().reset_player(player)
                        #Checking if the player has less than the dealer
                    elif sum(PLAYER_LIST[player].attributes["hand_value"]) < sum(PLAYER_LIST[0].attributes["hand_value"]):
                        PLAYER_LIST[player].attributes['pool'] -= PLAYER_LIST[player].attributes['bet_size']
                        print(f"Unlucky {PLAYER_LIST[player].attributes['name']} you have less than the dealer, your pool is now {PLAYER_LIST[player].attributes['pool']}.")
                        GameReset().reset_player(player)
                    else:
                        print(f"{PLAYER_LIST[player].attributes['name']} you have the same as the dealer, your pool is  {PLAYER_LIST[player].attributes['pool']} and unchanged.")
                        GameReset().reset_player(player)
        break

    GameReset().reset_game()

# NOTE: round_of_play()

#Step 11 - Allowing a player to leave the table
def leave_table(NO_PLAYERS,PLAYER_LIST):
    '''Allowing players to leave the table'''
    LEAVER_LIST = (input("\nDoes anyone wish to leave the table? Please enter your name(s) (in the format 'Player1Name Player2Name Player3Name' etc) if so. ")).split()
    for player in range(1,(NO_PLAYERS+1)):
        try:
            for leaver in LEAVER_LIST:
                if leaver in PLAYER_LIST[player].attributes['name']:
                    PLAYER_LIST[player].reset()
                    del(PLAYER_LIST[player])
                    NO_PLAYERS -= 1
        except IndexError:
            break
    return NO_PLAYERS,PLAYER_LIST

#Step 12 - Preparing players for a new round
def continue_playing(NO_PLAYERS,PLAYER_LIST,SKIP_JOIN):
    '''Setting remaining players as in round'''
    INDEX_POS = 1
    for player in range(1,(NO_PLAYERS+1)):
        try:
            PLAYER_LIST[INDEX_POS].attributes['in_round'] = True
            if PLAYER_LIST[INDEX_POS].attributes['pool'] <= 0:
                print(f"{PLAYER_LIST[INDEX_POS].attributes['name']} your pool is 0 so you're out of the game!")
                PLAYER_LIST[INDEX_POS].reset()
                del(PLAYER_LIST[INDEX_POS])
                INDEX_POS -= 1
                NO_PLAYERS -= 1
            INDEX_POS += 1
        except IndexError:
            break
    if PLAYER_LIST == [DEALER]:
        PLAYER_LIST = ORIGINAL_PLAYER_LIST
        for player in range(0,(len(ORIGINAL_PLAYER_LIST))):
            PLAYER_LIST[player].reset()
        SKIP_JOIN = True
        NO_PLAYERS,PLAYER_LIST = defining_players(NO_PLAYERS,PLAYER_LIST)
    PLAYER_LIST[0].attributes['in_round'] = True
    return NO_PLAYERS,PLAYER_LIST,SKIP_JOIN

#Step 13 - asking if any new players want to join the round
def join_table(NO_PLAYERS,PLAYER_LIST):
    '''Allowing players to join the table'''
    JOINER_LIST = (input("\nDoes anyone wish to join the table? Please enter your name(s) (in the format 'Player1Name Player2Name Player3Name' etc) if so. ")).split()
    INDEX_POS = 0
    for name in JOINER_LIST:
        if name.lower() == "no":
            return NO_PLAYERS,PLAYER_LIST
    if JOINER_LIST != []:
        for player in range(1,(len(JOINER_LIST)+len(PLAYER_LIST))):
            try:
                if ORIGINAL_PLAYER_LIST[player] not in PLAYER_LIST:
                    PLAYER_LIST.insert(player,ORIGINAL_PLAYER_LIST[player])
                    PLAYER_LIST[player].attributes['name'] = JOINER_LIST[INDEX_POS]
                    INDEX_POS += 1
                    NO_PLAYERS += 1
            except IndexError:
                break

    return NO_PLAYERS,PLAYER_LIST


#Once per game
NO_PLAYERS,PLAYER_LIST = defining_players(NO_PLAYERS,PLAYER_LIST)
#Every round
while GAME_STATE is True:
    SHUFFLED_DECK = shuffle_deck(SHUFFLED_DECK)
    print_pool()
    taking_bets()
    Deal().first_deal()
    check_natural()
    round_of_play()
    NO_PLAYERS,PLAYER_LIST = leave_table(NO_PLAYERS,PLAYER_LIST)
    NO_PLAYERS,PLAYER_LIST,SKIP_JOIN = continue_playing(NO_PLAYERS,PLAYER_LIST,SKIP_JOIN)
    if SKIP_JOIN is False:
        NO_PLAYERS,PLAYER_LIST = join_table(NO_PLAYERS,PLAYER_LIST)
    SKIP_JOIN = False
    continue
