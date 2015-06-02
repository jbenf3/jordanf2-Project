import numpy as np
import matplotlib.pyplot as plt
from players import Player
import pickle

def main():
	"""The main function of this program calls the auxiliary functions deals with displaying statistics for the end of a match."""
	player_one_name = raw_input("Enter the initial server's name: ")
	player_two_name = raw_input("Enter the initial receiver's name: ")
	global player_one
	player_one = Player(player_one_name)
	global player_two
	player_two = Player(player_two_name)

	while True:
		play_set(0)
		play_set(1)
		if player_one.sets == 1 and player_two.sets == 1:
			play_set(2)
		if player_one.sets == 2:
			print player_one.name + " has won!"
			displayStatistics()
			break
		if player_two.sets == 2:
			print player_two.name + " has won!"
			displayStatistics()
			break

def displayStatistics():
	"""Displays statistics of first serve percentage and second serve percentage for each player from the match."""
	f = plt.figure()
	plt.subplot(2,2,1)
	p1_fsp_dist = np.divide(np.cumsum(player_one.fsi), np.cumsum(player_one.tfs))*100
	p1_fs_pts = np.array([i for i in range(len(p1_fsp_dist))])
	plt.plot(p1_fs_pts, p1_fsp_dist)
	plt.ylabel("$First Serve Percentage$", fontsize=10)
	plt.title("First Serve Percentage for " + player_one.name + ": " + str(round(np.sum(player_one.fsi)/np.sum(player_one.tfs), 4)*100) + "%", fontsize=10)
	
	plt.subplot(2,2,2)
	p2_fsp_dist = np.divide(np.cumsum(player_two.fsi), np.cumsum(player_two.tfs))*100
	p2_fs_pts = np.array([i for i in range(len(p2_fsp_dist))])
	plt.plot(p2_fs_pts, p2_fsp_dist)
	plt.title("First Serve Percentage for " + player_two.name + ": " + str(round(np.sum(player_two.fsi)/np.sum(player_two.tfs), 4)*100) + "%", fontsize=10)
	
	plt.subplot(2,2,3)
	p1_ssp_dist = np.divide(np.cumsum(player_one.ssi), np.cumsum(player_one.tss))*100
	p1_ss_pts = np.array([i for i in range(len(p1_ssp_dist))])
	plt.plot(p1_ss_pts, p1_ssp_dist)
	plt.ylabel("$Second Serve Percentage$", fontsize=10)
	plt.title("Second Serve Percentage for " + player_one.name + ": " + str(round(np.sum(player_one.ssi)/np.sum(player_one.tss), 4)*100) + "%", fontsize=10)
	
	plt.subplot(2,2,4)
	p2_ssp_dist = np.divide(np.cumsum(player_two.ssi), np.cumsum(player_two.tss))*100
	p2_ss_pts = np.array([i for i in range(len(p2_ssp_dist))])
	plt.plot(p2_ss_pts, p2_ssp_dist)
	plt.title("Second Serve Percentage for " + player_two.name + ": " + str(round(np.sum(player_two.ssi)/np.sum(player_two.tss), 4)*100) + "%", fontsize=10)
	
	g = plt.figure()
	plt.annotate(player_one.name + ": winners: " + str(player_one.win) + "; errors: " + str(player_one.err), xy = (0.2,0.8))
	plt.annotate(player_two.name + ": winners: " + str(player_two.win) + "; errors: " + str(player_two.err), xy = (0.2,0.4))

	outFile = open("match-stats.jpg", "w")	
	pickle.dump(f, outFile)
	plt.show()


