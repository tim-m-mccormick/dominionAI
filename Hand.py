# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:57:48 2017

Hand class for Dominion

keeps track of hand stats (total buy points, number of action cards, etc)

@author: blenderherad
"""

## fill this in when Card class is implemented
class Hand:
    
    def __init__(self, cards):
        
        self.cards = cards
        self.coins = sum([card.value for card in cards])
        self.action_cards
        
        return None
    
    def extend(self, newcards):
        
        self.cards.extend(newcards)
        self.coins += sum([card.value for card in newcards])
        
        return self
        