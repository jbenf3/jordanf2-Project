#!/usr/bin/python

import numpy as np

"""This is a program that allows the user to input point-by-point
information about a tennis match and throughout the match will compile
statistics about first serve percentage, second serve percentage, winners,
errors, and points won to be displayed at the end of the match."""

class Player:

    """The Player class is a class of objects that represents a tennis
    player, which consists of a set of statistics including the number of
    points won, first serve percentage, second serve percentage, errors,
    winners, and name. """

    def __init__(self, points, tfs, fsi, tss, ssi, errors, winners, name):
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

    def fsi(self, fsi):
        """Increments the number of first serves in and total first serves by one. """
        self.fsi += 1
        self.tfs += 1
        
    def ssi(self, ssi):
        """Increments the number of second serves in and total second serves by one. """
        self.ssi += 1
        self.tss += 1

    def fsp(self, tfs, fsi):
        """Returns the first serve percentage. """
        return (float(fsi)/float(tfs))*100 + "%"

    def ssp(self, tss, ssi):
        """Returns the second serve percentage. """
        return (float(ssi)/float(tss))*100 + "%"

    def increment_score(self, points):
        self.points += 1

    def increment_winners(self, winners):
        self.win += 1

    def get_score(self, points):
        """Returns the score of the player (in total number of points). """
        return self.pts


def main():
    """Calls all of the auxiliary functions and declares the player objects. """
    print_welcome()
    player_1_name = raw_input("Enter player 1 name: ")
    player_2_name = raw_input("Enter player 2 name: ")
    player_1 = Player(0, 0, 0, 0, 0, 0, 0, player_1_name)
    player_2 = Player(0, 0, 0, 0, 0, 0, 0, player_2_name)
    player_1.disp_name()
    player_2.disp_name()
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
        playPoint(player_1, player_2)

def playPoint(player_1, player_2):
    """Simulates one point by asking the user for the outcome of the point
    (which player won the point) and then prompts the user for how the
    point ended (winner or error and by whom). Then this function alters
    the information stored in the player objects for both players."""
    point_outcome = raw_input("Outcome of the point: winner or  error")
    if point_outcome == "winner":
        point_winner = raw_input("Who won? (1 or 2): ")
        if point_winner == 1:
            player_1.increment_points
            player_1.increment_winners
        else:
            player_2.points.increment_points
            player_2.winners.increment_winners
            
    print "One point played."
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
