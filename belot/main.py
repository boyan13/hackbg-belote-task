from belote import Card, Deck, Player, Team, Round, Game, Score

def main():
	# Extract data from user to initialize Player and Team objects
	team1name = input("Team 1 name: ")
	team1player1 = input("Player 1 and 2:")
	team1player2 = input()
	team2name = input("Team 2 name: ")
	team2player1 = input("Player 1 and 2:")
	team2player2 = input()
	team1 = Team(team1name, team1player1, team1player2)
	team2 = Team(team2name, team2player1, team2player2)

	game = Game(team1, team2)

	# ENDLESS LOOP because play_round is not fully implemented
	while(!game.winner()):
		game.play_round() # Team rearrangement happens automatically


if __name__ == '__main__':
	main()