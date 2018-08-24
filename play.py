import sys
from six import string_types
import numpy as np

# a class containing all possible board states
class BoardState:
	NOUGHTS_WIN = 'NOUGHTS_WIN'
	CROSSES_WIN = 'CROSSES_WIN'
	DRAW = 'DRAW'
	CROSSES_TURN = 'CROSSES_TURN'
	NOUGHTS_TURN = 'NOUGHTS_TURN'
	INVALID_BOARD = 'INVALID_BOARD'
	
def play():
	"""
	Function that allows two users to play a game of noughts and croses.
	
	Crosses go first.
		
	the list adjascen to the board shows the number of each position on the board.
	
	Inputs must be of type int to put a nought or cross on the board.
	"""
	board = ['_','_','_','_','_','_','_','_','_']		# create a board
	plus = np.array([	[1, 	False, 	3, 6],			# nparray that will be used to add to the appropriate slots in lines nparray
						[False, False, 	3, 7],			# Falses make the array add to the number of turns in lines nparray, and additionally fill what would otherwise be a jagged array
						[2, 	False, 	3, 8],
						[False,	False, 	4, 6],
						[1, 	2, 		4, 7],
						[False,	False, 	4, 8],
						[2, 	False, 	5, 6],
						[False,	False, 	5, 7],
						[1, 	False, 	5, 8]	])
						
	lines = np.zeros ((2,9))							# nparray that will be used to store the number of O's and X's along each possible winning line
														# 0 = number of turns, 1 = diagonal from top left to bottom right, 2 = diagonal from top right to bottom left, 3-5 = colums 1-3, 6-8  = rows 1-3
	
	print ('',board[:3],[0,1,2],'\n',board[3:6],[3,4,5],'\n',board[6:],[6,7,8])		# print the board and how to place a tile in each slot to console 
	
	for i in range(9):																# 9 turns
		
		while True:																	# ask the user for an input, ensure it is valid, if it is not ask again informing them of how to 
			try :
				if i%2 ==0:
					num = int(input('Crosses\' turn: '))
				else:
					num = int(input('Noughts\' turn: '))
				if not 0 <= num < 9:
					print(' That is not on the board \n Please enter an integer 0-8 inclusive')
				elif board[num] != '_':
					print(' Space already taken\n Please choose a different space')
				else:
					break	
			except ValueError:
				print(' That input type doesn\'t work\n Please enter an integer 0-8 inclusive, in digits')
					
		if i%2 == 0:																		# check if it's crosses' turn
		
			board[num] = 'X'																# put a cross in the board
			lines[0,plus[num,:]] += 1														# add one to the appropriate lines for crosses
			print ('',board[:3],[0,1,2],'\n',board[3:6],[3,4,5],'\n',board[6:],[6,7,8])		# reprint the board and guide
			if np.any(lines[0,1:] == 3 ):													# check if crosses win
				return BoardState.CROSSES_WIN
				
				
		else:																				# check if it's noughts' turn
						
			board[num] = 'O'																# put a nought in the board
			lines[1,plus[num,:]] += 1														# add one to the appropriate lines for noughts
			print ('',board[:3],[0,1,2],'\n',board[3:6],[3,4,5],'\n',board[6:],[6,7,8])		# reprint the board and guide
			if np.any(lines[1,1:] == 3 ):													# check if noughts win
				return BoardState.NOUGHTS_WIN
	
	return BoardState.DRAW
	
print (play())	# call play() and print out it's boardstate
