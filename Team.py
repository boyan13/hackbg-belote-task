import random
import copy
from Card import Card
from Deck import Deck
from Player import Player

class Team:
    def __init__(self, name, player1, player2):
        self.__name = name
        self.player1 = copy.copy(player1)
        self.player2 = copy.copy(player2)
        self.__player_turn = 0 #it's 0 if it's player1's turn and 1 if it's player2's turn
    def __str__(self):
        return f'{self.__name}: {self.player1}, {self.player2}'
    def __eq__(self, other):
        return str(self) == str(other)
    def __hash__(self):
        return hash(self.__name)
    def get_player(self):#return the player whose turn is now and change the value of player_turn
        if self.__player_turn == 0:
            self.__player_turn += 1
            return self.player1
        elif self.__player_turn == 1:
            self.__player_turn -= 1
            return self.player2
        else:
            raise Exception("Can't reach the player.")

    def choose_player(self):#choosing random player who has to start the round
        random_num = random.random()
        if random_num <= 0.5:
            self.__player_turn = 0
        else:
            self.__player_turn = 1

    def swap_players(self):
        buf = self.player1
        self.player1 = self.player2
        self.player2 = buf

