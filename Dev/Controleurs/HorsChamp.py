
class ControleHC :
    def __init__(self, fen, can):
        self.Fen = fen
        self.Can = can

    def DelObjectHC(self):
    	# suppression des motifs hors champ
        self.Can.addtag_overlapping("HC" , -250, 2000, 2000, 2500) ## ajout d'un tag "hc" aux objets hors champs
        self.Can.delete("HC") ## suppression des objets portant le tag "hc"

        # boucle tkinter
        self.Fen.after(1, func=self.DelObjectHC)