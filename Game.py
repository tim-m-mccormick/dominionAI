# -*- coding: utf-8 -*-
from Kingdom import Kingdom
from Player  import Player
from itertools import cycle

"""
Created on Thu Nov 30 22:03:50 2017

Game of Dominion

@author: blenderherad
"""
class Game:
    
    def __init__(self, n_players=2, cards=None):
        if cards == None:            
            # if no provided cards, create "First Game"
            self.cards = ['Cellar',
                          'Market',
                          'Militia',
                          'Mine',
                          'Moat',
                          'Remodel',
                          'Smithy',
                          'Village',
                          'Woodcutter',
                          'Workshop']
        self.n_players = n_players
        self.kingdom   = Kingdom(n_players, self.cards)
        self.players   = n_players*[Player()]

        self.game_over = False
        
        return None
        
    def play(self):        
        player_list = cycle(enumerate(self.players))
        player_turn = self.n_players*[0]
        while not self.game_over:
            idx, player = next(player_list)
            print("Player " + str(idx) + " takes xer turn:")
            player.take_turn()
            player_turn[idx] += 1
            self.game_over = self.kingdom.check_game_over()
            
        final_points = list(map(lambda x: x.deck.points, self.players))
        print("Final scores:")
        print(list(enumerate(final_points)))
        
        return None