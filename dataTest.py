# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:22:20 2017

@author: tim-m-mccormick
"""

from DominionData import *
from Strategy import * 
import numpy as np

dataTest = DominionData(n_players = 2, strategy=[BigMoney,BigMoneySmithy],cards=None,n_games=4)
dataTest.run_simulation()

dataTest.hist_scores()
#hist, bin = np.histogram(dataTest.ind_scores)

print(dataTest.ind_scores)

