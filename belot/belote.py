import random

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
	def __init__(self, team1, team2, score):
		self.deck = Deck()
		self.rank = random.choice(['C', 'D', 'H', 'S', "NT", "AT"])
		self.team1 = team1
		self.team2 = team2
		self.score = score

	#This is where the round plays
	def start(self):
		pass

	# Archive round to JSON
	def to_json(self):
		pass

class Game:

	# Grab the 2 teams and init the scoreboard
	def __init__ (self, team1, team2):
		self.__team1 = team1
		self.__team2 = team2
		self.score = Score(team1, team2) #teams need to be hashable!
		self.rounds = 0

	# The entire round happens here
	def play_round(self):
		self.rounds += 1
		round = Round(self.__team1, self.__team2, self.score)
		round.start()
		#TODO make it json convertible

	# Should the game continue?
	def next_round(self):
		return (
			self.rounds < 3 or 
			not self.winner()
		)

	# Check if someone won (used in next_round())
	def winner(self):
		return (
			(self.score[self.__team1] > 150 or self.score[self.__team2] > 150) and
			(self.score[self.__team1] != self.score[self.__team2])
			)

	# Return the winner, or raise Exeption if there isn't one
	def get_winner(self):
		if not winner():
			raise Exception("Nobody won yet.")

		elif score[__team1] > 150:
			return __team1

		elif score[__team2] > 150:
			return __team2

class Score:

	# Init scoreboard with teams as keys
	def __init__ (self, team1, team2):
		self.score = {team1: 0, team2 : 0}

	# Direct access to the score dictionary
	def __getitem__ (self, arg):
		return self.score[arg]


