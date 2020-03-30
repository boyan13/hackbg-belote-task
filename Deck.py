import random
import copy
from Card import Card

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
