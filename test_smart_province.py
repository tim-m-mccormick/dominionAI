# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:52:07 2017

@author: tim-m-mccormick

Determines optimal turns for Big Money to buy provinces, dutchies, and estates
"""
from Strategy import *
from DominionData import DominionData
from Game import Game 
import numpy as np

games = 400

results = []

for d_buy in [1,2,3,4,5,6]:
    for e_buy in [1,2,3,4,5]:
        if e_buy >= d_buy:
            continue
        print(str(d_buy) + ',' + str(e_buy))
        data = DominionData(num_players = 2, 
                            strategy=[BigMoney,BigMoney_SP],
                            options = [{},{'duchy_buy':d_buy,'estate_buy':e_buy}], 
                            cards=None,n_games=games)
        data.run_simulation()
        
        results += [d_buy, e_buy, data.avg_scores[1]-data.avg_scores[0]]
        
print(results)
