#-------------------------------------------------------------------------------
# Name:        Menu
# Purpose:
#
# Author:      Louis Pro
#
# Created:     17/11/2017
# Copyright:   (c) Louis Pro 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import messagebox
from Avoid.Interface.Texte import *
from Avoid.Interface.Bouton import *
from Avoid.Game.Game import *

class Menu_Game :

    def App_Quitte(self) :
        rep = messagebox.askquestion("Quitter ?", "Voulez vous vraiment quitter ?")
        if(rep == "yes") :
            self.parent.destroy()

    def start_game(self) :
        self.hide_menu() ## fermeture du menu
        self.Game.StartGame() ## démarrage du jeu

    def __init__(self, Fen) :
        self.parent = Fen.fen
        self.Game = Game_Engine(self.parent, self, 500, 800) ## création du moteur de jeu
        Fen.fen.columnconfigure(0, weight=1) ## La colonne occupe toute l'esapce et les widgets sont donc centrez (si anchor = center)
        Fen.fen.rowconfigure(2, minsize=100)
        self.Titre_1 = Texte(Fen, "AVOID GAME", 0, 0, "h1")
        self.Sous_titre = Texte(Fen, "Accueil", 0, 1, "h2")
        # Bouton Play :
        self.BoutonPlay = Bouton(Fen, "PLAY", 0, 2)
        self.BoutonPlay.bouton.configure(command=self.start_game)
        self.BoutonQuitte = Bouton(Fen, "Quitter", 0, 3)
        self.BoutonQuitte.bouton.configure(command = self.App_Quitte)
       # Bouton Quitter :


    def show_menu(self) :
        self.Titre_1.show()
        self.Sous_titre.show()
        self.BoutonPlay.show()
        self.BoutonQuitte.show()

    def hide_menu(self) :
        self.Titre_1.hide()
        self.Sous_titre.hide()
        self.BoutonPlay.hide()
        self.BoutonQuitte.hide()