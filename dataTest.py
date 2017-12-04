# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:22:20 2017

@author: tim-m-mccormick
"""

from DominionData import DominionData
from Strategy import * 
import numpy as np

dataTest = DominionData(num_players = 2, 
                        strategy=[BigMoney,BigMoneyXCard],
                        options = [{},{'card_name':'Militia', 'n_Card':2}], cards=None,n_games=100)
dataTest.run_simulation()
dataTest.hist_scores(n_bins=10)

#dataTest.hist_scores()
#hist, bin = np.histogram(dataTest.ind_scores)

#print(dataTest.ind_scores)

