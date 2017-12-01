# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:22:12 2017

@author: blenderhead, tim-m-mccormick
"""
from Game import Game
import numpy as np

num_games = 5000
avg_scores = np.array([0., 0.])
for i in range(num_games):
    game = Game(verbose=False)
    game.play()
    avg_scores += np.sort(game.get_final_scores())
    
avg_scores /= num_games
print("Average scores (loser, winner):")
print(avg_scores)
    