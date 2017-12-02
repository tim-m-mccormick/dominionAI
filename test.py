# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:22:12 2017

@author: blenderhead, tim-m-mccormick
"""
from Game import Game
from Strategy import BigMoney, BigMoneySmithy
import numpy as np

num_games = 1000
avg_scores = np.array([0., 0.])
for i in range(num_games):
    game = Game(strategy=[BigMoney, BigMoneySmithy], verbose=False)
    game.play()
    avg_scores += game.get_final_scores()
    
avg_scores /= num_games
print("Average scores (BM, BM+S):")
print(avg_scores)
    