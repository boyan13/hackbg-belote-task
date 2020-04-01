import unittest
from Game import Belote
from Player import Player

class test_Game(unittest.TestCase):
    
    def test_init(self):
        e = None
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Marto", "Team2")
        player4 = Player("Gosho", "Team2")
        players = [[player1, player2], [player3, player4]]

        try:
            belote = Belote(players)
        except Exception as exc:
            e = exc 

        self.assertIsNone(e)
        self.assertEqual(belote.__dict__["players"][0], player1)
        self.assertEqual(belote.__dict__["players"][1], player3)
        self.assertEqual(belote.__dict__["players"][2], player2)
        self.assertEqual(belote.__dict__["players"][3], player4)
        self.assertEqual(belote.__dict__["score"]["Team1"], 0)
        self.assertEqual(belote.__dict__["score"]["Team2"], 0)
        self.assertEqual(belote.__dict__["order"], [0, 1, 2 ,3])

        self.assertEqual(belote.__dict__["game"], "")
        self.assertEqual(belote.__dict__["rounds"], [])
        self.assertEqual(belote.__dict__["contracts"], [])
        self.assertEqual(belote.__dict__["cards"], [])
        self.assertEqual(belote.__dict__["announcements"], [])
        self.assertEqual(belote.__dict__["points"], [])

    def test_init_dunder_with_same_team_in_both_team_lists(self):
        e = None
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Marto", "Team1")
        player4 = Player("Gosho", "Team1")
        players = [[player1, player2], [player3, player4]]

        try:
            g = Belote(players)
        except ValueError as exc:
            e = exc 

        self.assertIsNotNone(e)
        self.assertEqual(str(e), "Member of one team is already part of the other!")

    def test_init_dunder_with_a_player_belonging_to_a_third_team(self):
        e = None
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Marto", "Team2")
        player4 = Player("Gosho", "Team3")
        players = [[player1, player2], [player3, player4]]

        try:
            g = Belote(players)
        except ValueError as exc:
            e = exc 

        self.assertIsNotNone(e)
        self.assertEqual(str(e), "Members of different teams put in one team!")

    def test_init_dunder_with_duplicating_player(self):
        e = None
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Marto", "Team2")
        player4 = Player("Marto", "Team2")
        players = [[player1, player2], [player3, player4]]

        try:
            g = Belote(players)
        except ValueError as exc:
            e = exc 

        self.assertIsNotNone(e)
        self.assertEqual(str(e), "Duplicating players!")

    def test_init_dunder_with_fractured_teams(self):
        e1 = None
        e2 = None
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Marto", "Team2")
        player4 = Player("Gosho", "Team2")
        players1 = [[player1, player2], [player3]]
        players2 = [player1], [player3, player4]

        try:
            g = Belote(players1)
        except ValueError as exc:
            e1 = exc 
        try:
            g = Belote(players1)
        except ValueError as exc:
            e2 = exc 

        self.assertIsNotNone(e1)
        self.assertIsNotNone(e2)
        self.assertEqual(str(e1), "Too few members in a team.")
        self.assertEqual(str(e2), "Too few members in a team.")

    def test_init_dunder_with_fractured_list(self):
        e = None
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")

        players = [[player1, player2]]

        try:
            g = Belote(players)
        except ValueError as exc:
            e = exc 

        self.assertIsNotNone(e)
        self.assertEqual(str(e), "Only one team.")

    def test_init_dunder_with_bloated_teams(self):
        e1 = None
        e2 = None
        e3 = None
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Freeman", "Team1")
        player4 = Player("Marto", "Team2")
        player5 = Player("Gosho", "Team2")
        player6 = Player("Breen", "Team2")
        player7 = Player("ALyx", "Team3")
        player8 = Player("Mossman", "Team3")

        players1 = [[player1, player2], [player4, player5, player6]]
        players2 = [[player1, player2, player3], [player4, player5]]

        try:
            g = Belote(players1)
        except ValueError as exc:
            e1 = exc 
        try:
            g = Belote(players1)
        except ValueError as exc:
            e2 = exc 

        self.assertIsNotNone(e1)
        self.assertIsNotNone(e2)
        self.assertEqual(str(e1), "Too many members in a team.")
        self.assertEqual(str(e2), "Too many members in a team.")

    def test_init_dunder_with_bloated_list(self):
        e = None
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Freeman", "Team2")
        player4 = Player("Marto", "Team2")
        player5 = Player("Gosho", "Team3")
        player6 = Player("Breen", "Team3")

        players = [[player1, player2], [player3, player4], [player5, player6]]

        try:
            g = Belote(players)
        except ValueError as exc:
            e = exc 
  
        self.assertIsNotNone(e)
        self.assertEqual(str(e), "Too many teams to unpack!")

    def test_init_dunder_with_bad_type(self):
        e1 = None
        e2 = None
        e3 = None

        type1 = tuple()
        type2 = dict()
        type3 = int()

        try:
            g = Belote(type1)
        except TypeError as exc:
            e1 = exc
        try:
            g = Belote(type2)
        except TypeError as exc:
            e2 = exc
        try:
            g = Belote(type3)
        except TypeError as exc:
            e3 = exc

        self.assertIsNotNone(e1)
        self.assertIsNotNone(e2)
        self.assertIsNotNone(e3)
        self.assertEqual(str(e1), "Bad type.")
        self.assertEqual(str(e2), "Bad type.")
        self.assertEqual(str(e3), "Bad type.")

    def test_init_dunder_with_empty_list(self):
        e = None

        try:
            g = Belote([])
        except Exception as exc:
            e = exc

        self.assertIsNotNone(e)
        self.assertEqual(str(e), "Cannot create a game without players!")

    def test_shift_player_order_once(self):
        e = None
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Marto", "Team2")
        player4 = Player("Gosho", "Team2")
        players = [[player1, player2], [player3, player4]]

        try:
            g = Belote(players)
            g.shift_player_order()
        except Exception as exc:
            e = exc 

        self.assertIsNone(e)
        self.assertEqual(g.__dict__["order"], [1, 2, 3, 0])

    def test_shift_player_order_three_times(self):
        e = None
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Marto", "Team2")
        player4 = Player("Gosho", "Team2")
        players = [[player1, player2], [player3, player4]]

        try:
            g = Belote(players)
            g.shift_player_order()
            g.shift_player_order()
            g.shift_player_order()
        except Exception as exc:
            e = exc 

        self.assertIsNone(e)
        self.assertEqual(g.__dict__["order"], [3, 0, 1, 2])

    def test_shift_player_order_four_times(self):
        e = None
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Marto", "Team2")
        player4 = Player("Gosho", "Team2")
        players = [[player1, player2], [player3, player4]]

        try:
            g = Belote(players)
            g.shift_player_order()
            g.shift_player_order()
            g.shift_player_order()
            g.shift_player_order()
        except Exception as exc:
            e = exc 

        self.assertIsNone(e)
        self.assertEqual(g.__dict__["order"], [0, 1, 2, 3])

    def test_pick_first(self):
        e = None
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Marto", "Team2")
        player4 = Player("Gosho", "Team2")
        players = [[player1, player2], [player3, player4]]

        try:
            g = Belote(players)
            g.pick_first_from("Team2")
            first = g.__dict__["order"][0]
            first = g.__dict__["players"][first]
            third = g.__dict__["order"][2]
            third = g.__dict__["players"][third]
        except Exception as exc:
            e = exc

        self.assertIsNone(e)
        self.assertEqual(first.team, "Team2")
        self.assertEqual(third.team, "Team2")

    def test_pick_first_with_nonexistent_team(self):
        e = None
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Marto", "Team2")
        player4 = Player("Gosho", "Team2")
        players = [[player1, player2], [player3, player4]]

        try:
            g = Belote(players)
            g.pick_first_from("Team3")
        except ValueError as exc:
            e = exc

        self.assertIsNotNone(e)
        self.assertEqual(str(e), "Team not found.")

    def test_assign_hands(self):
        e = None
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Marto", "Team2")
        player4 = Player("Gosho", "Team2")
        players = [[player1, player2], [player3, player4]]

        try:
            g = Belote(players)
            g.assign_hands()
        except Exception as exc:
            e = exc

        self.assertIsNone(e)
        self.assertTrue(player1.__dict__["hand"] != [])
        self.assertTrue(player2.__dict__["hand"] != [])
        self.assertTrue(player3.__dict__["hand"] != [])
        self.assertTrue(player4.__dict__["hand"] != [])
        self.assertFalse(any(card in player1.hand for card in player2.hand))
        self.assertFalse(any(card in player1.hand for card in player3.hand))
        self.assertFalse(any(card in player1.hand for card in player4.hand))
        self.assertFalse(any(card in player2.hand for card in player3.hand))
        self.assertFalse(any(card in player3.hand for card in player4.hand))

    def test_teams_announcements(self):
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Freeman", "Team2")
        player4 = Player("Marto", "Team2")

        players = [[player1, player2], [player3, player4]]
        belote = Belote(players)

        annoucement = {player1:[('carre', 15)], player2: [('carre', 16)], player3: [('tierce', 10)], player4: []}
        expected_result = [
        [{0: [('carre', 15)], 3: [('tierce', 10)]}, {0: [('carre', 16)]}],
        [{0: [('carre', 15)]}, {0: [('carre', 16)]}, {3: [('tierce', 10)]}, {}]
        ]
        result= belote.get_teams_announcements(annoucement)
        self.assertEqual(result, expected_result)

    def test_final_announcement(self):
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Freeman", "Team2")
        player4 = Player("Marto", "Team2")

        players = [[player1, player2], [player3, player4]]
        belote = Belote(players)

        teams = [{0: [('carre', 10), ('carre', 12)]},{3:[('tierce', 14)]}]
        hist = [
        {0: [('carre', 10)]},
        {},
        {0: [('carre', 12),('tierce', 9)]},
        {3: [('tierce', 14)]}
        ]
        expected_result = [[('carre', 10)],[],[('carre', 12)],[('tierce', 14)]]

        result = belote.final_announcements(teams, hist)
        self.assertEqual(result, expected_result)


    def test_validate_no_announcements(self):
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Freeman", "Team2")
        player4 = Player("Marto", "Team2")

        players = [[player1, player2], [player3, player4]]
        belote = Belote(players)

        annoucement = {player1:[], player2: [], player3: [], player4: []}
        expected_result = {player1:[], player2: [], player3: [], player4: []}
        result = belote.validate_announcements(annoucement)

    def test_validate_no_announcements_in_team1(self):
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Freeman", "Team2")
        player4 = Player("Marto", "Team2")

        players = [[player1, player2], [player3, player4]]
        belote = Belote(players)

        annoucement = {player1:[], player2: [('carre', 12), ('carre',15)], player3: [], player4: [('carre', 12), ('carre',15)]}
        expected_result = {player1:[], player2: [('carre', 12), ('carre',15)], player3: [], player4: [('carre', 12), ('carre',15)]}
        result = belote.validate_announcements(annoucement)

    def test_validate_no_announcements_in_team2(self):
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Freeman", "Team2")
        player4 = Player("Marto", "Team2")

        players = [[player1, player2], [player3, player4]]
        belote = Belote(players)

        annoucement = {player1:[('carre', 12), ('carre',15)], player2: [], player3: [('carre', 12), ('carre',15)], player4: []}
        expected_result = {player1:[('carre', 12), ('carre',15)], player2: [], player3: [('carre', 12), ('carre',15)], player4: []}
        result = belote.validate_announcements(annoucement)


    def test_validate(self):
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Freeman", "Team2")
        player4 = Player("Marto", "Team2")

        players = [[player1, player2], [player3, player4]]
        belote = Belote(players)

        annoucement = {player1:[('carre', 12), ('carre',15)], player2: [('carre', 16)], player3: [('tierce', 10)], player4: []}
        expected_result = {player1:[], player2: [('carre', 11)], player3: [('carre', 12), ('carre',15)], player4: []}
        result = belote.validate_announcements(annoucement)

    def test__validate(self):
        player1 = Player("Boyan", "Team1")
        player2 = Player("Silvia", "Team1")
        player3 = Player("Freeman", "Team2")
        player4 = Player("Marto", "Team2")

        players = [[player1, player2], [player3, player4]]
        belote = Belote(players)

        annoucement = {player1:[('carre', 12), ('carre',15)], player2: [('carre', 16)], player3: [('tierce', 10)], player4: [('tierce', 11), ('belote', 2)]}
        expected_result = {player1:[], player2: [('carre', 16)], player3: [], player4: [('tierce', 11), ('belote', 2)]}
        belote.get_teams_announcements(annoucement)
        result = belote.validate_announcements(annoucement)
        self.assertEqual(result,expected_result)


    def test_to_txt(self):
        pass 

    def test_to_json(self):
        pass

if __name__ == '__main__':
    unittest.main()