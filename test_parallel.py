# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:38:45 2017

@author: blenderherad
"""

from DominionData import DominionData
from Strategy import *

if __name__ == '__main__':
    __spec__ = None
    data = DominionData(num_players=2,
                        strategy=[BigMoney, BigMoneyXCard],
                        options=[{},{'card_name':'Smithy', 'n_Card':1}])
    
    data.run_simulation_parallel()