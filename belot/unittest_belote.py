import unittest
from belote import Card, Deck, Player, Team

class TestCard(unittest.TestCase):
	
	def test_init_dunder(self):
		e = None

		try:
			card1 = Card("C", "7")
			card2 = Card("D", "J")
			card3 = Card("H", "K")
			card4 = Card("S", "A")
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(card1._Card__rank, "C")
		self.assertEqual(card1._Card__number, "7")				
		self.assertEqual(card2._Card__rank, "D")
		self.assertEqual(card2._Card__number, "J")
		self.assertEqual(card3._Card__rank, "H")
		self.assertEqual(card3._Card__number, "K")
		self.assertEqual(card4._Card__rank, "S")
		self.assertEqual(card4._Card__number, "A")

class TestHand(unittest.TestCase):
	pass

class TestDeck(unittest.TestCase):
	def test_init_dunder(self):
		deck = Deck()
		expected_result = '[7C, 8C, 9C, 10C, AC, QC, KC, AC, 7D, 8D, 9D, 10D, AD, QD, KD, AD, 7H, 8H, 9H, 10H, AH, QH, KH, AH, 7S, 8S, 9S, 10S, AS, QS, KS, AS]'
		self.assertEqual(str(deck), expected_result)
	def test_shuffle(self):
		deck = Deck()
		not_expected_result = '[7C, 8C, 9C, 10C, AC, QC, KC, AC, 7D, 8D, 9D, 10D, AD, QD, KD, AD, 7H, 8H, 9H, 10H, AH, QH, KH, AH, 7S, 8S, 9S, 10S, AS, QS, KS, AS]'
		deck.shuffle_deck()
		self.assertEqual(len(deck.cards), 32)
		self.assertTrue(str(deck) != not_expected_result)
	def test_get_one_hand(self):
		deck = Deck()
		hand = deck.get_hand()
		self.assertEqual(len(hand), 8)
		self.assertEqual(len(deck.cards), 24)
	def test_get_two_hands(self):
		deck = Deck()
		hand = [deck.get_hand(), deck.get_hand()]
		self.assertEqual(len(hand[0]),8)
		self.assertEqual(len(hand[1]),8)
		self.assertEqual(len(deck.cards), 16)
	def test_get_three_hands(self):
		deck = Deck()
		hand = [deck.get_hand(), deck.get_hand(), deck.get_hand()]
		self.assertEqual(len(hand[0]),8)
		self.assertEqual(len(hand[1]),8)
		self.assertEqual(len(hand[2]),8)
		self.assertEqual(len(deck.cards), 8)
	def test_get_four_hands(self):
		deck = Deck()
		hand = [deck.get_hand(), deck.get_hand(), deck.get_hand(), deck.get_hand()]
		self.assertEqual(len(hand[0]),8)
		self.assertEqual(len(hand[1]),8)
		self.assertEqual(len(hand[2]),8)
		self.assertEqual(len(hand[3]),8)
		self.assertEqual(len(deck.cards), 0)
	def test_get_four_hands(self):
		deck = Deck()
		hand = [deck.get_hand(), deck.get_hand(), deck.get_hand(), deck.get_hand()]
		self.assertEqual(len(hand[0]),8)
		self.assertEqual(len(hand[1]),8)
		self.assertEqual(len(hand[2]),8)
		self.assertEqual(len(hand[3]),8)
		self.assertEqual(len(deck.cards), 0)

