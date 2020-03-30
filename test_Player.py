import unittest
from Card import Card
from Deck import Deck
from Player import Player

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

	def test_check_for_consecutive(self):
		e = None

		p = Player(name="Ao")
		p.hand = [
		Card(rank='S', number='8'),
		Card(rank='S', number='7'),
		Card(rank='S', number='9'),
		Card(rank='S', number='Q'),
		Card(rank='C', number='J'),
		Card(rank='S', number='A'),
		Card(rank='S', number='K'),
		Card(rank='S', number='10')
		]
		cards = p.hand
		expected = [("quarte", "S", "7"),("tierce", "S", "Q")]

		try:
			result = p.check_for_consecutive(cards, "S")
		except Exception as exc:
			e = exc

		self.assertIsNone(e)
		self.assertEqual(result, expected)

	def test_check_for_belote(self):
		p = Player(name = 'Lin')
		p.hand = [Card(rank="H", number="K"),
		Card(rank="D", number="K"),
		Card(rank="S", number="K"),
		Card(rank="C", number="K"),
		Card(rank="H", number="7"),
		Card(rank="H", number="Q"),
		Card(rank="D", number="Q"),
		Card(rank="H", number="J")]
		
		t1 = p.check_for_belote("S")
		t2 = p.check_for_belote("C")
		t3 = p.check_for_belote("H")
		t4 = p.check_for_belote("D")
		t5 = p.check_for_belote("AT")
		self.assertEqual(t1, list())
		self.assertEqual(t2, list())
		self.assertEqual(t3, [('belote','H')])
		self.assertEqual(t4, [('belote','D')])
		self.assertEqual(t5, [('belote','D'),('belote','H')])

if __name__ == '__main__':
	unittest.main()
