#Variable Players: Y
#Player Names Retreived: Y
#Initial Bets Taken: Y
#Initial Card Deal: Y
#Conversion of Cards Dealt to Numerical Value: Y
#Natural Check: WIP
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
player_pools = {}
players_bets = {}
player_hands = {'Dealer':[]}
player_values = {'Dealer':[]}

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

#Defining the number of players
players = int(input("How many players are there? "))
for player in range(0,players):
    name = input(f"Player {(player+1)} what is your name? ")
    player_pools[name] = 100
    players_bets[name] = ""
    player_hands[name] = []
    player_values[name] = []

#Taking initial bets

for name in player_pools:
    players_bets[name] = int(input(f"{name} how much would you like to bet? "))

#print(players_bets)

#Testing adding bets to hands

#for name in player_pools:
#   if name == name in players_bets:
#        player_pools[name] += players_bets[name]

#print(player_pools)


    class FirstDeal:
        """Dealing the first round of cards"""
        def __init__(self,shuffled_deck):
            self.shuffled_deck = shuffled_deck
        def first_dealing(self):
            #Dealing out each player 2 cards
            for i in range(0,2):
                for name in player_hands:
                    dealt_card = self.shuffled_deck.pop(0)
                    player_hands[name].append(dealt_card)

            hand_string = ""
            print("\nThe result after the first deal:\n")
            for name in player_hands:
                if name == 'Dealer':
                    hand_string += f"Dealer: ['{(player_hands['Dealer'][0])}','?']\n"

                else:
                    hand_string += f"{name}:{player_hands[name]} "

            print(hand_string)

FirstDeal(shuffled_deck).first_dealing()


class ValueConverstion:
    """Converting the value of the cards in the players hand to their numerical value"""
    def check_value(self):
        for name in player_hands:
            for value in player_hands[name]:
                try:
                    player_values[name].append(int(value))
                except:
                    if value == "Ace":
                        player_values[name].append("Ace")
                    else:
                        player_values[name].append(10)

ValueConverstion().check_value()

class NaturalCheck:

    def natural_check(self):
        for name in player_hands:
            if name == "Dealer":
                if ("Ace" and 10 in player_values[name]):
                    dealer_natural = True
            else:
                 if ("Ace" and 10 in player_values[name]):


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



class

print(player_values)
print(player_hands)
print(shuffled_deck)




#Defining the beginning of the round
