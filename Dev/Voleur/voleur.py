from tkinter import *
from random import randrange

class Voleur:
	def __init__(self, fenetre, canevas, x_Gen = [855, 995, 1135], y_Gen = 300):
			self.Caneva = canevas #Canvas
			self.x_pos = x_Gen #Positions
			self.y_pos = y_Gen
			self.fen = fenetre
			self.photo_voleur = PhotoImage(file='images/voleur/voiture_voleur.png') #Image
			self.deplacement_en_cour = "non"


	def position(self, position = 2):
		self.Position = position
		self.position_x = self.x_pos[position]
		self.Caneva.create_image(self.position_x, self.y_pos, image=self.photo_voleur, tags = "Voleur") #Apparition du voleur

	def test(self):
		#self.Caneva.create_rectangle(800, 0, 925, 300)
		#self.Caneva.create_rectangle(930, 0, 1070, 300)
		#self.Caneva.create_rectangle(1080, 0, 1220, 300)
		gauche = self.Caneva.find_enclosed(800, -300, 925, 200)
		milieu = self.Caneva.find_enclosed(930, -300, 1070, 200)
		droite = self.Caneva.find_enclosed(1080, -300, 1220, 200)

		if self.deplacement_en_cour == "non":
			if self.Position == 0 and str(gauche) != "()": # Si la voiture est à gauche
				self.deplacement_en_cour = ["oui", "gauche", "centre"] #On effectue le déplacement vers le centre

			if self.Position == 1 and str(milieu) != "()": # Si la voiture est au centre
				if randrange(2) == 0:
					self.deplacement_en_cour = ["oui", "centre", "gauche"] #On effectue le déplacement vers gauche
				else:
					self.deplacement_en_cour = ["oui", "centre", "droite"] #On effectue le déplacement vers la droite

			if self.Position == 2 and str(droite) != "()":  # Si la voiture est à droite
				self.deplacement_en_cour = ["oui", "droite", "centre"]  # On effectue le déplacement vers le centre


		#Toute les 10 ms on réapelle la fonction
		self.fen.after(100 , func=self.test)

	def deplacement(self):
		if self.deplacement_en_cour[0] == "oui": #Si la voiture se déplace

			if self.deplacement_en_cour[1] == "gauche":
			#Si elle est à gauche on la déplace d'un vers la droite et on répéte dans qu'elle n'est pas dans sa postion
				self.Caneva.move("Voleur", 10, 0)
				if self.Caneva.coords("Voleur")[0] > self.x_pos[1]:
					self.deplacement_en_cour = "non"
					self.Position = 1

			if self.deplacement_en_cour[1] == "centre" and self.deplacement_en_cour[2] == "gauche":
			#Si elle est au centre et qu'elle va à gauche on la déplace d'un vers la gauche et on répéte dans qu'elle n'est pas dans sa postion
				self.Caneva.move("Voleur", -10, 0)
				if self.Caneva.coords("Voleur")[0] < self.x_pos[0] + 10 :
					self.deplacement_en_cour = "non"
					self.Position = 0

			if self.deplacement_en_cour[1] == "centre" and self.deplacement_en_cour[2] == "droite":
			#Si elle est au centre et qu'elle va à droite on la déplace d'un vers la droite et on répéte dans qu'elle n'est pas dans sa postion
				self.Caneva.move("Voleur", 10, 0)
				if self.Caneva.coords("Voleur")[0] > self.x_pos[2]:
					self.deplacement_en_cour = "non"
					self.Position = 2

			if self.deplacement_en_cour[1] == "droite":
			#Si elle est à droite on la déplace d'un vers la gauche et on répéte dans qu'elle n'est pas dans sa postion
				self.Caneva.move("Voleur", -10, 0)
				if self.Caneva.coords("Voleur")[0] < self.x_pos[1]+10:
					self.deplacement_en_cour = "non"
					self.Position = 1

		# Toute les 1 ms on réapelle la fonction
		self.fen.after(10, func=self.deplacement)