def play_set(sets_played):
	"""The algorithm for playing a set. If one of the players reaches 6 games, the loop stops."""
	while True:
		print "Current server: " + player_one.name
		play_even_game(sets_played)
		if (player_one.games == 6 and player_two.games < 6):
			print "New set!"
			player_one.sets += 1
			if sets_played == 0:
				player_one.set_1 = player_one.games
				player_two.set_1 = player_two.games
			elif sets_played == 1:
				player_one.set_2 = player_one.games
				player_two.set_2 = player_two.games
			elif sets_played == 2:
				player_one.set_3 = player_one.games
				player_two.set_3 = player_two.games
			player_one.games, player_two.games = 0, 0
			break
		elif (player_two.games == 6 and player_one.games < 6):
			player_two.sets += 1	
			if sets_played == 0:
				player_one.set_1 = player_one.games
				player_two.set_1 = player_two.games
			elif sets_played == 1:
				player_one.set_2 = player_one.games
				player_two.set_2 = player_two.games
			elif sets_played == 2:
				player_one.set_3 = player_one.games
				player_two.set_3 = player_two.games
			player_one.games, player_two.games = 0, 0
			break
		print "Current server: " + player_two.name
		play_odd_game(sets_played)
		if player_one.games == 6 and player_two.games < 6:
			print "New set!"
			player_one.sets += 1
			if sets_played == 0:
				player_one.set_1 = player_one.games
				player_two.set_1 = player_two.games
			elif sets_played == 1:
				player_one.set_2 = player_one.games
				player_two.set_2 = player_two.games
			elif sets_played == 2:
				player_one.set_3 = player_one.games
				player_two.set_3 = player_two.games
			player_one.games, player_two.games = 0, 0
			break
		elif player_two.games == 6 and player_one.games < 6:
			player_two.sets += 1	
			if sets_played == 0:
				player_one.set_1 = player_one.games
				player_two.set_1 = player_two.games
			elif sets_played == 1:
				player_one.set_2 = player_one.games
				player_two.set_2 = player_two.games
			elif sets_played == 2:
				player_one.set_3 = player_one.games
				player_two.set_3 = player_two.games
			player_one.games, player_two.games = 0, 0
			break
		
def play_even_game(sets_played):
	"""The algorithm for playing a game with player one serving."""
	while True:
		print_even_score(sets_played)
		play_even_point()
		if player_one.pts == 4 and player_two.pts < 4:
			player_one.games += 1
			player_one.pts, player_two.pts = 0, 0
			return
		elif player_two.pts == 4 and player_one.pts < 4:
			player_two.games += 1
			player_one.pts, player_two.pts = 0, 0
			return

def play_odd_game(sets_played):
	"""The algorithm for playing a game with player two serving."""
	while True:
		print_odd_score(sets_played)
		play_odd_point()
		if player_one.pts == 4 and player_two.pts < 4:
			player_one.games += 1
			player_one.pts, player_two.pts = 0, 0
			return
		elif player_two.pts == 4 and player_one.pts < 4:
			player_two.games += 1
			player_one.pts, player_two.pts = 0, 0
			return


def play_even_point():
	"""The algorithm for playing a point with player one serving."""
	serve_result = serve_menu()
	if serve_result.lower().startswith('f'):
		player_one.tfs = np.append(player_one.tfs, [1])
		player_one.fsi = np.append(player_one.fsi, [1])
	elif serve_result.lower().startswith('s'):
		player_one.tfs = np.append(player_one.tfs, [1])
		player_one.fsi = np.append(player_one.fsi, [0])
		player_one.tss = np.append(player_one.tss, [1])
		player_one.ssi = np.append(player_one.ssi, [1])
	elif serve_result.lower().startswith('d'):
		player_one.tfs = np.append(player_one.tfs, [1])
		player_one.fsi = np.append(player_one.fsi, [0])
		player_one.tss = np.append(player_one.tss, [1])
		player_one.ssi = np.append(player_one.ssi, [0])
		player_one.df += 1
		player_two.pts += 1
		player_two.tpts += 1
		return		
	elif serve_result.lower().startswith('a'):
		player_one.tfs = np.append(player_one.tfs, [1])
		player_one.fsi = np.append(player_one.fsi, [1])
		player_one.win += 1
		player_one.pts += 1
		player_one.tpts += 1
		return
	point_winner, point_result = point_menu()
	if point_winner.lower().startswith('s') and point_result.lower().startswith('w'):
		player_one.win += 1
		player_one.pts += 1
		player_one.tpts += 1
	elif point_winner.lower().startswith('s') and point_result.lower().startswith('e'):
		player_one.pts += 1
		player_two.err += 1
		player_one.tpts += 1
	elif point_winner.lower().startswith('r') and point_result.lower().startswith('w'):
		player_two.pts += 1
		player_two.win += 1
		player_two.tpts += 1
	elif point_winner.lower().startswith('r') and point_result.lower().startswith('e'):
		player_two.pts += 1
		player_one.err += 1
		player_two.tpts += 1

