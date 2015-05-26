import numpy as np
import matplotlib.pyplot as plt
from players import Player

def main():
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
			print "Statistics for " + player_one.name + ":"
			print "Winners: " + str(player_one.win)
			print "Errors: " + str(player_one.err)
			print player_one.tfs
			print  player_one.tss
			break
		if player_two.sets == 2:
			print player_two.name + " has won!"
			break

def play_set(sets_played):
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
		print "Current server: " + player_two.name
def play_even_game(sets_played):
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
	serve_result = serve_menu()
	if serve_result.lower().startswith('f'):
		player_one.tfs = np.append(player_one.tfs, [1])
		player_one.fsi = np.append(player_one.fsi, [1])
		player_one.tss = np.append(player_one.tss, [0])
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
		return		
	elif serve_result.lower().startswith('a'):
		player_one.tfs = np.append(player_one.tfs, [1])
		player_one.fsi = np.append(player_one.fsi, [1])
		player_one.tss = np.append(player_one.tss, [0])
		player_one.win += 1
		player_one.pts += 1
		return
	point_winner, point_result = point_menu()
	if point_winner.lower().startswith('s') and point_result.lower().startswith('w'):
		player_one.win += 1
		player_one.pts += 1
	elif point_winner.lower().startswith('s') and point_result.lower().startswith('e'):
		player_one.pts += 1
		player_two.err += 1
	elif point_winner.lower().startswith('r') and point_result.lower().startswith('w'):
		player_two.pts += 1
		player_two.win += 1
	elif point_winner.lower().startswith('r') and point_result.lower().startswith('e'):
		player_two.pts += 1
		player_one.err += 1

def play_odd_point():
	serve_result = serve_menu()
	if serve_result.lower().startswith('f'):
		player_two.tfs = np.append(player_two.tfs, [1])
		player_two.fsi = np.append(player_two.fsi, [1])
		player_two.tss = np.append(player_two.tss, [0])
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
		return		
	elif serve_result.lower().startswith('a'):
		player_two.tfs = np.append(player_two.tfs, [1])
		player_two.fsi = np.append(player_two.fsi, [1])
		player_two.tss = np.append(player_two.tss, [0])
		player_two.win += 1
		player_two.pts += 1
		return
	point_winner, point_result = point_menu()
	if point_winner.lower().startswith('s') and point_result.lower().startswith('w'):
		player_two.win += 1
		player_two.pts += 1
	elif point_winner.lower().startswith('s') and point_result.lower().startswith('e'):
		player_two.pts += 1
		player_one.err += 1
	elif point_winner.lower().startswith('r') and point_result.lower().startswith('w'):
		player_one.pts += 1
		player_one.win += 1
	elif point_winner.lower().startswith('r') and point_result.lower().startswith('e'):
		player_one.pts += 1
		player_two.err += 1

def serve_menu():
	return raw_input("Input serve result:(A)ce, (F)irst serve in, (S)econd serve in, (D)ouble fault: ")

def point_menu():
	winner = raw_input("Did (S)erver or (R)eceiver win?: ")
	result = raw_input("Point outcome: (W)inner or (E)rror?: ")
	return winner, result

def print_even_score(sets_played):
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
