from tkinter import *
from random import randrange
import time

class landscape :
    def __init__(self, game, fenetre, canvas, vit = 360) :
        self.Game = game
        self.Fen = fenetre
        self.Can = canvas
        path_ = "images/routes/"
        self.Route_img = {
        1 : PhotoImage(file=path_ + "riviere_v2.png"),
        2 : PhotoImage(file=path_ + "riviere_v2.png"),
        3 : PhotoImage(file=path_ + "riviere_v2.png")}
        self.HeightRoute = 500
        self.PosY = 0
        self.landType = 1
        self.LastTime = time.time()

    def InitLandScape(self) :
        self.Can.create_image(615, -250, image=self.Route_img[self.landType], tags="route")
        self.Can.create_image(615, -250 + self.HeightRoute, image=self.Route_img[self.landType], tags="route")
        self.Can.create_image(615, -250 + 2*self.HeightRoute, image=self.Route_img[self.landType], tags="route")

    def defil(self) :
        # défilement des motifs de route
        DeltaT = time.time() - self.LastTime
        self.LastTime = time.time()
        DeltaY = round(self.Game.Vitesse * DeltaT)
        self.Can.move("route", 0, DeltaY)
        self.PosY += DeltaY

        # ajout d'un nouveaux motif si besoin
        if(self.PosY >= self.HeightRoute- (self.Game.Vitesse/50)) :
            if(randrange(1, 100) == 1) :
                t = self.landType
                while(t == self.landType) :
                    t = randrange(1, 4)
                self.landType = t
            self.Can.create_image(615, -250, image=self.Route_img[self.landType], tags="route")
            self.PosY = 0

        # maintiens de la route en arriere plan
        self.Can.tag_lower("route")

        # boucle tkinter
        self.Fen.after(1, func=self.defil)
