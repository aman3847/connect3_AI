# Name: Aman Gupta
# ID: 2014B2A70201P

class State:
	'''Data Structure for the Nodes'''
	def __init__(self,board,typeOfNode,action):
		'''Constructs a new State Node'''
		self.board = board # Current State of the board
		self.typeOfNode = typeOfNode # 1 = Max Node (AI), 2 = Min Node (Human)
		self.utilityValue = None # Utility value of current node
		self.action = action # Action taken by parent node to reach this node
		self.bestMove = None # Best move to be taken in this state by the player