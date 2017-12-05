# -*- coding: utf-8 -*-

from random import shuffle
"""
Created on Thu Nov 30 19:57:48 2017

Stack class for Dominion

keeps track of hand stats (total buy points, number of action cards, etc)

can be used for discard pile, draw pile, hand, deck, and kingdom stacks

@author: blenderhead, tim-m-mccormick
"""

## fill this in when Card class is implemented
# subclasses Hand and Deck to avoid counting victory/coins for
# stacks in Kingdom unnecessarily. 
class Stack:
    
    def __init__(self, cards=[]):        

        self.cards = cards
        self.update()        
        return None
    
    def update(self):        
        pass
    
    def extend(self, newcards):        
        self.cards.extend(newcards)
        self.update()
        return self
    
    def append(self, newcard):
        self.cards.append(newcard)
        self.update()
        return self
    
    def pop(self):
        popped = self.cards.pop()
        self.update()
        return popped
    
    def pop_all(self):
        popped = []
        for card in self.cards:
            popped += [self.pop()]
        self.update()
        return popped
    
    def remove(self, card):
        self.cards.remove(card)
        self.update()
        return None
    
    def shuffle(self):        
        shuffle(self.cards)       
        return None
    
    def size(self):
        return len(self.cards)
    
    def names(self):
        return [str(card) for card in self.cards]
    
    def count(self, card_name):
        return self.names().count(card_name)

# Hand subclass keeps track of total coin value when updated     
class Hand(Stack):
    
    def update(self):
        self.coins = sum([card.value for card in self.cards])
        return self
        
    # function returns the first Card in the Hand with name == card_name 
    def first(self, card_name):
        for card in self.cards:
            if str(card) == card_name:
                return card
        print("No " + card_name + " card in hand!")
        
# Deck subclass keeps track of victory point total when updated
class Deck(Stack):
    
    def update(self):
        self.points = sum([card.points for card in self.cards])
        self.coins  = sum([card.value for card in self.cards])
        return self