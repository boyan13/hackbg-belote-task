import random
import copy

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
		self.hand = deck.get_hand

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
	def __init__(self, teams, score, lastGameWinner = None):
		self.deck = Deck()
		self.rank = random.choice(['C', 'D', 'H', 'S', "NT", "AT"])

		self.score = score

		if lastGameWinner is None:
			self.team1 = teams[0]
			self.team2 = teams[1]
		else:
			if teams[0] == lastGameWinner:
				self.team2 = teams[1]
			elif teams[1] == lastGameWinner:
				self.team2 = teams[0]
			else:
				raise Exception("Team passed as \"Last Game's Winner\" is invalid.")

			self.team1 = lastGameWinner
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

	# The entire round happens here
	def play_round(self, lastGameWinner = None):
		round = Round(self.teams, self.score, lastGameWinner = lastGameWinner)
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




