# -*- coding: utf-8 -*-
from Stack import Stack
from Card  import Card
from numpy import concatenate
"""
Created on Thu Nov 30 21:13:42 2017

Kingdom class for Dominion

@author: blenderhead, tim-m-mccormick
"""

class Kingdom:
    
    def __init__(self, game = 'none'):
        
        self.game    = game
        self.stacks  = {}
        self.stacks['Copper']   = Stack([Card('Copper',   self.game) for i in range(60-7*self.game.n_players)])
        self.stacks['Silver']   = Stack([Card('Silver',   self.game) for i in range(40)])
        self.stacks['Gold']     = Stack([Card('Gold',     self.game) for i in range(30)])       
        self.stacks['Curse']    = Stack([Card('Curse',    self.game) for i in range(self.n_curs(self.game.n_players))])
        self.stacks['Estate']   = Stack([Card('Estate',   self.game) for i in range(self.n_vict(self.game.n_players))])
        self.stacks['Duchy']    = Stack([Card('Duchy',    self.game) for i in range(self.n_vict(self.game.n_players))])
        self.stacks['Province'] = Stack([Card('Province', self.game) for i in range(self.n_vict(self.game.n_players))])
        
        for card in self.game.cards:
            self.stacks[card] = Stack([Card(card, self.game) for i in range(10)]) # needs to be adjusted for things like Gardens
    
    def pop(self, card):
        return self.stacks[card].pop()
    
    @staticmethod
    def n_vict(n):
        if n == 2:
            return 8
        elif n == 3 or n == 4:
            return 12
        else:
            return 15
        
    @staticmethod
    def n_curs(n):
        return 10*(n-1)
            
    def check_game_over(self):
        if self.stacks['Province'].size() == 0:
            return True
        ## need to implement 3-empty rule here once we go beyond BigMoney
        else:
            return False
    
    def display(self):
        print(75*'-')
        print("K I N G D O M".center(75))
        print(75*'-')
        fmt = "%10s(%2s) "
        print(3*fmt % tuple(concatenate([[x, self.stacks[x].size()] for x in ['Copper', 'Silver', 'Gold']])))
        print(4*fmt % tuple(concatenate([[x, self.stacks[x].size()] for x in ['Estate', 'Duchy', 'Province', 'Curse']])))
        print(5*fmt % tuple(concatenate([[x, self.stacks[x].size()] for x in list(self.stacks.keys())[7:12]])))
        print(5*fmt % tuple(concatenate([[x, self.stacks[x].size()] for x in list(self.stacks.keys())[12:]])))

        return None
        