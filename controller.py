# Auteurs:

### Controller
# Ce module comporte le code pour gérer l'interaction avec l'utilisateur-rice

import pygame
from model import *
from view import *

# des constantes
texte_bouton = pygame.font.SysFont('Corbel', 30, bold=True)


class Controller:
    """
    Une classe qui s'occupe de gérer toutes les entrées de l'utilisateur-rice.
    """

    def __init__(self, model):
        self.model = model
        
    def obtenir_tuile(x, y):
        for keys, values in dictiTuile.items():
            if (values[0][0] <= x <= values[0][1]) and (values[1][0] <= y <= values[1][1]):
                return keys 
        #print("Erreur de code")
        return None
    
    def gerer_input(self):

        souris_x, souris_y = pygame.mouse.get_pos()
     

        for event in pygame.event.get():

            ### clavier
            if event.type == pygame.KEYDOWN:
                
                # fermer le jeux
                if event.key == pygame.K_ESCAPE:
                    self.model.done = True

                # deplacer le personnage
                if event.key == pygame.K_UP:
                    self.model.personnage.deplacer("haut")
                if event.key == pygame.K_DOWN:
                    self.model.personnage.deplacer("bas")
                if event.key == pygame.K_LEFT:
                    self.model.personnage.deplacer("gauche")
                if event.key == pygame.K_RIGHT:
                    self.model.personnage.deplacer("droite")
            ### souris
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for bouton in self.model.boutons:
                    bouton.est_cible(souris_x, souris_y)
                    if bouton.clique:
                        print(bouton.clique)
                        if bouton.nom == "PeaShooter":
                            tuile = obtenir_tuile(souris_x, souris_y)
                            if tuile != None:
                                peaShooter = Plante("peaShooter",tuile ,0.07)
                                peaShooter.apparaitre(tuile)
                               
                                
                                
                                

                                
            

            ### fenetre
            elif event.type == pygame.QUIT:
                self.model.done = True


class Bouton:
    """
    Classe qui modélise un bouton à cliquer
    """

    def __init__(self, nom, x, y, img, scale):
        # on utilise un nom pour différencier les boutons
        #https://www.youtube.com/watch?v=G8MYGDf_9ho Vidéo utilisé
        self.nom = nom
        self.largeur = img.get_width()
        self.hauteur = img.get_height()
        self.img = pygame.transform.scale(img, (int(self.largeur*scale), int(self.hauteur*scale)))
        self.clique = False
        
        
        self.x, self.y = x, y
        self.rect = self.img.get_rect()
        #self.rect.topleft = (x, y)
    def est_cible(self, x, y):
        """
        x et y : la position de la souris
        Sortie : Vrai si la souris est sur le bouton, Faux sinon
        """
        
        souris_x, souris_y = pygame.mouse.get_pos()
        
        if self.img.get_rect().collidepoint(souris_x, souris_y) and self.clique == False:
            self.clique = True
        
        elif self.img.get_rect().collidepoint(souris_x, souris_y) and self.clique:
            self.clique = False
        



