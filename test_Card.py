import unittest
from Card import Card

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

	def test_equal_rank(self):
		card1 = Card(rank="D", number="7")
		card2 = Card(rank="D", number="J")
		card3 = Card(rank="S", number="K")
		card4 = Card(rank="S", number="A")

		self.assertTrue(Card.equal_rank(card3, card4))
		self.assertFalse(Card.equal_rank(card2,card3))
		self.assertTrue(Card.equal_rank(card1, card2))
		self.assertFalse(Card.equal_rank(card1,card3))
		self.assertFalse(Card.equal_rank(card1, card4))
		self.assertFalse(Card.equal_rank(card2,card4))

if __name__ == '__main__':
	unittest.main()

