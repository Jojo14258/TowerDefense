# Auteurs:

### View
# Ce module comporte le code pour afficher le jeu

import pygame, os, model

# des constantes
SCREEN_WIDTH = 866
SCREEN_HEIGHT = 514
couleur_boutons = (150, 150, 150)
couleur_fond = (25,200,25)

class View:
    """
    Une classe qui s'occupe de tout l'affichage.
    """

    def __init__(self, model):
        # on connecte la vue à l'état interne du jeu
        self.model = model
        # l'écran du jeu
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("image")
        self.imp = pygame.image.load("./ressources/jardin.png").convert()
        
        # liste des éléments à afficher
        self.elems = []

    def get_screen(self):
        return self.screen

    def add_elem(self, elem):
        self.elems.append(elem)

    def draw(self):
        """
        Fonction appellée à la fin de chaque tour de simulation du jeu
        """
        self.screen.blit(self.imp, (0, 0))
        # redessine le fond si besoin:
        #self.screen.fill(couleur_fond)

        # deplace les elements du jeux
        for elem in self.elems:
            elem.update()
            elem.draw(self.screen)

        # dessiner les boutons
        for b in self.model.boutons:
            self.screen.blit(b.img, (b.x + 3, b.y + 3))

        pygame.display.update()


class ViewPersonnage(pygame.sprite.Sprite):
    """
    Une classe qui permet d'afficher un personnage

    NOTE: Ne concerne pas la logique du personnage (Model), que l'affichage (V)
    NOTE: Cette classe est une sous-classe de Sprite.
          Cela permet d'utiliser les fonctions de la classe Sprite de pygame.
          https://www.pygame.org/docs/ref/sprite.html
    """

    def __init__(self, personnage):
        super().__init__()

        # les attributs de la classe
        self.personnage = personnage
        self.sprites = []   #séquence d'image pour l'animation
        self.actuelle = 0
        # l'image du personnage
     
        if ("zombie" in str(personnage.nom)) or ("peaShooter" in str(personnage.nom)):
            self.TabAnimation(personnage)
            
            
        else:
            self.image = pygame.image.load("ressources/personnage.png").convert_alpha() #si c'est le truc controlable du joueur, on met un .Png
            self.image = pygame.transform.scale(self.image, (30, 30))
            self.sprites.append(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.personnage.get_position()
    
    def TabAnimation(self, personnage):
        """
        personnage : - l'objet de classe personnage
        Génère un tableau d'animation à dérouler. L'animation se fait en fonction de la valeur dans l'attribut
        personnage.nom
        Voir vidéo https://www.youtube.com/watch?v=MYaxPa_eZS0
        """
        for i in range(1, len(os.listdir(f"ressources/{str(personnage.nom)}_marche"))):
                
                self.image = pygame.image.load(f"ressources/{str(personnage.nom)}_marche/frame-{i}.gif").convert_alpha()
                if "zombie" in str(self.personnage.nom):
                    self.image = pygame.transform.scale(self.image, (226, 153))
                elif "pea" in self.personnage.nom:
                    self.image = pygame.transform.scale(self.image, (185//2.7, 157//2.7))
                self.sprites.append(self.image)    #Initialisation d'un tableau contenant l'ensemble des image d'animation
        self.image = self.sprites[self.actuelle]
        
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        #self.image = pygame.image.load(f"ressources/{str(personnage.nom)}.gif") #si c'est un zombie, on met la version gif
        
    def animer(self, personnage, vitesse=0.0150):
        self.rect.x, self.rect.y = self.personnage.get_position()
        self.actuelle += personnage.vitesse
        if self.actuelle >= len(self.sprites):
            self.actuelle = 0
        self.image = self.sprites[int(self.actuelle)]
        
    def update(self):  
        if ("zombie" in str(self.personnage.nom)):
            self.animer(self.personnage, model.vitesse)
        else: #il s'agit d'une plante
            self.animer(self.personnage)

    def draw(self, screen):
        nouvelle_position = self.personnage.get_position()
        if "zombie" in str(self.personnage.nom):
            screen.blit(self.image, ((nouvelle_position[0] - self.image.get_width()/2), nouvelle_position[1] - self.image.get_height()+40))
        elif "pea" in str(self.personnage.nom):
            screen.blit(self.image, ((nouvelle_position[0] - self.image.get_width()/2.5), nouvelle_position[1] - self.image.get_height()+30))

 