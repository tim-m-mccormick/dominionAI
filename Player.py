# -*- coding: utf-8 -*-

from Strategy import Strategy, BigMoney
from Stack    import Stack, Hand, Deck
from Card     import Card

"""
Created on Thu Nov 30 13:14:45 2017

Player class for Dominion

attributes:
    deck:           list of Cards in deck, unsorted and mutable
    draw_pile:      current draw pile, a stack with fixed order
    discard_pile:   another stack with fixed order
    strategy:       a Strategy class with take_turn and discard methods

methods:
    draw(n):    draws n cards
    discard(n): discards n cards
    shuffle():  shuffles deck
    reshuffle():    shuffles discard pile into deck
    

@author: blenderhead, tim-m-mccormick
"""
class Player:
    
    # constructor used to create a new player at the beginning of a Game
    def __init__(self, game, strategy=None):
        
        # kingdom is passed to each Player
        # and gets modified during buy()
        self.game = game
        if strategy is None:
            self.strategy = BigMoney(self, self.game.kingdom.stacks.keys())
        else:
            self.strategy = strategy(self, self.game.kingdom.stacks.keys())
        
        self.discard_pile = Stack(cards = list(map(lambda x: Card(x, self.game),7*['Copper'] + 3*['Estate'])))
        self.draw_pile = Stack(cards=[])
        self.hand      = Hand(cards=[])
        self.deck      = Deck(cards=self.discard_pile.cards + self.draw_pile.cards)
        self.reshuffle()
        self.draw(5)
        
        return None
    
    # private method to reshuffle     
    def reshuffle(self):
        
        if self.game.verbose:
            print("   reshuffles")
        self.draw_pile = Stack(cards=self.discard_pile.cards)
        self.discard_pile = Stack(cards=[])
        self.draw_pile.shuffle()
        
        return None
        
    # private method to draw n cards
    def draw(self, n):

        for i in range(n):
            if self.draw_pile.size() == 0:
                if self.discard_pile.size() > 0 :
                    self.reshuffle()
                else:
                    if self.game.verbose:
                        print("   has exhausted deck")
                    return None
            self.hand.extend([self.draw_pile.pop()])

        #print(self.hand.names())
        return None
    
    # private method for discarding. used for cleanup and attacks
    def discard(self, n):
        
        if n == self.hand.size():
            self.discards = tuple(self.hand.cards)
#            print(discards)
#            print(self.hand.cards)
        else:
            self.discards = tuple(self.strategy.discard(n)) # this should not happen yet
                   
        for c in self.discards: 
            self.hand.remove(c)
        self.discard_pile.extend(self.discards)
        del self.discards
        return None
    
    def discard_to(self, n):
        self.discard(self.hand.size()-n)
        return None
    
    def others_discard_to(self, n):
        for p in self.game.other_players:
            p.discard_to(n)
        return None
    
    def others_discard(self, n):
        for p in self.game.other_players:
            p.discard(n)
        return None
    
    def trash(self, card):
        
        return None # not used yet
    
    # take turn by passing self to self's strategy, which calls play_action(), buy() and cleanup()
    def take_turn(self):
        
        self.actions     = 1
        self.buys        = 1
        self.coins       = 0
        self.in_play = Stack(cards=[])
        self.strategy.take_turn(self) # magic happens here
        self.cleanup()
    
    def cleanup(self):
        
        if self.in_play.size() > 0:
            self.discard_pile.extend(self.in_play.pop_all())
        self.discard(self.hand.size())
        self.draw(5)
       
    def buy(self, card):
        if self.game.verbose:
            print("   has hand: ", self.hand.names())
            print("   buys " + card)
        popped = self.game.kingdom.pop(card)
        self.discard_pile.extend([popped])
        self.deck.extend([popped])
        self.coins -= popped.cost
        return None
    
    def play_action(self, card_name):
        assert card_name in self.hand.names(), "Playing a card you don't have? Cheater!"
        card = self.hand.first(card_name)
        if self.game.verbose:
            print("   has hand: ", self.hand.names())
            print("   plays " + card_name)
        self.hand.remove(card)
        self.in_play.append(card)
        self.actions -= 1
        card.card_action()
        return None
        
