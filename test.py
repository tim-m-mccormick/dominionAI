# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:22:12 2017

@author: blenderhead, tim-m-mccormick
"""
from Game import Game
from Strategy import *
import numpy as np

cards = ['Chapel', 'Village', 'Workshop', 'Witch', 'Market',
         'Moat', 'Woodcutter', 'Militia', 'Smithy', 'Mine']

num_games = 10000
avg_scores = np.array([0., 0.])
for i in range(num_games):
    game = Game(n_players=2,
                strategy=[BigMoney, BigMoneyXCard],
                options = [{},{'card_name':'Chapel', 'n_Card':1}], cards = cards, verbose=False)
    game.play()
    avg_scores += game.get_final_scores()
    
avg_scores /= num_games
print("Average scores (BM, BM+S, BM+M):")
print(avg_scores)
print(game.get_final_turn())
    