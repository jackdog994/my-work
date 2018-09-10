#Variable Players: Y
#Player Names Retreived: Y
#Initial Bets Taken: Y
#Initial Card Deal: Y
#Conversion of Cards Dealt to Numerical Value: Y
#Natural Check: Y
#Stand/Hit/Bust: WIP
#Calculating Bet Result: N
#Confirming Whether Player Out of Game: N
#Option to Leave Table: N
#New Round: N
#New Game: N

#Blackjack
GAME_STATE = True

#Defining the deck
deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","Ace"]*4
decksize = 13*4
shuffled_deck = list(range(0,decksize))

#Shuffling the deck
for card in deck:
    while GAME_STATE == True:
        import random
        deck_pos = random.randint(0,decksize)
        if deck_pos in shuffled_deck:
            shuffled_deck[deck_pos] = card
            break
        else:
            continue

print(shuffled_deck)

#Class for defining playername

class Player:

    def __init__(self):
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

#Logic to either reset the round or take the player out of the round
class GameReset:
    ''' Class to either reset the round or take the player out of the round '''
    def reset_player(self,player_reset):
        '''Remove a player from the round'''
        self.player_reset = player_reset
        player_list[player_reset].attributes['bet_size'] = 0
        player_list[player_reset].attributes['natural'] = False
        player_list[player_reset].attributes['hand'] = []
        player_list[player_reset].attributes['hand_value'] = []
        player_list[player_reset].attributes['in_round'] = False

    def reset_game(self):
        '''Reset the round'''
        for player in range(0,(no_players+1)):
            self.reset_player(player)

#Dealing the first round of cards
class FirstDeal:
    """Dealing the first round of cards"""
    def __init__(self,shuffled_deck):
        self.shuffled_deck = shuffled_deck
    def first_dealing(self):
        for i in range(0,2):
            for player in range(0,(no_players+1)):
                dealt_card = self.shuffled_deck.pop(0)
                player_list[player].update_hand(dealt_card)

        hand_string = ""
        print("\nThe result after the first deal:\n")
        for player in range(0,(no_players+1)):
            if player_list[player].attributes['name'] == 'Dealer':
                hand_string += f"Dealer: [{player_list[0].attributes['hand'][0]},'?']\n"

            else:
                hand_string += f"{player_list[player].attributes['name']}:{player_list[player].attributes['hand']} "

        print(hand_string)

#Creating a list of the numerical value of the cards
class ValueConverstion:
    """Converting the value of the cards in the players hand to their numerical value"""
    def check_value(self):
        for player in range(0,(no_players+1)):
            for value in player_list[player].attributes['hand']:
                try:
                    player_list[player].attributes['hand_value'].append(int(value))
                except:
                    if value == "Ace":
                        player_list[player].attributes['hand_value'].append("Ace")
                    else:
                        player_list[player].attributes['hand_value'].append(10)

#Checking for a Natural on the first go
class NaturalCheck:
    '''Checking for a Natural on the first go'''
    def check_natural(self):
        #Checking if any player has a natural
        for player in range(0,(no_players+1)):
            if 10 in player_list[player].attributes['hand_value']:
                if "Ace" in player_list[player].attributes['hand_value']:
                    player_list[player].attributes['natural'] = True
                else:
                    continue
            else:
                continue

        #Actions to take upon a Natural occurring
        for player in range(1,(no_players+1)):
            print("1aa")
            #Checking if any player has 'natural' = True
            if player_list[player].attributes['natural'] == True:
                print("2aa")
                #Checking if the dealer also 'natural' = True
                #Natural players will retain their pool size, all other players lose their bet
                if player_list[0].attributes['natural'] == True:
                    print("2ba")
                    player_list[player].attributes['pool'] += player_list[player].attributes['bet_size']
                    for notnaturals in range(0,(no_players+1)):
                        print("2bb")
                        player_list[notnaturals].attributes['pool'] -= player_list[notnaturals].attributes['bet_size']
                    print(f"Both the dealer and {player_list[player].attributes['name']} had a natural 21. {player_list[player].attributes['name']} loses nothing, all other players lose their bets.")
                    GameReset().reset_game()
                else:
                    print("2bc")
                    print(f"Congratulations {player_list[player].attributes['name']} you had a natural 21. You receive your bet x 1.5.")
                    player_list[player].attributes['pool'] += (1.5 * player_list[player].attributes['bet_size'])
                GameReset().reset_player(player)
                break
                print("2ab")
                #If only a player has a natural


            elif player_list[0].attributes['natural'] == True:
                print("3aa")
                print("Unlucky! The dealer had a natural 21, all players lose their bets.")
                for notnaturals in range(1,(no_players+1)):
                    print("3ab")
                    player_list[notnaturals].attributes['pool'] -= player_list[notnaturals].attributes['bet_size']
                GameReset().reset_game()

#Setting up player variables

dealer = Player()
player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()
player5 = Player()
player6 = Player()

dealer.update_name("Dealer")

player_list = [dealer, player1, player2, player3, player4, player5, player6]

index_pos = -1

player_no = 1

#Determining how many players

no_players = int(input("How many players are there? "))
for player in range(no_players,7):
    try:
        del(player_list[player-index_pos])
        index_pos += 1
    except IndexError:
        break

#Asking for player.name
for player in range(1,(no_players+1)):
    input_name = input(f"Player {player_no} what is your name? ")
    player_list[player].update_name(input_name)
    player_no += 1

#Taking initial bets
for player in range(1,(no_players+1)):
    bet_size = int(input(f"{player_list[player].attributes['name']} how much would you like to bet? "))
    player_list[player].update_bet(bet_size)
    player_no += 1

#Dealing the first round of cards
FirstDeal(shuffled_deck).first_dealing()

#Converting the cards to their numerical value
ValueConverstion().check_value()

#Checking for a Natural 21 after the first deal
NaturalCheck().check_natural()





#class StandHitOrBust:
    """Calculating the available moves to each player""
    for name in player_values:
        if sum(player_values[name]) > 21:
            print("Bust! You lose your bet")
              player_pools[name] -= players_bets[name]
        elif sum(player_values[name]) < 21:
            stand_or_hit = input(f"Your current hand is worth {sum(player_values[name])}. Do you want to stand or hit?").lower()
            if stand_or_hit == "stand":
                continue
            elif stand_or_hit == "hit"
                Deal()"""
