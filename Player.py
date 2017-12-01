# -*- coding: utf-8 -*-

from Strategy import Strategy, BigMoney
from Stack    import Stack, Hand, Deck
from Card     import Card
"""
Created on Thu Nov 30 13:14:45 2017

Player class for Dominion

attributes:
    deck:           list of Cards in deck, unsorted and mutable
    draw_pile:      current draw pile, a stack with fixed order
    discard_pile:   another stack with fixed order
    strategy:       a Strategy class with take_turn and discard methods

methods:
    draw(n):    draws n cards
    discard(n): discards n cards
    shuffle():  shuffles deck
    reshuffle():    shuffles discard pile into deck
    

@author: blenderherad
"""
class Player:
    
    # constructor used to create a new player at the beginning of a Game
    def __init__(self, kingdom, strategy=None):
        
        # kingdom is passed to each Player
        # and gets modified during buy()
        self.kingdom = kingdom
        
        if strategy is None:
            self.strategy = BigMoney(self, kingdom.stacks.keys())
        else:
            self.strategy = strategy(self, kingdom.stacks.keys())
        
        initial_cards  = list(map(Card, 3*['Estate'] + 7*['Copper']))
        
        self.discard_pile = Stack()
        self.hand = Hand()

        self.deck = Deck(initial_cards)
        self.draw_pile = Stack(initial_cards)
        print (self.hand.size())
        print (self.discard_pile.size())
        self.draw_pile.shuffle()
        
        # need way to dynamically update hand, discard, draw and deck neatly
        
        self.draw(5)
        
        return None
    
    # private method to reshuffle     
    def reshuffle(self):
        
        self.draw_pile = self.discard_pile
        self.discard_pile = Stack()
        self.draw_pile.shuffle()
        
        return None
        
    # private method to draw n cards
    def draw(self, n):

        print(self.hand.size())
        for i in range(n):
            if self.draw_pile.size() == 0:
                self.reshuffle()    
            self.hand.extend([self.draw_pile.pop()])
        print(self.hand.size())
        #print(self.hand.names())
        return None
    
    # private method for discarding. used for cleanup and attacks
    def discard(self, n):
        
        if n == self.hand.size():
            discards = tuple(self.hand.cards)
#            print(discards)
#            print(self.hand.cards)
        else:
            discards = tuple(self.strategy.discard(self.hand, n)) # this should not happen yet
        
        print(len(discards))            
        for c in discards: 
            self.hand.remove(c)
        self.discard_pile.extend(discards)
        del discards
        return None
    
    def discard_to(self, n):
        self.discard(self.hand.size()-n)
        return None
    
    def trash(self, card):
        
        return None # not used yet
    
    # take turn by passing self to self's strategy, which calls play_action(), buy() and cleanup()
    def take_turn(self):
        
        self.actions = 1
        self.buys    = 1
        self.strategy.take_turn(self) # magic happens here        
        self.cleanup()
    
    def cleanup(self):
        
        self.discard(self.hand.size())
        self.draw(5)
        
        ## how to interface with Kingdom and Game instance?
    def buy(self, card):
        print("   buys " + card)
        popped = self.kingdom.pop(card)
        self.discard_pile.extend([popped])
        self.deck.extend([popped])
        return None
        
