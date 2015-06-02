import numpy as np
import matplotlib as plt

class Player:

    	"""The Player class is a class of objects that represents a tennis player, which consists of a set of statistics 
	including the number of points won, first serve percentage, second serve percentage, errors, winners, name, 
	games won, and sets won. """

	def __init__(self, name, points = 0, games = 0, sets = 0, set_1 = 0, set_2 = 0, set_3 = 0, df = 0, tpts = 0, tfs = np.array([]), fsi = np.array([]), tss = np.array([]), ssi = np.array([]), errors = 0, winners = 0):
		self.pts = points
        	self.games = games
		self.sets = sets
		self.tpts = tpts
		self.tfs = tfs
        	self.fsi = fsi
        	self.tss = tss
        	self.ssi = ssi
        	self.err = errors
        	self.win = winners
		self.name = name
		self.df = df
		self.set_1 = set_1
		self.set_2 = set_2
		self.set_3 = set_3
