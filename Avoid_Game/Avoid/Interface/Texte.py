#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Louis Pro
#
# Created:     17/11/2017
# Copyright:   (c) Louis Pro 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
import tkinter.font as tkFont

class Texte :
    def __init__(self, parent, texte_, posX, posY, typePolice = "normal", color = "#FFE699", back = "#203864") :
        if(typePolice == "h1") :
            self.font = ('Elephant', 34)
        elif(typePolice == "h2") :
            self.font = ('Californian FB', 28, 'bold underline')
        elif(typePolice == "normal") :
            self.font = ('Comic Sans MS', 14)
        elif(typePolice == "acc") :
            self.font = ('Comic Sans MS', 16, 'bold')
        try :
            self.texte = Label(parent.fen, text=texte_, fg=color, bg=back, font=self.font, anchor="n")
        except :
            self.texte = Label(parent, text=texte_, fg=color, bg=back, font=self.font, anchor="n")

        self.x = posX
        self.y = posY

        self.texte.grid(row=self.y, column=self.x) ## première affichage
        self.texte.grid_remove() ## on cache le texte

    def show(self) :
        self.texte.grid() ## affichage

    def hide(self) :
        self.texte.grid_remove() ## cache le texte mais garde ces propriété