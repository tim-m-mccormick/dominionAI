# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:22:12 2017

@author: blenderhead, tim-m-mccormick
"""
from Game import Game
from Strategy import BigMoney, BigMoneySmithy, BigMoneyMilitia, BigMoneyXSmithy, VillageSmithy, VillageMilitia
import numpy as np
from time import time

num_games = 1
avg_scores = np.array([0., 0.])
ti = time()
for i in range(num_games):
    game = Game(n_players=2, 
                strategy=[VillageMilitia, BigMoneyXSmithy], 
                options=[{'n_Militia':3, 'n_Village':5}, {'n_Smithy':1}], 
                verbose=True)
    game.play()
    avg_scores += game.get_final_scores()

tf = time()
avg_scores /= num_games
print("Average scores (V+M, BM+S):")
print(avg_scores)
print("Runtime = " + str(tf-ti) + " seconds")
    