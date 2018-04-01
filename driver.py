# Name: Aman Gupta
# ID: 2014B2A70201P

import minimaxDecision
import alphaBetaSearch
import gui
import terminalTest
import turtle as t
from state import *
from successor import *
import sys
from time import time

# Global Variables Initialized
humanMove = None
newGameFlag = 0
humanMoveFlag = 0
minimaxFlag = 0
alphaBetaFlag = 0
restartFlag = 0
exitFlag = 0
analysisFlag = 0
timeAlphaBeta = 0
timeMinimax = 0
alphaBetaNodes = 0
sizeOfAlphaBetaNode = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0
r7 = 0
r8 = 0
r9 = (0,0)
r10 = 0
r11 = 0
r12 = 0

def checkEnded(state):
	'''Checks whether the game has ended or not. If YES then calls printResult function for printing the result of the game on the canvas'''
	if(terminalTest.terminalTest(state,checkEndedFlag=True)):
		if(terminalTest.checkNoMovesLeft(state.board)):
			gui.printResult(0)
			return True
		else:
			gui.printResult(state.typeOfNode)
			return True
	return False

def findMove(gameState,algo):
	'''Uses algo for the AI as desired by the User'''
	if(algo == 1):
		print "Running Minimax"
		return minimaxDecision.minimaxDecision(gameState)
	elif(algo == 2):
		print "Running Alpha Beta"
		return alphaBetaSearch.alphaBetaSearch(gameState)

def findRow(board,col):
	'''Finds a valid row where coin is to be placed. If not found returns -1'''
	for row in range(3,-1,-1):
		if(board[row][col]!=0):
			return row
	return -1

def setAnalysisRestartExitFlag(x,y):
	'''sets analysisFlag/restartFlag/exitFag based on user input'''
	'''Listener Function for Analysis/Restart/Exit Buttons'''
	global restartFlag
	global exitFlag
	global analysisFlag
	if(x>=-250 and x<=-50 and y>=-540 and y<=-490):
		restartFlag = 1
	elif(x>=50 and x<=250 and y<=-490 and y>=-540):
		exitFlag = 1
	elif(x>=50 and x<=250 and y>=-450 and y<=-400):
		analysisFlag = 1

def setRestartExitFlag(x,y):
	'''sets restartFlag/exitFlag based on user input'''
	'''Listener Function for Restart/Exit Buttons'''
	global restartFlag
	global exitFlag
	if(x>=-250 and x<=-50 and y>=-540 and y<=-490):
		restartFlag = 1
	elif(x>=50 and x<=250 and y<=-490 and y>=-540):
		exitFlag = 1

def setAlgoFlag(x,y):
	'''Sets minimaxFlag/aplhaBetaFlag based on user input'''
	'''Listener Function for Minimax and Alpha-Beta Buttons'''
	global minimaxFlag
	global alphaBetaFlag
	if(x>=50 and x<=250 and y>=-375 and y<=-325):
		minimaxFlag = 1
	elif(x>=-250 and x<=-50 and y>=-450 and y<=-400):
		alphaBetaFlag = 1

def setNewGameFlag(x,y):
	'''Sets newGameFlag'''
	'''Listener Function for New Game Button'''
	global newGameFlag
	if(x>=-250 and x<=-50 and y>=-375 and y<=-325):
		newGameFlag = 1

def setHumanMove(x,y):
	'''Selects the column and assigns it to humanMove'''
	'''Listener Function for humanMove'''
	global humanMove
	global humanMoveFlag
	if(x>-200 and x<-100 and y>=-200 and y<=200):
		humanMove = 0
		humanMoveFlag = 1
	elif(x>-100 and x<0 and y>=-200 and y<=200):
		humanMove = 1	
		humanMoveFlag = 1
	elif(x>0 and x<100 and y>=-200 and y<=200):
		humanMove = 2
		humanMoveFlag = 1
	elif(x>100 and x<200 and y>=-200 and y<=200):
		humanMove = 3
		humanMoveFlag = 1

