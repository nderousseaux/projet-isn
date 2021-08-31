## Classe de génération et de la gestion des obstacles

from random import randrange
from tkinter import *
from math import *
import time

class ObsGen :
    def __init__(self, name, game, fenetre, mainCan, posGen = [125, 250, 375], hGen = -50, vit = 100, interval = 500, avant = True) :
        self.Name = "obs_" + name
        self.Game = game
        self.fen = fenetre
        self.Caneva = mainCan
        self.PosxGen = posGen
        self.HauteurGen = hGen
        self.VitDefil = vit ## vitesse en pixels / seconde
        if(avant) :
            path_ = "images/obs/avant/"
        else :
            path_ = "images/obs/arriere/"

        self.ObsImages = {
        1: PhotoImage(file= path_ + "voiture_1.png"),
        2: PhotoImage(file= path_ + "voiture_2.png"),
        3: PhotoImage(file= path_ + "voiture_3.png"),
        4: PhotoImage(file= path_ + "camion_1.png")
        }

        self.PosyGen = 0
        self.LastPosyGen = 0
        self.IntervalGen = interval ## interval moyen entre chaque voiture

        self.LastTime = time.time()

    def randGen(self) :
        xPos = self.PosxGen[randrange(0,3)]
        obs = randrange(1,4)
        self.Caneva.create_image(xPos, self.HauteurGen, image=self.ObsImages[obs], tags=self.Name)

    def upDateObs(self, deplacement_y) :
        self.Caneva.move(self.Name, 0, deplacement_y)
        self.PosyGen += round(deplacement_y)

    def controleurGen(self) :
        if(self.PosyGen - self.LastPosyGen >= self.IntervalGen) :
            self.randGen()
            self.LastPosyGen = self.PosyGen
        #print(self.IntervalGen)
        self.fen.after(10, func=self.controleurGen)

    def controleurDefilement(self) :
        DeltaT = time.time() - self.LastTime
        self.LastTime = time.time()

        # defilement :
        self.upDateObs(-(self.VitDefil - self.Game.Vitesse ) * DeltaT)

        # boucle tkinter
        self.fen.after(10, func=self.controleurDefilement)
