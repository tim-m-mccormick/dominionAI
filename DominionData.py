# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 19:57:48 2017

DominionData class for Dominion

Runs basic statistics for different dominion strategies

@author: blenderhead, tim-m-mccormick
"""
from Strategy import *
from Game import Game
from Kingdom import Kingdom
from Player import Player
import numpy as np
import matplotlib.pyplot as plt

class DominionData:
    """
    Statistics package for evaluating dominion strategies
    """
    def __init__(self,num_players=2, strategy=[BigMoney,BigMoneySmithy], cards=None, n_games = 1):
        """constructor for DominionData"""
        self.verbose = False
        self.n_players = num_players
        self.strats = strategy
        if len(self.strats) != self.n_players:
            print('Need a number of strategies equal to number of players!')
            
        self.n_games = n_games
        if cards == None:            
            # if no provided cards, create "First Game"
            self.cards = ['Cellar',
                          'Market',
                          'Militia',
                          'Mine',
                          'Moat',
                          'Remodel',
                          'Smithy',
                          'Village',
                          'Woodcutter',
                          'Workshop']
        
        #we need a default game to call to kingdom
        self.def_game  = Game(n_players=2, strategy=self.strats, cards=self.cards, verbose=False)
        self.kingdom   = Kingdom(self.def_game)
        self.players   = [Player(self, self.strats[n]) for n in range(self.n_players)]
        
        #Some individual quantities
        self.ind_scores = np.ndarray(shape=(self.n_games,self.n_players), dtype = int)
        self.ind_turns  = np.ndarray(shape=(self.n_games), dtype = int)
        
        #Some average quantities
        self.avg_scores = self.n_players*[0]
        
        #Some statistical quantities
        self.turn_std_dev   = None
        self.scores_std_dev = self.n_players*[0]
        
        return None
    
    def run_simulation(self):
        """runs simulation and calculates some basic statistics on scores and turns"""
        for i in range(self.n_games):
            
            game = Game(n_players=self.n_players, strategy=self.strats, cards=self.cards, verbose=False)
            game.play()
            
            self.ind_scores[i] = game.get_final_scores()
            self.ind_turns[i]  = game.get_final_turn()
            
            self.avg_scores += game.get_final_scores()
            
            
        return None
    
    def hist_scores(self):
        """Plots histogram of scores of each player"""
        hists = self.n_players*[0]
        bin_edges = self.n_players*[0]
        scoresTrans = self.ind_scores.T.tolist()
        for i in range(len(scoresTrans)):
            plt.hist(scoresTrans[i], alpha = 1.0/len(scoresTrans), label=self.strats[i].name)
        plt.legend(loc = 'upper right')
        plt.show() 
        
        return None