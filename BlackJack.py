'''
Created on Jun 18, 2018

@author: pyjain
'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    
    def __str__(self):
        deck1=""
        for card in self.deck:
            deck1+="\n "+ card.__str__()
        return f"The deck contains:\n{deck1}"

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card=self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0   
        self.aces = 0   
    
    def add_card(self,card):
        self.cards.append(card)
        a=values[card.rank]
        self.value += a
        if a==11:
            self.aces+=1
    
    def adjust_for_ace(self):
         if self.aces!=0 and self.value>21:
                self.value=self.value-10
                self.aces-=1

class Chips:
    
    def __init__(self,total):
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total+=(self.bet*2)
    
    def lose_bet(self):
        self.total-=self.bet
        
def take_bet(chips):
    play=True
    while play:
        
        try:
            bet_value=int(input("Enter the value for the bet: "))
            if chips.total<bet_value:
                print("Wrong bet value")
            else:
                chips.bet=bet_value
                play=False
        
        except:
            print("Invalid input")


def hit(deck,hand):
    popped_card=deck.deal()
    hand.add_card(popped_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing 
    while True:
        
        hit_stand=input("Do you want to hit or stand? ").upper()
        if hit_stand=="HIT":
            hit(deck,hand)
            print("The player wants to hit")
            break
        elif hit_stand=="STAND":
            print("The player wants to stand")
            playing= False
            break
        else:
            print('Please enter the correct value')
            continue

def show_some(player,dealer):
    print("Player's cards:", *player.cards, sep="\n")
    print("Player's cards value: ", player.value)
    
    print("Dealer's cards:")
    print(dealer.cards[0])
   
def show_all(player,dealer):

    print("Player's cards:", *player.cards, sep="\n")
    print("Dealer's cards:", *dealer.cards, sep="\n")
    print("Player's cards value: ", player.value)
    print("Dealer's cards value: ", dealer.value)

def player_busts(player,chips):
    if player.value>21:
        print("Player busts")
        chips.lose_bet()
        return True
        

def player_wins(player,dealer,chips):
    if (player.value<21 and player.value>dealer.value) or player.value==21:
        print("Player wins")
        chips.win_bet()
        return True

def dealer_busts(dealer,chips):
    
    if dealer.value>21:
        print("Dealer busts")
        chips.win_bet() 
        return True
def dealer_wins(dealer,player,chips):
    if dealer.value>player.value or dealer.value==21:
        print("Dealer wins")
        chips.lose_bet()
        return True
def push(player,dealer):
    if player.value==dealer.value:
        print("Tie Game!!")
        return True
    

total=100
deck=Deck()
deck.shuffle()
while True:
    # Print an opening statement
    print("Welcome to Black Jack")

    # Create & shuffle the deck, deal two cards to each player
    player=Hand()
    dealer=Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())    
    # Set up the Player's chips
    chips=Chips(total)
    
    # Prompt the Player for their bet
    take_bet(chips)
    # Show cards (but keep one dealer card hidden)

    show_some(player,dealer)
    playing=True
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        status=player_busts(player,chips)
        if status:
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if not status:
        
        while dealer.value<17:
            hit(deck,dealer)
        # Show all cards
        show_all(player,dealer)
        # Run different winning scenarios
        if player_wins(player,dealer,chips):
            print("")
            
        elif dealer_busts(dealer,chips):
            print("")
        elif dealer_wins(dealer,player,chips):
            print("")
            
        elif push(player,dealer):
            print("")
            
            
    # Inform Player of their chips total 
    total=chips.total
    print("Player's chips total: ", chips.total)
    
    # Ask to play again
    play_again=input("Do you want to play again: yes/no? ").lower()
    if play_again=="yes":
        continue
    else:
        break   

