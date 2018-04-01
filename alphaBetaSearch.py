# Name: Aman Gupta
# ID: 2014B2A70201P

import terminalTest
from successor import *

def alphaBetaSearch(state):
	'''Returns best possible move in the given state using Alpha Beta Pruning'''
	state.utilityValue = maxValueAB(state,-100,100)
	return state.bestMove

def maxValueAB(state,alpha,beta):
	'''Returns the utility value of the current state to the Max node'''
	if(terminalTest.terminalTest(state)):
		return utilityValue(state)
	state.utilityValue = -100 # Setting utility value of current node to (-)infinity
	# col is the action being passed to successor function
	# In this game there are 4 possible actions: 0,1,2,3
	for col in range(4):
		s = successor(state,col) # s is the generated child node that the successor function returns
		if(s is False):
			'''If the action passed is unable to generate a legal child node then the loop continues over the remaining possible actions'''
			continue
		value = minValueAB(s,alpha,beta)
		if(value > state.utilityValue):
			state.utilityValue = value
			state.bestMove = s.action
		if(value >= beta):
			state.utilityValue = value
			state.bestMove = s.action
			return state.utilityValue
		alpha = max(alpha,value)
	return state.utilityValue

def minValueAB(state,alpha,beta):
	'''Returns the utility value of the current state to the Min node'''
	if(terminalTest.terminalTest(state)):
		return utilityValue(state)
	state.utilityValue = 100 # Setting utility value of current node to (+)infinity
	# col is the action being passed to successor function
	# In this game there are 4 possible actions: 0,1,2,3
	for col in range(4):
		s = successor(state,col) # s is the generated child node that the successor function returns
		if(s is False):
			'''If the action passed is unable to generate a legal child node then the loop continues over the remaining possible actions'''
			continue
		value = maxValueAB(s,alpha,beta)
		if(value < state.utilityValue):
			state.utilityValue = value
			state.bestMove = s.action
		if(value <= alpha):
			state.utilityValue = value
			state.bestMove = s.action
			return state.utilityValue
		beta = min(beta,value)
	return state.utilityValue

def utilityValue(state):
	'''Returns utility value of a leaf node'''
	if(terminalTest.checkNoMovesLeft(state.board)):
		'''No more coins can be placed on the board hence, the result is a DRAW'''
		state.utilityValue = 0
		return 0
	elif(state.typeOfNode == 1):
		'''It was Player-1's (Max) turn to play but since the state is a terminal state it means Player-2 (Min) has won'''
		state.utilityValue = -1
		return -1
	elif(state.typeOfNode == 2):
		'''It was Player-2's (Min) turn to play but since the state is a terminal state it means Player-1 (Max) has won'''
		state.utilityValue = 1
		return 1