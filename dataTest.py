# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:22:20 2017

@author: tim-m-mccormick
"""

from DominionData import DominionData
from Strategy import * 
import numpy as np

cards = ['Cellar', 'Village', 'Workshop', 'Witch', 'Market',
         'Moat', 'Woodcutter', 'Militia', 'Smithy', 'Laboratory']

dataTest = DominionData(num_players = 2,
                        strategy=[BigMoneySmithy, TwoCardEngine],
                        options = [{},
                                   {'card_1':'Village','n_1':1,'card_2':'Witch','n_2':1,'overpay_by':1,'skip_gold':True}],
                        cards=cards,
                        n_games=5000, verbose=False)
#dataTest.best_parameter_1d(player_number=1, parameter='n_Card', pvals=range(0,6), assign_best=True, n_games=1)
dataTest.run_simulation()
dataTest.hist_scores(n_bins=10)

#dataTest.hist_scores()
#hist, bin = np.histogram(dataTest.ind_scores)

#print(dataTest.ind_scores)

