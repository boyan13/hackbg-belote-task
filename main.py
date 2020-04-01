from Game import Belote
from Player import Player

def main():
    player1 = Player("Boyan", "Team1")
    player2 = Player("Silvia", "Team1")
    player3 = Player("Freeman", "Team2")
    player4 = Player("Marto", "Team2")

    players = [[player1, player2], [player3, player4]]
    belote = Belote(players)

    belote.play()

if __name__ == '__main__':
    main()
