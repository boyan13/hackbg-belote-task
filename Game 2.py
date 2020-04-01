import copy

class Belote:
    # ranks as follow: Spades = 1, Diamonds = 2, Hearts = 3, Clubs = 4
    # alues as follow: ......... J = 11, Q = 12, K = 13, A = 14

    # if card looks like this card = {'rank' : 2, 'value' : 12}
    # deck = [card, card, card, card ..... all cards]

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
        self.score = {player1.team : 0, player2.team : 0}
        self.order = [0, 1, 2, 3]

        # For json conversion
        self.game = ""
        self.rounds = []
        self.contracts = []
        self.cards = []
        self.announcements = []
        self.points = []

    def to_json(self):
        # game_json = {
        #   self.game : {

        #   }
        # }
    
        # all_dicts = []

        # for i in range(len(self.rounds)): #for every round
        #   new_dict = {
        #       self.round[i] : {
        #           "contract" : self.contract[i]
        #           self.players[0].team : {
        #               self.players[0] : {
        #                   "cards" : self.cards[i][0]
        #                   "announcements" : self.announcements[i][0]
        #               } 
        #               self.players[2] : {
        #                   "cards" : self.cards[i][2]
        #                   "announcements" : self.announcements[i][2]
        #               }
        #           }
        #           self.players[1].team : {
        #               self.players[1] : {
        #                   "cards" : self.cards[i][1]
        #                   "announcements" : self.announcements[i][1]
        #               }
        #               self.players[3] : {
        #                   "cards" : self.cards[i][3]
        #                   "announcements" : self.announcements[i][3]
        #               }
        #           }
        #       }
        #   }
            
        #   for dictionary in all_dicts:    
        #       game_json[self.game] = dictionary
        pass

    # CONCEPTUALLY belote.__dict__["game"].to_json()
    #    pass

    # self.order shift (aka [1, 2, 3 ,4] -> [4, 1, 2, 3])
    def shift_player_order(self):
        # b = order.pop()
        # a = [b] + a
        pass

    def assign_hands(self):
        # shuffle deck
        # for i in range(0, 32, 8):
        #   each player.get_hand[i:i+8]
        pass

    def round_won(self):
        # TRUE if round is one aka:
        # 1 team has more than 150 points? (in score)
        # and maybe other conditions...

        #FALSE if nobody won yet
        pass

    def winner(self):
        #return the team that won 2 games
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
        # PSEUDO CODE!!!!!!!!!!!
        # for i in range(3): #FULL GAME ROUND (in json: "game1", f"game{i + 1}")
        #   self.game = f"game{i+1}"

        #   j = 0
        #   while (not round_won): #PLAY ROUNDS UNTIL WINNER
        #       #ROUND (in json: "round1", f"round{j + 1}")
        #       self.rounds.append(f"round{i+1}")
                
        #       assign_hands()

        #       if j > 0:
        #           shifft_player_order()

        #       contract = ("Spades", "Diamonds", "Hearts", "Clubs", "All Trumps" , "No Trumps").choose()
        #       #CONTRACT (in json: "contract:", f"contract")
        #       self.contracts.append(contract)
        
        #       announcements = [] #priority decreasing from left to right -->
        #       for player in order:
        #           announcements.append( {player : players[player(with correct index)].announce(contract)} )

        #       validate_announcements(announcements)?????? #or strip
        #       self.announcements.append( announcements )

        #       j += 1;
        # returns the winner after someone wins, also make everything to json
        pass

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

    def filal_announcements(self, teams, hist):
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

        pl_list = self.filal_announcements([team1,team2], player_hist)
        for i in range(4):
            new_announcements[keys[i]] = pl_list[i]

        return new_announcements