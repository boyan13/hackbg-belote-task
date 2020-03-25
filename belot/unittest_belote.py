import unittest
from belote.py import Card, Deck, Player

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
		self.assertEqual(card1._Card__rank, "D")
		self.assertEqual(card1._Card__number, "J")
		self.assertEqual(card1._Card__rank, "H")
		self.assertEqual(card1._Card__number, "K")
		self.assertEqual(card1._Card__rank, "S")
		self.assertEqual(card1._Card__number, "A")

class TestHand(unittest.TestCase):
	pass

class TestDeck(unittest.TestCase):
	pass

class TestPlayer(unittest.TestCase):
	pass

class TestTeam(unittest.TestCase):
	pass

class TestRound(unittest.TestCase):
	pass

class TestGAme(unittest.TestCase):
	pass


if __name__ == '__main__':
	unittest.main()
