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
    
    def __init__(self, n_players=2, strategy=[], options=[], cards=None, verbose=True):
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
        else:
            self.cards = cards
        self.verbose   = verbose
        self.n_players = n_players
        self.kingdom   = Kingdom(self)
        self.players   = [Player(self, strategy[n], **options[n]) for n in range(n_players)]
        self.game_over = False
        self.active_player = None
        self.other_players = None
        self.final_scores  = None
        self.final_turn    = None
        return None
    
    def _quiet_play(self):
        """plays a game of Dominion with no printing"""
        player_list = cycle(enumerate(self.players))
        player_turn = self.n_players*[0]
        while not self.game_over:
            idx, self.active_player = next(player_list)
            self.other_players = set(self.players)-set([self.active_player])
            self.active_player.take_turn()
            player_turn[idx] += 1
            self.final_turn = player_turn[idx]
            self.game_over = self.kingdom.check_game_over()
            
            
        self.final_points = list(map(lambda x: x.deck.points, self.players))
        
    def _print_play(self):  
        """plays a game of dominion with full output"""
        player_list = cycle(enumerate(self.players))
        player_turn = self.n_players*[0]
        while not self.game_over:
            idx, self.active_player = next(player_list)
            if idx == 0:
                print('Begin turn ' + str(player_turn[0]+1))
            self.other_players = set(self.players)-set([self.active_player])
            print("Player " + str(idx) + " takes xer turn:")
            self.active_player.take_turn()
            player_turn[idx] += 1
            self.final_turn = player_turn[idx]
            self.game_over = self.kingdom.check_game_over() 
            
        self.final_points = list(map(lambda x: x.deck.points, self.players))
        print('Final decks:')
        for i in range(self.n_players):
            print('player ' + str(i) + 's deck:')
            print(self.players[i].deck.names())
        print("Final scores:")
        print(list(enumerate(self.final_points)))
        
        return None
    
    def play(self):
        """plays a game of Dominion"""
        if self.verbose:
            self._print_play()
        else:
            self._quiet_play()
    
    def get_final_scores(self):
        """get final scores of a game of Dominion"""
        assert self.game_over, "play the game first!"
        return self.final_points
    
    def get_final_turn(self):
        """returns the final turn of the game"""
        assert self.game_over, "play the game first!"
        return self.final_turn