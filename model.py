# Auteurs:

### Model
# Ce module comporte tout l'état interne et la logique du jeu

import pygame

# des constantes
STEP_SIZE = 20

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
