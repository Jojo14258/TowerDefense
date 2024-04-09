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
                    if bouton.est_Clique:
                        if bouton.nom == "PeaShooter":
                            for element in self.model.boutons: #parcours des boutons
                                if element.est_Clique and (not("Pea" in element.nom)): #Si un autre bouton est déjà cliqué...
                                    element.deselectionner() #on déselectionne l'autre bouton déjà cliqué
                            tuile = obtenir_tuile(souris_x, souris_y)
                            bouton_sauvegarde = bouton
                            if (tuile != None) and (tuile not in dico_plantes.keys()): #Si une plante n'est pas déjà placé sur la tuile...
                                peaShooter = PeaShooter("peaShooter",tuile ,0.8, 600, 40, 5) 
                                peaShooter.apparaitre(tuile)
                                
                        elif bouton.nom == "Wallnut":
                            for element in self.model.boutons:
                                if element.est_Clique and (not("Wallnut" in element.nom)):
                                    element.deselectionner()
                            tuile = obtenir_tuile(souris_x, souris_y)
                            bouton_sauvegarde = bouton
                            if (tuile != None) and (tuile not in dico_plantes.keys()):
                                wallnut = Wallnut("wallnut",tuile ,0.3, 900)
                                wallnut.apparaitre(tuile)

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
        self.est_Clique = False
        
        
        self.x, self.y = x, y
        self.rect = self.img.get_rect(topleft = (self.x, self.y)) #synchronisation de la collision du bouton avec l'image
        
        pygame.draw.rect(self.img, (0,0,0), [0, 0, self.rect.width, self.rect.height], 2)
        #self.rect.topleft = (x, y)
        
    def deselectionner(self):
        """
        Une fonction pour déselectionner un bouton.
        Sortie - None : Modifie par effet de bord l'attribut est_Clique (bool) à False et redessine la bordure du bouton. 
        """
        self.est_Clique = False
        pygame.draw.rect(self.img, (0,0,0), [0, 0, self.rect.width, self.rect.height], 2)
    def est_cible(self, x, y):
        """
        x et y : la position de la souris
        Sortie - None : modifie par effet de bord l'attribut est_Clique à True (bool) si la souris est sur le bouton, False (bool) sinon
        """
        
        souris_x, souris_y = pygame.mouse.get_pos()
       # print(self.est_Clique)
        if self.rect.collidepoint(souris_x, souris_y) and self.est_Clique == False:
            self.est_Clique = True
            pygame.draw.rect(self.img, (255,0,0), [0, 0, self.rect.width, self.rect.height], 2)

       
        elif self.rect.collidepoint(souris_x, souris_y) and self.est_Clique:
            
            self.deselectionner()




