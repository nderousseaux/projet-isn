#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Louis Pro
#
# Created:     18/11/2017
# Copyright:   (c) Louis Pro 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *

class Player :
    def __init__(self, fen_parent, can_parent, game_parent, x0 = 250, y0 = 650) :
        self.Voiture_Img = PhotoImage(file="player.png")
        self.Fen_Parent = fen_parent
        self.Can_Parent = can_parent
        self.Game_Parent = game_parent
        self.Can_Parent.create_image(x0, y0, image=self.Voiture_Img, tags="player")

        self.Fen_Parent.bind('<Key>', self.PlayerControleur)

        self.X_Pos_Viser = 250

        self.PlayerLoop()

        self._prefixe_debug = "[Debug] -> {Player} : "

    def GetCoord(self) :
        return self.Can_Parent.coords("player")

    def Left(self) :
        self.Can_Parent.move("player", -10, 0)

    def Right(self) :
        self.Can_Parent.move("player", 10, 0)

    def GoLeft(self) :
        self.X_Pos_Viser -= 150

    def GoRight(self) :
        self.X_Pos_Viser += 150

    def PlayerControleur(self, evt) :
        if(self.Game_Parent._GamePause != 1 and self.Game_Parent._Loose != 1 and self.Game_Parent.Started == 1) :
            key = evt.keysym
            if(key == "Left" and self.X_Pos_Viser > 100) :
                self.GoLeft()
            elif(key == "Right" and self.X_Pos_Viser < 400) :
                self.GoRight()

    def PlayerLoop(self) :
        _time = 3
        if(self.Game_Parent._GamePause == 0 and self.Game_Parent._Loose == 0 and self.Game_Parent.Started == 1) :
            if(self.X_Pos_Viser > self.GetCoord()[0]) :
                self.Fen_Parent.after(_time, self.Right)
            elif(self.X_Pos_Viser < self.GetCoord()[0]) :
                self.Fen_Parent.after(_time, self.Left)
        self.Fen_Parent.after(_time, self.PlayerLoop)