#prints "Go Fish!" at the start of the game
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
start_game = input('Welcome ' + player_1_name + ' and ' + player_2_name+ '! ' +player_1_name + ' will go first (click enter).')
deal_cards = input('The cards have been dealt!' + player_1_name + ', here are the cards in your deck. You currently have 0 matches. What rank are you requesting from' + player_2_name + '?')

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

# print(player_1_hand) check that player 1 was dealt 7 random cards
