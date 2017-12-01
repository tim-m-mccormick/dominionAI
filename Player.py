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
        
        self.deck = Deck(initial_cards)
        self.deck.shuffle()
        
        # need way to dynamically update hand, discard, draw and deck neatly
        
        self.draw_pile = self.deck
        self.draw(5)
        
        return None
    
    # private method to reshuffle     
    def reshuffle(self):
        
        self.draw_pile = self.discard_pile
        self.discard_pile = []
        self.draw_pile.shuffle()
        
        return None
        
    # private method to draw n cards
    def draw(self, n):

        for i in range(n):
            if len(self.draw_pile) == 0:
                self.reshulffle()    
            self.hand.extend([self.draw_pile.pop()])
            
        return None
    
    # private method for discarding. used for cleanup and attacks
    def discard(self, n):
        
        if n == len(self.hand):
            discards = tuple(self.hand)
        else:
            discards = tuple(self.strategy.discard(self.hand, n)) # this should not happen yet
            
        for c in discards: self.hand.remove(c)
        self.discard_pile.extend(discards)
        
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
        
        self.discard(len(self.hand))
        self.draw(5)
        
        ## how to interface with Kingdom and Game instance?
    def buy(self, card):
        self.discard_pile
        
        
