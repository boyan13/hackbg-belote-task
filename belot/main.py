from belote import Card, Deck, Player, Team, Round, Game, Score

def main():
	team1Name = input("Team1 name: ")
	team2Name = input("Team2 name: ")
	player1A = input("Team1 players: ")
	player2A = input()
	player1B = input ("Team2 players: ")
	player2B = input()

	team1 = Team(team1Name, player1A, player2A)
	team2 = Team(team2Name, player1B, player2B)

	game = Game(team1, team2)

	# ENDLESS LOOP because play_round is not fully implemented
	# while(game.next_round()):
	# 	game.play_round()

if __name__ == '__main__':
	main()