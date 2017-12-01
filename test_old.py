# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:22:12 2017

@author: blenderherad
"""
from itertools import cycle
import random
class Kingdom:
    
    def __init__(self):
        self.cards = {}
        self.cards['Province'] = 8*['Province']
        self.cards['Copper']   = 46*['Copper']
        self.cards['Silver']   = 30*['Silver']
        self.cards['Gold']     = 20*['Gold']
        return None
    
    def pop(self, card):
        return self.cards[card].pop()
    
    def check_endgame(self):
        return len(self.cards['Province']) == 0
    
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
        coins = 1*self.hand.count('Copper') + 2*self.hand.count('Silver') + 3*self.hand.count('Gold')
        if coins <= 2:
            card = 'Copper'
        elif coins <= 5:
            card = 'Silver'
        elif coins <= 7:
            card = 'Gold'
        else:
            card = 'Province'
            
        print("   buys " + card)
            
        popped = self.kingdom.pop(card)
        self.hand.extend([popped])
        self.deck.extend([popped])
        return None
        
    def turn(self):        
        self.buy()
        self.cleanup()
        return None
        
    def discard(self, n):        
        if n == len(self.hand):
            discards = tuple(self.hand)
        else:
            discards = tuple(self.strategy.discard(self.hand, n)) # this should not happen yet            
        for c in discards: 
            self.hand.remove(c)
        self.discard_pile.extend(discards)
        return None      
    
    def cleanup(self):
        self.discard(len(self.hand))
        self.draw(5)
        return None
        
num_games = 100
winner_points = []
for i in range(num_games)
    
    kingdom = Kingdom()
    player1 = Player(kingdom)
    player2 = Player(kingdom)
    
    player_list = cycle(enumerate([player1, player2]))
    game_over = False
    Verbose = False
    player_turn = 2*[0]
    while not game_over:
        idx, player = next(player_list)
        print("Player " + str(idx) + " takes xer turn")
        player.turn()
        player_turn[idx] += 1
        game_over = kingdom.check_endgame()
        
    final_points = list(map(lambda x: 3 + 6*x.deck.count('Province'), [player1, player2]))
    #print("Final scores (Player, Points):")
    #print(list(enumerate(final_points)))
    #print(player_turn)
    
    winner_points.append(final_points[]) 


        
        