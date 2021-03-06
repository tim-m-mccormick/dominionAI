# -*- coding: utf-8 -*-

"""
Created on Fri Dec  1 10:50:40 2017

@author: blenderhead, tim-m-mccormick
"""
curse_cards     = ['Curse']
victory_cards   = ['Estate', 'Duchy', 'Province', 'Colony']
treasure_cards  = ['Copper', 'Silver', 'Gold', 'Platinum']
base_game_cards = ['Adventurer', 'Bureaucrat', 'Cellar', 'Chancellor', 'Chapel', 
                   'CouncilRoom', 'Feast', 'Festival', 'Gardens', 'Laboratory', 
                   'Library', 'Market', 'Militia', 'Mine', 'Moat', 
                   'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief', 
                   'ThroneRoom', 'Village', 'Witch', 'Woodcutter', 'Workshop']
supported_cards = curse_cards + victory_cards + treasure_cards + base_game_cards

def Card(card, game):
    
    if card in supported_cards:
        return eval(card + "(game=game)")
    raise NotImplementedError(card + " not yet implemented! do it yourself!")

    
class CardClass:
    
    def __init__(self, game=None):
        pass
    
    # __repr__ is how objects are represented in lists, so we give it a
    # unique tag to make sure 'card in player.hand' looks for unique cards
    def __repr__(self):
        return self.__class__.__name__ + str(id(self))
    
    # if no __str__ method exists it defaults to __repr__ but here we don't
    # want to print the unique id's every time
    def __str__(self):
        return self.__class__.__name__
    
    # boolean function to handle multi-type cards like harem
    def is_type(self, card_type):
        return card_type in self.type.split()
    
    # boolean function to tell you if something is just one type
    def is_only(self, card_type):
        return card_type == self.type
    
    # effect when played
    def card_action(*args):
        pass
    
    # effect on gain (common in hinterlands)
    def on_gain(*args):
        pass
    
    # duration effect (common in seaside?)
    def duration(*args):
        pass
    """ add other null functions here as we incorporate more expansion functionality """

""" Curse cards """
class Curse(CardClass):
    def __init__(self, game=None):
        self.type   = 'Curse'
        self.points = -1
        self.value  = 0
        self.cost   = 0
        self.game   = game
        
""" Treasure cards """
class Copper(CardClass):
    def __init__(self, game=None):
        self.type   = 'Treasure'
        self.points = 0
        self.value  = 1
        self.cost   = 0
        
class Silver(CardClass):
    def __init__(self, game=None):
        self.type   = 'Treasure'
        self.points = 0
        self.value  = 2
        self.cost   = 3
        self.game   = game
        
class Gold(CardClass):
    def __init__(self, game=None):
        self.type   = 'Treasure'    
        self.points = 0
        self.value  = 3
        self.cost   = 6
        self.game   = game
        
class Platinum(CardClass):
    def __init__(self, game=None):
        self.type   = 'Treasure'    
        self.points = 0
        self.value  = 5
        self.cost   = 9
        self.game   = game
        
""" Victory cards """
class Estate(CardClass):
    def __init__(self, game=None):
        self.type   = 'Victory'    
        self.points = 1
        self.value  = 0
        self.cost   = 2
        self.game   = game
        
class Duchy(CardClass):
    def __init__(self, game=None):
        self.type   = 'Victory'    
        self.points = 3
        self.value  = 0
        self.cost   = 5
        self.game   = game
        
class Province(CardClass):
    def __init__(self, game=None):
        self.type   = 'Victory'    
        self.points = 6
        self.value  = 0
        self.cost   = 8
        self.game   = game
        
class Colony(CardClass):
    def __init__(self, game=None):
        self.type   = 'Victory'    
        self.points = 10
        self.value  = 0
        self.cost   = 11
        self.game   = game
        
""" Base game kingdom cards """
class Adventurer(CardClass):    
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 6
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        pass

class Bureaucrat(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action Attack'
        self.points = 0
        self.value  = 0
        self.cost   = 4
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        pass

class Cellar(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 2
        self.game   = game
        self.terminal_action = False
        
    def card_action(self):
        self.game.active_player.actions += 1
        self.game.active_player.cycle()
        return None

class Chancellor(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 3
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        pass

class Chapel(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 2
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        self.game.active_player.trash()
        return None

class CouncilRoom(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 5
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        self.game.active_player.draw(4)
        self.game.active_player.buys += 1
        self.game.active_player.others_draw(1)
        return None

class Feast(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 4
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        pass

class Festival(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 5
        self.game   = game
        self.terminal_action = False
        
    def card_action(self):
        self.game.active_player.actions += 2
        self.game.active_player.buys += 1
        self.game.active_player.coins += 2
        return None

class Gardens(CardClass):
    def __init__(self, game=None):
        self.type   = 'Victory'
        self.points = 0
        self.value  = 0##WRONG, FIX!!!!
        self.cost   = 4
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        pass

class Laboratory(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 5
        self.game   = game
        self.terminal_action = False
    
    def card_action(self):
        self.game.active_player.draw(2)
        self.game.active_player.actions += 1
        return None

class Library(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 5
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        pass

class Market(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost = 5
        self.game   = game
        self.terminal_action = False
    
    def card_action(self):
        self.game.active_player.draw(1)
        self.game.active_player.actions += 1
        self.game.active_player.coins += 1
        self.game.active_player.buys += 1
        return None
    
class Militia(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action Attack'
        self.points = 0
        self.value  = 0
        self.cost   = 4
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        self.game.active_player.coins += 2
        self.game.active_player.others_discard_to(3)
        return None
            
class Mine(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 5
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        pass

class Moat(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 2
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        pass

class Moneylender(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 4
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        pass

class Remodel(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 4
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        pass

class Smithy(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 4
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        self.game.active_player.draw(3)
        return None

class Spy(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 4
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        pass

class Thief(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 4
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        pass

class ThroneRoom(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 4
        self.game   = game
        self.terminal_action = 0.5
        
    def card_action(self):
        pass

class Village(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 3
        self.game   = game
        self.terminal_action = False
        
    def card_action(self):
        self.game.active_player.actions += 2
        self.game.active_player.draw(1)
        return None
    
class Witch(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 5
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        self.game.active_player.draw(2)
        self.game.active_player.others_gain('Curse')
        return None
    
class Woodcutter(CardClass):
    def __init__(self, game=None):
        self.type   = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 3
        self.game   = game
        self.terminal_action = True
        
    def card_action(self):
        self.game.active_player.buys += 1
        self.game.active_player.coins += 2
        return None

class Workshop(CardClass):
    def __init__(self, game=None):
        self.type = 'Action'
        self.points = 0
        self.value  = 0
        self.cost   = 3
        self.gmae   = game
        self.terminal_action = True
        
    def card_action(self):
        pass