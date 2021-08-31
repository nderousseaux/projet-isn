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
from random import *

class Obstacles :
    def __init__(self, fen_parent, can_parent) :
        self.Fen_Parent = fen_parent
        self.Can_Parent = can_parent
        self.VoitureObstacle_img = PhotoImage(file="obstacle.png")

        self._ProbaObstacle_One = 1 ## 1/x
        self._ProbaObstacle_Two = 3 ## 1/x

    def _move(self, vit) :
        self.Can_Parent.move("obstacle", 0, vit)

    def _removeAll(self) :
        self.Can_Parent.delete("obstacle")

    def AddObstacle(self, posY) :
        _One = 0
        if(_One == 0) :
            _One_Pos = randrange(1, 4)

            if(_One_Pos == 1) :
                self.Can_Parent.create_image(100, posY, image=self.VoitureObstacle_img, tags="obstacle")
            elif(_One_Pos == 2) :
                self.Can_Parent.create_image(250, posY, image=self.VoitureObstacle_img, tags="obstacle")
            elif(_One_Pos == 3) :
                self.Can_Parent.create_image(400, posY, image=self.VoitureObstacle_img, tags="obstacle")

        _Two = randrange(0, self._ProbaObstacle_Two + 1)
        if(_Two == 0) :
            _Two_Pos = randrange(1, 4)

            if(_Two_Pos == 1) :
                self.Can_Parent.create_image(100, posY, image=self.VoitureObstacle_img, tags="obstacle")
            elif(_Two_Pos == 2) :
                self.Can_Parent.create_image(250, posY, image=self.VoitureObstacle_img, tags="obstacle")
            elif(_Two_Pos == 3) :
                self.Can_Parent.create_image(400, posY, image=self.VoitureObstacle_img, tags="obstacle")
