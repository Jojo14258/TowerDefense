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
sprites_entites = {} #dicionaire dont les clés sont le nom des entités et les valeurs leur sprite d'animation sous la forme [[spriteAnimation1], [SpriteAnimation2]...]
   


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
        self.menu = pygame.image.load("ressources/Menu.jpg").convert_alpha()
        self.imp = pygame.image.load("./ressources/jardin.png").convert()
        self.PointsUI = pygame.image.load("ressources/UIPoints.png").convert_alpha()
        self.font = pygame.font.SysFont(None, 24)
        self.ecriturePoints = self.font.render(str(100), True, (0,0,0))
        self.Jouer = False #Le mode jeu n'est pas encore activé
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

        if self.Jouer:
            if "PeaShooter" in self.model.boutons.keys():
                Argent = self.model.boutons["PeaShooter"].monnaie #Si les boutons sont bien initialisés
                self.ecriturePoints = self.font.render(str(Argent), True, (0,0,0)) #ecriture du nombre d'argent
                if  Argent > 1000:
                    self.ecriturePoints = self.font.render(str(1000)+'+', True, (0,0,0))
                self.screen.blit(self.imp, (0, 0))
                self.screen.blit(self.PointsUI, (0,400))
                self.screen.blit(self.ecriturePoints, (32, 482)) #affichage de l'argent
            else:
                self.ecriturePoints = self.font.render(str(0)+'+', True, (0,0,0)) 

    
        # deplace les elements du jeux
        for elem in self.elems:
            elem.update()
            elem.draw(self.screen)

        # dessiner les boutons
        if "Jouer" in self.model.boutons.keys():
            if self.model.boutons["Jouer"].est_Clique: #Si le bouton "jouer" du menu est cliqué..."
                del self.model.boutons["Jouer"] #On le retire des boutons
            else:
                BoutonJouer = self.model.boutons["Jouer"] #Si le bouton n'est pas encore cliqué, on continue d'afficher le menu
                self.screen.blit(self.menu, (self.menu.get_rect().x, self.menu.get_rect().y))
                self.screen.blit(BoutonJouer.img, (BoutonJouer.rect.x, BoutonJouer.rect.y))
    
        elif "Jouer" not in self.model.boutons.keys():  #Si le bouon "jouer" a été supprimé (et cliqué donc)
            for instance in self.model.boutons.values(): #On parcours l'ensemble des boutons
                if instance.nom != "Jouer":  #On affiche tout sauf le bouton jouer qu'on retire
                    self.screen.blit(instance.img, (instance.rect.x, instance.rect.y))
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
        
        self.spritesTir = []  #séquence d'image pour l'animation de tir des plantes
        self.actuelle = 0 
        if ("zombie" in str(personnage.nom)) and (personnage.nom not in sprites_entites.keys()):
            self.TabAnimationZombie(personnage)
        elif ("peaShooter"  in str(personnage.nom)) or  ("wallnut" in str(personnage.nom) or ("sunFlower" in str(personnage.nom))):
            self.TabAnimationPlante(personnage)
        self.spritesMarche = sprites_entites[personnage.nom][0]   #séquence d'image pour l'animation basique de toute entité
        self.spritesManger =  sprites_entites[personnage.nom][1]   #séquence d'image pour l'animation manger des zombies
        self.image = self.spritesMarche[0]
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
            if personnage.nom not in sprites_entites.keys(): #Si nous n'avons pas déjà chargé une animation de l'entité
                sprites_entites[personnage.nom] = [self.image], [] #un tableau pour l'animation marche, un autre pour manger
            sprites_entites[personnage.nom][0].append(self.image)
                     #Initialisation d'un tableau contenant l'ensemble des image d'animation
            
        for i in range(1, len(os.listdir(f"ressources/{str(personnage.nom)}_manger"))):
            self.image = pygame.image.load(f"ressources/{str(personnage.nom)}_manger/frame-{i}.gif").convert_alpha()
            if "zombie1" in personnage.nom:
                self.image = pygame.transform.scale(self.image, (226//1.2, 153//1.2))
            elif "Gargantuar" in personnage.nom:
                self.image = pygame.transform.scale(self.image, (768//1.5, 724//1.5))
            elif "Football" in personnage.nom:
                self.image = pygame.transform.scale(self.image, (129//1.2, 156//1.2))
            

            
            sprites_entites[personnage.nom][1].append(self.image)  #Si nous n'avons pas chargé de tableau sprite pour l'animation manger
        

        
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
                self.image = pygame.transform.scale(self.image, (185//2.7, 157//2.7)) #On ajuste la taille de l'image en fonction du nom
            if "wallnut" in self.personnage.nom:
                self.image = pygame.transform.scale(self.image, (64//1.2, 72//1.2))
            if "sunFlower" in self.personnage.nom:
                self.image = pygame.transform.scale(self.image, (360//4, 360//4))
            if personnage.nom not in sprites_entites.keys(): #Si nous n'avons pas déjà chargé une animation de l'entité
                sprites_entites[personnage.nom] = [self.image], [] #un tableau pour l'animation marche, un autre tirer 
            sprites_entites[personnage.nom][0].append(self.image)
            
        if "pea" in self.personnage.nom: #seul les peas peuvent tirer, donc seuls eux ont une animation de tir
            for i in range(1, len(os.listdir(f"ressources/{str(personnage.nom)}_tir"))):
                self.image = pygame.image.load(f"ressources/{str(personnage.nom)}_tir/frame-{i}.gif").convert_alpha()
                self.image = pygame.transform.scale(self.image, (185//2.7, 157//2.7))
                self.spritesTir.append((self.image, f"frame-{i}.gif"))    #Initialisation d'un tableau contenant l'ensemble des image d'animation de tirs avec le nom de la frame
                sprites_entites[personnage.nom][1].append(self.image) 

    
    def animer(self, personnage, vitesse=0.0150):
        """
        personnage : - l'objet de la classe personnage.
        vitesse : int, attribut qui représente la vitesse d'animation de la classe personnage.
        Fonction pour parcourir les sprites de l'instance un à un.
        """
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
                    self.image = self.spritesTir[int(self.actuelle)]
                    self.Pea_Apparaitre()
                else:
                    self.image = self.spritesMarche[int(self.actuelle)] #Si la plante ne tire pas, on la fait marcher.
            if "wallnut" in personnage.nom:
                self.image = self.spritesMarche[int(self.actuelle)]
            if "sunFlower" in personnage.nom:
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
                
                if self.personnage.tirer:
                    screen.blit(self.image[0], ((nouvelle_position[0] - self.image[0].get_width()/2.5), nouvelle_position[1] - self.image[0].get_height()+30))
                    if len(projectiles) != 0: #si il y a un projectile tiré...
                        for element in projectiles:
                            screen.blit(element.image, ((element.get_position()[0] - self.image[0].get_width()/2.5)+60, element.get_position()[1] - self.image[0].get_height()+35))
                if not(self.personnage.tirer):
                    screen.blit(self.image, ((nouvelle_position[0] - self.image.get_width()/2.5), nouvelle_position[1] - self.image.get_height()+30))
                
            elif "wallnut" in str(self.personnage.nom):
                screen.blit(self.image, ((nouvelle_position[0] - self.image.get_width()/2.5), nouvelle_position[1] - self.image.get_height()+30))
            elif "sunFlower" in str(self.personnage.nom):
                screen.blit(self.image, ((nouvelle_position[0] - self.image.get_width()/2), nouvelle_position[1] - self.image.get_height()+30))
