class Score:

    # Init scoreboard with teams as keys
    def __init__ (self, team1, team2):
        self.score = {team1: 0, team2 : 0}

    # Direct access to the score dictionary
    def __getitem__ (self, arg):
        return self.score[arg]

    def __iadd__ (self, other):
        if len(self.score) != len(other.score):
            raise Exception("Cannot sum scores with different number of teams.")

        for key in self.score.keys():
            if key not in other.score.keys():
                raise Exception("Scoreboard teams don't match, impossible addition.")

        for key in self.score.keys():
            self.score[key] += other.score[key]

    # A method that extracts and converts announcements into points
    # and returns a Score object to be summed with the main score 
    @classmethod
    def calc_points(cls, announcements):
        pass
