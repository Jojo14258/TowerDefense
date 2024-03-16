# Auteurs:

### View
# Ce module comporte le code pour afficher le jeu

import pygame

# des constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
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
        pygame.display.set_caption("Planet Simulation")

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

        # redessine le fond si besoin:
        self.screen.fill(couleur_fond)

        # deplace les elements du jeux
        for elem in self.elems:
            elem.update()
            elem.draw(self.screen)

        # dessiner les boutons
        for b in self.model.boutons:
            pygame.draw.rect(self.screen,couleur_boutons,[b.x, b.y, b.largeur, b.longueur])
            if b.text != None:
                self.screen.blit(b.text, (b.x + 3, b.y + 3))

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
        # l'image du personnage
        self.image = pygame.image.load("ressources/personnage.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.personnage.get_position()

    def update(self):
        self.rect.x, self.rect.y = self.personnage.get_position()

    def draw(self, screen):
        nouvelle_position = self.personnage.get_position()
        screen.blit(self.image, nouvelle_position)

