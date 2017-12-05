# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:22:20 2017

@author: tim-m-mccormick
"""

from DominionData import DominionData
from Strategy import * 
import numpy as np

cards = ['Cellar', 'Village', 'Workshop', 'Witch', 'Market',
         'Moat', 'Woodcutter', 'Militia', 'Smithy', 'Mine']

dataTest = DominionData(num_players = 2, 
                        strategy=[BigMoneyXCard,BigMoneyXCard],
                        options = [{'smart_buy':True, 'card_name':'Smithy', 'n_Card':1},
                                   {'smart_buy':True, 'card_name':'Militia','n_Card':2}],
                        cards=cards,
                        n_games=1000, verbose=False)
dataTest.best_parameter_1d(player_number=1, parameter='n_Card', pvals=range(0,6), assign_best=True, n_games=1000)
dataTest.run_simulation()
dataTest.hist_scores(n_bins=10)

#dataTest.hist_scores()
#hist, bin = np.histogram(dataTest.ind_scores)

#print(dataTest.ind_scores)

