# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:43:45 2017

Strategy base class for Dominion

ALL Strategy SUBCLASSES REQUIRE TWO FUNCTIONS:
    action_phase : decides the order of actions to play
    buy_phase    : decides what to buy based on available coins/buys


@author: blenderhead, tim-m-mccormick
"""

class Strategy:
    
    """
    Virtual parent class for strategies
    """
    def __init__(self, player, kingdom_cards, **kwargs):
        
        self.kwargs = kwargs
        self.k_cards = kingdom_cards
        self.name = self.__str__

        return None
    
    def __repr__(self):
        """
        return a name with alphabetically-ordered kwargs appended
        """
        return self.__class__.__name__ + ''.join([str(self.kwargs[kw]) for kw in sorted(self.kwargs.keys())])
        
    def take_turn(self, player):
        """
        executes action_phase and buy_phase
        """
        
        self.action_phase(player)
        player.coins += player.hand.coins # bonus coins from actions plus money
        self.buy_phase(player)
        
        return None
    
    def action_phase(self):
        """
        default is to take no actions
        """
        pass
    
    def discard(self, player, n):
        """
        default discarding strategy priority is: victory cards, coppers, silvers,
        terminal actions, other actions, and gold
        """
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

###############################################################################
    
class BigMoney(Strategy):
    """
    Simplest possible big money strategy
    Buys the most valuable money card it can afford
    Buys provinces as soon as it can afford them
    """

    def action_phase(self, player):
        pass
    
    def buy_phase(self, player):

        if player.coins <= 2:
            pass
        elif player.coins <= 5:
            player.buy('Silver')
        elif player.coins <= 7:
            player.buy('Gold')
        else:
            player.buy('Province')

###############################################################################

class BigMoney_SP(Strategy):
    """
    Big money strategy with smart province buy
    Buys the most valuable money card it can afford while there are less provinces than duchy_buy
    Buys provinces as soon as it can afford them
    Buys duchies instead of provinces when number of provinces is less than duchy_buy
    Buys estates instead of provinces or duchies when #provinces is less than estate_buy
    """
    
    def action_phase(self, player):
        pass
    
    def buy_phase(self, player):
        
        if self.k_cards['Province'].size() > self.kwargs['duchy_buy']:
            #Do BigMoney
            if player.coins <= 2:
                pass
            elif player.coins <= 5:
                player.buy('Silver')
            elif player.coins <= 7:
                player.buy('Gold')
            else:
                player.buy('Province')
           
        #SHOULD MAKE SURE THERE ARE DUCHIES LEFT
        elif (self.k_cards['Duchy'].size() > 0) and (self.k_cards['Province'].size() <= self.kwargs['duchy_buy']) and (self.k_cards['Province'].size() > self.kwargs['estate_buy']):
            #Buy duchies
            if player.coins <= 2:
                pass
            elif player.coins <= 4:
                player.buy('Silver')
            elif player.coins <= 7:
                player.buy('Duchy')
            else:
                player.buy('Province')
                
        #SHOULD MAKE SURE THERE ARE ESTATES LEFT
        elif (self.k_cards['Estate'].size() > 0) and (self.k_cards['Province'].size() <= self.kwargs['estate_buy']):
            #Buy estate
            if player.coins <= 7:
                player.buy('Estate')
            else:
                player.buy('Province')
                
        else:
            #Do BigMoney
            if player.coins <= 2:
                pass
            elif player.coins <= 5:
                player.buy('Silver')
            elif player.coins <= 7:
                player.buy('Gold')
            else:
                player.buy('Province')

###############################################################################
         
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
            if player.coins <= 2:
                pass
            elif player.coins <= 3:
                player.buy('Silver')
            else:
                player.buy('Smithy')
        else: 
            if player.coins <= 2:
                pass
            elif player.coins <= 5:
                player.buy('Silver')
            elif player.coins <= 7:
                player.buy('Gold')
            else:
                player.buy('Province')
                
###############################################################################
                
class BigMoneyMilitia(Strategy):
    """
    Simplest big money + militia card
    Buys militia as soon as it has $4, then as BigMoney:
        Buys the most valuable money card it can afford
        Buys provinces as soon as it can afford them
        """
    
    def action_phase(self, player):
        if player.hand.count('Militia') == 1:
            player.play_action('Militia')
            
    def buy_phase(self, player):
        
        if player.deck.count('Militia') == 0:
            if player.coins <= 2:
                pass
            elif player.coins <= 3:
                player.buy('Silver')
            else:
                player.buy('Militia')
        else: 
            if player.coins <= 2:
                pass
            elif player.coins <= 5:
                player.buy('Silver')
            elif player.coins <= 7:
                player.buy('Gold')
            else:
                player.buy('Province')

###############################################################################
            
class BigMoneyXSmithy(Strategy):
    """
    allows for an adjustable MAXIMUM number of smithies for the player to buy.
    there is no guarantee that this number of smithies will be bought, but if
    the player has 4 or 5 coins and less than the provided number, xe will buy
        KEYWORD ARGUMENTS:
            n_Smithy = maximum number of Smithies to buy
    """
    
    def action_phase(self, player):
        if 'Smithy' in player.hand.names():
            player.play_action('Smithy')
        return None
    
    def buy_phase(self, player):
        # if four or five player.coins in hand and fewer than 3 smithies, buy a smithy
        if player.coins in [4,5] and player.deck.count('Smithy') < self.kwargs['n_Smithy']:
            player.buy('Smithy')
        # otherwise do big money
        elif player.coins <= 2:
            pass
        elif player.coins <= 5:
            player.buy('Silver')
        elif player.coins <= 7:
            player.buy('Gold')
        else:
            player.buy('Province')

###############################################################################

class BigMoneyXCard(Strategy):
    """
    allows for an adjustable MAXIMUM number of given single card for the player to buy.
    there is no guarantee that this number of smithies will be bought, but if
    the player has 4 or 5 coins and less than the provided number, xe will buy
        KEYWORD ARGUMENTS:
            n_Card = maximum number of CARD to buy
            card_name = string correponding to card to buy
    """
    def action_phase(self, player):
        if self.kwargs['card_name'] in player.hand.names():
            player.play_action(self.kwargs['card_name'])
        return None
    
    #NEED TO DECIDE WHEN TO BUY CARD
    def buy_phase(self, player):
        # if four or five player.coins in hand and fewer than 3 smithies, buy a smithy
        if player.coins in [] and player.deck.count(self.kwargs['card_name']) < self.kwargs['n_Card']:
            player.buy(self.kwargs['card_name'])
        # otherwise do big money
        elif player.coins <= 2:
            pass
        elif player.coins <= 5:
            player.buy('Silver')
        elif player.coins <= 7:
            player.buy('Gold')
        else:
            player.buy('Province')

###############################################################################

class VillageSmithy(Strategy):
    """
    village / smithy engine with adjustable MAX numbers of each. No guarantee that
    player will buy the provided number as with BigMoneyXSmithy
        KEYWORD ARGUMENTS:
            n_Smithy  = maximum number of Smithies to buy
            n_Village = maximum number of Villages to buy
    """
    
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
        if player.coins in [4,5] and player.deck.count('Smithy') < self.kwargs['n_Smithy']:
            player.buy('Smithy')
        elif player.coins == 3 and player.deck.count('Village') < self.kwargs['n_Village']:
            player.buy('Village')
        # then just buys money and provinces
        elif player.coins <= 2:
            pass
        elif player.coins <= 5:
            player.buy('Silver')
        elif player.coins <= 7:
            player.buy('Gold')
        else:
            player.buy('Province')

###############################################################################
            
class VillageMilitia(Strategy):
    """
    similar to village/smithy but purchases militia in place of smithies
        KEYWORD ARGUMENTS:
            n_Militia = maximum number of Militias to buy
            n_Village = maximum number of Villages to buy
    """    
    
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
        if player.coins in [4,5] and player.deck.count('Militia') < self.kwargs['n_Militia']:
            player.buy('Militia')
        elif player.coins == 3 and player.deck.count('Village') < self.kwargs['n_Village']:
            player.buy('Village')
        # then just buys money and provinces
        elif player.coins <= 2:
            pass
        elif player.coins <= 5:
            player.buy('Silver')
        elif player.coins <= 7:
            player.buy('Gold')
        else:
            player.buy('Province')
