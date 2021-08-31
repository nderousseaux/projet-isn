# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      bastien Salvi
#
# Created:     05/04/2018
# Copyright:   (c) basts_kkzauqe 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import*
from sys import exit
from PIL import Image, ImageTk
# création d'une fenetre tkinter
menu = Tk()
menu.configure(bg="#36B1BF") #On confugure la couleur de la fenetre
menu.title("MENU") #ON donne le nom a la fenetre
menu.wm_geometry("500x700") #LA dimension de la fenetre est de 500 pixels sur 700 pixels

label = -1

#Fontion : ouvrir fenetre "fermer"




def ouvrir_fermer():


    # Fenetre "fermer"
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

    def fermer_les_deux():
        fermer.destroy()
        menu.destroy()

    bouton=Button(fermer, text="     OUI     ",command=fermer_les_deux, fg="#B9121B", bg="#4C1B1B", bd="7")
    # bouton qui se trouvera a gauche et a 62 pixel du bord
    bouton.pack(side=LEFT,padx =62, pady =0)
    bouton=Button(fermer, text="     NON     ",command=fermer.destroy, fg="#B9121B", bg="#4C1B1B", bd="7")
    # bouton qui se trouvera a droite et a 62 pixel du bord
    bouton.pack(side=RIGHT,padx =62, pady =0)


    # fermeture de la fenetre, "fermer"
    fermer.mainloop()



# On crès une fonction clignote
def clignotement():

    global canvas, photo_giro_state

        # Si le label est affiché
    if photo_giro_state == 'place':
                # On le cache et on change son statut
        canvas.itemconfigure("giro", state="hidden")
        photo_giro_state = 'not_place'
    # Sinon
    else:
                # On l'affiche et on change son status
        canvas.itemconfigure("giro", state="normal")
        photo_giro_state = 'place'

        # Et on boucle tout les 700ms
    menu.after(700, clignotement)


# Dans la fenetre on crée un texte sans rien pour faire un saut de ligne
txt = Label(menu, text="    ",bg='#36B1BF')
txt.pack()

# C'est le titre du jeu, avec les dimensions du texte, ca police, et la couleur de l'arrière plans
txt = Label(menu, text="COURSE POURSUITE",bg='#36B1BF', font="Arial 35 italic")
txt.pack()

# On agrémente les deux images, la voiture et le giro-phare
photo_police = PhotoImage(file=Image.open("./images/menu/police1.png"))
photo_giro = PhotoImage (file="./images/menu/lumiere_rouge.png")
e
# On crès un canevas dans la fenetre de 700 * 300 pixels
canvas = Canvas(menu,width=700, height=300,bg="#36B1BF" )
# On crès l'image dans le canevas à 50 et 60 pixels du bord pour permettree de centré l'image
canvas.create_image(50, 60, anchor=NW, image=photo_police, tags="photo_police")
# On crès l'image dans le canevas à 150 et 0 pixels du bord pour permettree de centré l'image, par rapport au giro-phare de la voiture
canvas.create_image(155, 0, anchor=NW, image=photo_giro, tags="giro")

# Avant de lancer la fonction clignotement, l'image du giro doient etre place
photo_giro_state = 'place'
clignotement()


# On ferme le caneva, et il s'execute
canvas.pack()

# Dans la fenetre on crèe un texte avec le mot "MENU"
txt = Label(menu, text="MENU",bg='#36B1BF', font="Arial 19 bold underline")
txt.pack()

# Dans la fenetre on crée un texte sans rien pour faire un saut de ligne
txt = Label(menu, text="    ",bg='#36B1BF')
txt.pack()

# On crès un bouton Fermer pour permettre de partir de la fenetre
bouton=Button(menu, text="                                          Fermer                                       ",command=ouvrir_fermer, bg="#E9F1DF", fg="#F5A503", bd="7")
bouton.pack()


# Dans la fenetre on crée un texte sans rien pour faire un saut de ligne
txt = Label(menu, text="    ",bg='#36B1BF')
txt.pack()

# On crès un bouton Jouer pour permettre de rentrer dans le jeu
bouton2=Button(menu, text="                                          Jouer                                          ", bg="#E9F1DF", fg="#F5A503", bd="7" )
bouton2.pack()


# ouverture de la fenetre, "fenetre"
menu.mainloop()




