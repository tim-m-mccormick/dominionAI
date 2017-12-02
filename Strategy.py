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
        player.coins += player.hand.coins # bonus coins from actions plus money
        self.buy_phase(player)
        
        return None
    
    def action_phase(self):
        pass
    
    def discard(self, n):
        discards = []
        while len(discards) < n:
            for card in player.hand.cards:
                if card.type == 'Victory'
                    discards += [card]
                    break
    
class BigMoney(Strategy):
    
    name = "Big Money"
    
    def action_phase(self, player):
        pass
    
    def buy_phase(self, player):

        if player.coins <= 2:
            player.buy('Copper')
        elif player.coins <= 5:
            player.buy('Silver')
        elif player.coins <= 7:
            player.buy('Gold')
        else:
            player.buy('Province')
            
class BigMoneyXSmithy(Strategy):
    
    name = "Big Money + Smithy"
    
    def action_phase(self, player):
        if 'Smithy' in player.hand.names():
            player.play_action('Smithy')
        return None
    
    def buy_phase(self, player):
        # if four or five player.coins in hand and fewer than 3 smithies, buy a smithy
        if player.coins in [4,5] and player.deck.count('Smithy') < 3:
            player.buy('Smithy')
        # otherwise do big money
        elif player.coins <= 2:
            player.buy('Copper')
        elif player.coins <= 5:
            player.buy('Silver')
        elif player.coins <= 7:
            player.buy('Gold')
        else:
            player.buy('Province')

class VillageSmithy(Strategy):
    
    name = "Village/Smithy Engine"
    
    def action_phase(self, player):        
        while player.actions > 0:
            if 'Village' in player.hand.names():
                player.play_action('Village')
            elif 'Smithy' in player.hand.names():
                player.play_action('Smithy')
            else:
                break
        return None
    
    def buy_phase(self, player):
        # First aims to get 5 village and 3 smithy "engine"
        if player.coins in [4,5] and player.deck.count('Smithy') < 3:
            player.buy('Smithy')
        elif player.coins == 3 and player.deck.count('Village') < 5:
            player.buy('Village')
        # then just buys money and provinces
        elif player.coins <= 2:
            player.buy('Copper')
        elif player.coins <= 5:
            player.buy('Silver')
        elif player.coins <= 7:
            player.buy('Gold')
        else:
            player.buy('Province')
            
class VillageMilitia(Strategy):
    
    name = "Village/Smithy Engine"
    
    def action_phase(self, player):        
        while player.actions > 0:
            if 'Village' in player.hand.names():
                player.play_action('Village')
            elif 'Militia' in player.hand.names():
                player.play_action('Militia')
            else:
                break
        return None
    
    def buy_phase(self, player):
        # First aims to get 5 village and 3 militia
        if player.coins in [4,5] and player.deck.count('Militia') < 3:
            player.buy('Militia')
        elif player.coins == 3 and player.deck.count('Village') < 5:
            player.buy('Village')
        # then just buys money and provinces
        elif player.coins <= 2:
            player.buy('Copper')
        elif player.coins <= 5:
            player.buy('Silver')
        elif player.coins <= 7:
            player.buy('Gold')
        else:
            player.buy('Province')