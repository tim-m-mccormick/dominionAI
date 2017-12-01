# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:43:45 2017

Strategy base class for Dominion
including BigMoney subclass

@author: blenderherad
"""

class Strategy:
    
    def __init__(self, player, kingdom_cards):
        
        return None
    
    def take_turn(self, player):
        
        self.action_phase(player)
        self.buy_phase(player)
        
        return None
    
    def action_phase(self):
        pass
    
class BigMoney(Strategy):
    
    def action_phase(self, player):
        pass
    
    def buy_phase(self, player):
        
        if player.hand.coins <= 2:
            player.buy('Copper')
        elif player.hand.coins <= 5:
            player.buy('Silver')
        elif player.hand.coins <= 7:
            player.buy('Gold')
        else:
            player.buy('Province')
            
#class BigMoneySmithy(Strategy):
    
#    def action_phase(self, player):
#        if player.hand.