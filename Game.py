class Belote:
	# ranks as follow: Spades = 1, Diamonds = 2, Hearts = 3, Clubs = 4
	# alues as follow: ......... J = 11, Q = 12, K = 13, A = 14

	# if card looks like this card = {'rank' : 2, 'value' : 12}
	# deck = [card, card, card, card ..... all cards]

	def __init__(self):
		# self.score = {player1.team : 0, player2.team : 0}
		# self.players = [player1, player2, player3, player 4]
		# self.order = [1, 2 ,3 ,4], pointers to players OR [0, 1, 2 ,3] whatever we choose
		# self.game = {}

		# EVERYTHING THAT TO_JSON NEEDS
		# self.game
		# self.rounds = [0, 1, 2, 4]
		# self.contract = []
		# self.cards = []
		# self.announcements = []
		# self.points =[]
		# + ALSO
		#from player some stuff
			pass

	def to_json(self):
		# game_json = {
		# 	self.game : {

		# 	}
		# }
	
		# all_dicts = []

		# for i in range(len(self.rounds)): #for every round
		# 	new_dict = {
		# 		self.round[i] : {
		# 			"contract" : self.contract[i]
		# 			self.players[0].team : {
		# 				self.players[0] : {
		# 					"cards" : self.cards[i][0]
		# 					"announcements" : self.announcements[i][0]
		# 				} 
		# 				self.players[2] : {
		# 					"cards" : self.cards[i][2]
		# 					"announcements" : self.announcements[i][2]
		# 				}
		# 			}
		# 			self.players[1].team : {
		# 				self.players[1] : {
		# 					"cards" : self.cards[i][1]
		# 					"announcements" : self.announcements[i][1]
		# 				}
		# 				self.players[3] : {
		# 					"cards" : self.cards[i][3]
		# 					"announcements" : self.announcements[i][3]
		# 				}
		# 			}
		# 		}
		# 	}
			
		# 	for dictionary in all_dicts:	
		# 		game_json[self.game] = dictionary
		pass

	# CONCEPTUALLY belote.__dict__["game"].to_json()
		pass

	# self.order shift (aka [1, 2, 3 ,4] -> [4, 1, 2, 3])
	def shift_player_order(self):
		# b = order.pop()
		# a = [b] + a
		pass

	def assign_hands(self):
		# shuffle deck
		# for i in range(0, 32, 8):
		# 	each player.get_hand[i:i+8]
		pass

	def round_won(self):
		# TRUE if round is one aka:
		# 1 team has more than 150 points? (in score)
		# and maybe other conditions...

		#FALSE if nobody won yet
		pass

	def winner(self):
		#return the team that won 2 games
		pass

	# THE JSON EXAMPLE
	# {
	#   "game 1": {
	#     "round 1": {
	#       "contract": "Hearts",
	#       "Mecheta": {
	#         "Marto": {
	#           "cards:": ["7s", "8s", "9s", "10c", "Jd", "Qh", "Kh", "As"],
	#           "announcements": ["belote"],
	#           "points": 20
	#         },
	#         "Rado": {
	#           "cards:": ["7d", "8c", "9d", "10d", "Js", "Qs", "Kd", "Ac"],
	#           "announcements": [],
	#           "points": 0
	#         }
	#       },
	#       "Koteta": {
	#         "Gosho": {
	#           "cards:": ["7c", "8d", "9c", "10s", "Jh", "Qc", "Kc", "Ad"],
	#           "announcements": [],
	#           "points": 0
	#         },
	#         "Pesho": {
	#           "cards:": ["7h", "8h", "9h", "10h", "Jc", "Qd", "Ks", "Ah"],
	#           "announcements": ["quarte"],
	#           "points": 50
	#         }
	#       }
	#     }
	#     // rest of the rounds here ....
	#   }
	# }

	def play(self):
		# PSEUDO CODE!!!!!!!!!!!
		# for i in range(3): #FULL GAME ROUND (in json: "game1", f"game{i + 1}")
		# 	self.game = f"game{i+1}"

		# 	j = 0
		# 	while (not round_won): #PLAY ROUNDS UNTIL WINNER
		# 		#ROUND (in json: "round1", f"round{j + 1}")
		# 		self.rounds.append(f"round{i+1}")
				
		# 		assign_hands()

		# 		if j > 0:
		# 			shifft_player_order()

		# 		contract = ("Spades", "Diamonds", "Hearts", "Clubs", "All Trumps" , "No Trumps").choose()
		# 		#CONTRACT (in json: "contract:", f"contract")
		# 		self.contracts.append(contract)
		
		# 		announcements = [] #priority decreasing from left to right -->
		# 		for player in order:
		# 			announcements.append( {player : players[player(with correct index)].announce(contract)} )

		# 		validate_announcements(announcements)?????? #or strip
		# 		self.announcements.append( announcements )

		# 		j += 1;
		# returns the winner after someone wins, also make everything to json

		def validate_announcements(self, announcements):
			pass