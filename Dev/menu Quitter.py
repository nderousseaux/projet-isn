#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      basts_kkzauqe
#
# Created:     17/04/2018
# Copyright:   (c) basts_kkzauqe 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import*

fermer=Tk()
# création d'une fenetre tkinter
fermer.configure(bg="#B9121B") #On confugure la couleur de la fenetre
fermer.title("FERMER") #ON donne le nom a la fenetre
fermer.wm_geometry("400x220") #LA dimension de la fenetre est de 400 pixels sur 220 pixels

# Dans la fenetre on crée un texte sans rien pour faire un saut de ligne
txt = Label(fermer, text="    ",bg='#B9121B')
txt.pack()

# On crès un canevas dans fermer de 300 * 125 pixels
canvas = Canvas(fermer,width=300, height=125,bg="#4C1B1B")

# Crèe un texte dans le canevas
txt = canvas.create_text(150, 50, text="QUITTER", font="Arial 25 bold", fill="#B9121B")
txt = canvas.create_text(50, 100, text="OUI", font="Arial 20", fill="#B9121B")
txt = canvas.create_text(250, 100, text="NON", font="Arial 20", fill="#B9121B")

# On ferme le caneva, et il s'execute
canvas.pack()


txt = Label(fermer, text="    ",bg='#B9121B')
txt.pack()

bouton=Button(fermer, text="Fermer",command=fermer.destroy, fg="#B9121B", bg="#4C1B1B", bd="7")
bouton.pack()
bouton=Button(fermer, text="Fermer",command=fermer.destroy, fg="#B9121B", bg="#4C1B1B", bd="7")
bouton.pack()



# fermeture de la fenetre, "fermer"
fermer.mainloop()