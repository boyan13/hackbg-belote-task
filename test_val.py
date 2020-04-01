import unittest
from Game import Belote
from Player import Player

class TestBelote(unittest.TestCase):
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
        
        result = belote.filal_announcements(teams, hist)
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
    
if __name__ == '__main__':
    unittest.main()