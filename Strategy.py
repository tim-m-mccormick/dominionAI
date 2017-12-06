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
        
        # set default non-action buying behavior 
        # to smart with duchy_buy=5, estate_buy=1
        # other default behavior options can go here
        if 'smart_buy' not in kwargs.keys():
            kwargs['smart_buy']  = True
            kwargs['duchy_buy']  = 5
            kwargs['estate_buy'] = 1
        elif kwargs['smart_buy']:
            if 'duchy_buy' not in kwargs.keys():
                kwargs['duchy_buy'] = 5
            if 'estate_buy' not in kwargs.keys():
                kwargs['estate_buy'] = 1
        
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
    
    def buy_non_actions(self, player):
        """ 
        all strategies can now call this function 
        after deciding not to buy action cards
        """
        if self.kwargs['smart_buy']:
            self.smart_buy(player)
        else:
            self.naive_buy(player)
    
    def naive_buy(self, player):
        """
        old big-money naive buy
        """
        if player.coins <= 2:
            player.buys -= 1 # if we get to this point, player has a useless buy
                             # which he "spends" on nothing to kick out of while buys > 0 loops
        elif player.coins <= 5:
            player.buy('Silver')
        elif player.coins <= 7:
            player.buy('Gold')
        else:
            player.buy('Province')
    
    def smart_buy(self, player):
        if self.k_cards['Province'].size() > self.kwargs['duchy_buy']:
            #Do BigMoney
            self.naive_buy(player)
           
        #SHOULD MAKE SURE THERE ARE DUCHIES LEFT
        elif player.coins >= 5 and self.k_cards['Duchy'].size() > 0 and \
        self.k_cards['Province'].size() <= self.kwargs['duchy_buy']:
            
            #Buy duchy or province
            if player.coins <= 7:
                player.buy('Duchy')
            else:
                player.buy('Province')         
            
        #SHOULD MAKE SURE THERE ARE ESTATES LEFT
        elif player.coins >= 2 and self.k_cards['Estate'].size() > 0 and \
        self.k_cards['Province'].size() <= self.kwargs['estate_buy']:
            
            #Buy estate or province
            if player.coins <= 7:
                player.buy('Estate')
            else:
                player.buy('Province')
                
        else:
            # back to money
            self.naive_buy(player)
        
    def discard(self, player, n):
        """
        default discarding strategy priority is: victory cards, coppers, silvers,
        terminal actions, other actions, and gold
        """
        discards = []    
        
        # first look at victories and return an 
        # appropriately sized list if sufficient,
        # then add coppers and do the same etc.      
        for func in [lambda x: x.is_only('Victory'),
                     lambda x: str(x) == 'Copper',
                     lambda x: str(x) == 'Silver',
                     lambda x: x.is_type('Action') and x.terminal_action,
                     lambda x: x.is_type('Action') and not x.terminal_action,
                     lambda x: str(x) == 'Gold']:
            
            discards += list(filter(func, player.hand.cards))
            if len(discards) >= n:
                while len(discards) > n:
                    discards.pop()
                return discards
                
        return discards # this should never happen
    
    def trash(self, player):
        """
        Defaults trashing strategy priority is: Estates, coppers
        Default trashing strategy only trashes
        """
        trashers = []
        
        for card in player.hand.cards:
            if str(card) == 'Estate' and card not in trashers and player.game.kingdom.stacks['Province'].size() > 1:
                trashers += [card]
                
        coinDeckCount = player.deck.coins
        copperHandCount = player.hand.count('Copper')
        
        if coinDeckCount <= 3:
            pass
        elif coinDeckCount > 3 and (coinDeckCount-copperHandCount) <= 3:
            for c in player.hand.cards:
                if str(c) == 'Copper':
                    trashers += [c]
                    coinDeckCount -= 1
                    copperHandCount -= 1
                if (coinDeckCount <=3) or (copperHandCount == 0):
                    break
        else:
            for c in player.hand.cards:
                if str(c) == 'Copper':
                    trashers += [c]
        
        return trashers
        
    def cycle(self, player):
        """
        Basic cycling function
        Will discard all victory cards
        Will discard copper if (total coins in draw pile)/(card in draw pile) 
        is greater than (total coins in hand)/(card in hand)
        """
        if player.hand.size() == 0:
            return 0 # if empty hand nothing do discard
        
        cyclers = 0
        handValue     = player.hand.coins/player.hand.size()
        # must first make sure that draw pile is not empty
        if player.draw_pile.size() is not 0:
            drawPileValue = player.draw_pile.coins/player.draw_pile.size()
        elif player.discard_pile.size() is not 0:
            drawPileValue = player.discard_pile.coins/player.discard_pile.size()
        else:
            return 0 # if all cards not in hand are in play, no reason to cycle
        for c in player.hand.cards:
            if c.type == 'Victory' or (str(c) == 'Copper' and handValue > drawPileValue):
                cyclers += 1
        
        return cyclers

###############################################################################
    
