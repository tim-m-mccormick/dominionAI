# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:22:12 2017

@author: blenderhead, tim-m-mccormick
"""
from Game import Game
from Strategy import BigMoney, BigMoneySmithy, VillageSmithy, VillageMilitia
import numpy as np

num_games = 1
avg_scores = np.array([0., 0.])
for i in range(num_games):
    game = Game(n_players=2, strategy=[BigMoney, VillageMilitia], verbose=True)
    game.play()
    avg_scores += game.get_final_scores()
    
avg_scores /= num_games
print("Average scores (BM, BM+S, V+S):")
print(avg_scores)
    