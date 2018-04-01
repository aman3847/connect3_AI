## Connect 3

- A mini-version of the connect 4 game implemented using Python 2 and Turtle Graphics.
- The intelligent agent uses Minimax Algorithm or Alpha-Beta Pruning based on user's choice.

## Playing the Game

- Open the terminal and type `python driver.py` to play the game.
	- The intelligent agent always makes the first move.
	- The user needs to click on the corresponding column to put the coin in that column.
	- Whenever the game ends, click on RESTART to reset the game or EXIT to quit.
	
## Analysis Tab

- The descrption of the various values in the Analysis tab are as follows
	- Minimax algorithm based analysis
		- R1: Number of nodes generated till the problem is solved
		- R2: Amount of memory allocated to one node
		- R3: Maximum growth of the stack
		- R4: Total time to play the game
		- R5: Number of nodes created in one micro second
	- Alpha Beta pruning based analysis
		- R6: Number of nodes generated till the problem is solved
		- R7: The ratio (R1 - R6)/R1 as saving using pruning
		- R8: Total time to play a game
	- Comparative Analysis
		- R9: Comparison of the memory used in both the techniques
		- R10: Average time to play the game 10 times
		- R11: Number of wins by the intelligent agent divided by 10
		- R12: Number of wins by the intelligent agent divided by 20
