#prints "Go Fish!" at the start of the game
print("""
GGGGG OOOOO   FFFFF I SSSSS H   H !
G     O   O   F     I S     H   H !
G  GG O   O   FFF   I SSSSS HHHHH !
G   G O   O   F     I     S H   H
GGGGG OOOOO   F     I SSSSS H   H !""")

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
print(deck)