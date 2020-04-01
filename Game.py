import random
import copy
import json

class Belote:
    # ranks as follow: Spades = 1, Diamonds = 2, Hearts = 3, Clubs = 4
    # alues as follow: ......... J = 11, Q = 12, K = 13, A = 14

    # if card looks like this card = {'rank' : 2, 'value' : 12}

    # Expects list of 2 lists containing 2 players of the same team each
    # Example [ [player1, player3], [player2, player4] ]
    def __init__(self, players):

        # =============== VALIDATION ===============

        # Validate enclosing list
        if type(players)is not list:
            raise TypeError("Bad type.")

        if len(players) == 0:
            raise ValueError("Cannot create a game without players!")
        elif len(players) == 1:
            raise ValueError("Only one team.")
        elif len(players) > 2:
            raise ValueError("Too many teams to unpack!")
        else:

            # Validate the list of players for both teams
            teams = []

            for team in players:
                if type(team) is not list:
                    raise TypeError("Bad type.")

                if len(team) == 0:
                    raise ValueError("Empty team.")
                elif len(team) == 1:
                    raise ValueError("Too few members in a team.")
                elif len(team) > 2:
                    raise ValueError("Too many members in a team.")
                
                teams.append(team)

        # Validate players are in correct team
        # Validate there are no duplications
        for team in teams:
            if team[0].team != team[1].team:
                raise ValueError("Members of different teams put in one team!")
            if team[0].name == team[1].name:
                raise ValueError("Duplicating players!")

        player1 = teams[0][0]
        player2 = teams[1][0]
        player3 = teams[0][1]
        player4 = teams[1][1]

        if player1.team == player2.team or player1.team == player4.team:
            raise ValueError("Member of one team is already part of the other!")
        if player1.name == player2.name or player1.name == player4.name:
            raise ValueError("Duplicating players!")
        if player3.team == player2.team or player3.team == player4:
            raise ValueError("Member of one team is already part of the other!")
        if player3.name == player2.name or player3.name == player4.name:
            raise ValueError("Duplicating players!")       

        # =============== END OF VALIDATION ===============

        self.players = [player1, player2, player3, player4]
        self.team1 = player1.team
        self.team2 = player2.team
        self.score = {self.team1 : 0, self.team2 : 0}
        self.points = {self.team1 : 0, self.team2 : 0}
        self.order = [0, 1, 2, 3]
        self.deck = [
        {"rank" : 0, "value" : 7}, {"rank" : 0, "value" : 8},
        {"rank" : 0, "value" : 9}, {"rank" : 0, "value" : 10},
        {"rank" : 0, "value" : 11}, {"rank" : 0, "value" : 12},
        {"rank" : 0, "value" : 13}, {"rank" : 0, "value" : 14},

        {"rank" : 1, "value" : 7}, {"rank" : 1, "value" : 8},
        {"rank" : 1, "value" : 9}, {"rank" : 1, "value" : 10},
        {"rank" : 1, "value" : 11}, {"rank" : 1, "value" : 12},
        {"rank" : 1, "value" : 13}, {"rank" : 1, "value" : 14},

        {"rank" : 2, "value" : 7}, {"rank" : 2, "value" : 8},
        {"rank" : 2, "value" : 9}, {"rank" : 2, "value" : 10},
        {"rank" : 2, "value" : 11}, {"rank" : 2, "value" : 12},
        {"rank" : 2, "value" : 13}, {"rank" : 2, "value" : 14},

        {"rank" : 3, "value" : 7}, {"rank" : 3, "value" : 8},
        {"rank" : 3, "value" : 9}, {"rank" : 3, "value" : 10},
        {"rank" : 3, "value" : 11}, {"rank" : 3, "value" : 12},
        {"rank" : 3, "value" : 13}, {"rank" : 3, "value" : 14}
        ]

        # For json conversion
        self.game = ""
        self.rounds = []
        self.contracts = []
        self.cards = []
        self.announcements = []
        self.round_points = []

    def to_txt(self):
        pass

    def to_json(self):
        # PSEUDO-CODE
        game_dict = {
            self.game : {
            }
        }

        all_dicts = []

        for i in range(len(self.rounds)): #for every round
          new_dict = {
              self.round[i] : {
                  "contract" : self.contract[i],
                  self.team1 : {
                      self.players[0] : {
                          "cards" : self.cards[i][0],
                          "announcements" : self.announcements[i][0],
                          "points" : self.round_points[0]
                      },
                      self.players[2] : {
                          "cards" : self.cards[i][2],
                          "announcements" : self.announcements[i][2],
                          "points" : self.round_points[2]
                      }
                  },
                  self.team2 : {
                      self.players[1] : {
                          "cards" : self.cards[i][1],
                          "announcements" : self.announcements[i][1],
                          "points" : self.round_points[1]
                      },
                      self.players[3] : {
                          "cards" : self.cards[i][3],
                          "announcements" : self.announcements[i][3],
                          "points" : self.round_points[3]
                      }
                  }
              }
          }
        
        j = 1
        for dictionary in all_dicts:    
            game_dict[self.game] = dictionary
            with open("game1.json", w):
                json.dump(game_dict)
                j += 1
            

    # First player becomes last in the play order
    # Example: [0, 1, 2, 3] --> [1, 2, 3, 0]
    def shift_player_order(self):
        first = self.order[0]
        del self.order[0]
        self.order += [first]

    # Rearrange the play order so that 
    # one of the players in the given team (chosen randomly)
    # opens the round
    def pick_first_from(self, team):
        if team != self.team1 and team != self.team2:
            raise ValueError("Team not found.")

        first = random.choice([0,1])

        if (first == 0):
            self.order = [0, 1, 2, 3]
            if self.players[0].team != team:
                self.shift_player_order()
        else:
            self.order = [2, 3, 0, 1]
            if self.players[2].team != team:
                self.shift_player_order()

    def assign_hands(self):
        random.shuffle(self.deck)
        self.players[0].get_hand(self.deck[0:9])
        self.players[1].get_hand(self.deck[9:17])
        self.players[2].get_hand(self.deck[17:25])
        self.players[3].get_hand(self.deck[25:])
        pass

    def round_won(self):
        return (
        self.score[self.team1] > 150 or self.score[self.team2] > 150 and
        self.score[self.team1] != self.score[self.team2]
        )

    def get_round_winner(self):
        pass

    def get_game_winner(self):
        pass

    # THE JSON EXAMPLE
    # {
    #   "game 1": {
    #     "round 1": {
    #       "contract": "Hearts",
    #       "Mecheta": {
    #         "Marto": {
    #           "cards:": ["7s", "8s", "9s", "10c", "Jd", "Qh", "Kh", "As"],
    #           "announcements": ["belote"],
    #           "points": 20
    #         },
    #         "Rado": {
    #           "cards:": ["7d", "8c", "9d", "10d", "Js", "Qs", "Kd", "Ac"],
    #           "announcements": [],
    #           "points": 0
    #         }
    #       },
    #       "Koteta": {
    #         "Gosho": {
    #           "cards:": ["7c", "8d", "9c", "10s", "Jh", "Qc", "Kc", "Ad"],
    #           "announcements": [],
    #           "points": 0
    #         },
    #         "Pesho": {
    #           "cards:": ["7h", "8h", "9h", "10h", "Jc", "Qd", "Ks", "Ah"],
    #           "announcements": ["quarte"],
    #           "points": 50
    #         }
    #       }
    #     }
    #     // rest of the rounds here ....
    #   }
    # }

    def play(self):
        round_victor_team = str()

        # Play 3 rounds and announce winner
        for game_index in range(3):
            self.game = f"game{game_index+1}" # Status update (later used for json)

            if game_index > 0:
                self.pick_first_from(round_victor_team)
            round_index = 1; # The round counter
            while (not self.round_won()):

                self.assign_hands()

                if round_index > 0:
                    self.shifft_player_order()

                # [0] - "Spades"
                # [1] - "Diamonds"
                # [2] - "Hearts"
                # [3] - "Clubs"
                # []  - No Trumps
                # [0, 1, 2, 3] - All Trumps
                contract = random.choice([0], [1], [2], [3], [], [0, 1, 2, 3])

                # Announcements extracted in the order of the self.order
                # (1-st to play --> 2-nd to play --> 3-rd to play --> 4-th to play)
                announcements = [] 
                for player in self.order:
                    announcements.append({players[player] : self.players[player].announce()})

                valid_announcements = self.validate_announcements(announcements) # Strip nulified announcements

                    
                pl1_points, pl2_points, pl3_points, pl4_points = self.to_points(announcements)

                self.score[team1] += (pl1_points + pl3_points)
                self.score[team2] += (pl2_points + pl4_points)

                # Document round for json conversiom
                self.rounds.append(f"round{round_index}")
                if contract == [0]:
                    self.contract.append("Spades")
                elif contract == [1]:
                    self.contract.append("Diamonds")
                elif contract == [2]:
                    self.contract.append("Hearts")
                elif contract == [3]:
                    self.contract.apend("Clubs")
                elif contract == [0, 1, 2, 3]:
                    self.contracts.append("All Trumps")
                else:
                    self.contract.append("No Trumps")
                hands_in_order = []
                for player in players:
                    hands_in_order.append(player.hand)
                self.cards = hands_in_order
                self.announcements.append(valid_announcements) 
                self.round_points.append([pl1_points, pl2_points, pl3_points, pl4_points]) 

                round_index += 1

            round_victor_team = self.get_round_winner()

    def get_teams_announcements(self, announcements):
        declaretions = {'carre': 0, 'quinta': 1, 'quarte': 2, 'tierce': 3, 'belote': 4}
        hist = [
        {0:[], 1: [], 2: [], 3: [], 4: []},
        {0:[], 1: [], 2: [], 3: [], 4: []},
        {0:[], 1: [], 2: [], 3: [], 4: []},
        {0:[], 1: [], 2: [], 3: [], 4: []}
        ]
        teams_decl = [
        {0:[], 1: [], 2: [], 3: [], 4: []},
        {0:[], 1: [], 2: [], 3: [], 4: []}
        ]
        teams = [{},{}]
        player_hist = [{},{},{},{}]
        keys = announcements.keys()
        lst = list(announcements.values())
        index = []
        for i in range(4):
            if len(lst[i]) != 0:
                index.append(i)

        for i in index:
            for key in declaretions.keys():
                for j in range(len(lst[i])):
                    if key == lst[i][j][0]:
                        hist[i][declaretions[key]].append(lst[i][j])
                        teams_decl[i%2][declaretions[key]].append(lst[i][j])
        for i in range(4):
            for key in hist[i].keys():
                if hist[i][key] != []:
                    player_hist[i][key] = hist[i][key]
        for i in range(2):
            for key in teams_decl[i].keys():
                if teams_decl[i][key] != []:
                    teams[i][key] = teams_decl[i][key]

        return [teams,player_hist]

    def final_announcements(self, teams, hist):
        team1, team2 = teams
        pl_announcements = [[],[],[],[]]
        for i in range(4):
            if i%2==0:
                for key in hist[i].keys():
                    if key in team1.keys():
                        for item in hist[i][key]:
                            if item in team1[key]:
                                pl_announcements[i].append(item)

            if i%2==1:
                for key in hist[i].keys():
                    if key in team2.keys():
                        for item in hist[i][key]:
                            if item in team2[key]:
                                pl_announcements[i].append(item)
        return pl_announcements

    def validate_announcements(self, announcements):
        new_announcements = {}
        keys = list(announcements.keys())
        lst = list(announcements.values())

        if len(lst[0]) == 0 and len(lst[1]) == 0 and len(lst[2]) == 0 and len(lst[3]) == 0:
            return announcements
        if len(lst[0]) == 0 and len(lst[2]) == 0:
            return announcements
        if len(lst[1]) == 0 and len(lst[3]) == 0:
            return announcements
        teams, player_hist = self.get_teams_announcements(announcements)
        team1, team2 = copy.deepcopy(teams)

        for k in team1.keys():
            team1[k].sort(key = lambda x: x[1])
        for k in team2.keys():
            team2[k].sort(key = lambda x: x[1])

        #carre
        if 0 in team1 and 0 in team2:
            if team1[0][len(team1[0])-1] > team2[0][len(team2[0])-1]:
                del team2[0]
            else:
                del team1[0]

        keys_team1 = list(team1.keys())
        keys_team2 = list(team2.keys())

        #remove carre and belote from keys
        if 0 in keys_team1:
            keys_team1.remove(0)
        if 0 in keys_team2:
            keys_team2.remove(0)
        if 4 in keys_team1:
            keys_team1.remove(4)
        if 4 in keys_team2:
            keys_team2.remove(4)

        if len(keys_team1)> 0 and len(keys_team2) > 0:
            if keys_team1[0] == keys_team2[0]:
                if team1[keys_team1[0]] > team2[keys_team2[0]]:
                    for i in [1,2,3]:
                        if i in keys_team1:
                            del team1[i]
                elif team1[keys_team1[0]] < team2[keys_team2[0]]:
                    for i in [1,2,3]:
                        if i in keys_team1:
                            del team1[i]
                else:
                    for i in [1,2,3]:
                        if i in keys_team1:
                            del team1[i]
                    for i in [1,2,3]:
                        if i in keys_team1:
                            del team1[i]
            if keys_team1[0] > keys_team2[0]:
                for i in [1,2,3]:
                        if i in keys_team2:
                            del team2[i]
            if keys_team1[0] < keys_team2[0]:
                for i in [1,2,3]:
                    if i in keys_team1:
                            del team1[i]

        pl_list = self.final_announcements([team1,team2], player_hist)
        for i in range(4):
            new_announcements[keys[i]] = pl_list[i]

        return new_announcements 