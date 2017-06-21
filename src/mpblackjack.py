#======================================================================================
# Author : Ed Friesema    Date: 6/20/2017
# Goal : To expand the single player game to a multiplayer  text blackjack game'using OOP
# Input : Selcts user inputs to determine playersnames actions bankroll and bet size
# Output modify player variables
#=======================================================================================
import random


# Creates a Class for a deck of cards
# Methods - Shuffle, deal, new deck
#  Attributes = deck[]

class Deck(object):
    # Class describing a complete deck of cards
    # Attributes : cards-  a list of strings representing all of the current cards in the deck
    #              count- an integer count of the total number of cards in the deck
    # Methods :    shuffle() randomize the current cards in the deck,  reutrning the new list of cards and the count
    #              dealCard() removes one card from the deck and decrements the count, returns card value and new count
    #              printDeck() prints out the entire contents of the deck(used for early debugging)
    #              newDeck() resets the deck to a brand new orderded 52 card deck
    
    
    freshDeck = ['2h','3h','4h','5h','6h','7h','8h','9h','Th','Jh','Qh','Kh','Ah',
                 '2d','3d','4d','5d','6d','7d','8d','9d','Td','Jd','Qd','Kd','Ad',
                 '2c','3c','4c','5c','6c','7c','8c','9c','Tc','Jc','Qc','Kc','Ac',
                 '2s','3s','4s','5s','6s','7s','8s','9s','Ts','Js','Qs','Ks','As']
    #Initiate a full deck of cards  
    def __init__(self, cards= [], count= 52):
        self.cards = cards
        self.count = count
        
    #Method for shuffling cards
    def shuffle(self):
        self.cards= random.sample(self.cards,len(self.cards))
        return (self.cards, self.count)
    
    #Method to deal a card
    def dealCard(self):
        newCard =self.cards.pop()
        self.count -= 1
        return newCard
    
    #print deck
    def printDeck(self):
        print(self.cards,  'Count =',self.count)

    #Reset the deck
    def newDeck(self):
        self.cards= Deck.freshDeck
        self.count= 52
        
class Player(object):
    # an object to define the player
    # Attributes:  Name- Plaers's name
    #              hand - list representing players current hand 
    #              bankroll - Amount player currently has in his bank
    #              bet - size of the player'scurrent bet
    # Methods:     loseBet() - deducts current bet from bankroll
    #              winBet() -adds current bet to bankroll
    #              giveCard(string)- appends card represented by string to player hand
    #              checkHand() -  checks the value for a players hand and also returns a boolean teling if they were dealt blacjack
    #              changeBet(int) - changes the size of the players bet
    #              muckHand()-  resets the players hand to an empty list
    
    def __init__(self, name, bankroll,hand,bet ):
        self.name = name
        self.bankroll = bankroll
        self.hand = []
        self.bet = bet 
   
    def loseBet(self):
        self.bankroll -= self.bet
        print(self.name , "\'s bankroll is now ",self.bankroll)
        if (self.bankroll <=0 ):
            print(self.name,", you're busted!!")
        return self.bankroll
    
    def winBet(self):
        self.bankroll += self.bet
        print(self.name , "\'s bankroll is now ",self.bankroll)
        return self.bankroll
    
    def giveCard(self,card):
        self.hand.append(card)
        return self.hand
    
    def checkHand(self):
        value=0
        aces =0
        jacks = 0
        numCards = len(self.hand)
        blackjack = False
        for card in self.hand:
            if card[0] =='A':
                aces +=1
            elif (card[0] == 'K' ) or (card[0] == 'Q' ) or (card[0] =='T'):
                value +=10
            elif card[0] == 'J':
                jacks +=1
                value +=10
            else :
                value += int(card[0])
        if  aces == 2:
            if value >= 19:
                value +=2
            else :
                value += 12
        elif aces == 1:
            if value <= 10:
                value += 11
            else :
                value +=1
        if (numCards ==2) and(aces == 1) and (jacks == 1):
            blackjack =True
        return (value,blackjack)
    
    def muckHand(self):
        self.hand =[]
        return 0
    
    def changeBet(self, newBet):
        if (newBet > self.bankroll):
            print("You need to bet less than your current bankroll!")
            self.bet = int(input("How much do you wish to bet(cannot be more than your current bankroll)?"))
        else :
            self.bet = newBet
        return 0;

