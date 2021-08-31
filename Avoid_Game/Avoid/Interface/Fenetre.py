#-------------------------------------------------------------------------------
# Name:        Fenetre
# Purpose:     Créer et gère la fenêtre principale
#
# Author:      Louis Pro
#
# Created:     17/11/2017
# Copyright:   (c) Louis Pro 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *

class Fenetre :

    def __init__(self, fen_title, fen_width, fen_height) :
        self.fen = Tk()
        self.fen.geometry(str(fen_width) + "x" + str(fen_height + 50) +
        "+" + str(int(self.fen.winfo_screenwidth() / 2 - (fen_width / 2))) +
        "+" + str(int(self.fen.winfo_screenheight() / 2 - (fen_height / 2) - 50)))
        self.fen.wm_title(fen_title)
        self.fen.configure(background="#203864")
        self.fen.resizable(0, 0)

    def loop(self) :
        self.fen.mainloop()

