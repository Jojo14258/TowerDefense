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
            self.screen.blit(b.img, (b.rect.x, b.rect.y))

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
        self.spritesMarche = []   #séquence d'image pour l'animation basique de toute entité
        self.spritesManger = []  #séquence d'image pour l'animation manger des zombies
        self.spritesTir = []  #séquence d'image pour l'animation de tir des plantes
        self.actuelle = 0 
        # l'image du personnage
     
        if ("zombie" in str(personnage.nom)):
            self.TabAnimationZombie(personnage)
        elif ("peaShooter" in str(personnage.nom)):
            self.TabAnimationPlante(personnage)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.personnage.get_position()
        self.rect.topleft = (personnage.x, personnage.y)
        self.personnage.collider = self.rect
        self.image.set_colorkey((0,0,0))
        
    def TabAnimationZombie(self, personnage):
        """
        personnage : - l'objet de classe personnage
        Génère un tableau d'animation à dérouler. L'animation se fait en fonction de la valeur dans l'attribut
        personnage.nom
        Voir vidéo https://www.youtube.com/watch?v=MYaxPa_eZS0
        """
        for i in range(1, len(os.listdir(f"ressources/{str(personnage.nom)}_marche"))):
            self.image = pygame.image.load(f"ressources/{str(personnage.nom)}_marche/frame-{i}.gif").convert_alpha()
            self.image = pygame.transform.scale(self.image, (226//1.2, 153//1.2))
            self.spritesMarche.append(self.image)    #Initialisation d'un tableau contenant l'ensemble des image d'animation
            
        for i in range(1, len(os.listdir(f"ressources/{str(personnage.nom)}_manger"))):
            self.image = pygame.image.load(f"ressources/{str(personnage.nom)}_manger/frame-{i}.gif").convert_alpha()
            self.image = pygame.transform.scale(self.image, (226//1.2, 153//1.2))
            self.spritesManger.append(self.image) 
        
        self.image = self.spritesMarche[self.actuelle]
        
        
        #self.image = pygame.image.load(f"ressources/{str(personnage.nom)}.gif") #si c'est un zombie, on met la version gif
        
        
    def TabAnimationPlante(self, personnage):
        """
        personnage : - l'objet de classe personnage
        Génère un tableau d'animation à dérouler. L'animation se fait en fonction de la valeur dans l'attribut
        personnage.nom
        Voir vidéo https://www.youtube.com/watch?v=MYaxPa_eZS0
        """
        for i in range(1, len(os.listdir(f"ressources/{str(personnage.nom)}_marche"))):
                
                self.image = pygame.image.load(f"ressources/{str(personnage.nom)}_marche/frame-{i}.gif").convert_alpha()
                if "pea" in self.personnage.nom:
                    self.image = pygame.transform.scale(self.image, (185//2.7, 157//2.7))
                self.spritesMarche.append(self.image)    #Initialisation d'un tableau contenant l'ensemble des image d'animation basique
        for i in range(1, len(os.listdir(f"ressources/{str(personnage.nom)}_tir"))):
                self.image = pygame.image.load(f"ressources/{str(personnage.nom)}_tir/frame-{i}.gif").convert_alpha()
                self.image = pygame.transform.scale(self.image, (185//2.7, 157//2.7))
                self.spritesTir.append(self.image)    #Initialisation d'un tableau contenant l'ensemble des image d'animation de tir
        self.image = self.spritesMarche[self.actuelle]
        
        #self.image = pygame.image.load(f"ressources/{str(personnage.nom)}.gif") #si c'est un zombie, on met la version gif
        
    def animer(self, personnage, vitesse=0.0150):
        if not(self.personnage.Est_mort):
            self.rect.x, self.rect.y = self.personnage.get_position()
            self.actuelle += personnage.vitesse
            nombre_image = len(self.spritesMarche)
            if "pea" in personnage.nom:
                if personnage.tirer:
                    nombre_image = len(self.spritesTir)
            if "zombie" in personnage.nom:
                if personnage.manger:
                    nombre_image = len(self.spritesManger)
            if self.actuelle >= nombre_image:
                self.actuelle = 0
            if "zombie" in personnage.nom:
                if personnage.manger:
                    self.image = self.spritesManger[int(self.actuelle)]
                else:
                    self.image = self.spritesMarche[int(self.actuelle)]
            if "pea" in personnage.nom:
                if personnage.tirer:
                    self.image = self.spritesTir[int(self.actuelle)]
                else:
                    self.image = self.spritesMarche[int(self.actuelle)]
        else:
            self.image = None 
            
    def update(self):  
        if ("zombie" in str(self.personnage.nom)):
            self.animer(self.personnage, self.personnage.vitesse)
        else: #il s'agit d'une plante
            self.animer(self.personnage)

    def draw(self, screen):
        if not(self.personnage.Est_mort):
            nouvelle_position = self.personnage.get_position()
            if "zombie" in str(self.personnage.nom):
                screen.blit(self.image, ((nouvelle_position[0] - self.image.get_width()/2), nouvelle_position[1] - self.image.get_height()+40))
            elif "pea" in str(self.personnage.nom):
                screen.blit(self.image, ((nouvelle_position[0] - self.image.get_width()/2.5), nouvelle_position[1] - self.image.get_height()+30))

 