# PROGRAM BEGINS       
print("************** Let's play some BlackJack! ***********************")
dealerDeck = Deck()
table = []

## Creates table[]  a list of the dealer and all of the players in the game. Dealer will always be at table[0]
table.append( Player("Dealer",0,[],0))
playerCount = int(input("How many players at the table?"))
for i in range(playerCount):
    print("Player", i+1,end="")
    name = input(", what is your name?")
    bank = int(input("How much do you plan to start with($100-$500)?"))
    table.append(Player(name,bank,[],0))
for player in table:
    print(player.name,", bankroll : $",player.bankroll)
    
# Loop that continues until the player syays they do not want to play any more
while (True):
    for player in table:
        player.muckHand()
    play = input("Do you want to play a hand(y/n)?")
    if (play == 'n' or play == 'N'):
        break   
    for player in table[1:]:
        print(player.name, end="")     
        bet = int(input(", how much do you wish to bet(cannot be more than your current bankroll)"))
        player.changeBet(bet)   
         
    #  Deck is suffle and cards are dealt to full table of players starting with the dealer
    print("Let's deal the cards----")
    dealerDeck.newDeck()
    dealerDeck.shuffle()
    for player in table:
        player.giveCard(dealerDeck.dealCard())
    for player in table:
        player.giveCard(dealerDeck.dealCard())
    print("The dealer's hand is now [**],",table[0].hand[1] )
    (dealerValue ,dealerHasBlackjack) = table[0].checkHand()
    for player in table[1:]:
        print(player.name, "\'s hand is ", player.hand)
        
    # check if dealer and/or players has black jack. if not let each player play in turn and let the dealer play last 
    #  then adjust and cash the winning and losing bets from each player. if a player busts he loses his bet immediately
    if dealerHasBlackjack:
        for player in table[1:]:
            print(player.name, "\'s hand is ", player.hand)
            (playerValue, playerHasBlackjack)=player.checkHand()
            if playerHasBlackjack:
                print("You both have blackjack!")
            else :
                print("The dealer has blackjack. You lose!")
                player.loseBet()  
    else :
        bustCount =0
        for player in table[1:]:
            (playerValue, playerHasBlackjack)=player.checkHand()
            if playerHasBlackjack:
                print("You have blackjack! You win 1.5 times your bet")
                player.changeBet(1.5*player.bet)
                player.winBet()
            else:
                action = 'p';
                while (action != 's') and (action != 'S'):
                    print(player.name,", your hand is ",player.hand)
                    action = input("What would you like to do? (h)it, (s)tand, or (d)ouble down?")
                    if (action == 'h') or (action == 'H'):
                        player.giveCard(dealerDeck.dealCard())
                        print(player.name,"\'s hand =", player.hand)
                        (playerValue,hasBJ) = player.checkHand()
                        if playerValue >= 21 :
                            action = 's'
                    elif (action == 'd') or (action == 'D'):
                        player.giveCard(dealerDeck.dealCard())
                        print(player.name,"\'s hand =",player.hand)
                        player.changeBet (2*player.bet)
                        (playerValue,hasBJ) = player.checkHand()
                        action = 's'
                    if playerValue > 21:
                        bustCount +=1
                        print("You've busted!")
                        player.loseBet()
                        player.changeBet(0)
        if (bustCount == playerCount):
            print("Everyone busted out!")
        else:
            print("Now it's time for the dealer to play!")
            while(dealerValue <17):
                table[0].giveCard(dealerDeck.dealCard())
                (dealerValue, hasBJ) = table[0].checkHand()
                if dealerValue > 21:
                    print("Dealer's hand :",table[0].hand)
                    print("The dealer busted")
                    for player in table[1:]:
                        player.winBet()
            if (dealerValue <= 21):       
                for player in table[1:]:
                    (playerValue,hasBJ) = player.checkHand()
                    print("Dealer's hand :",table[0].hand)
                    if playerValue > 21:
                        continue                 
                    elif dealerValue  == playerValue :                       
                        print( player.name,", the hand is a push")
                    elif dealerValue > playerValue :
                        print("Dealer wins")
                        player.loseBet()
                    else :           
                        print(player.name," wins!")
                        player.winBet()
    print("**************************")
print("Thanks for playing! Come back soon!")





    