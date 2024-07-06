import random
import os

# prints "Go Fish!" at the start of the game
print("""
GGGGG OOOOO   FFFFF I SSSSS H   H !
G     O   O   F     I S     H   H !
G  GG O   O   FFF   I SSSSS HHHHH !
G   G O   O   F     I     S H   H
GGGGG OOOOO   F     I SSSSS H   H !
      """)

#prints out prompts to obtain player names as part of welcome messages
player_1_name = input('Welcome to the game of Go Fish! What is the name of player 1?')
player_2_name = input('Let us grab an online opponent. Create a fun name for player 2?')
input('Welcome ' + player_1_name + ' and ' + player_2_name+ '! ' +player_1_name + ' will go first (click Enter).')
player_1_matches = 0
input('The cards have been dealt!' + player_1_name + ', here are the cards in your deck. You currently have player_1_matches matches.') 

#card variables
suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
kinds = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

#create nested list named deck that has an identity 1-52 for each card suit and kind
deck = [] #open list for editing
for index in range(52): #for each index for a total of 52...
    identity = index+1 # each cards identity is based on a number from 1-52
    suit = suits[index // 13] # every 13 cards will be a different suit, 4 suits total
    kind = kinds[index % 13] # cycles through every 13 cards from ace to King
    card = [identity, suit, kind] # each card has an ID, suit, and kind associated with it
    deck.append(card) # the deck of cards is appended with the 52 cards created
# print(deck) run this line to make sure all 52 cards are correct

# deal 7 cards to player 1
import random # use random to randomize deck
random.shuffle(deck)

player_1_hand = deck[:7] # player 1 gets dealt the first 7 cards
player_2_hand = deck[7:14] # player 2 gets dealt cards 8-14
stock_pile = deck[14:] # stock pile is the remaining cards left

# clears the screen of displaying cards
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#displays player 1's cards
def display_hands(player_name, hand):
    clear_console()
    input(f"{player_name}, click Enter to see your hand")
    print(f'{player_name}'s hand is: {hand})
    input(f"{player_name} press Enter when done viewing")
    clear_console()

#checks for matches and updates hand to display what has no match yet
def matches_check(hand):
    matches = [] #creates open list for matches
    kinds_in_hand = [card[2] for card in hand] #checks the third set of data in the hand of cards and makes a list of each kind
    for kind in kinds:
        if kinds_in_hand.count(kind)==4 #checks if 4 of a kind are in hand to lay down matches
        matches.append(kind) #adds the matches to the open list matches
    for match in matches:
        hand[:] = [card for card in hand if card[2] != match] # updates hand with cards that are not matches
    return matches

#establish the game of go fish using a loop


