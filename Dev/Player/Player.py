from tkinter import *
import time
import perdu

class Player:
    def __init__(self, game, can, fen) :
        self.Game = game
        self.Can = can
        self.Fen = fen
        self.PlayerImage = PhotoImage(file = "images/Player/player_img_tmp.png")
        self.GirosImage = [PhotoImage(file = "images/Player/Giro_Bleu.png"), PhotoImage(file = "images/Player/Giro_Rouge.png")]
        self.PosY0 = 600
        self.PosX = 995
        self.Can.create_image(995, 900, image=self.PlayerImage, tags=("player_car","player"))
        self.Can.create_image(980, 910, image=self.GirosImage[0], tags=("giro_bleu", "player"))
        self.Can.create_image(1010, 910, image=self.GirosImage[1], tags=("giro_rouge", "player"))
        self.Fen.bind('<KeyPress>', self.KeyPressControl) # liaison d'evenement pour le controle du joueur
        self.Fen.bind('<KeyRelease>', self.KeyReleaseControl)

        self.LastTime_giro = time.time() * 1000 ## conversion en ms
        self.giroState = 0

        self.LastTime_PAcc = time.time()

        self.PlayerV_max = 1500 ## px/s
        self.PlayerAcc = 250 ## px / s / s
        self.PlayerBreakForce = 1000 ##px / s / s

        self.PlayerIsAcc = False
        self.PlayerIsBreaking = False

        self.vitesse_deplacement_lateral = 10

    def right(self) :
        self.Can.move("player", self.vitesse_deplacement_lateral, 0)
    def left(self) :
        self.Can.move("player", -self.vitesse_deplacement_lateral, 0)

    def InitPlayer(self) :
        self.Can.move("player", 0, -1)
        if(self.Can.coords("player")[1] != self.PosY0) :
            self.Fen.after(10, self.InitPlayer)

    def KeyPressControl(self, evt) :
        # gestion du controle du joueur
        key = evt.keysym
        if(key == "q" and self.PosX > 855) :
            self.PosX -= 140
        elif(key == "d" and self.PosX < 1135) :
            self.PosX += 140
        elif(key == "z" and self.Game.Vitesse < self.PlayerV_max) :
            self.PlayerIsAcc = True
        elif(key == "s" and self.Game.Vitesse > 0) :
            self.PlayerIsBreaking = True

    def KeyReleaseControl(self, evt) :
        # gestion du controle du joueur
        key = evt.keysym
        if(key == "z") :
            self.PlayerIsAcc = False
        elif(key == "s") :
            self.PlayerIsBreaking = False

    def ControlLoop(self) :
        # déplacement du joueur si besoin
        if(self.Can.coords("player")[0] > self.PosX) :
            self.left()
        elif(self.Can.coords("player")[0] < self.PosX) :
            self.right()
        if(self.PlayerIsAcc and self.Game.Vitesse < self.PlayerV_max) :
            self.Game.Vitesse += self.PlayerAcc * (time.time() - self.LastTime_PAcc)
        elif(self.PlayerIsBreaking and self.Game.Vitesse > 0) :
            self.Game.Vitesse -= self.PlayerBreakForce * (time.time() - self.LastTime_PAcc)

        self.LastTime_PAcc = time.time()

        # clignotement des girophares
        if time.time() * 1000 - self.LastTime_giro >= 500 :
            if self.giroState == 0 :
                self.Can.itemconfigure("giro_bleu", state = "hidden") # cache le giro bleu
                self.Can.itemconfigure("giro_rouge", state = "normal") # affiche le giro rouge
                self.giroState = 1
            else :
                self.Can.itemconfigure("giro_bleu", state = "normal") # affiche le giro bleu
                self.Can.itemconfigure("giro_rouge", state = "hidden") # cache le giro rouge
                self.giroState = 0
            self.LastTime_giro = time.time() * 1000

        # boucle tkinter
        self.Fen.after(10, self.ControlLoop)




    #Nath#
   
    #Colisions
    def detection_colisions(self):
        self.position_police = self.Can.coords("player")  #Coordonées voiture de police
        #print (self.Can.find_overlapping(self.position_police[0]-50, 525, self.position_police[0] + 50, 675))

        if len(self.Can.find_overlapping(self.position_police[0]-50, 525, self.position_police[0] + 50, 675)) == 5: 
            #Si la longueur de la liste des objets sur la position de la voiture ecede 1, il y a colision.
            print("Collision !!!!")
            self.Fen.destroy()
            perdu.perdu()

        #Toute les 10 ms on réapelle la fonction
        self.Fen.after(10 , func=self.detection_colisions)


    def augmentation_vitesse(self):
        self.PlayerV_max += 30

        # Toute les 100 ms on réapelle la fonction
        self.Fen.after(1000, func=self.augmentation_vitesse)


    def augmentation_vitesse_lateralle(self):
        self.vitesse_deplacement_lateral += 1
        print("a")
        # Toute les 100 ms on réapelle la fonction
        self.Fen.after(1000, func=self.augmentation_vitesse_lateralle)


