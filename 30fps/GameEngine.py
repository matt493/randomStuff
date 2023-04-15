import time
from dataclasses import dataclass
import os

@dataclass()
class Pixel:
	x : int
	y : int
	# color : tuple[int, int, int]
	symbol : str = '█'

	def __str__(self) -> str:
		return self.symbol

class Canvas:
	width : int
	height : int
	canvas : list[list[Pixel]]

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.canvas = [[Pixel(x,y) for x in range(self.width)] for y in range(self.height)]

	def drawCanvas(self):
		frame : str = ""
		for row in self.canvas:
			print(frame.join([pixel.symbol for pixel in row]))
	
	def clearCanvas(self):
		pass

class Engine:
	
	start : None
	draw : None
	stop : None
	frameRate : int
	running : bool

	def __init__(self, start, draw, stop, frameRate:int=25):
		self.start = start
		self.draw = draw
		self.stop = stop
		self.frameRate = frameRate
		self.running = False
		
	def initGameLoop(self, canvas : Canvas):
		self.running = True

		if self.running:
			self.start()
			while self.running:
				timeBefore = time.time()
				self.clearScreen()
				self.draw()
				canvas.drawCanvas()
				timeAfter = time.time()
				timeDelta = timeAfter - timeBefore
				delay = ((1000.0 / self.frameRate) - timeDelta) / 1000.0
				time.sleep(0 if delay < 0 else delay)
			self.stop()
	
	def startEngine(self, canvas : Canvas):
		self.initGameLoop(canvas=canvas)
		pass
	
	def stopEngine(self):
		self.running = False
		pass

	def clearScreen(self):
		if os.name == 'nt':
			os.system('cls')	# for windows
		else:
			os.system('clear')	# for mac & linux
		pass