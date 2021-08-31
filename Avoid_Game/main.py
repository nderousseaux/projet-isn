#-------------------------------------------------------------------------------
# Name:        Avoid
# Purpose:     Eviter des obstacle en voiture
#
# Author:      Louis
#
# Created:     12/11/2017
# Copyright:   (c) Louis 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from Avoid.Interface.Texte import *
from Avoid.Interface.Fenetre import *
from Avoid.Interface.Menu_Game import *

Fen_Game = Fenetre("AVOID GAME !", 500, 750) ## création de la fenêtre du jeu
MainMenu = Menu_Game(Fen_Game) ## création du menu

MainMenu.show_menu() ## affichage du menu

# fin du programme : boucle déxécution de Tk
Fen_Game.loop()