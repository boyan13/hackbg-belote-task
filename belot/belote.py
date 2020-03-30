import random
import copy

# Клас карта, съдържа номера на картата и боята й
class Card:

    ranks = {"S" : 1, "D" : 2, "H" : 3, "C" : 4}
    numbers = {"7" : 1, "8" : 2, "9" : 3, "10" : 4, "J" : 5, "Q" : 6, "K" : 7, "A" : 8}

    #Инициализираме картата
    def __init__(self, rank, number):
        self.__rank = str(rank)
        self.__number = str(number)
    def __str__(self):
        return f'{self.__number}{self.__rank}'
    def __repr__(self):
        return f'{self.__number}{self.__rank}'
    def __eq__(self, other):
        return str(self) == str(other)
    def __lt__(self, other):
        if self.__rank != other.__rank:
            return Card.ranks[self.__rank] < Card.ranks[other.__rank]
        elif self.__number != other.__number:
            return Card.numbers[self.__number] < Card.numbers[other.__number]
        else:
            raise Exception ("Cards are equal in rank and value") 
    def __hash__(self):
        return hash(self.__rank+self.__number)

    def get_number(self):
        return self.__number

    def get_rank(self):
        return self.__rank

    #Check if the rank of two cards is the same
    @classmethod
    def equal_rank(cls, card1, card2):
        return card1.__rank == card2.__rank

# @classmethod
# def arrange_hand(self, hand):
#     # Insertion sort
#     shand = copy.deepcopy(hand)
#     for i in range(len(shand)):
#         buf = shand[i]

#         j = i - 1

#         while j >= 0:
#             if shand[j+1] > buf:
#                 shand[j+1] = shand[j]
#                 j = j - 1
#             else:
#                 shand[j+1] = buf
#                 break

#     return shand

#Клас тесте, представлява тесте от 32 елемента на класа Карта
class Deck:
    #Пълним тестето с карти
    def __init__(self):
        ranks = ['C', 'D', 'H', 'S']
        numbers = ['7','8','9','10','A','Q','K','A']
        self.cards = []
        for rank in ranks:
            for number in numbers:
                self.cards.append(Card(number = number, rank = rank))

    def __str__(self):
        return f'{self.cards}'

    #Функция, която разбърква тестето от карти
    def shuffle_deck(self):
        random.shuffle(self.cards)

    #Функция, която раздава 8 карти, ако тестето не е празно
    def get_hand(self):
        if len(self.cards) > 0 and len(self.cards) % 8 == 0:
            hand = self.cards[0:8]
            del self.cards[0:8]
            return hand
        else:
            raise Exeption('No more cards in the deck.')
    
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

    def announce(self):
        pass

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
        team1.player1.draw_hand()
        team1.player2.draw_hand()
        team2.player1.draw_hand()
        team2.player2.draw_hand()

        announcements = {1 : "", 2 : "", 3 : "", 4 : ""}

        for i in range(1,5):
            if i % 2 == 1:
                ann = team1.get_player().announce()
            else:
                ann = team2.get_player().announce()
            announcements[i] = ann

            self.score += score.calc_points(announcements)

    # Archive round to JSON
    def to_json(self):
        pass

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
