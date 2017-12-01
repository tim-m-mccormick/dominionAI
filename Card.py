# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 10:50:40 2017

@author: blenderhead, tim-m-mccormick
"""
class Card:
    
    def __init__(self, card='Copper', game = 'none'):
        if game == 'none':
            print('did not pass a game to card!!')
        #default points is zero
        self.name = card
        self.points = 0
        self.value  = 0
        #Check cards and call appropriate constructor
        if card in ['Copper', 'Silver', 'Gold', 'Platinum']:
            self.money_card(self.name)
        elif card in ['Estate', 'Dutchy', 'Province', 'Colony']:
            self.victory_card(self.name)
        elif card in ['Curse']:
            self.curse_card(self.name)
        elif card in ['Adventurer', 'Bureaucrat', 'Cellar', 'Chancellor', 'Chapel', 
                      'CouncilRoom', 'Feast', 'Festival', 'Gardens', 'Laboratory', 
                      'Library', 'Market', 'Militia', 'Mine', 'Moat', 
                      'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief', 
                      'ThroneRoom', 'Village', 'Witch', 'Woodcutter', 'Workshop']:
            self.base_game_card(card, game)
            

    def money_card(self, card):
        #Check what type of card
        if card == 'Copper':
            self.cost = 0
            self.value = 1
        elif card == 'Silver':
            self.cost = 3
            self.value = 2    
        elif card == 'Gold':
            self.cost = 6
            self.value = 3
        elif card == 'Platinum':
            self.cost = 9
            self.value = 5
        else:
            print('money_card() called using non-money arguement')
            
    def victory_card(self, card):
        #check what type of victory card
        if card == 'Estate':
            self.cost = 2
            self.points = 1
        elif card == 'Dutchy':
            self.cost = 5
            self.points = 3
        elif card == 'Province':
            self.cost = 8
            self.points = 6
        elif card == 'Colony':
            self.cost = 11
            self.points = 10
        else:
            print('victory_card() called with non-victory arguement')
            
    def curse_card(self, card):
        if card == 'Curse':
            self.cost = 0
            self.points = -1
        else:
            print('curse_card() called with non-curse card')
            
    def base_game_card(self, card):
        if card == 'Adventurer': '
            pass
        elif card == 'Bureaucrat':
            pass
        elif card == 'Cellar':
            pass
        elif card == 'Chancellor':
            pass
        elif card == 'Chapel':
            pass
        elif card == 'CouncilRoom':
            pass
        elif card == 
