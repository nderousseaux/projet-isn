#-------------------------------------------------------------------------------
# Name:        Moteur de jeu
# Purpose:
#
# Author:      Louis Pro
#
# Created:     18/11/2017
# Copyright:   (c) Louis Pro 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from Avoid.Game.Player import *
from Avoid.Game.Obstacles import *
from Avoid.Interface.Menu_Pause import *
from math import *

class Game_Engine :
    def __init__(self, Fen_parent, Menu_parent, CanWidth, CanHeight) :
        self.InisGame()
        self.parent = Fen_parent
        self.MenuParent = Menu_parent
        self.Can = Canvas(self.parent, background="#FFE699", height=CanHeight, width=CanWidth)
        self.MenuPause = Menu_Pause(self.parent, self)

        self._SpaceBetween = 500

        self._TimeActu = 15 ## actu toutes les 15ms pour rester au dessus de 60 deplacment par seconde

        self._PlayerY0 = 650
        self.player = Player(self.parent, self.Can, self, 250, self._PlayerY0)
        self.obstacles = Obstacles(self.parent, self.Can)
        self._TextScore_ID = self.Can.create_text(250, 60, text = "0", font = ('Californian FB', 65, 'bold'), fill = "#203864")

        self.parent.bind('<Key>', self.GameControl, self.player.PlayerControleur) ## Liaison controleur du déroulement

        self.GameLoop() ## Boucle d'actualisation du jeu

    def InisGame(self) :
        self.Started = 0
        self._GamePause = 0
        self._Loose = 0

        self._WorldPos = 0 ## position y en pixel du monde
        self._Score = 0 ## Nombre d'obstacle passé
        self._VitDefilement = 10
        self._LastPos = 0
        self._LastAcc = 0 ## indique la dernière ligne ou les obstacles ont été accélérer
        self._LineBetweenAcc = 30 ## acceléraion du niveau toutes les x lignes
        self._ObAcc = 1 ## accélération des obstacles

    def StartGame(self) :
        self.obstacles._removeAll()

        self.MenuParent.hide_menu()
        self.MenuPause.hide_menu()

        self.Can.grid()
        self.Can.create_text(250, 200, text="Appuie sur une touche pour jouer",
                             width=350, font=('Californian FB', 40, 'bold'),
                             justify = "center",
                             tags="HitsForStart")

        self.Can.itemconfigure(self._TextScore_ID, text="0")

        self.InisGame() ## Réinitialisation des variable du jeu

    def GoMenu(self) :
        self.Can.grid_remove()
        self.MenuPause.hide_menu()
        self.MenuParent.show_menu()

    def PauseGame(self) :
        self._GamePause = 1
        self.Can.grid_remove()
        self.MenuPause.Texte_Score.texte.configure(text = "Score : " + str(self._Score))
        self.MenuPause.show_menu()

    def UnpauseGame(self) :
        self._GamePause = 0
        self.MenuPause.hide_menu()
        self.Can.grid()

    def Loose(self) :
        self._Loose = 1
        self._TexteLoose = self.Can.create_text(250, 300, text="PERDU :(\nAppuyer sur une touche pour rejouer",
                             width=350, font=('Californian FB', 40, 'bold'),
                             justify = "center",
                             tags="TexteOfLoose")

    def GameControl(self, evt) :
        key = evt.keysym
        if(self.Started == 0) :
            self.Can.delete("HitsForStart")
            self.Started = 1
        elif(self._Loose == 1) :
            self.Can.delete("TexteOfLoose")
            self.StartGame()
        elif(key == "space" and self._GamePause == 0) :
            self.PauseGame()

    def GameLoop(self) :
        if(self._GamePause == 0 and self._Loose == 0 and self.Started == 1) :
            self.obstacles._move(self._VitDefilement)
            self._WorldPos += self._VitDefilement
            self._LastPos += self._VitDefilement
            ## Ajout d'un nouvelle obstacke :
            if(self._LastPos >= self._SpaceBetween) :
                self.obstacles.AddObstacle(-self._SpaceBetween)
                self._LastPos = 0
            ## Actualisation du score :
            _Score_tmp = floor(((self._WorldPos - self._PlayerY0 - 100) / self._SpaceBetween))
            if(_Score_tmp > 0 and _Score_tmp != self._Score) :
                self._Score = _Score_tmp
                self.Can.itemconfigure(self._TextScore_ID, text=self._Score)

            ## Acceleration des obstacles :
            if(self._Score - self._LastAcc >= self._LineBetweenAcc) :
                self._VitDefilement += self._ObAcc
                self._LastAcc = self._Score

            ## Supression des onbstacles dépasser :
            self.Can.addtag_overlapping("Ob_depasser", -100, 1000, 600, 10000)
            self.Can.delete("Ob_depasser")

            ## On vérifie que le joueur ne sois pas en contacte avec un obstacle :
            self.Can.addtag_overlapping("HIT",
                                        self.player.GetCoord()[0] - 40,
                                        self._PlayerY0 + 90,
                                        self.player.GetCoord()[0] + 40,
                                        self._PlayerY0 -90)

            if(self.Can.find_withtag("HIT") != (1, )) :
                self.Loose()


        self.parent.after(self._TimeActu, self.GameLoop)
