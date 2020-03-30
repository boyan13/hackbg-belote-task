import random
import copy
from Deck import Deck
from Player import Player
from Team import Team

class Round:
    def __init__(self, teams, score, pickRandomFirst = False):
        self.deck = Deck()
        self.rank = random.choice(['C', 'D', 'H', 'S', "NT", "AT"])
        self.score = score
        self.team1 = teams[0]
        self.team2 = teams[1]

        if pickRandomFirst:
            self.team1.choose_player()

    #This is where the round plays
    def start(self):
        self.deck.shuffle_deck()
        self.team1.player1.draw_hand()
        self.team1.player2.draw_hand()
        self.team2.player1.draw_hand()
        self.team2.player2.draw_hand()

        announcements = {1 : "", 2 : "", 3 : "", 4 : ""}

        #if rank is "NT" makes the score 0
        if self.rank == "NT":
            self.score += Score(self.team1, self.team2)

        else:
            for i in range(1,5):
                if i % 2 == 1:
                    ann = team1.get_player().announce(self.rank)
                else:
                    ann = team2.get_player().announce(self.rank)
                announcements[i] = ann

                self.score += Score.calc_points(announcements)

    # Archive round to JSON
    def to_json(self):
        pass

