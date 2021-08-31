#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      basts_kkzauqe
#
# Created:     06/05/2018
# Copyright:   (c) basts_kkzauqe 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import*
from sys import*

gagner = Tk()
gagner.configure(bg="#FFFF6B") #On confugure la couleur de la fenetre
gagner.title("GAGNER") #ON donne le nom a la fenetre
gagner.wm_geometry("700x400") #LA dimension de la fenetre est de 700 pixels sur 400 pixels

txt = Label(gagner, text="    ",bg='#FFFF6B')
txt.pack()

canvas_B = Canvas(gagner,width=650, height=300,bg="#F6DC12")

txt = canvas_B.create_text(320, 70, text="VOUS  AVEZ", font="Algerian 40 bold", fill="#B9121B")

txt = canvas_B.create_text(325, 120, text="  GAGNER  ", font="Algerian 40 bold", fill="#B9121B")

txt = canvas_B.create_text(330, 180, text="Le voleur a été capturé", font="Arial 25 italic", fill="#B9121B")

canvas_B.pack()

txt = Label(gagner, text="    ",bg='#FFFF6B')
txt.pack()

bouton_sortie=Button(gagner, text="        QUITTER        ",command=gagner.destroy, fg="#B9121B", bg="#F6DC12", bd="7")
bouton_sortie.pack()

gagner.mainloop()
