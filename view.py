# Auteurs:

### View
# Ce module comporte le code pour afficher le jeu

import pygame, os, model

# des constantes
SCREEN_WIDTH = 866
SCREEN_HEIGHT = 514
ecran =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #optimisation : on génère une fois l'écran
couleur_boutons = (150, 150, 150)
couleur_fond = (25,200,25)
projectiles = []  #tableau de l'ensemble des projectiles

#initialisation des images 
image_pea = pygame.image.load("./ressources/Pea.png").convert_alpha() #optimisation - au lieu de load dans une classe, on la fait une fois ici
image_pea = pygame.transform.scale(image_pea, (2000//70, 2000//70)) #cela permet de ne pas charger à chaque instance l'image lorsqu'un pea est tiré

class View:
    """
    Une classe qui s'occupe de tout l'affichage.
    """

    def __init__(self, model):
        # on connecte la vue à l'état interne du jeu
        self.model = model
        # l'écran du jeu
        self.screen = ecran
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
        #Initialisation des images
        self.personnage = personnage
        self.temps = 0
        self.spritesMarche = []   #séquence d'image pour l'animation basique de toute entité
        self.spritesManger = []  #séquence d'image pour l'animation manger des zombies
        self.spritesTir = []  #séquence d'image pour l'animation de tir des plantes
        self.actuelle = 0 
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
            if "zombie1" in personnage.nom:
                self.image = pygame.transform.scale(self.image, (226//1.2, 153//1.2))
            elif "Football" in personnage.nom:
                self.image = pygame.transform.scale(self.image, (129//1.2, 156//1.2))
            elif "Gargantuar" in personnage.nom:
                self.image = pygame.transform.scale(self.image, (768//2, 724//2))
            elif "zombieX" in personnage.nom:
                self.image = pygame.transform.scale(self.image, (226//2.1, 153//1.8))
            self.spritesMarche.append(self.image)    #Initialisation d'un tableau contenant l'ensemble des image d'animation
            
        for i in range(1, len(os.listdir(f"ressources/{str(personnage.nom)}_manger"))):
            self.image = pygame.image.load(f"ressources/{str(personnage.nom)}_manger/frame-{i}.gif").convert_alpha()
            if "zombie1" in personnage.nom:
                self.image = pygame.transform.scale(self.image, (226//1.2, 153//1.2))
            elif "Gargantuar" in personnage.nom:
                self.image = pygame.transform.scale(self.image, (768//1.5, 724//1.5))
            elif "Football" in personnage.nom:
                self.image = pygame.transform.scale(self.image, (129//1.2, 156//1.2))
            
            self.spritesManger.append(self.image) 
        
        self.image = self.spritesMarche[self.actuelle]
        
        
        #self.image = pygame.image.load(f"ressources/{str(personnage.nom)}.gif") #si c'est un zombie, on met la version gif
        
    def Pea_Apparaitre(self):
        """
        Cette fonction permet au PeaShooter d'envoyer un projectile (Pea). 
        Le délai est géré par la vitesse d'animation, lorsqu'une certaine frame spécifique est atteinte, 
        une nouvelle instance Pea est automatiquement créé et répertiorié dans la variable globale "projectiles" dont les éléments
        sont mis à jour dans le while du main.
        """
        image_Projectile = pygame.transform.scale(image_pea, (2000//70, 2000//70)) 
        if self.spritesTir[int(self.actuelle)][1] == "frame-33.gif":
            self.actuelle += 1
            Pea = model.Pea(self.personnage.tuile, 1, self.personnage.degats, "Pea")
            projectiles.append(Pea)
            
        
    def TabAnimationPlante(self, personnage):
        """
        personnage : - l'objet de classe personnage
        Génère un tableau d'animation à dérouler (sprite). L'animation se fait en fonction de la valeur dans l'attribut
        personnage.nom
        Voir vidéo https://www.youtube.com/watch?v=MYaxPa_eZS0
        """
        for i in range(1, len(os.listdir(f"ressources/{str(personnage.nom)}_marche"))):
                
                self.image = pygame.image.load(f"ressources/{str(personnage.nom)}_marche/frame-{i}.gif").convert_alpha()
                if "pea" in self.personnage.nom:
                    self.image = pygame.transform.scale(self.image, (185//2.7, 157//2.7))
                self.spritesMarche.append(self.image)    #Initialisation d'un tableau contenant l'ensemble des image d'animation basique
                self.image = self.spritesMarche[self.actuelle]
        for i in range(1, len(os.listdir(f"ressources/{str(personnage.nom)}_tir"))):
                self.image = pygame.image.load(f"ressources/{str(personnage.nom)}_tir/frame-{i}.gif").convert_alpha()
                self.image = pygame.transform.scale(self.image, (185//2.7, 157//2.7))
                self.spritesTir.append((self.image, f"frame-{i}.gif"))    #Initialisation d'un tableau contenant l'ensemble des image d'animation de tir
                self.image = self.spritesMarche[self.actuelle]
    
    def animer(self, personnage, vitesse=0.0150):
        if not(self.personnage.Est_mort):
            self.rect.x, self.rect.y = self.personnage.get_position()
            
            nombre_image = len(self.spritesMarche)
            if "pea" in personnage.nom:  #On initialise la longueur du sprite à parcourir en fonction de l'instance.
                if personnage.tirer:
                    nombre_image = len(self.spritesTir)
            if "zombie" in personnage.nom:
                if personnage.manger:
                    nombre_image = len(self.spritesManger)
            self.actuelle += personnage.vitesse
            if self.actuelle >= nombre_image:
                self.actuelle = 0
            if "zombie" in personnage.nom:
                if personnage.manger:
                    self.image = self.spritesManger[int(self.actuelle)]
                else:
                    self.image = self.spritesMarche[int(self.actuelle)]
            if "pea" in personnage.nom:
                if personnage.tirer:    #On charge l'animation de tir
                    self.image = self.spritesTir[int(self.actuelle)][0]
                    self.Pea_Apparaitre()
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
                if len(projectiles) != 0: #si il y a un projectile tiré...
                    for element in projectiles:
                        screen.blit(element.image, ((element.get_position()[0] - self.image.get_width()/2.5)+60, element.get_position()[1] - self.image.get_height()+35))
