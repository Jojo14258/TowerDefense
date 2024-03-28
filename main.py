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
    #print(map(220,  154))
    
    
    
    
    print(dictiTuile)
    # les boutons:
    bouton1 = Bouton("bouton1", 30, 30, 100, 50, "clique")
    model.ajouter_bouton(bouton1)

    # le personnage et son image:
    perso = Personnage(str("perso"),False) #2 attributs, nom et si NPC
    zombie1 = Zombie(str("zombie1")) 
    zombie1.set_position((701,301))
    perso.set_position((300, 300))
    model.personnage = perso
    modelZombie.personnage = zombie1
    
    vue_perso = ViewPersonnage(perso)
    view.add_elem(vue_perso)
    view.add_elem(ViewPersonnage(zombie1))

    
    i = 1
   

    ### Boucle du jeu
    # chaque tour de boucle est un 'pas' dans le jeux
    while not model.done:
        # d'abord les entrées utilisateur
        controller.gerer_input()
        # puis la logique du jeu
        #model.update()
        modelZombie.update()
        if i == 1:
            print(zombie1.get_position())
            print(zombie1.obtenir_tuile())
            zombie1.set_position((780, 400))
            print(i)
            i += 1
        
        zombie1.obtenir_tuile()
        # puis on affiche
        view.draw()
        #pygame.draw.line(view.screen, (255,0,0), (dictiTuile[45][0][0], dictiTuile[45][1][0]), (dictiTuile[45][0][1], dictiTuile[45][1][0]), 3)
        #pygame.draw.line(view.screen, (255,0,0), (dictiTuile[45][0][0], dictiTuile[45][1][0]), (dictiTuile[45][0][0], dictiTuile[45][1][1]), 3)

        #pygame.display.flip()
        #for keys, value in dictiTuile.items():
            #pygame.draw.line(view.screen, (255,0,0), (value[0][0], value[1][0]), (value[0][0], value[1][1]), 3)
            #pygame.draw.line(view.screen, (255,0,0), (value[0][0], value[1][0]), (value[0][1], value[1][0]), 3)
            
            #pygame.display.flip()

except Exception as e:
    pygame.quit()
    raise e

pygame.quit()
print("pygame_quit")

