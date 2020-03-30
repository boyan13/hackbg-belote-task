import random
import copy
from Deck import Deck
from Player import Player
from Team import Team
from Round import Round

class Game:

    # Grab the 2 teams and init the scoreboard
    def __init__ (self, team1, team2):
        self.teams = [copy.deepcopy(team1), copy.deepcopy(team2)]
        self.score = Score(team1, team2) #teams need to be hashable!

    def swap_team_positions(self):
        buf = self.teams[0]
        self.teams[0] = self.teams[1]
        self.teams[1] = buf

    # Progresses the game
    # If lastGameWinner is passed, a random player from that team opens the round
    # This function takes care of team rearrangement
    def play_round(self, lastGameWinner = None):
        pickRandomFirst = False

        if lastGameWinner is not None:
            pickRandomFirst = True
            if lastGameWinner == teams[1]:
                self.swap_team_positions()


        round = Round(self.teams, self.score, pickRandomFirst = pickRandomFirst)
        round.start()
        self.teams[0].swap_players()
        self.swap_team_positions() 

    # Check if someone has won
    def winner(self):
        return (
            (self.score[self.teams[0]] > 150 or self.score[self.teams[1]] > 150) and
            (self.score[self.teams[0]] != self.score[self.teams[1]])
            )

    # Return the winner, or raise Exeption if there isn't one
    def get_winner(self):
        if not winner():
            raise Exception("Nobody won yet.")

        elif score[teams[0]] > 150 and score[teams[0]] > score[teams[1]]:
            return teams[0]

        elif score[teams[1]] > 150 and score[teams[1]] > score[teams[0]]:
            return teams[1]

        else:
            raise Exception("Nobody won.")

