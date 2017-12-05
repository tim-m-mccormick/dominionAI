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
import multiprocessing

class DominionData:
    """
    Statistics package for evaluating dominion strategies
    """
    def __init__(self,num_players=2, 
                 strategy=[BigMoney,BigMoneySmithy], 
                 options = [{},{}], cards=None, n_games = 1, verbose=False):
        """constructor for DominionData"""
        self.verbose = verbose
        self.n_players = num_players
        self.strats = strategy
        self.options = options
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
        else:
            self.cards = cards
        
        #we need a default game to call to kingdom
        self.def_game  = Game(n_players=2, strategy=self.strats,
                              options = self.options, cards=self.cards, verbose=self.verbose, random_order=False)
        self.kingdom   = Kingdom(self.def_game)
        self.players   = [Player(self, self.strats[n]) for n in range(self.n_players)]
        
        # workaround due to new naming scheme for players. a neat name for strategy
        # is generated by str, which calls, __repr__, which can't be called before instantiation.
        # these names include keyword args (alphabetical order) so we can distinguish
        # between BM + 2Smithy and BM + 1Smithy etc.
        self.names     = [str(x.strategy) for x in self.def_game.players] 
        
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
            
            game = Game(n_players=self.n_players, 
                        strategy=self.strats, 
                        options = self.options,
                        cards=self.cards,
                        verbose=self.verbose,
                        random_order=True)
            game.play()
            
            self.ind_scores[i] = game.get_final_scores()
            self.ind_turns[i]  = game.get_final_turn()
            
        self.avg_scores = np.sum(self.ind_scores, axis=0)/self.n_games
            
    def run_simulation_parallel(self, n_proc=multiprocessing.cpu_count()):
        """runs simulation in parallel and calculates some basic statistics on scores and turns"""
        pool = multiprocessing.Pool(n_proc)
        
        self.ind_scores, self.ind_turns = zip(*pool.map(self._run, range(self.n_games)))
                    
        self.avg_scores = np.sum(self.ind_scores, axis=0)/self.n_games
            
        return None
    
    def _run(self, *args):
        """ used by parallel run"""
        game = Game(n_players=self.n_players, 
                        strategy=self.strats, 
                        options = self.options,
                        cards=self.cards,
                        verbose=False,
                        random_order=True)
        game.play()
        return game.get_final_scores(), game.get_final_turn()
    
    def hist_scores(self, n_bins=5):
        """Plots histogram of scores of each player"""
        min_score = np.min(self.ind_scores)
        max_score = np.max(self.ind_scores)
        binboundaries = np.linspace(min_score, max_score, n_bins)
        scoresTrans = self.ind_scores.T.tolist()
        plt.figure(figsize=(8,6))
        plt.xlabel('Final Score')
        plt.ylabel('Counts')
        for i in range(len(scoresTrans)):
            plt.hist(scoresTrans[i], 
                     alpha = 1.0/len(scoresTrans), 
                     label=self.names[i],
                     bins=binboundaries)
            
        plt.legend(bbox_to_anchor=(0,1), loc=3)
        plt.show() 
        
        return None
    
