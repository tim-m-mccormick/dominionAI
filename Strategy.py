# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:43:45 2017

Strategy base class for Dominion
including BigMoney subclass

@author: blenderherad
"""

class Strategy:
    
    name = None
    
    def __init__(self, player, kingdom_cards):
        
        self.name = None
        return None
    
    def take_turn(self, player):
        
        self.action_phase(player)
        self.buy_phase(player)
        
        return None
    
    def action_phase(self):
        pass
    
class BigMoney(Strategy):
    
    name = "Big Money"
    
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
            
class BigMoneySmithy(Strategy):
    
    name = "Big Money + Smithy"
    
    def action_phase(self, player):
        if 'Smithy' in player.hand.names():
            player.play_action('Smithy')
        return None
    
    def buy_phase(self, player):
        # if four or five coins in hand and fewer than 3 smithies, buy a smithy
        if player.hand.coins in [4,5] and player.deck.count('Smithy') < 3:
            player.buy('Smithy')
        # otherwise do big money
        elif player.hand.coins <= 2:
            player.buy('Copper')
        elif player.hand.coins <= 5:
            player.buy('Silver')
        elif player.hand.coins <= 7:
            player.buy('Gold')
        else:
            player.buy('Province')