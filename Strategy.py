# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:43:45 2017

Strategy base class for Dominion
including BigMoney subclass

@author: blenderhead, tim-m-mccormick
"""

class Strategy:
    
    name = None
    """
    Virtual parent class for strategies
    """
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
    
    def discard(self, player, n):
        discards = []
        while len(discards) < n:
            for card in player.hand.cards:
                if card.type == 'Victory' and card not in discards:
                    discards += [card]
                    break
                elif card.name == 'Copper' and card not in discards:
                    discards += [card]
                    break
                elif card.name == 'Silver' and card not in discards:
                    discards += [card]
                    break
                elif card.type == 'Action' and card.terminal_action and card not in discards:
                    discards += [card]
                    break
                elif card.type == 'Action' and not card.terminal_action and card not in discards:
                    discards += [card]
                    break
                elif card.name == 'Gold' and card not in discards:
                    discards += [card]
                    break

        return discards
    
class BigMoney(Strategy):
    """
    Simplest possible big money strategy
    Buys the most valuable money card it can afford
    Buys provinces as soon as it can afford them
    """
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
            
class BigMoneySmithy(Strategy):
    """
    Simplest big money + smithy card
    Buys smithy as soon as it has $4, then as BigMoney:
        Buys the most valuable money card it can afford
        Buys provinces as soon as it can afford them
    """
    def action_phase(self, player):
        if player.hand.count('Smithy') == 1:
            player.play_action('Smithy')
            
    def buy_phase(self, player):
        
        if player.deck.count('Smithy') == 0:
            if player.hand.coins <= 2:
                player.buy('Copper')
            elif player.hand.coins <= 3:
                player.buy('Silver')
            else:
                player.buy('Smithy')
        else: 
            if player.hand.coins <= 2:
                player.buy('Copper')
            elif player.hand.coins <= 5:
                player.buy('Silver')
            elif player.hand.coins <= 7:
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
