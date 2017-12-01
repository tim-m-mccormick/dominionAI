# -*- coding: utf-8 -*-
from Kingdom import Kingdom
from Player  import Player
from itertools import cycle

"""
Created on Thu Nov 30 22:03:50 2017

Game of Dominion

@author: blenderherad, tim-m-mccormick
"""
class Game:
    
    def __init__(self, n_players=2, cards=None, verbose=True):
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
        self.verbose   = verbose
        self.n_players = n_players
        self.kingdom   = Kingdom(self)
        self.players   = [Player(self) for n in range(n_players)]
        self.game_over = False
        self.active_player = None
        self.final_scores  = None
        return None
    
    def _quiet_play(self):
        player_list = cycle(enumerate(self.players))
        player_turn = self.n_players*[0]
        while not self.game_over:
            idx, player = next(player_list)
            player.take_turn()
            player_turn[idx] += 1
            self.game_over = self.kingdom.check_game_over()
            
        self.final_points = list(map(lambda x: x.deck.points, self.players))
        
    def _print_play(self):        
        player_list = cycle(enumerate(self.players))
        player_turn = self.n_players*[0]
        while not self.game_over:
            idx, self.active_player = next(player_list)
            print("Player " + str(idx) + " takes xer turn:")
            self.active_player.take_turn()
            player_turn[idx] += 1
            self.game_over = self.kingdom.check_game_over()
            
        self.final_points = list(map(lambda x: x.deck.points, self.players))
        print('Final decks:')
        for i in range(self.n_players):
            idx, player = next(player_list)
            print('player ' + str(idx) + 's deck:')
            print(player.deck.names())
        print("Final scores:")
        print(list(enumerate(self.final_points)))
        
        return None
    
    def play(self):
        if self.verbose:
            self._print_play()
        else:
            self._quiet_play()
    
    def get_final_scores(self):
        assert self.game_over, "play the game first!"
        return self.final_points