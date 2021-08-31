from tkinter import *
from random import randrange

class colisions
	def __init__(self, fenetre, canevas):]
			self.Caneva = canevas #Canvas
			self.fen = fenetre

	def trouver_emplacement_police(self):
		self.Caneva.create_rectangle(800, 0, 925, 300)
		self.Caneva.create_rectangle(930, 0, 1070, 300)
		self.Caneva.create_rectangle(1080, 0, 1220, 300)
		gauche = self.Caneva.find_enclosed(800, -300, 925, 200)
		milieu = self.Caneva.find_enclosed(930, -300, 1070, 200)
		droite = self.Caneva.find_enclosed(1080, -300, 1220, 200)


		if self.Position == 0 and str(gauche) != "()":
			if str(milieu) != "()":
				#Aller à droite depuis la gauche
				self.Caneva.moveto("Voleur", self.Ecart_plus * 2, 0)
				self.Position = 2

			else:
				#Aller au milieu depuis la gauche
				self.Caneva.move("Voleur", self.Ecart_plus, 0)
				self.Position = 1

		if self.Position == 1 and str(milieu) != "()":
			if randrange(2) == 0:
				if str(droite) != "()":
					#Aller à gauche depuis le milieu
					self.Caneva.move("Voleur", self.Ecart_moin, 0)
					self.Position = 0
				else:
					#Aller à droite depuis le milieu
					self.Caneva.move("Voleur", self.Ecart_plus, 0)
					self.Position = 2

			else:
				if str(gauche) != "()":
					#Aller à droite depuis le milieu
					self.Caneva.move("Voleur", self.Ecart_plus, 0)
					self.Position = 2
				else:
					#Aller à gauche depuis le milieu
					self.Caneva.move("Voleur", self.Ecart_moin, 0)
					self.Position = 0

		if self.Position == 2 and str(droite) != "()":
			if str(milieu) != "()":
				#Aller à gauche depuis la droite
				self.Caneva.move("Voleur", self.Ecart_moin * 2, 0)
				self.Position = 0
			else:
				#Aller au milieu depuis la droite
				self.Caneva.move("Voleur", self.Ecart_moin, 0)
				self.Position = 1

		#Toute les 10 ms on réapelle la fonction
		self.fen.after(100 , func=self.test)