def playGame(gameState,algo):
	'''Game Play with the algo for AI given as input by the user'''
	while(True):
		global r1
		global r2
		global r3
		global r4
		global r5
		global r6
		global r7
		global r8
		global r9
		global r10
		global r11
		global r12
		global averageTimeAlphaBeta
		global timeMinimax
		global alphaBetaNodes
		global sizeOfAlphaBetaNode
		global timeAlphaBeta
		global analysisFlag
		global restartFlag
		global exitFlag		
		global humanMoveFlag
		global humanMove
		
		# AI's Turn to play the move
		bestMove = findMove(gameState,algo)
		gameState = successor(gameState,bestMove)
		row = findRow(gameState.board,bestMove)
		if(row!=-1):
			gui.placeCoin(row,bestMove,gameState.typeOfNode)
		
		if(checkEnded(gameState)):
			'''If game has ended update data for analysis'''
			if(algo == 1):
				r1 = getNoOfNodes()
				r2 = sys.getsizeof(gameState)
				r3 = 16
				r4 = time() - timeMinimax
				r5 = float(r1)/(r4*1000000)
				r9 = ((r1*r2),(alphaBetaNodes*sizeOfAlphaBetaNode))
				r10 += float(r4)/10
			elif(algo == 2):
				r6 = getNoOfNodes()
				if(r1!=0):
					r7 = float(r1-r6)/r1
				r8 = time() - timeAlphaBeta
				alphaBetaNodes = getNoOfNodes()
				sizeOfAlphaBetaNode = sys.getsizeof(gameState)
				r9 = ((r1*r2),(alphaBetaNodes*sizeOfAlphaBetaNode))
				r10 += float(r8)/10
			r11 += 1
			r12 = float(r11)/20
			
			t.onscreenclick(setAnalysisRestartExitFlag) 
			while(analysisFlag == 0 and exitFlag == 0 and restartFlag == 0):
				# Waits for User to click Analysis Button or Restart Button or Exit Button
				t.update()
			if(analysisFlag == 1):
				# Actions to be taken if Analysis button is clicked
				gui.showAnalysis(R1=r1,R2=r2,R3=r3,R4=r4,R5=r5,R6=r6,R7=r7,R8=r8,R9=r9,R10=r10,R11=r11,R12=r12)
				analysisFlag = 0
			else:
				if(exitFlag == 1):
					# Actions to be taken if EXIT Button was clicked
					exitFlag = 0
					exit()
				elif(restartFlag == 1):
					# Actions to be taken if Restart Button was clicked
					restartFlag = 0
					main()

			t.onscreenclick(setRestartExitFlag)
			while(restartFlag == 0 and exitFlag == 0):
				# Waits for user to click Restart Button or EXIT Button
				t.update()
			if(exitFlag == 1):
				# Actions to be taken if EXIT Button was clicked
				exitFlag = 0
				exit()
			elif(restartFlag == 1):
				# Actions to be taken if Restart Button was clicked
				restartFlag = 0
				main()

		# USER's Turn to Play the move
		while(True):
			while(humanMove is None):
				t.onscreenclick(setHumanMove)
				while(humanMoveFlag == 0):
					# Waits for User to select a column
					t.update()

			humanMoveFlag = 0
			tempState = successor(gameState,humanMove)
			if(tempState is False):
				'''If User selects an invalid column then successor function returns False instead of the Child. This process continues until the User selects a valid column'''
				humanMove = None
				continue
			else:
				decrementNoOfNodes()
				gameState = tempState
				row = findRow(gameState.board,humanMove)
				gui.placeCoin(row,humanMove,gameState.typeOfNode)
				break

		humanMove = None

		if(checkEnded(gameState)):
			'''If game has ended update data for analysis'''
			if(algo == 1):
				r1 = getNoOfNodes()
				r2 = sys.getsizeof(gameState)
				r3 = 16
				r4 = time() - timeMinimax
				r5 = float(r1)/(r4*1000000)
				r9 = ((r1*r2),(alphaBetaNodes*sizeOfAlphaBetaNode))
				r10 += float(r4)/10
			elif(algo == 2):
				r6 = getNoOfNodes()
				if(r1!=0):
					r7 = float(r1-r6)/r1
				r8 = time() - timeAlphaBeta
				alphaBetaNodes = getNoOfNodes()
				sizeOfAlphaBetaNode = sys.getsizeof(gameState)
				r9 = ((r1*r2),(alphaBetaNodes*sizeOfAlphaBetaNode))
				r10 += float(r8)/10
				# r9 = r1/r6
			r11 += 1
			r12 = float(r11)/20

			t.onscreenclick(setAnalysisRestartExitFlag) 
			while(analysisFlag == 0 and exitFlag == 0 and restartFlag == 0):
				# Waits for User to click Analysis Button or Restart Button or Exit Button
				t.update()
			if(analysisFlag == 1):
				# Actions to be taken if Analysis button is clicked
				gui.showAnalysis(R1=r1,R2=r2,R3=r3,R4=r4,R5=r5,R6=r6,R7=r7,R8=r8,R9=r9,R10=r10,R11=r11,R12=r12)
				analysisFlag = 0
			else:
				if(exitFlag == 1):
					# Actions to be taken if EXIT Button was clicked
					exitFlag = 0
					exit()
				elif(restartFlag == 1):
					# Actions to be taken if Restart Button was clicked
					restartFlag = 0
					main()

			t.onscreenclick(setRestartExitFlag)
			while(restartFlag == 0 and exitFlag == 0):
				# Waits for user to click Restart Button or EXIT Button
				t.update()
			if(exitFlag == 1):
				# Actions to be taken if EXIT Button was clicked
				exitFlag = 0
				exit()
			elif(restartFlag == 1):
				# Actions to be taken if Restart Button was clicked
				restartFlag = 0
				main()

def startGame():
	'''Starts New Game'''
	gameState = State([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],1,None)
	global minimaxFlag
	global alphaBetaFlag
	t.onscreenclick(setAlgoFlag)
	while(alphaBetaFlag == 0 and minimaxFlag == 0):
		t.update()
	if(minimaxFlag == 1):
		minimaxFlag = 0
		global timeMinimax
		timeMinimax = time()
		playGame(gameState,1)
	elif(alphaBetaFlag == 1):
		alphaBetaFlag = 0
		global timeAlphaBeta 
		timeAlphaBeta = time()
		playGame(gameState,2)

def main():
	'''Main Driver Function'''
	global gameState
	initializeNoOfNodes()
	gui.start()
	global newGameFlag
	t.onscreenclick(setNewGameFlag)
	while(newGameFlag == 0):
		t.update()
	newGameFlag = 0
	gui.drawGameBoard()
	
if __name__ == "__main__":
	main()