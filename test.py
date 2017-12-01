# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:22:12 2017

@author: blenderherad
"""
from itertools import cycle
import random
class Kingdom:
    
    def __init__(self):
        self.cards = 8*['Province']
        return None
    
    def pop(self):
        return self.cards.pop()
    
    def check_endgame(self):
        return len(self.cards) == 0
    
class Player:
    
    def __init__(self, kingdom):
        self.kingdom = kingdom
        self.discard_pile  = 7*['Copper'] + 3*['Estate']
        self.draw_pile = []
        self.hand     = []
        self.deck     = self.discard_pile + self.draw_pile
        self.reshuffle()
        self.draw(5)
        
        return None
        
    def draw(self, n):
        for i in range(n):
            if len(self.draw_pile) == 0:
                self.reshuffle()    
            self.hand.extend([self.draw_pile.pop()])
            
        return None
        
    def reshuffle(self):        
        self.draw_pile = self.discard_pile
        self.discard_pile = []
        random.shuffle(self.draw_pile)
        
        return None
    
    def buy(self):
        
        popped = self.kingdom.pop()
        self.hand.extend([popped])
        self.deck.extend([popped])
        return None
        
    def turn(self):        
        self.buy()
        self.cleanup()
        return None
        
    def discard(self, n):        
        print("Before discard: ", self.hand)

        if n == len(self.hand):
            discards = tuple(self.hand)
        else:
            discards = tuple(self.strategy.discard(self.hand, n)) # this should not happen yet            
        for c in discards: 
            self.hand.remove(c)
            print(c)
        self.discard_pile.extend(discards)
        return None      
    
    def cleanup(self):
        print(len(self.hand), " cards in hand")
        self.discard(len(self.hand))
        self.draw(5)
        return None
        
        
kingdom = Kingdom()
player1 = Player(kingdom)
player2 = Player(kingdom)

player_list = cycle(enumerate([player1, player2]))
game_over = False
while not game_over:
    idx, player = next(player_list)
    player.turn()
    game_over = kingdom.check_endgame()
    

print(player1.discard_pile)
print(player1.draw_pile)
print(player1.hand)
#print(player2.discard_pile)
#print(player2.deck)
#print(kingdom.cards)
        
        