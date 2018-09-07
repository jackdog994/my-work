#Blackjack
GAME_STATE = True

#Defining the deck
deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","Ace"]*4
decksize = 13*4
shuffled_deck = list(range(0,decksize))
player_names = {}
player_bets = {}
player_hand = {}
dealt_card = []

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
    player_names[name] = 100
    player_bets[name] = ""
    player_hand[name] = []

#Taking initial bets

for name in player_names:
    player_bets[name] = int(input(f"{name} how much would you like to bet? "))

#print(player_bets)

#Testing adding bets to hands

#for name in player_names:
#   if name == name in player_bets:
#        player_names[name] += player_bets[name]

#print(player_names)

#Dealing a card

class Deal:

    def __init__(self,shuffled_deck,dealt_card):
        self.shuffled_deck = shuffled_deck
        self.dealt_card = dealt_card
    def dealing(self):
        dealt_card = []
        dealt_card += shuffled_deck.pop(0)
        print(dealt_card)

#Dealing the first round of cards

for name in player_hand:
    Deal(shuffled_deck,dealt_card).dealing()
    player_hand[name] += dealt_card


print(player_hand)
print(shuffled_deck)




#Defining the beginning of the round
