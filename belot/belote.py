class Team:import random

# Клас карта, съдържа номера на картата и боята й
class Card:
	#Инициализираме картата
	def __init__(self, rank, number):
		self.__rank = rank
		self.__number = number
	def __str__(self):
		return f'{self.__number}{self.__rank}'
	def __repr__(self):
		return f'{self.__number}{self.__rank}'
	def __eq__(self, other):
		pass
	def __lt__(self):
		pass
	def __le__(self):
		pass

#class Hand:
#	pass

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
		if len(self.cards) > 0:
			hand = self.cards[0:8]
			del self.cards[0:8]
			return hand
		else:
			raise Exeption('No more cards in the deck.')



		
class Player:
	def __init__(self, name, hand):
		self.name = name
		self.hand = hand

class Team:
	def __init__(self, name, player1, player2):
		self.name = name
		self.player1 = player1
		self.player2 = player2

class Round:
	def __init__(self, rank, team1, team2):
		self.deck = Deck()
		self.rank = rank
		self.team1 = team1
		self.team2 = team2

class Game:
	pass

