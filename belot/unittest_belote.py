import unittest
from belote import Card, Deck, Player, Team, Round, Game, Score

class TestCard(unittest.TestCase):
	def test_init_dunder(self):
		e = None

		try:
			card1 = Card(rank="C", number="7")
			card2 = Card(rank="D", number="J")
			card3 = Card(rank="H", number="K")
			card4 = Card(rank="S", number="A")
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

	def test_lt_dunder(self):
		card1 = Card(rank="C", number="7")
		card2 = Card(rank="D", number="J")
		card3 = Card(rank="H", number="K")
		card4 = Card(rank="S", number="A")

		self.assertFalse(card1 < card2)
		self.assertFalse(card1 < card3)
		self.assertFalse(card1 < card4)
		self.assertTrue(card2 < card3)
		self.assertFalse(card2 < card4)
		self.assertFalse(card3 < card4)

	def test_gt_dunder(self):
		card1 = Card(rank="C", number="7")
		card2 = Card(rank="D", number="J")
		card3 = Card(rank="H", number="K")
		card4 = Card(rank="S", number="A")

		self.assertTrue(card1 > card2)
		self.assertTrue(card1 > card3)
		self.assertTrue(card1 > card4)
		self.assertFalse(card2 > card3)
		self.assertTrue(card2 > card4)
		self.assertTrue(card3 > card4)

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
			p1 = Player(name = 'Silvia')
			p2 = Player(name = 'Boyan')
			p3 = Player(name = 'Ivan')
			p4 = Player(name = 'Gosho')
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(p1.name, 'Silvia')
		self.assertEqual(p2.name, 'Boyan')
		self.assertEqual(p3.name, 'Ivan')
		self.assertEqual(p4.name, 'Gosho')
	def test_eq_dunder(self):
		e = None

		try:
			deck = Deck()

			p1 = Player(name = 'Silvia')
			p1.draw_hand(deck)

			p2 = Player(name = 'Boyan')
			p2twin = Player(name = 'Boyan')
			p2.draw_hand(deck)
			p2twin.__dict__["hand"] = p2.__dict__["hand"]

			p3 = Player(name = 'Ivan')
			p4 = Player(name = 'Silvia')

		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertTrue(p1 == p1)
		self.assertTrue(p2 == p2twin)
		self.assertFalse(p3 == p4)
		self.assertFalse(p1 == p4)

	def test_carre(self):
		p = Player(name = 'Lin')
		p.hand = [Card(rank="H", number="K"),
		Card(rank="D", number="K"),
		Card(rank="S", number="K"),
		Card(rank="C", number="K"),
		Card(rank="H", number="7"),
		Card(rank="H", number="Q"),
		Card(rank="D", number="Q"),
		Card(rank="H", number="J")]
		carre, hand = p.check_for_carre()
		self.assertEqual(carre, [('carre', 'K')])
		self.assertEqual(hand, ['7H', 'QH', 'QD', 'JH'])

		



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

class TestRound(unittest.TestCase):
	
	def test_init_dunder(self):
		pass


class TestGAme(unittest.TestCase):
	pass


if __name__ == '__main__':
	unittest.main()
