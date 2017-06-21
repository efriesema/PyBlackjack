#=========================================================================
# Author : Ed Friesema    Date: 6/4/2017
# Goal :to make a simple  text sungle player blackjack game'using OOP
#
#=========================================================================
import random


# Creates a Class for a deck of cards
# Methods - Shuffle, deal, new deck
#  Attributes = deck[]

class Deck(object):
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
    #an object to define the player
    # Attributes-- Name,hand, bankroll
    #Methods - checkHand,changeBank,giveCard
    
    def __init__(self, name, bankroll,hand ):
        self.name = name
        self.bankroll = bankroll
        self.hand = [] 
   
    def changeBank(self, amount):
        self.bankroll += amount
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
    

    
        
         

        
print("************** Let's play some BlackJack! ***********************")
dealerDeck = Deck()
name = input("What's the player's name?")
bank = int(input("How much do you plan to start with($100-$500)?"))
player1 = Player(name,bank,[])
dealer = Player("Dealer",0,[])
bust = False
while (True):
    dealer.muckHand()
    player1.muckHand()
    play = input("Do you want to play a hand(y/n)?")
    if (play == 'n' or play == 'N'):
        break    
    
    bet = int(input("How much do you wish to bet(cannot be more than your current bankroll)"))
    while (bet > player1.bankroll):
        print("You need to bet less than your current bankroll!")
        bet = int(input("How much do you wish to bet(cannot be more than your current bankroll)"))
    print("Let's deal the cards----")
    dealerDeck.newDeck()
    dealerDeck.shuffle()
    dealer.giveCard(dealerDeck.dealCard())
    player1.giveCard(dealerDeck.dealCard())
    dealer.giveCard(dealerDeck.dealCard())
    player1.giveCard(dealerDeck.dealCard())
    print("The dealer's hand is now [**],",dealer.hand[1] )
    print(player1.name, "\'s hand is now ", player1.hand)
    (dealerValue ,dealerHasBlackjack) = dealer.checkHand()
    (player1Value, player1HasBlackjack) = player1.checkHand()
    action = 'p';
    if dealerHasBlackjack and player1HasBlackjack:
        print("You both have blackjack!")
    elif dealerHasBlackjack:
        print("The dealer has blackjack. You lose!")
        player1.changeBank(-bet)
    elif player1HasBlackjack:
        print("You have blackjack! You win 1.5 times your bet")
        player1.changeBank(1.5*bet)
    else :
        while (action != 's') and (action != 'S'):
            action = input("What would you like to do? (h)it, (s)tand, or (d)ouble down?")
            if (action == 'h') or (action == 'H'):
                player1.giveCard(dealerDeck.dealCard())
                print(player1.name,"\'s hand =",player1.hand)
                (player1Value,hasBJ) = player1.checkHand()
                if player1Value >= 21 :
                    action = 's'
            elif (action == 'd') or (action == 'D'):
                player1.giveCard(dealerDeck.dealCard())
                print(player1.name,"\'s hand =",player1.hand)
                bet *= 2
                (player1Value,hasBJ) = player1.checkHand()
                action = 's'
        if player1Value > 21:
            print("You've busted!")
            player1.changeBank(-bet)
        else :
            print("Now it's time for the dealer to play!")
            
            while(dealerValue <17):
                dealer.giveCard(dealerDeck.dealCard())
                (dealerValue, hasBJ) = dealer.checkHand()
            if dealerValue > 21:
                print("Dealer's hand :",dealer.hand)
                print("The dealer busted")
                player1.changeBank(bet)
            elif dealerValue  == player1Value :
                print("Dealer's hand :",dealer.hand)
                print( "The hand is a push")
            elif dealerValue > player1Value :
                print("Dealer's hand :",dealer.hand)
                print("Dealer wins")
                player1.changeBank(-bet)
            else :
                print("Dealer's hand :",dealer.hand)
                print("You win!")
                player1.changeBank(bet)
        
    
    print("**************************")
    
print("Thanks for playing! Come back soon!")





    