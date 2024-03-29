# Auteurs:

### Model
# Ce module comporte tout l'état interne et la logique du jeu

import pygame

# des constantes
STEP_SIZE = 20


def carteVersMatrice(x, y):
    longueur = 64  #debut = 284 - 220 
    largeur = 81  #235 - 154
    departy = (y-largeur)
    dictTuiles = {}
    for y in range(0,5):
        departx = x
        numero = 9*(y)+1
        while numero <= 9*y+9:
            dictTuiles[numero] = [departx, departx+longueur], [departy, departy+largeur]
            departx += longueur
            numero += 1
        departy += largeur
    return dictTuiles

dictiTuile = carteVersMatrice(220,  155) #génération d'une matrice
#On corrige les imperfections liés aux irrégularités du terrain (voir le commit 04.5 du Github pour la correction manuelle avec le code)
dictiTuile = {1: ([220, 284], [74, 155]), 2: ([284, 358], [74, 155]), 3: ([358, 422], [74, 155]), 4: ([422, 501], [74, 155]), 5: ([501, 565], [74, 155]), 6: ([565, 629], [74, 155]), 7: ([629, 693], [74, 155]), 8: ([693, 757], [74, 155]), 9: ([757, 821], [74, 155]), 10: ([218, 282], [155, 236]), 11: ([282, 353], [155, 236]), 12: ([353, 427], [155, 236]), 13: ([427, 491], [155, 236]), 14: ([491, 565], [155, 236]), 15: ([565, 629], [155, 236]), 16: ([629, 693], [155, 236]), 17: ([693, 760], [155, 236]), 18: ([760, 824], [155, 236]), 19: ([215, 291], [236, 317]), 20: ([291, 353], [236, 317]), 21: ([353, 432], [236, 317]), 22: ([432, 496], [236, 317]), 23: ([496, 560], [236, 317]), 24: ([560, 639], [236, 317]), 25: ([639, 703], [236, 317]), 26: ([703, 767], [236, 317]), 27: ([767, 831], [236, 317]), 28: ([215, 294], [317, 398]), 29: ([294, 358], [317, 398]), 30: ([358, 432], [317, 398]), 31: ([432, 496], [317, 398]), 32: ([496, 565], [317, 398]), 33: ([565, 629], [317, 398]), 34: ([629, 693], [317, 398]), 35: ([693, 772], [317, 398]), 36: ([772, 836], [317, 398]), 37: ([210, 294], [398, 479]), 38: ([294, 358], [398, 479]), 39: ([358, 422], [398, 479]), 40: ([422, 491], [398, 479]), 41: ([491, 560], [398, 479]), 42: ([560, 629], [398, 479]), 43: ([629, 698], [398, 479]), 44: ([698, 772], [398, 479]), 45: ([772, 836], [398, 479])}

class Model:
    """
    Une classe qui contient tous les éléments logiques du jeux
    """

    def __init__(self):

        # on initialise les attributs necessaires
        self.personnage = None
        self.boutons = []

        # un booleen qui dit si le jeu est fini
        self.done = False

    def done(self):
        """
        Renvoie si le jeu est fini
        """
        return done

    def ajouter_bouton(self, bouton):
        """
        Fonction qui permet de rajouter un bouton a la liste des boutons
        """
        self.boutons.append(bouton)

    def update(self):
        """
        Fonction appellée à chaque tour de simulation du jeu
        """
        # on update chaque éléments
        self.personnage.update()


class Personnage:
    """
    Une classe qui modélise un personnage
    NOTE: ca ne concerne pas l'affichage (View), que le modéle (M)
    """

    def __init__(self, nom, NPC=True):
        """
        NPC - : Bool, True si il s'agit d'un personnage contrôlable par le joueur, fase sinon.
        """
        self.x = 0
        self.y = 0
        self.nom = nom
        self.NPC = NPC
    

    def get_position(self):
        return (self.x, self.y)

    def obtenir_tuile(self):
        for keys, values in dictiTuile.items():
            if (values[0][0] <= self.x <= values[0][1]) and (values[1][0] <= self.y <= values[1][1]):
                return keys 
        #print("Erreur de code")
        return "Erreur de code"
    
    def set_position(self, pos):
        self.x, self.y = pos
        
    

    def deplacer(self, direction):

        if not(self.NPC):
            if direction == "haut":
                self.y += -STEP_SIZE
            if direction == "bas":
                self.y -= -STEP_SIZE
            if direction == "droite":
                self.x -= -STEP_SIZE
            if direction == "gauche":
                self.x += -STEP_SIZE

    def update(self):
        if self.NPC:
            self.x -= 0.010 #vitesse déplacement
            self.set_position((self.x, self.y))
class Zombie(Personnage):
    """
    Une sous classe enfant de la classe Personnage.
    """