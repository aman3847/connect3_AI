# Name: Aman Gupta
# ID: 2014B2A70201P

import gui

def terminalTest(state,checkEndedFlag=False):
	'''Checks whether the current state is a terminal state or not'''
	ended = False
	ended = checkRowWise(state.board,checkEndedFlag)
	if(ended is True):
		return True
	else:
		ended = checkColumnWise(state.board,checkEndedFlag)
		if(ended is True):
			return True
		else:
			ended = checkDiagonalWise(state.board,checkEndedFlag)
			if(ended is True):
				return True
			else:
				ended = checkNoMovesLeft(state.board)
				if(ended is True):
					return True
				else:
					return False

def checkRowWise(board,checkEndedFlag):
	'''Checks for 3 consecutive coins of the same type in a Row'''
	for i in range(4):
		if(board[i][1] != 0 and (board[i][0] == board[i][1] == board[i][2])):
			if(checkEndedFlag):
				setXY(i,0,i,1,i,2,"Horizontal 3 ")
			return True
		elif(board[i][1] != 0 and (board[i][1] == board[i][2] == board[i][3])):
			if(checkEndedFlag):
				setXY(i,1,i,2,i,3,"Horizontal 3 ")
			return True

def checkColumnWise(board,checkEndedFlag):
	'''Checks for 3 consecutive coins of the same type in a Column'''
	for j in range(4):
		if(board[1][j] != 0 and (board[0][j] == board[1][j] == board[2][j])):
			if(checkEndedFlag):
				setXY(0,j,1,j,2,j,"Vertical 3 ")
			return True
		elif(board[1][j] != 0 and (board[1][j] == board[2][j] == board[3][j])):
			if(checkEndedFlag):
				setXY(1,j,2,j,3,j,"Vertical 3 ")
			return True

def checkDiagonalWise(board,checkEndedFlag):
	'''Checks for 3 consecutive coins of the same type in a Diagonal'''
	if(board[0][0] != 0 and (board[0][0] == board[1][1] == board[2][2])):
		if(checkEndedFlag):
			setXY(0,0,1,1,2,2,"Diagonal 3 ")
		return True
	elif(board[0][1] != 0 and (board[0][1] == board[1][2] == board[2][3])):
		if(checkEndedFlag):
			setXY(0,1,1,2,2,3,"Diagonal 3 ")
		return True
	elif(board[0][2] != 0 and (board[0][2] == board[1][1] == board[2][0])):
		if(checkEndedFlag):
			setXY(0,2,1,1,2,0,"Diagonal 3 ")
		return True
	elif(board[0][3] != 0 and (board[0][3] == board[1][2] == board[2][1])):
		if(checkEndedFlag):
			setXY(0,3,1,2,2,1,"Diagonal 3 ")
		return True
	elif(board[1][0] != 0 and (board[1][0] == board[2][1] == board[3][2])):
		if(checkEndedFlag):
			setXY(1,0,2,1,3,2,"Diagonal 3 ")
		return True
	elif(board[1][1] != 0 and (board[1][1] == board[2][2] == board[3][3])):
		if(checkEndedFlag):
			setXY(1,1,2,2,3,3,"Diagonal 3 ")
		return True
	elif(board[1][2] != 0 and (board[1][2] == board[2][1] == board[3][0])):
		if(checkEndedFlag):
			setXY(1,2,2,1,3,0,"Diagonal 3 ")
		return True
	elif(board[1][3] != 0 and (board[1][3] == board[2][2] == board[3][1])):
		if(checkEndedFlag):
			setXY(1,3,2,2,3,1,"Diagonal 3 ")
		return True

def checkNoMovesLeft(board):
	'''Checks whether a coin can be placed on the board or not'''
	for i in range(4):
		for j in range(4):
			if(board[i][j] == 0):
				return False
	return True

def setXY(row1,col1,row2,col2,row3,col3,text):
	'''Sets X and Y coordinates of the coins that form the winning combination to draw the line depicting the winning combination'''
	text = text + "(" + str(row1) + "," + str(col1) + ")," + "(" + str(row2) + "," + str(col2) + ")," + "(" + str(row3) + "," + str(col3) + ")"
	gui.writeText(-185,-285,text)
	initX = 0
	initY = 0
	finalX = 0
	finalY = 0
	if(row1 == 0):
		initY = 150
	elif(row1 == 1):
		initY = 50
	elif(row1 == 2):
		initY = -50
	elif(row1 == 3):
		initY = -150
	if(col1 == 0):
		initX = -150
	elif(col1 == 1):
		initX = -50
	elif(col1 == 2):
		initX = 50
	elif(col1 == 3):
		initX = 150
	if(row3 == 0):
		finalY = 150
	elif(row3 == 1):
		finalY = 50
	elif(row3 == 2):
		finalY = -50
	elif(row3 == 3):
		finalY = -150
	if(col3 == 0):
		finalX = -150
	elif(col3 == 1):
		finalX = -50
	elif(col3 == 2):
		finalX = 50
	elif(col3 == 3):
		finalX = 150
	gui.drawLine(initX,initY,finalX,finalY,winLine=True)