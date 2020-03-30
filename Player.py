import random
import copy
from Card import Card
from Deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def __str__(self):
        return f'{self.name}'
    def __repr__(self):
        return f'{self.name}: {self.hand}'
    def __eq__(self, other):
        return self.name == other.name and self.hand == other.hand
    def draw_hand(self, deck): 
        self.hand = deck.get_hand()

    def announce(self, rank):
        announcement, cards = self.check_for_carre()
        if len(cards) > 0:
            consecutives = self.check_for_consecutive(cards = cards, rank = rank)
            belote = self.check_for_belote(rank)
            announcement = announcement + consecutives + belote
        return announcement

    #check if there is carre in the player hand and adds it in declare 
    def check_for_carre(self):
        #makes a copy of hand
        cards = copy.deepcopy(self.hand)
        #list for all carres
        arr_carre = []
        #indexes of all elements in carre
        to_del = []
        #check if there is a carre
        numbers = {"7" : 5, "8" : 5, "9" : 0, "10" : 0, "J" : 0, "Q" : 0, "K" : 0, "A" : 0}
        for card in self.hand:
            numbers[card.get_number()] += 1
        #if the player has carre it's added to the arr_carre and removed from the card list
        for key in numbers.keys():
            if numbers[key]==4:
                carre = ('carre', key)
                arr_carre.append(carre)
                for i in range(len(cards)):
                    if cards[i].get_number() == key:
                        to_del.append(i)
        to_del = to_del[::-1]
        for i in to_del:
            del cards[i]
        #returns all caress and a list of the rest of the cards
        return (arr_carre, cards)

    def check_for_consecutive(self, cards, rank):

        # Storage for all found sequences
        arr_consecutives = []

        # Determine valid rank for comparison
        if rank == "NT":
            return list()
        elif rank == "AT":
            validrank = ["S", "H", "D", "C"]
        else:
            validrank = rank

        # Use vlist as indexation for values.keys()
        values = {"7" : 0, "8" : 0, "9" : 0, "10" : 0, "J" : 0, "Q" : 0, "K" : 0, "A" : 0}
        vlist = ["7", "8", "9", "10", "J", "Q", "K", "A"]

        # Make a histogram of all ocurances that match the valid rank
        for card in cards:
            crank = card.get_rank()
            if crank in validrank:
                values[card.get_number()] += 1

        # Iterate the dictionary (histogram) and extract all sequences without overlap
        # The histogram accounts for the need for the cards to be sorted
        i = 0
        while i <= 5:
            ikey = vlist[i]
            jkey = vlist[i+1]
            wkey = vlist[i+2]  
            if values[ikey] > 0 and values[jkey] > 0 and values[wkey] > 0: #Check for TIERCE

                if i <= 4: # If not end of hand
                    pkey = vlist[i+3]
                    if values[pkey] > 0: # Check for QUARTE

                        if i <= 3: # If not end of hand
                            qkey = vlist[i+4]
                            if values[qkey] > 0: # Check for QUINTE

                                # Extract QUINTE and shift i forward
                                arr_consecutives.append(("quinte", crank, ikey))
                                i += 5

                            else: # Extract QUARTE and shift i forward
                                arr_consecutives.append(("quarte", crank, ikey))
                                i += 4

                        else: # Extract QUARTE and shift i forward
                            arr_consecutives.append(("quarte", crank, ikey))
                            i += 4

                    else: # Extract TIERCE and shift i forward
                        arr_consecutives.append(("tierce", crank, ikey))
                        i += 3

                else: # Extract TIERCE and shift i forward
                     arr_consecutives.append(("tierce", crank, ikey))
                     i += 3
            else:
                i += 1
                       
        # return all found sequences as list 
        return arr_consecutives

    #check if there is belote in the player hand and adds it in declare
    def check_for_belote(self, rank):
        self.hand.sort()
        belote_arr = []

        if rank == "NT":
            return list()

        for i in range(len(self.hand)-1):
            if self.hand[i]._Card__number == 'Q':
                if self.hand[i+1]._Card__number == 'K':
                    if Card.equal_rank(self.hand[i],self.hand[i+1]):
                        belote_arr.append(('belote', self.hand[i]._Card__rank))


        if rank == "AT":
            #returns a list of tuples -> tuple('belote', rank)
            return belote_arr 
        if ('belote', rank) in belote_arr:
            #returna list of tuple('belote', rank)
            return [('belote', rank)]
        return list()      

