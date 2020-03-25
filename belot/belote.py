class Card:
	def __init__(self, rank, number):
		self.__rank = rank
		self.__number = number	
	def __str__(self):
		return f'{self.number} {self.rank}'
	def __repr__(self):
		return f'{self.number} {self.rank}'
	def __eq__(self, other):
		pass
	def __lt__(self):
		pass
	def __le__(self):
		pass

#class Hand:
#	pass

class Deck:
	def __init__(self):
		ranks = ['C', 'D', 'H', 'S']
		numbers = ['7','8','9','10','A','Q','K','A']
		self.cards = []
		for rank in ranks:
			for number in numbers:
				cards.append(Card(number = number, rank = rank))

	def shuffle(self):
		pass

	def return_hand(self):
		pass



		
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


