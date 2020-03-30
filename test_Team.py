import unittest
from Deck import Deck
from Player import Player
from Team import Team

class TestTeam(unittest.TestCase):
	def test_init_dunder(self):
		e = None

		try:
			deck = Deck()
			h1 = deck.get_hand()
			h2 = deck.get_hand()
			h3 = deck.get_hand()
			h4 = deck.get_hand()
			p1 = Player(name = 'Silvia')
			p1.hand = h1
			p2 = Player(name = 'Boyan')
			p2.hand = h2
			p3 = Player(name = 'Ivan')
			p3.hand = h3
			p4 = Player(name = 'Gosho')
			p4.hand = h4
			team1 = Team(name = 'bat', player1 = p1, player2 = p2)
			team2 = Team(name = 'snake', player1 = p3, player2 = p4)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(team1.__dict__["_Team__name"], 'bat')
		self.assertEqual(team1.player1, p1)
		self.assertEqual(team1.player1.hand, h1)
		self.assertEqual(team1.player2, p2)
		self.assertEqual(team1.player2.hand, h2)
		self.assertEqual(team2.__dict__["_Team__name"], 'snake')
		self.assertEqual(team2.player1, p3)
		self.assertEqual(team2.player1.hand, h3)
		self.assertEqual(team2.player2, p4)
		self.assertEqual(team2.player2.hand, h4)
	
	def test_eq_dunder(self):
		e = None

		try:
			p1 = Player(name = 'Silvia')
			p2 = Player(name = 'Boyan')
			p3 = Player(name = 'Ivan')
			p4 = Player(name = 'Gosho')
			team1 = Team(name = 'bat', player1 = p1, player2 = p2)
			team2 = Team(name = 'snake', player1 = p3, player2 = p4)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(team1, Team(name = 'bat', player1 = p1, player2 = p2))
		self.assertEqual(team2, Team(name = 'snake', player1 = p3, player2 = p4))
	
	def test_get_player(self):
		e = None

		p1 = Player(name = 'Silvia')
		p2 = Player(name = 'Boyan')
		team1 = Team(name = 'bat', player1 = p1, player2 = p2)

		try:
			res1 = team1.get_player()
			res2 = team1.get_player()
			res3 = team1.get_player()
		except Exception as exc:
			e = exc

		self.assertEqual(res1, p1)
		self.assertEqual(res2, p2)
		self.assertEqual(res3, p1)
	
	def test_get_player_with_corrupted_turn_member(self):
		p1 = Player(name = 'Silvia')
		p2 = Player(name = 'Boyan')
		team1 = Team(name = 'bat', player1 = p1, player2 = p2)
		team1.__dict__["_Team__player_turn"] = 69

		try:
			res1 = team1.get_player()
		except Exception as exc:
			e = exc

		self.assertIsNotNone(e)
		self.assertEqual(str(e), "Can't reach the player.")

	def test_choose_player(self):
		pass

if __name__ == '__main__':
	unittest.main()
