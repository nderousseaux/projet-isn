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

perdu = Tk()
perdu.configure(bg="#FF0000") #On confugure la couleur de la fenetre
perdu.title("PERDU") #ON donne le nom a la fenetre
perdu.wm_geometry("700x400") #LA dimension de la fenetre est de 700 pixels sur 400 pixels

txt = Label(perdu, text="    ",bg='#FF0000')
txt.pack()

canvas_C = Canvas(perdu,width=650, height=300,bg="#E9383F")

txt = canvas_C.create_text(320, 70, text="VOUS  AVEZ", font="Algerian 40 bold", fill="#FFF000")

txt = canvas_C.create_text(325, 120, text="  PERDU  ", font="Algerian 40 bold", fill="#FFF000")

txt = canvas_C.create_text(330, 180, text="Le voleur n'a pas été capturé", font="Arial 25 italic", fill="#FFF000")

canvas_C.pack()

txt = Label(perdu, text="    ",bg='#FF0000')
txt.pack()

bouton_sortie=Button(perdu, text="        QUITTER        ",command=perdu.destroy, fg="#FFF000", bg="#E9383F", bd="7")
bouton_sortie.pack()

perdu.mainloop()