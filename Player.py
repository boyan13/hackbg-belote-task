class Player:
    def __init__(self, name, team):
        self.name = name #My name
        self.team = team#Name of the team I am part of
        self.hand = []
        self.hand_histogram = [
        {7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0}, # Spades at index 0 because their priority is 0 (lowest)
        {7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0}, # Diamonds at index 1 because their priority is 1
        {7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0}, # Hearts at index 2 because their priority is 2
        {7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0}  # Clubs at index 3 because their priority is 3 (highest)
        ]

    def get_hand(self, hand):
        self.hand = hand

    def build_histogram(self):
        # Fill hand histogram
        for card in self.hand:
 
            cr = card["rank"]
            cv = card["value"]

            self.hand_histogram[cr][cv] = 1
    def clear_histogram(self):
        for card in self.hand:
 
            cr = card["rank"]
            cv = card["value"]

            self.hand_histogram[cr][cv] = 0

    def announce(self, rank):
        # Fill hand histogram
        self.build_histogram()
        if rank == []:
            return []
        result = []
        result = self.get_carres() + self.get_quintas(rank) + self.get_quartes(rank) + self.get_tierces(rank) + self.get_belotes(rank) 
        self.clear_histogram()
        return result

    def get_carres(self):
        # returns: [("carre", value, points), ...]
        carres = []
        carre = 0;
        for card in self.hand:
            value = card["value"]
            carre = 0
            if value == 7 or value == 8:
                continue

            for rank in [0, 1, 2, 3]:
                if self.hand_histogram[rank][value] == 1:
                    carre += 1;
                else: 
                    break
                if carre == 4:
                    for rank in [0, 1, 2 ,3]:
                        self.hand_histogram[rank][value] = 0 
                    carres.append( ("carre", value) )
        return carres

    def get_quintas(self, rank):
        # returns [("quinta", last card's value), ...]
        quintas = []
        count = 0

        for i in rank:
            count = 0
            for j in range(7,15):
                if self.hand_histogram[i][j] == 1:
                    count += 1
                elif self.hand_histogram[i][j] == 0:
                    if count == 5:
                        for k in range(j-5, j):
                            self.hand_histogram[i][k] == 0
                        quintas.append(("quinta", j-1))
                        return quintas
        return quintas              

    def get_quartes(self, rank):
        # returns [("quarte", last card's value), ...]
        quartes = []
        count = 0

        for i in rank:
            count = 0
            for j in range(7,15):
                if self.hand_histogram[i][j] == 1:
                    count += 1
                    if count == 4:
                        for k in range(j-3, j+1):
                            self.hand_histogram[i][k] == 0
                        quartes.append(("quarte", j))
                        count = 0
                elif self.hand_histogram[i][j] == 0:
                    count = 0
                    
        return quartes

    def get_tierces(self, rank):
        # returns [("tierce", last card's value), ...]
        tierces = []
        count = 0

        for i in rank:
            count = 0
            for j in range(7,15):
                if self.hand_histogram[i][j] == 1:
                    count += 1
                    if count == 3:
                        for k in range(j-2, j+1):
                            self.hand_histogram[i][k] == 0
                        tierces.append(("tierce", j))
                        count = 0
                elif self.hand_histogram[i][j] == 0:
                    count = 0
        
        return tierces

    def get_belotes(self, rank):
        # check in hand not hand_histogram!!
        self.hand = sorted(self.hand, key=lambda k: k['value'])
        self.hand = sorted(self.hand, key=lambda k: k['rank'])
        belote_arr = []


        if rank == []:
            return belote_arr

        for i in range(len(self.hand)-1):
            if self.hand[i]['value'] == 12:
                if self.hand[i+1]['value']== 13:
                    if self.hand[i]['rank'] == self.hand[i+1]['rank']:
                        belote_arr.append(('belote', self.hand[i]['rank']))


        if rank == [0,1,2,3]:
            #returns a list of tuples -> tuple('belote', rank)
            return belote_arr 
        
        if ('belote', rank) in belote_arr:
            #returna list of tuple('belote', rank)
            return [('belote', rank)]
        return belote_arr