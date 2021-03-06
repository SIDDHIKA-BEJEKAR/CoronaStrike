# my_enemy.py
import pygame
import time
import random
import math

class my_corona_1():
#level 1 corona-virus
	def __init__(self, mode):
		self.corona_1_Img_right = [None]*5
		self.corona_1_Img_left = [None]*5
		
		self.Img_right = ['corona_2_h1.png', 'corona_2_h4.png', 'corona_2_h3.png', 'corona_2_h5.png', 'corona_2_h2.png']
		for i in range(5):
			self.corona_1_Img_right[i] = pygame.image.load(self.Img_right[0])
		# self.corona_1_Img_right = pygame.image.load(self.Img_right[0])

		self.Img_left = ['corona_1_h1.png', 'corona_1_h4.png', 'corona_1_h3.png', 'corona_1_h5.png', 'corona_1_h2.png']
		for i in range(5):
			self.corona_1_Img_left[i] = pygame.image.load(self.Img_left[0])
		# self.corona_1_Img_left = pygame.image.load(self.Img_left[0])
		
		self.corona_1_Img = [self.corona_1_Img_right[0]]*5
		self.corona_1X = [None]*5
		self.corona_1Y = [None]*5
		self.corona_choice = [30, 78, 126, 174]
		self.corona_movX = [1]*5
		self.corona_movY = [48]*5
		self.corona_vel = 0.3*(mode/2)
		# print("thy modeva ", mode)
		self.health = [mode]*5
		self.alive = [True]*5
		
	def spawn_corona(self, i):
		# for i in range(5):
		again = True
		self.corona_1_Img_right[i] = pygame.image.load(self.Img_right[random.randint(0,4)])
		self.corona_1_Img_left[i] = pygame.image.load(self.Img_left[random.randint(0,4)])
		while again:
			# self.corona_1X.append(random.randint(100, 600))
			# self.corona_1Y.append(random.choice(self.corona_choice))
			self.corona_1X[i] = random.randint(100, 600)
			self.corona_1Y[i] = random.choice(self.corona_choice)
			# print("[", self.corona_1X[i], ",", self.corona_1Y[i], "]")
			if i == 0:
				break
			for j in range(0, i):
				if i == j:
					continue
				if (self.corona_1Y[i] == self.corona_1Y[j]) and (abs(self.corona_1X[i] - self.corona_1X[j]) < 48):
				# (self.corona_1Y[i] == self.corona_1Y[j]) and
					again = True
					# self.corona_1X.pop()
					# self.corona_1Y.pop()
					break
				else:
					again = False


	def corona_1(self, corona_1X, corona_1Y, screen):	
		for i in range(5):
			if not self.alive[i]:
				continue
			screen.blit(self.corona_1_Img[i], (int(corona_1X[i]), int(corona_1Y[i])))

	# Boundary conditions : don't leave the screen
	def check_corona_1(self, dt):
				#for corona_1
		for i in range(5):
			if self.corona_1X[i] < 0:
				self.corona_1X[i] = 0
				self.corona_1_Img[i] = self.corona_1_Img_right[i]
				self.corona_movX[i] = -self.corona_movX[i]
				self.corona_1Y[i] += self.corona_movY[i]	
			elif self.corona_1X[i] > 752:
				self.corona_1X[i] = 752
				self.corona_1_Img[i] = self.corona_1_Img_left[i]
				self.corona_movX[i] = -self.corona_movX[i]
				self.corona_1Y[i] += self.corona_movY[i]
			if self.corona_1Y[i] < 0:
				self.corona_1Y[i] = 0		
			elif self.corona_1Y[i] > 552:
				self.corona_1Y[i] = 552
			self.corona_1X[i] += self.corona_movX[i] * (dt * self.corona_vel)

			if self.corona_movX[i] > 0:
				self.corona_1_Img[i] = self.corona_1_Img_right[i]
			else:
				self.corona_1_Img[i] = self.corona_1_Img_left[i]
			