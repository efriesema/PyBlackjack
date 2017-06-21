
# Author : Ed Friesema    Date: 6/20/2017
# Goal : To expand the single player game to a multiplayer  text blackjack game'using OOP
# Input : Selects user inputs to determine players' names, actions, bankroll, and bet size
# Output : modify player variables


    class Deck(object):
    # Class describing a complete deck of cards
    # Attributes : cards-  a list of strings representing all of the current cards in the deck
    #              count- an integer count of the total number of cards in the deck
    # Methods :    shuffle() randomize the current cards in the deck,  reutrning the   new list of cards and the count
    #              dealCard() removes one card from the deck and decrements the count, returns card value and new count
    #              printDeck() prints out the entire contents of the deck(used for early debugging)
    #              newDeck() resets the deck to a brand new orderded 52 card deck
    
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