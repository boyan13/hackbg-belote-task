class Player:
    def __init__(self, name):
        self.name = name #My name
        self.team = 'team'#Name of the team I am part of
        self.hand = []
        self.hand_histogram = [
        {7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0}, # Spades at index 0 because their priority is 0 (lowest)
        {7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0}, # Diamonds at index 1 because their priority is 1
        {7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0}, # Hearts at index 2 because their priority is 2
        {7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0}  # Clubs at index 3 because their priority is 3 (highest)
        ]

    def get_hand(self, hand):
        self.hand = hand

        # Fill hand histogram
        for card in hand:
 
            cr = card["rank"]
            cv = card["value"]

            self.hand_histogram[cr][cv] = 1

    def announce(self, rank):
        result = []
        result = self.get_belotes(rank) + self.get_carres() + self.get_quintas(rank) + self.get_quartes(rank) + self.get_tierces(rank)
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
        pass

    def get_quartes(self, rank):
        # returns [("quarte", last card's value), ...]
        pass

    def get_tierces(self, rank):
        # returns [("tierce", last card's value), ...]
        pass

    def get_belotes(self, rank):
        # check in hand not hand_histogram!!
        self.hand = sorted(self.hand, key=lambda k: k['value'])
        self.hand = sorted(self.hand, key=lambda k: k['rank'])
        belote_arr = []


        if rank == "No Trumps":
            return belote_arr

        for i in range(len(self.hand)-1):
            if self.hand[i]['value'] == 12:
                if self.hand[i+1]['value']== 13:
                    if self.hand[i]['rank'] == self.hand[i+1]['rank']:
                        belote_arr.append(('belote', self.hand[i]['rank']))


        if rank == "All Trumps":
            #returns a list of tuples -> tuple('belote', rank)
            return belote_arr 
        else:
            if rank == "Spades":
                rank = 0
            elif rank == "Diamonds":
                rank = 1
            elif rank == "Hearts":
                rank = 2
            else:
                rank = 3
        if ('belote', rank) in belote_arr:
            #returna list of tuple('belote', rank)
            return [('belote', rank)]
        return belote_arr
        


    def check_for_consecutive(self, cards, rank):
        # # Storage for all found sequences
        # arr_consecutives = []

        # # Determine valid rank for comparison
        # if rank == "NT":
        #     return list()
        # elif rank == "AT":
        #     validrank = ["S", "H", "D", "C"]
        # else:
        #     validrank = rank

        # # Use vlist as indexation for values.keys()
        # values = {"7" : 0, "8" : 0, "9" : 0, "10" : 0, "J" : 0, "Q" : 0, "K" : 0, "A" : 0}
        # vlist = ["7", "8", "9", "10", "J", "Q", "K", "A"]

        # # Make a histogram of all ocurances that match the valid rank
        # for card in cards:
        #     crank = card.get_rank()
        #     if crank in validrank:
        #         values[card.get_number()] += 1

        # # Iterate the dictionary (histogram) and extract all sequences without overlap
        # # The histogram accounts for the need for the cards to be sorted
        # i = 0
        # while i <= 5:
        #     ikey = vlist[i]
        #     jkey = vlist[i+1]
        #     wkey = vlist[i+2]  
        #     if values[ikey] > 0 and values[jkey] > 0 and values[wkey] > 0: #Check for TIERCE

        #         if i <= 4: # If not end of hand
        #             pkey = vlist[i+3]
        #             if values[pkey] > 0: # Check for QUARTE

        #                 if i <= 3: # If not end of hand
        #                     qkey = vlist[i+4]
        #                     if values[qkey] > 0: # Check for QUINTE

        #                         # Extract QUINTE and shift i forward
        #                         arr_consecutives.append(("quinte", crank, ikey))
        #                         i += 5

        #                     else: # Extract QUARTE and shift i forward
        #                         arr_consecutives.append(("quarte", crank, ikey))
        #                         i += 4

        #                 else: # Extract QUARTE and shift i forward
        #                     arr_consecutives.append(("quarte", crank, ikey))
        #                     i += 4

        #             else: # Extract TIERCE and shift i forward
        #                 arr_consecutives.append(("tierce", crank, ikey))
        #                 i += 3

        #         else: # Extract TIERCE and shift i forward
        #              arr_consecutives.append(("tierce", crank, ikey))
        #              i += 3
        #     else:
        #         i += 1
                       
        # # return all found sequences as list 
        # return arr_consecutives
        pass

    #check if there is belote in the player hand and adds it in declare
    def check_for_belote(self, rank):
        # self.hand.sort()
        # belote_arr = []

        # if rank == "NT":
        #     return list()

        # for i in range(len(self.hand)-1):
        #     if self.hand[i]._Card__number == 'Q':
        #         if self.hand[i+1]._Card__number == 'K':
        #             if Card.equal_rank(self.hand[i],self.hand[i+1]):
        #                 belote_arr.append(('belote', self.hand[i]._Card__rank))


        # if rank == "AT":
        #     #returns a list of tuples -> tuple('belote', rank)
        #     return belote_arr 
        # if ('belote', rank) in belote_arr:
        #     #returna list of tuple('belote', rank)
        #     return [('belote', rank)]
        # return list()  
        pass    