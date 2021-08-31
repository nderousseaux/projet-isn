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

        self.Titre_Pause = Texte(self.fen_parent, "PAUSE", 0, 0, "h1")
        self.Texte_Score = Texte(self.fen_parent, "Score : " + str(self.game_parent._Score), 0, 1, "h2")

        self.BoutonPlay = Bouton(self.fen_parent, "REPPRENDRE", 0, 2)
        self.BoutonPlay.bouton.configure(command=self.game_parent.UnpauseGame)

        self.BoutonRestart = Bouton(self.fen_parent, "RECOMMANCER", 0, 3)
        self.BoutonRestart.bouton.configure(command=self.game_parent.StartGame)

        self.BoutonMenu = Bouton(self.fen_parent, "MENU", 0, 4)
        self.BoutonMenu.bouton.configure(command=self.game_parent.GoMenu)


    def show_menu(self) :
        self.Titre_Pause.show()
        self.Texte_Score.show()
        self.BoutonPlay.show()
        self.BoutonRestart.show()
        self.BoutonMenu.show()

    def hide_menu(self) :
        self.Titre_Pause.hide()
        self.Texte_Score.hide()
        self.BoutonPlay.hide()
        self.BoutonRestart.hide()
        self.BoutonMenu.hide()