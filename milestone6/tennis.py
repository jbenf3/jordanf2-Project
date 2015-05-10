#!/usr/bin/python

import numpy as np
import matplotlib as plt
from Tkinter import *
import re


"""This is a program that allows the user to input point-by-point
information about a tennis match and throughout the match will compile
statistics about first serve percentage, second serve percentage, winners,
errors, and points won to be displayed at the end of the match."""

class Player:

    """The Player class is a class of objects that represents a tennis
    player, which consists of a set of statistics including the number of
    points won, first serve percentage, second serve percentage, errors,
    winners, and name. """

    def __init__(self, name,  points = np.array([]), tfs = np.array([]), fsi = np.array([]), tss = np.array([]), ssi = np.array([]), errors = np.array([]), winners = np.array([])):
        self.pts = points
        self.tfs = tfs
        self.fsi = fsi
        self.tss = tss
        self.ssi = ssi
        self.err = errors
        self.win = winners
        self.name = name

    def disp_name(self):
        """Prints the name of the player. """
        print "Player name is: " + self.name

    def fsi(self):
        """Increments the number of first serves in and total first serves by one. """

    def ssi(self):
        """Increments the number of second serves in and total second serves by one. """

    def fsp(self):
        """Returns the first serve percentage. """
        return (float(fsi)/float(tfs))*100 + "%"

    def ssp(self):
        """Returns the second serve percentage. """
        return (float(ssi)/float(tss))*100 + "%"

    def get_score(self):
        """Returns the score of the player (in total number of points). """
        return self.pts

def main():
    """Calls all of the auxiliary functions and declares the player objects. """
    print_welcome()
    player_1_name = raw_input("Enter player 1 name: ")
    player_2_name = raw_input("Enter player 2 name: ")
    player_1 = Player(player_1_name)
    player_2 = Player(player_2_name)
    play_point(player_1, player_2)
    print player_1.get_score()
    playMatch(player_1, player_2)
    
def print_welcome():
    """Prints the welcome message at the beginning of the program. """
    print "Tennis Match:"
    print "The format will be a six game set with no-ad scoring"
    print "and a 9-point tiebreaker at 5 games all."

def playMatch(player_1, player_2):
    """Executes the match play and finishes when one of the players has
    reached 24 points. """
    while (player_1.pts != 24) or (player_2.pts != 24):
        play_point(player_1, player_2)

def play_point(player_1, player_2):
    """Simulates one point by asking the user for the outcome of the point
    (which player won the point) and then prompts the user for how the
    point ended (winner or error and by whom). Then this function alters
    the information stored in the player objects for both players."""
    point_outcome = raw_input("Outcome of the point: winner or error? ")
    if point_outcome == "winner" or re.search("w\w+|W\w+", point_outcome):
        point_winner = raw_input("Who won? (1 or 2): ")
        if point_winner == 1:
	    np.append(player_1.pts, [1], axis=0)
	    #player_1.winners.append(1)
	    #player_1.errors.append(0)
	    #player_2.pts.append(0)
	    #player_2.winners.append(0)
	    #player_2.errors.append(0)
	#else:
	    #player_2.pts.append(1)
	    #player_2.winners.append(1)
	    #player_2.errors.append(0)
	    #player_1.pts.append(0)
	    #player_1.winners.append(0)
	    #player_1.errors.append(0)
    #elif point_outcome == "error" or re.search("e\w+|E\+", point_outcome):
	#point_winner = raw_input("Who won? (1 or 2): ")
	#if point_winner == 1:
 	    #player_1.points.append(1)
	    #player_1.errors.append(0)
	    #player_1.winners.append(0)
	    #player_2.errors.append(1)
	    #player_2.points.append(0)
	    #player_2.winners.append(0)
	#else:
	    #player_2.points.append(1)
	    #player_2.winners.append(0)
	    #player_2.errors.append(0)
	    #player_1.points.append(0)
	    #player_1.errors.append(1)
	    #player_1.winners.append(0)	
	      
    #print "One point played."
    # yet to be written, but this will prompt the user for the outcome of
    # the point (which player won the point) and then prompt the user for
    # how the point ended (winner or error and by whom). then it will
    # alter the information stored in the player objects for player 1 and
    # player 2.

main()
# throughout the program, keep track of statistics in the following
# variables:
# 1) first_serve_percentage
# 2) second_serve_percentage
# 3) unforced_errors
# 4) winners
# 5) points_won (each player)


# at the end of the program, the user will be asked if he or she wants a
# visual display of the data that has been collected throughout the
# duration of the program

# the visual information will be shown in the form of graphs of various
# types made with numpy and scipy
