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

class Menu_Pause :
    def __init__(self, Fen, game) :
        self.fen_parent = Fen
        self.game_parent = game

        self.Titre_GameOver = Texte(self.fen_parent, "GAME OVER !", 0, 0, "h1")
        self.Texte_Score = Texte(self.fen_parent, "Score : " + str(self.game_parent._Score), 0, 1, "h2")

        self.BoutonRestart = Bouton(self.fen_parent, "RECOMMANCER", 0, 2)
        self.BoutonRestart.bouton.configure(command=self.game_parent.StartGame)

        self.BoutonMenu = Bouton(self.fen_parent, "MENU", 0, 3)
        self.BoutonMenu.bouton.configure(command=self.game_parent.GoMenu)


    def show_menu(self) :
        self.Titre_GameOver.show()
        self.Texte_Score.show()
        self.BoutonRestart.show()
        self.BoutonMenu.show()

    def hide_menu(self) :
        self.Titre_GameOver.hide()
        self.Texte_Score.hide()
        self.BoutonRestart.hide()
        self.BoutonMenu.hide()