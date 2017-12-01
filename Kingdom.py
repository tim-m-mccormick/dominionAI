# -*- coding: utf-8 -*-
from Stack import Stack
from Card import Card
"""
Created on Thu Nov 30 21:13:42 2017

Kingdom class for Dominion

@author: blenderherad
"""

class Kingdom:
    
    def __init__(self, n_players=2, cards=[]):
        
        self.stacks  = {}
        self.stacks['Copper']   = (Stack((60-7*n_players)*[Card('Copper')]))
        self.stacks['Silver']   = Stack(40*[Card('Silver')])
        self.stacks['Gold']     = Stack(30*[Card('Gold')])       
        self.stacks['Curse']    = Stack(self.n_curs(n_players)*[Card('Curse')])
        self.stacks['Estate']   = Stack(self.n_vict(n_players)*[Card('Estate')]
        self.stacks['Duchy']    = Stack(self.n_vict(n_players)*[Card('Duchy')])
        self.stacks['Province'] = Stack(self.n_vict(n_players)*[Card('Province')])
        
        for card in cards:
            self.stacks[card] = Stack(10*[Card(card)])
    
    def n_vict(n):
        if n == 2:
            return 8
        elif n == 3 or n == 4:
            return 12
        else:
            return 15
    
    def n_curs(n):
        return 10*(n-1)
            
    def check_game_over(self):
        if self.stacks['Province'].size() == 0:
            return True
        ## need to implement 3-empty rule here once we go beyond BigMoney
        else:
            return False
        