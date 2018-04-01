# Name: Aman Gupta
# ID: 2014B2A70201P

import turtle as t
from state import *
from driver import *

def start():
	'''Generates the Initial State of the Game'''
	t.reset()
	t.setup(1200,800)
	t.screensize(1200,800)
	t.setworldcoordinates(-900,-550,300,250)
	t.title("align3")
	t.color("Black")
	t.pensize(3)
	t.tracer(1,2)
	
	# Making partitions on the canvas
	drawLine(-300,-550,-300,250)
	drawLine(-300,-300,300,-300)
	drawLine(-300,-475,300,-475)

	# Four Control Buttons
	drawBox(-250,-325,-50,-375) # New Game
	drawBox(50,-325,250,-375) # Minmax
	drawBox(-250,-400,-50,-450) # Alpha-Beta
	drawBox(50,-400,250,-450) # Statistics

	# Filling the Button Text
	writeText(-230,-370,"New Game")
	writeText(90,-370,"Minimax")
	writeText(-230,-445,"Alpha-Beta")
	writeText(90,-445,"Analysis")

def drawGameBoard():
	'''Drawing the Game Board
	Also calls the start() function defined in driver.py file'''
	drawLine(-250,230,250,230,True) # Base Line
	drawLine(-200,-200,-200,200)
	drawLine(-100,-200,-100,200)
	drawLine(0,-200,0,200)
	drawLine(100,-200,100,200)
	drawLine(200,-200,200,200)
	drawLine(-200,-200,200,-200)
	drawLine(-200,-100,200,-100)
	drawLine(-200,0,200,0)
	drawLine(-200,100,200,100)
	drawLine(-200,200,200,200)
	startGame()

def drawLine(initX,initY,finalX,finalY,baseLine=False,winLine=False):
	'''Draws lines on the canvas on the basis of given coordinates'''
	# baseLine is used as a flag variable to draw base line of RED color and 10 Width
	# winLine is used as a flag variable to show the winning combination in case of a win
	if(winLine):
		t.color("Yellow")
		t.pensize(10)
		t.penup()
		t.setpos(initX,initY)
		t.pendown()
		t.setpos(finalX,finalY)
		t.color("Black")
		t.pensize(3)
	elif(baseLine):
		t.color("Red")
		t.pensize(10)
		t.penup()
		t.setpos(initX,initY)
		t.pendown()
		t.setpos(finalX,finalY)
		t.color("Black")
		t.pensize(3)
	else:	
		t.penup()
		t.setpos(initX,initY)
		t.pendown()
		t.setpos(finalX,finalY)

def writeText(initX,initY,text):
	'''Writes text on the canvas'''
	t.color("black")
	t.penup()
	t.setpos(initX,initY)
	t.pendown()
	t.write(text,font=("Arial",24,"normal"))

def drawBox(initX,initY,finalX,finalY):
	'''Draws boxes on the canvas'''
	drawLine(initX,initY,finalX,initY)
	drawLine(finalX,initY,finalX,finalY)
	drawLine(finalX,finalY,initX,finalY)
	drawLine(initX,finalY,initX,initY)

def drawCircle(centreX,centreY,lastPlayer):
	'''Draws circles depicting coins placed on the board'''
	t.penup()
	t.setpos(centreX,centreY)
	t.pendown()
	t.begin_fill()
	if(lastPlayer==1):
		t.color("blue")
	elif(lastPlayer==2):
		t.color("green")
	t.circle(50)
	t.end_fill()

def placeCoin(row,col,player):
	'''Places coin in the selected Column'''
	if(row == 0 and col == 0):
		drawCircle(-150,100,player)
	elif(row == 0 and col == 1):
		drawCircle(-50,100,player)
	elif(row == 0 and col == 2):
		drawCircle(50,100,player)
	elif(row == 0 and col == 3):
		drawCircle(150,100,player)
	elif(row == 1 and col == 0):
		drawCircle(-150,0,player)
	elif(row == 1 and col == 1):
		drawCircle(-50,0,player)
	elif(row == 1 and col == 2):
		drawCircle(50,0,player)
	elif(row == 1 and col == 3):
		drawCircle(150,0,player)
	elif(row == 2 and col == 0):
		drawCircle(-150,-100,player)
	elif(row == 2 and col == 1):
		drawCircle(-50,-100,player)
	elif(row == 2 and col == 2):
		drawCircle(50,-100,player)
	elif(row == 2 and col == 3):
		drawCircle(150,-100,player)
	elif(row == 3 and col == 0):
		drawCircle(-150,-200,player)
	elif(row == 3 and col == 1):
		drawCircle(-50,-200,player)
	elif(row == 3 and col == 2):
		drawCircle(50,-200,player)
	elif(row == 3 and col == 3):
		drawCircle(150,-200,player)

def printResult(winner):
	'''Prints the result of the game on the canvas'''
	if(winner == 1):
		writeText(-100,-245,"Human Wins!!")
	elif(winner == 2):
		writeText(-45,-245,"AI Wins!!")
	elif(winner == 0):
		writeText(-100,-245,"It's a DRAW!!")

	# Drawing Restart and Exit Buttons
	drawBox(-250,-490,-50,-540) # Restart
	writeText(-200,-535,"Restart")
	drawBox(50,-490,250,-540) # EXIT
	writeText(115,-535,"EXIT")

def showAnalysis(R1=0,R2=0,R3=0,R4=0,R5=0,R6=0,R7=0,R8=0,R9=(0,0),R10=0,R11=0,R12=0):
	'''Shows the analysed values on the left hand side of the canvas'''
	writeText(-850,180,"R1 = " + str(R1) + " nodes")
	writeText(-850,120,"R2 = " + str(R2) + " bytes")
	writeText(-850,60,"R3 = " + str(R3) + " nodes")
	writeText(-850,0,"R4 = " + str(round(R4,3)) + " seconds")
	writeText(-850,-60,"R5 = " + str(round(R5,3)) + " nodes/microsecond")
	writeText(-850,-120,"R6 = " + str(R6) + " nodes")
	writeText(-850,-180,"R7 = " + str(R7))
	writeText(-850,-240,"R8 = " + str(round(R8,3)) + " seconds")
	writeText(-850,-300,"R9: minimax = " + str(R9[0]) + " bytes")
	writeText(-850,-360,"R9: alphaBeta = " + str(R9[1] )+ " bytes")
	writeText(-850,-420,"R10 = " + str(round(R10,3)) + " seconds")
	writeText(-850,-480,"R11 = " + str(R11) + " win(s)")
	writeText(-850,-540,"R12 = " + str(R12) + " win(s)")
