import sys
from six import string_types
import numpy as np
# complete this enum with all the possible states of a noughts and crosses board (there's more than 3)
class BoardState:
	NOUGHTS_WIN = 'NOUGHTS_WIN'
	CROSSES_WIN = 'CROSSES_WIN'
	DRAW = 'DRAW'
	CROSSES_TURN = 'CROSSES_TURN'
	NOUGHTS_TURN = 'NOUGHTS_TURN'
	INVALID_BOARD = 'INVALID_BOARD'
# complete this function so that it returns the correct board state


def getStateOfBoard(board):
	"""
	This function returns the state of any noughts and crosses board.
	
	The board must be written as a string that is 9 characters long consisting of only _'s, uppercase X's and O's, 
	aditionally there must be an appropriate proportion of O's and X's so that X's could have gone first.
	
	If one or more of these constraints are not met the Board State will be returned as 'INVALID_BOARD'
	"""
	
	
	lines = np.zeros ((2,9))									# nparray that will be used to store the number of O's and X's along each possible winning line
																# 0 = number of turns, 1 = diagonal from top left to bottom right, 2 = diagonal from top right to bottom left, 3-5 = colums 1-3, 6-8  = rows 1-3
	
	plus = np.array([	[1, 	False, 	3, 6, False],			# nparray that will be used to add to the appropriate slots in lines nparray
						[False, False, 	3, 7, False],			# Falses make the array add to the number of turns in lines nparray, and additionally fill what would otherwise be a jagged array
						[2, 	False, 	3, 8, False],
						[False,	False, 	4, 6, False],
						[1, 	2, 		4, 7, False],
						[False,	False, 	4, 8, False],
						[2, 	False, 	5, 6, False],
						[False,	False, 	5, 7, False],
						[1, 	False, 	5, 8, False]	])
	
	
	if (len(board) != 9):										# only accept boards of the correct length
		return BoardState.INVALID_BOARD
	
	for i in range (9):											# for each O and X add one to the number in each appropriate line
		if board[i] is 'X':	
			lines[0,plus[i,:]] += 1

		elif board[i] is 'O':
			lines[1,plus[i,:]] += 1
						
		elif board[i] is '_':
			continue	
		
		else:													# return the boardstate as invalid if any character in the string is not one of the allowed 3
			return BoardState.INVALID_BOARD
	
	if not ( lines[1,0] <= lines [0,0] <= (lines[1,0]+1) ) or ((np.any(lines[0,1:] == 3 )) and (np.any(lines[1,1:] == 3 ))):	# invalid board if the proportion of O's and X's are wrong
		return BoardState.INVALID_BOARD
			
	elif np.any(lines[0,1:] == 3 ):								# if there is 3 X's in any line crosses win
		return BoardState.CROSSES_WIN
		
	elif np.any(lines[1,1:] == 3 ):								# if there is 3 O's in any line noughts win
		return BoardState.NOUGHTS_WIN	
	
	elif lines[0,0] + lines[1,0] == 9:							# if there are 9 O's and X's on the board it's a draw
		return BoardState.DRAW			
		
	elif lines[0,0] == lines[1,0]:								# if there are equal number of O's and X's then it's crosses turn
		return BoardState.CROSSES_TURN
		
	elif lines[0,0] == lines[1,0] + 1:							# if there are unequal number of O's and X's then it's noughts turn
		return BoardState.NOUGHTS_TURN

# leave this part unchanged
for arg in sys.argv[1:]:
	print(getStateOfBoard(arg))