def play_odd_point():
	"""The algorithm for playing a point with player two serving."""
	serve_result = serve_menu()
	if serve_result.lower().startswith('f'):
		player_two.tfs = np.append(player_two.tfs, [1])
		player_two.fsi = np.append(player_two.fsi, [1])
	elif serve_result.lower().startswith('s'):
		player_two.tfs = np.append(player_two.tfs, [1])
		player_two.fsi = np.append(player_two.fsi, [0])
		player_two.tss = np.append(player_two.tss, [1])
		player_two.ssi = np.append(player_two.ssi, [1])
	elif serve_result.lower().startswith('d'):
		player_two.tfs = np.append(player_two.tfs, [1])
		player_two.fsi = np.append(player_two.fsi, [0])
		player_two.tss = np.append(player_two.tss, [1])
		player_two.ssi = np.append(player_two.ssi, [0])
		player_two.df += 1
		player_one.pts += 1
		player_one.tpts += 1
		return		
	elif serve_result.lower().startswith('a'):
		player_two.tfs = np.append(player_two.tfs, [1])
		player_two.fsi = np.append(player_two.fsi, [1])
		player_two.win += 1
		player_two.pts += 1
		player_two.tpts += 1
		return
	point_winner, point_result = point_menu()
	if point_winner.lower().startswith('s') and point_result.lower().startswith('w'):
		player_two.win += 1
		player_two.pts += 1
		player_two.tpts += 1
	elif point_winner.lower().startswith('s') and point_result.lower().startswith('e'):
		player_two.pts += 1
		player_one.err += 1
		player_two.tpts += 1
	elif point_winner.lower().startswith('r') and point_result.lower().startswith('w'):
		player_one.pts += 1
		player_one.win += 1
		player_one.tpts += 1
	elif point_winner.lower().startswith('r') and point_result.lower().startswith('e'):
		player_one.pts += 1
		player_two.err += 1
		player_one.tpts += 1

def serve_menu():
	return raw_input("Input serve result:(A)ce, (F)irst serve in, (S)econd serve in, (D)ouble fault: ")

def point_menu():
	winner = raw_input("Did (S)erver or (R)eceiver win?: ")
	result = raw_input("Point outcome: (W)inner or (E)rror?: ")
	return winner, result

def print_even_score(sets_played):
	"""Prints the score of the match, including the scores of previously played sets."""
	server_score = 0
	receiver_score = 0
	score = ""
	if player_one.pts == 1:
		server_score = 15
	elif player_one.pts == 2:
		server_score = 30
	elif player_one.pts == 3:
		server_score = 40
	if player_two.pts == 1:
		receiver_score = 15
	elif player_two.pts == 2:
		receiver_score = 30
	elif player_two.pts == 3:	
		receiver_score = 40	
	if sets_played == 1:
		score += (str(player_one.set_1) + "-" + str(player_two.set_1) + " ")
	elif sets_played == 2:
		score += (str(player_one.set_1) + "-" + str(player_two.set_1) + " " + str(player_one.set_2) + "-" + str(player_two.set_2) + " ")
	score += str(player_one.games) + "-" + str(player_two.games) + " " + str(server_score) + "-" + str(receiver_score)
	print score

def print_odd_score(sets_played):
	"""Prints the score of the match, including the scores of previously played sets."""
	server_score = 0
	receiver_score = 0
	score = ""
	if player_two.pts == 1:
		server_score = 15
	elif player_two.pts == 2:
		server_score = 30
	elif player_two.pts == 3:
		server_score = 40
	if player_one.pts == 1:
		receiver_score = 15
	elif player_one.pts == 2:
		receiver_score = 30
	elif player_one.pts == 3:	
		receiver_score = 40
	if sets_played == 1:
		score += (str(player_two.set_1) + "-" + str(player_one.set_1) + " ")
	elif sets_played == 2:
		score += (str(player_two.set_1) + "-" + str(player_one.set_1) + " " + str(player_two.set_2) + "-" + str(player_one.set_2) + " ")
	score += (str(player_two.games) + "-" + str(player_one.games) + " " + str(server_score) + "-" + str(receiver_score))
	print score

main()