class BigMoney(Strategy):
    """
    Simplest possible big money strategy
    Buys the most valuable money card it can afford
    Buys provinces as soon as it can afford them
    and buys other victory cards according to 'smart_buy' keyword arg
    """

    def action_phase(self, player):
        pass
    
    def buy_phase(self, player):
        self.buy_non_actions(player)

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
            self.buy_non_actions(player)
                
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
            self.buy_non_actions(player)

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
        # otherwise do buy non actions
        else:
            self.buy_non_actions(player)

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
        
        while player.actions > 0 and self.kwargs['card_name'] in player.hand.names():
            player.play_action(self.kwargs['card_name'])
        return None
    
    #NEED TO DECIDE WHEN TO BUY CARD
    def buy_phase(self, player):
        card_cost = self.k_cards[self.kwargs['card_name']].cards[0].cost # ugly but works
        # if four or five player.coins in hand and fewer than 3 smithies, buy a smithy
        if player.coins >= card_cost and player.deck.count(self.kwargs['card_name']) < self.kwargs['n_Card']:
            player.buy(self.kwargs['card_name'])
        # otherwise do big money
        else:
            self.buy_non_actions(player)
        
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
        else:
            self.buy_non_actions(player)

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
        else:
            self.buy_non_actions(player)

class TwoCardEngine(Strategy):
    """
    based on village/smithy, will buy action cards when hand.coins
    is in the right range. plays non-terminal actions before terminal
    ones. intended for use with one terminal and one non-terminal action
    
        KEYWORD_ARGUMENTS:
            card_1 : name of 1st card
            n_1    : number of 1st card
            card_2 : name of 2nd card
            n_2    : number of 2nd card
            overpay_by : (optional) prevents bot from over-paying for
                            listed actions by more than overpay_by.
                            defaults to 10 which should be sufficient
                            to always over-pay
            skip_gold : (optional) if True, bot will overpay for action
                            even if it could by a gold. defaults to True.
                            will not skip buying provinces but a similar
                            switch could be added for that
    """

    def action_phase(self, player):
        non_terminal = list(filter(lambda x: x.is_type('Action') and not x.terminal_action, player.hand.cards))
        terminal     = list(filter(lambda x: x.is_type('Action') and x.terminal_action, player.hand.cards))
        for card in non_terminal + terminal: # plays all non-terminals and as many terminals as possible
            if player.actions > 0:
                player.play_action(str(card))
            else:
                break
            
        return None
    
    def buy_phase(self, player):
        """ 
        note that there is presently no guarantee the bot will actually buy
        both of the cards. could be re-worked to force the bot to look for a balance
        i.e. buy the provided card it has fewer of, given other conditions
        """        
        empty_piles = list(map(lambda x: player.game.kingdom.stacks[x].size() is 0,
                               [self.kwargs['card_1'], self.kwargs['card_2']]))
        
        if all(empty_piles):
            while player.buys > 0:
               self.buy_non_actions(player)
            return None
        
        # set default kwargs if they weren't provided
        if 'overpay_by' not in self.kwargs.keys():
            self.kwargs['overpay_by'] = 10
        if 'skip_gold' not in self.kwargs.keys():
            self.kwargs['skip_gold'] = True
               
        indices     = [0,1] # for checkign counts of other card during loop
        cards       = [self.kwargs['card_1'], self.kwargs['card_2']]
        targets     = [self.kwargs['n_1'], self.kwargs['n_2']]  
        counts      = list(map(lambda x: player.deck.count(x), cards))             
        terminal    = list(map(lambda x: player.game.kingdom.stacks[x].cards[0].terminal_action, cards))        
        costs       = list(map(lambda x: player.game.kingdom.stacks[x].cards[0].cost, cards))
        
        while player.buys > 0:
            for idx, term, cost, card, count, target, empty in \
                list(zip(indices, terminal, costs, cards, counts, targets, empty_piles)):
                #print(term, cost, card, count, target, empty, player.buys)
                # buys terminal actions first (probably bad idea, just based on smithy/village)                    
                    if player.coins >= 8: # don't skimp on provinces
                        self.buy_non_actions(player) 
                        break
                    elif player.coins >= 6 and not self.kwargs['skip_gold']:
                        self.buy_non_actions(player)
                        break
                    elif term and player.coins >= cost and \
                    player.coins <= cost + self.kwargs['overpay_by'] and \
                    count < target and count <= counts[(idx+1)%2] and not empty: # 2-cards is hard coded
                         player.buy(card)
                         break # jump out of the for loop so buys>0 gets tested
                    elif not term and player.coins >= cost and \
                    player.coins <= cost + self.kwargs['overpay_by'] and \
                    count < target and count <= counts[(idx+1)%2] and not empty:
                        player.buy(card)
                        break
    
            # if we get here, bot thinks it has enough actions
            self.buy_non_actions(player)
                    
        return None
             
###############################################################################
            
class Random(Strategy):
    """
    for model-training purposes:
    buys a random affordable card on every buy phase. Plays random
    actions until it's out of actions. Discards random cards from hand, etc.
    """
    pass # need to finish implementing all cards first
    
class SmartRandom(Strategy):
    """
    for model-training purposes:
    buys a random card costing exactly the number of coins,
    or one less, etc. Plays non-terminal actions before terminal
    actions and discards cards using the default function
    """
    pass # need to finish implementing all cards first