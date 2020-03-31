import unittest
from Player import Player

class testPlayer(unittest.TestCase):
    def test_get_hand(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':1,'value':14},
        {'rank':0,'value':14},{'rank':2,'value':12},
        {'rank':2,'value':10},{'rank':3,'value':8},
        {'rank':1,'value':9},{'rank':3,'value':11}
        ]

        player.get_hand(hand)

        self.assertEqual(player.hand, hand)
    
    def test_build_histogram(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':1,'value':14},
        {'rank':0,'value':14},{'rank':2,'value':12},
        {'rank':2,'value':10},{'rank':3,'value':8},
        {'rank':1,'value':9},{'rank':3,'value':11}
        ]

        hand_histogram = [
        {7 : 1, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 1},
        {7 : 0, 8 : 0, 9 : 1, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 1},
        {7 : 0, 8 : 0, 9 : 0, 10 : 1, 11 : 0, 12 : 1, 13 : 0, 14 : 0},
        {7 : 0, 8 : 1, 9 : 0, 10 : 0, 11 : 1, 12 : 0, 13 : 0, 14 : 0}
        ]
        player.get_hand(hand)
        player.build_histogram()

        self.assertEqual(player.hand_histogram, hand_histogram)

    def test_clear_histogram(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':1,'value':14},
        {'rank':0,'value':14},{'rank':2,'value':12},
        {'rank':2,'value':10},{'rank':3,'value':8},
        {'rank':1,'value':9},{'rank':3,'value':11}
        ]

        hand_histogram = [
        {7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0},
        {7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0},
        {7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0},
        {7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0}
        ]
        player.get_hand(hand)
        player.build_histogram()
        player.clear_histogram()

        self.assertEqual(player.hand_histogram, hand_histogram)

    def test_annouce_one_carre(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':1,'value':12},
        {'rank':0,'value':12},{'rank':2,'value':12},
        {'rank':2,'value':10},{'rank':3,'value':8},
        {'rank':1,'value':9},{'rank':3,'value':12}
        ]
        player.get_hand(hand)

        expected_result = [('carre', 12)]
        result = player.announce([0])
        self.assertEqual(result, expected_result)
    
    def test_annouce_one_carre_one_tierces_one_belote(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':0,'value':11},
        {'rank':3,'value':14},{'rank':0,'value':12},
        {'rank':1,'value':14},{'rank':0,'value':13},
        {'rank':2,'value':14},{'rank':0,'value':14}
        ]
        player.get_hand(hand)
        expected_result = [('carre', 14), ('tierce', 13), ('belote', 0)]
        result = player.announce([0])
        self.assertEqual(result, expected_result)
    
    def test_annouce_one_carre_one_tierces_one_belote__all_trumps(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':2,'value':9},{'rank':2,'value':11},
        {'rank':3,'value':12},{'rank':0,'value':12},
        {'rank':1,'value':12},{'rank':0,'value':13},
        {'rank':2,'value':12},{'rank':2,'value':10}
        ]
        player.get_hand(hand)
        expected_result = [('carre', 12), ('tierce', 11), ('belote', 0)]
        result = player.announce([0,1,2,3])
        self.assertEqual(result, expected_result)
    
    def test_annouce_no_trumps(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':2,'value':9},{'rank':2,'value':11},
        {'rank':3,'value':12},{'rank':0,'value':12},
        {'rank':1,'value':12},{'rank':0,'value':13},
        {'rank':2,'value':12},{'rank':2,'value':10}
        ]
        player.get_hand(hand)
        expected_result = []
        result = player.announce([])
        self.assertEqual(result, expected_result)
    
    def test_get_carre_one_carre(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':1,'value':12},
        {'rank':0,'value':12},{'rank':2,'value':12},
        {'rank':2,'value':10},{'rank':3,'value':8},
        {'rank':1,'value':9},{'rank':3,'value':12}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = [('carre', 12)]
        result = player.get_carres()
        self.assertEqual(result, expected_result)
    
    def test_get_carre_two_carres(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':9},{'rank':1,'value':12},
        {'rank':1,'value':9},{'rank':2,'value':12},
        {'rank':2,'value':9},{'rank':3,'value':12},
        {'rank':3,'value':9},{'rank':0,'value':12}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = [('carre', 9),('carre', 12)]
        result = player.get_carres()
        self.assertEqual(result, expected_result)
    
    def test_get_carre_no_carre(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':1,'value':12},
        {'rank':0,'value':11},{'rank':2,'value':12},
        {'rank':2,'value':10},{'rank':3,'value':8},
        {'rank':1,'value':9},{'rank':3,'value':12}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = []
        result = player.get_carres()
        self.assertEqual(result, expected_result)
    
    def test_get_quintas(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':0,'value':11},
        {'rank':0,'value':8},{'rank':2,'value':12},
        {'rank':0,'value':9},{'rank':3,'value':8},
        {'rank':0,'value':10},{'rank':3,'value':11}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = [('quinta', 11)]
        result = player.get_quintas([0])
        self.assertEqual(result, expected_result)
    
    def test_get_quintas_all_trumps(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':0,'value':11},
        {'rank':0,'value':8},{'rank':2,'value':12},
        {'rank':0,'value':9},{'rank':3,'value':8},
        {'rank':0,'value':10},{'rank':3,'value':11}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = [('quinta', 11)]
        result = player.get_quintas([0,1,2,3])
        self.assertEqual(result, expected_result)
    
    def test_get_quintas_no_trumps(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':0,'value':11},
        {'rank':0,'value':8},{'rank':2,'value':12},
        {'rank':0,'value':9},{'rank':3,'value':8},
        {'rank':0,'value':10},{'rank':3,'value':11}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = []
        result = player.announce([])
        self.assertEqual(result, expected_result)

    def test_get_quintas_no_quintas_in_hand(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':1,'value':11},
        {'rank':0,'value':8},{'rank':2,'value':12},
        {'rank':0,'value':9},{'rank':3,'value':8},
        {'rank':0,'value':10},{'rank':3,'value':11}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = []
        result = player.get_quintas([0])
        self.assertEqual(result, expected_result)

    def test_get_quartes_one_quartes(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':1,'value':11},
        {'rank':0,'value':8},{'rank':2,'value':12},
        {'rank':0,'value':9},{'rank':3,'value':8},
        {'rank':0,'value':10},{'rank':3,'value':11}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = [('quarte', 10)]
        result = player.get_quartes([0])
        self.assertEqual(result, expected_result)

    def test_get_quartes_two_quartes(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':0,'value':11},
        {'rank':0,'value':8},{'rank':0,'value':12},
        {'rank':0,'value':9},{'rank':0,'value':13},
        {'rank':0,'value':10},{'rank':0,'value':14}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = [('quarte', 10), ('quarte', 14)]
        result = player.get_quartes([0])
        self.assertEqual(result, expected_result)
    
    def test_get_quartes_two_quartes_all_trumps(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':2,'value':11},
        {'rank':0,'value':8},{'rank':2,'value':12},
        {'rank':0,'value':9},{'rank':2,'value':13},
        {'rank':0,'value':10},{'rank':2,'value':14}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = [('quarte', 10), ('quarte', 14)]
        result = player.get_quartes([0,1,2,3])
        self.assertEqual(result, expected_result)
    
    def test_get_quartes_two_quartes_no_trumps(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':2,'value':11},
        {'rank':0,'value':8},{'rank':2,'value':12},
        {'rank':0,'value':9},{'rank':2,'value':13},
        {'rank':0,'value':10},{'rank':2,'value':14}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = []
        result = player.get_quartes([])
        self.assertEqual(result, expected_result)
    
    def test_get_quartes_no_quartes(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':0,'value':11},
        {'rank':2,'value':8},{'rank':2,'value':12},
        {'rank':0,'value':9},{'rank':0,'value':13},
        {'rank':1,'value':10},{'rank':2,'value':14}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = []
        result = player.get_quartes([0])
        self.assertEqual(result, expected_result)
    
    def test_get_tierces_one_tierces(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':0,'value':11},
        {'rank':0,'value':8},{'rank':2,'value':12},
        {'rank':0,'value':9},{'rank':0,'value':13},
        {'rank':2,'value':10},{'rank':1,'value':14}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = [('tierce', 9)]
        result = player.get_tierces([0])
        self.assertEqual(result, expected_result)
    
    def test_get_tierces_two_tierces(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':2,'value':11},
        {'rank':0,'value':8},{'rank':0,'value':12},
        {'rank':0,'value':9},{'rank':0,'value':13},
        {'rank':2,'value':10},{'rank':0,'value':14}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = [('tierce', 9),('tierce', 14)]
        result = player.get_tierces([0])
        self.assertEqual(result, expected_result)
    
    def test_get_tierces_two_tierces_all_trumps(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':2,'value':11},
        {'rank':0,'value':8},{'rank':2,'value':12},
        {'rank':0,'value':9},{'rank':0,'value':13},
        {'rank':2,'value':10},{'rank':0,'value':14}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = [('tierce', 9),('tierce', 12)]
        result = player.get_tierces([0,1,2,3])
        self.assertEqual(result, expected_result)

    def test_get_tierces_two_tierces_no_trumps(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':2,'value':11},
        {'rank':0,'value':8},{'rank':2,'value':12},
        {'rank':0,'value':9},{'rank':0,'value':13},
        {'rank':2,'value':10},{'rank':0,'value':14}
        ]
        player.get_hand(hand)
        player.build_histogram()

        expected_result = []
        result = player.get_tierces([])
        self.assertEqual(result, expected_result)

    def test_get_belote(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':2,'value':11},
        {'rank':0,'value':8},{'rank':0,'value':12},
        {'rank':0,'value':9},{'rank':0,'value':13},
        {'rank':2,'value':10},{'rank':0,'value':14}
        ]
        player.get_hand(hand)

        expected_result = [('belote', 0)]
        result = player.get_belotes([0])
        self.assertEqual(result, expected_result)

    def test_get_belote_all_trumps(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':2,'value':11},
        {'rank':0,'value':8},{'rank':0,'value':12},
        {'rank':0,'value':9},{'rank':0,'value':13},
        {'rank':2,'value':10},{'rank':0,'value':14}
        ]
        player.get_hand(hand)

        expected_result = [('belote', 0)]
        result = player.get_belote([0])
        self.assertEqual(result, expected_result)

    def test_get_belote_all_trumps(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':7},{'rank':2,'value':12},
        {'rank':0,'value':8},{'rank':0,'value':12},
        {'rank':0,'value':9},{'rank':0,'value':13},
        {'rank':2,'value':13},{'rank':0,'value':14}
        ]
        player.get_hand(hand)

        expected_result = [('belote', 0),('belote', 2)]
        result = player.get_belotes([0,1,2,3])
        self.assertEqual(result, expected_result)
    
    def test_get_belote_no_trumps(self):
        player = Player(name = 'az', team = 'one')
        hand = [
        {'rank':0,'value':9},{'rank':2,'value':12},
        {'rank':0,'value':7},{'rank':0,'value':12},
        {'rank':0,'value':8},{'rank':0,'value':13},
        {'rank':2,'value':11},{'rank':0,'value':14}
        ]
        player.get_hand(hand)

        expected_result = []
        result = player.get_belotes([])
        self.assertEqual(result, expected_result)
    

if __name__ == '__main__':
    unittest.main()