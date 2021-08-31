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

class Bouton :
    def __init__(self, parent, texte_, posX, posY) :
        try :
            self.bouton = Button(
                          parent.fen,
                          text=texte_,
                          font=('Californian FB', 22, 'bold'),
                          fg="#FFE699",
                          bg="#203864",
                          activeforeground = "#203864",
                          activebackground ="#FFE699",
                          width=100,
                          borderwidth=5
                          )
        except :
            self.bouton = Button(
                          parent,
                          text=texte_,
                          font=('Californian FB', 22, 'bold'),
                          fg="#FFE699",
                          bg="#203864",
                          activeforeground = "#203864",
                          activebackground ="#FFE699",
                          width=100,
                          borderwidth=5
                          )

        self.x = posX
        self.y = posY

        self.bouton.grid(row=self.y, column=self.x, sticky="s") ## première affichage
        self.bouton.grid_remove()

    def show(self) :
        self.bouton.grid() ## affichage

    def hide(self) :
        self.bouton.grid_remove() ## cache le texte mais garde ces