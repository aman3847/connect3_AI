# Name: Aman Gupta
# ID: 2014B2A70201P

from copy import deepcopy
from state import *

noOfNodes = 0
def successor(state,col):
	tempBoard = deepcopy(state.board) # Creates a copy of the board in the current state
	for row in range(4):
		global noOfNodes
		global maxNoOfNodes
		if(tempBoard[row][col]==0):
			tempBoard[row][col] = state.typeOfNode
			global noOfNodes
			global maxNoOfNodes
			if(state.typeOfNode==1):
				newState = State(tempBoard,2,col)
				noOfNodes += 1
				return newState
			elif(state.typeOfNode==2):
				newState = State(tempBoard,1,col)
				noOfNodes += 1
				return newState
			break
	return False

def getNoOfNodes():
	'''Accessor Method for accessing no of nodes generated'''
	return noOfNodes

def initializeNoOfNodes():
	'''Resets no of nodes to Zero'''
	global noOfNodes
	noOfNodes = 0

def decrementNoOfNodes():
	'''Decrement the no of nodes created to incorporate the node created by the user'''
	global noOfNodes
	noOfNodes -= 1