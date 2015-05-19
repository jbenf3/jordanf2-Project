#!/usr/bin/python

import numpy as np
import matplotlib as plt

class Player:

    """The Player class is a class of objects that represents a tennis
    player, which consists of a set of statistics including the number of
    points won, first serve percentage, second serve percentage, errors,
    winners, and name. """

    def __init__(self, name, points = 0, tfs = np.array([]), fsi = np.array([]), tss = np.array([]), ssi = np.array([]), errors = np.array([]), winners = np.array([]), games = 0):
        self.pts = points
        self.games = games
	self.tfs = tfs
        self.fsi = fsi
        self.tss = tss
        self.ssi = ssi
        self.err = errors
        self.win = winners
	self.name = name
  
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
