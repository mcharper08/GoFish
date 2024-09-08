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
player_2_name = input('Thanks! Player 2, what is your name?')
input('Welcome ' + player_1_name + ' and your opponent! ' +player_1_name + ' will go first (click Enter).')
player_1_matches = 0
player_2_matches = 0    

class Deck:
    def __init__(self):
        suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
        kinds = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [[identity + 1, suits[identity // 13], kinds[identity % 13]] for identity in range(52)]
        random.shuffle(self.cards)
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]

    def draw_card(self):
        return self.cards.pop(0) if self.cards else None

deck = Deck()
deck.shuffle()

player_1_hand = deck.deal(7) # player 1 gets dealt the first 7 cards
player_2_hand = deck.deal(7) # player 2 gets dealt cards 8-14
stock_pile = deck.cards # stock pile is the remaining cards left

# clears the screen of displaying cards
#def clear_console():
    #os.system('cls' if os.name == 'nt' else 'clear')

#displays player 1's cards
def display_hands(player_name, hand):
    #clear_console()
    input(f"{player_name}, click Enter to see your hand")
    print(f"{player_name}'s hand is: {hand}")
    input(f"{player_name} press Enter when done viewing")
    #clear_console()

#checks for matches and updates hand to display what has no match yet
def matches_check(hand):
    matches = [] #creates open list for matches
    kinds_in_hand = [card[2] for card in hand] #checks the third set of data in the hand of cards and makes a list of each kind
    for kind in kinds:
        if kinds_in_hand.count(kind)==4: #checks if 4 of a kind are in hand to lay down matches
            matches.append(kind) #adds the matches to the open list matches
    for match in matches:
        hand[:] = [card for card in hand if card[2] != match] # updates hand with cards that are not matches
    return matches

def go_fish(player_name, hand):
    if stock_pile:
        new_card=stock_pile.pop(0) #grabs the first card from the stock pile if opponent says go fish
        hand.append(new_card)
        print(f"{player_name} went fish and drew a {new_card[2]} of {new_card[1]}")

def turn(player_name, player_hand, opponent_hand):
    display_hands(player_name, player_hand) #show the current player their hand
    do_you_have = input(f"{player_name}, what kind are you asking from your opponent?") #ask the player what card they would like from their opponent
    while do_you_have not in kinds:
        print('Invalid input, try again!')
        do_you_have = input(f"{player_name}, what kind are you asking from your opponent?") 
    opponent_kinds = [card[2] for card in opponent_hand] #searches opponent's hand for kinds
    match_boolean = False

    for card in opponent_hand:
        if card[2] == do_you_have: #if requested kind is a match in the opponent's hand...
            player_hand.append(card) #the player gets the card
            opponent_hand.remove(card) #the opponent loses the card
            match_boolean = True
            print(f"{do_you_have} was found!")
    if match_boolean == False:
        print("Go Fish!") #if the requested kind is not in the opponent's hand
        go_fish(player_name, player_hand) #the player must pick from the stock pile 

#create matches to keep track of the game
player_1_matches = []
player_2_matches = []

#establish the game of go fish using a while loop
while len(stock_pile) > 0 and (len(player_1_hand) > 0 and len(player_2_hand) > 0): #establish the game
    turn(player_1_name, player_1_hand, player_2_hand)
    player_1_matches += matches_check(player_1_hand)

    if len(player_1_hand) == 0:
        print(f'{player_1_name} + is out of cards!')
        break #if this occurs, the game is over
    
    turn(player_2_name, player_2_hand, player_1_hand)
    player_2_matches += matches_check(player_2_hand)
              
    if len(player_2_hand) == 0:
        print(f"{player_2_name} is out of cards!")
        break #if this occurs, the game is over

#Determine winner of the game
if len(player_1_matches) > len (player_2_matches):
    print(f"{player_1_name} is the winner!")
elif len(player_2_matches) < len(player_1_matches):
    print(f"{player_2_name} is the winner!")
else:
    print("It's a tie!")