class TestPlayer(unittest.TestCase):
	def test_init_dunder(self):
		e = None

		try:
			deck = Deck()
			h1 = deck.get_hand()
			h2 = deck.get_hand()
			h3 = deck.get_hand()
			h4 = deck.get_hand()
			p1 = Player(name = 'Silvia', hand = h1)
			p2 = Player(name = 'Boyan', hand = h2)
			p3 = Player(name = 'Ivan', hand = h3)
			p4 = Player(name = 'Gosho', hand = h4)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(p1.name, 'Silvia')
		self.assertEqual(p1.hand, h1)
		self.assertEqual(p2.name, 'Boyan')
		self.assertEqual(p2.hand, h2)
		self.assertEqual(p3.name, 'Ivan')
		self.assertEqual(p3.hand, h3)
		self.assertEqual(p4.name, 'Gosho')
		self.assertEqual(p4.hand, h4)
	def test_eq_dunder(self):
		e = None

		try:
			deck = Deck()
			h1 = deck.get_hand()
			h2 = deck.get_hand()
			h3 = deck.get_hand()
			h4 = deck.get_hand()
			p1 = Player(name = 'Silvia', hand = h1)
			p2 = Player(name = 'Boyan', hand = h2)
			p3 = Player(name = 'Ivan', hand = h3)
			p4 = Player(name = 'Gosho', hand = h4)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(p1, Player(name = 'Silvia', hand = h1))
		self.assertEqual(p2, Player(name = 'Boyan', hand = h2))
		self.assertEqual(p3, Player(name = 'Ivan', hand = h3))
		self.assertEqual(p4, Player(name = 'Gosho', hand = h4))

		



class TestTeam(unittest.TestCase):
	pass
	def test_init_dunder(self):
		e = None

		try:
			deck = Deck()
			h1 = deck.get_hand()
			h2 = deck.get_hand()
			h3 = deck.get_hand()
			h4 = deck.get_hand()
			p1 = Player(name = 'Silvia', hand = h1)
			p2 = Player(name = 'Boyan', hand = h2)
			p3 = Player(name = 'Ivan', hand = h3)
			p4 = Player(name = 'Gosho', hand = h4)
			team1 = Team(name = 'bat', player1 = p1, player2 = p2)
			team2 = Team(name = 'snake', player1 = p3, player2 = p4)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(team1.name, 'bat')
		self.assertEqual(team1.player1, p1)
		self.assertEqual(team1.player2, p2)
		self.assertEqual(team2.name, 'snake')
		self.assertEqual(team2.player1, p3)
		self.assertEqual(team2.player2, p4)
	def test_eq_dunder(self):
		e = None

		try:
			deck = Deck()
			h1 = deck.get_hand()
			h2 = deck.get_hand()
			h3 = deck.get_hand()
			h4 = deck.get_hand()
			p1 = Player(name = 'Silvia', hand = h1)
			p2 = Player(name = 'Boyan', hand = h2)
			p3 = Player(name = 'Ivan', hand = h3)
			p4 = Player(name = 'Gosho', hand = h4)
			team1 = Team(name = 'bat', player1 = p1, player2 = p2)
			team2 = Team(name = 'snake', player1 = p3, player2 = p4)
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(team1, Team(name = 'bat', player1 = p1, player2 = p2))
		self.assertEqual(team2, Team(name = 'snake', player1 = p3, player2 = p4))
	def test_get_player_one(self):
		deck = Deck()
		h1 = deck.get_hand()
		h2 = deck.get_hand()
		p1 = Player(name = 'Silvia', hand = h1)
		p2 = Player(name = 'Boyan', hand = h2)
		team1 = Team(name = 'bat', player1 = p1, player2 = p2)
		res = team1.get_player()
		self.assertEqual(res, p1)
	def test_get_player_two(self):
		deck = Deck()
		h1 = deck.get_hand()
		h2 = deck.get_hand()
		p1 = Player(name = 'Silvia', hand = h1)
		p2 = Player(name = 'Boyan', hand = h2)
		team1 = Team(name = 'bat', player1 = p1, player2 = p2)
		res1 = team1.get_player()
		res2 = team1.get_player()
		self.assertEqual(res1, p1)
		self.assertEqual(res2, p2)
	def test_get_player_three(self):
		deck = Deck()
		h1 = deck.get_hand()
		h2 = deck.get_hand()
		p1 = Player(name = 'Silvia', hand = h1)
		p2 = Player(name = 'Boyan', hand = h2)
		team1 = Team(name = 'bat', player1 = p1, player2 = p2)
		res1 = team1.get_player()
		res2 = team1.get_player()
		res3 = team1.get_player()
		self.assertEqual(res1, p1)
		self.assertEqual(res2, p2)
		self.assertEqual(res1, p1)
	def test_chose_player(self):
		pass



class TestRound(unittest.TestCase):
	pass

class TestGAme(unittest.TestCase):
	pass


if __name__ == '__main__':
	unittest.main()
