# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:57:48 2017

DominionData class for Dominion

Runs basic statistics for different dominion strategies

@author: blenderhead, tim-m-mccormick
"""
from Strategy import *

class DominionData:
    """
    Statistics package for evaluating dominion strategies
    """
    def __init__(self,n_players=2, strategies=[BigMoney,BigMoneySmithy],cards=None, n_games = 1):
        """constructor for DominionData"""
        self.n_players = n_players
        self.strats = strategies
        if len(self.strats) != n_players:
            print('Need a number of strategies equal to number of players!')
            
        self.n_games = n_games
        self.cards = cards
        
        self.kingdom   = Kingdom(self)
        self.players   = [Player(self, strategy[n]) for n in range(n_players)]
        
        self.avg_scores    = n_players*[0]
        self.avg_num_turns = n_players*[0]
        
        return None
    
    def run_simulation():
        