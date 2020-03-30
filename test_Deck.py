import unittest
from Card import Card
from Deck import Deck

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

if __name__ == '__main__':
	unittest.main()

