# Auteurs:

### Main pour notre jeu
# L'architecture du jeu utilise trois modules selon le patron de conception MVC

import pygame

pygame.init()
pygame.font.init()

from model import *
from controller import *
from view import *

try:

    ### Initialisation
    model = Model()
    modelZombie = Model()
    view = View(model)
    controller = Controller(model)

    # les boutons:
    bouton1 = Bouton("bouton1", 30, 30, 100, 50, "clique")
    model.ajouter_bouton(bouton1)

    # le personnage et son image:
    perso = Personnage(str("perso"),False) #2 attributs, nom et si NPC
    zombie1 = Personnage(str("zombie1")) 
    zombie1.set_position((701,301))
    perso.set_position((300, 300))
    model.personnage = perso
    modelZombie.personnage = zombie1
    
    vue_perso = ViewPersonnage(perso)
    view.add_elem(vue_perso)
    view.add_elem(ViewPersonnage(zombie1))

    ### Boucle du jeu
    # chaque tour de boucle est un 'pas' dans le jeux
    while not model.done:
        # d'abord les entrées utilisateur
        controller.gerer_input()
        # puis la logique du jeu
        model.update()
        modelZombie.update()
        # puis on affiche
        view.draw()

except Exception as e:
    pygame.quit()
    raise e

pygame.quit()
print("pygame_quit")

