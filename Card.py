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
