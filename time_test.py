# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:22:12 2017

@author: blenderhead, tim-m-mccormick
"""
from Game import Game
from Strategy import *
import numpy as np
from time import time
import matplotlib.pylab as plt
num_games = 400

ti = time()
scores = []
smithies=range(0,3)
for x in smithies:
    avg_scores = np.array([0., 0.])
    for i in range(num_games):
        game = Game(n_players=2, 
                    strategy=[BigMoney, BigMoneyXCard], 
                    options=[{}, {'card_name':'Smithy', 'n_Card':x}], 
                    verbose=False)
        game.play()
        avg_scores += game.get_final_scores()

    avg_scores /= num_games
    scores.append(list(avg_scores))
tf = time()
print("Average scores (V+M, BM+S):")
print(avg_scores)
print("Runtime = " + str(tf-ti) + " seconds")

fig = plt.figure(figsize=(8,6), dpi=100)
ax = fig.add_subplot(111)

ax.set_xlabel('Max. number of Smithies')
ax.set_ylabel('Avg. Score (' + str(num_games) + ' games)')

plt.plot(smithies,np.array(scores)[:,0], label='BM')
plt.plot(smithies,np.array(scores)[:,1], label='BM+S')

plt.legend()


plt.show()
    