import pygame

pygame.init()
pygame.font.init()

from model import *
from controller import *
from view import *

try:

    ### Initialisation
    model = Model()
    #modelZombie = Model()
    view = View(model)
    controller = Controller(model)
    #print(map(220,  154))
    
    
    
    
    
    # les boutons:
    bouton1 = Bouton("bouton1", 30, 30, 100, 50, "clique")
    model.ajouter_bouton(bouton1)

    # le personnage et son image:
    perso = Personnage(str("perso"),False) #2 attributs, nom et si NPC
    zombie1 = Zombie("zombie1", 1, 0.67) 
    zombie2 = Zombie("zombie1", 2, 0.047) 
    zombie3 = Zombie("zombie1", 3, 0.02) 
    peaShooter = Plante("peaShooter", 2, 0.07)
    peaShooter1 = Plante("peaShooter", 14, 0.07)
    perso.set_position((300, 300))
    model.personnage = perso
    #modelZombie.personnage = zombie1
    #modelZombie.persozombie2 = Zombie("zombie1", 2) 

    #vue_perso = ViewPersonnage(perso)
    
    
    #view.add_elem(vue_perso)
    view.add_elem(ViewPersonnage(zombie1))
    view.add_elem(ViewPersonnage(zombie2))
    view.add_elem(ViewPersonnage(zombie3))
    view.add_elem(ViewPersonnage(peaShooter))
    view.add_elem(ViewPersonnage(peaShooter1))
    i = 1
   
    ligne = 1
    print(peaShooter1.x, peaShooter1.y)
    ### Boucle du jeu
    # chaque tour de boucle est un 'pas' dans le jeux
    while not model.done:
        # d'abord les entrées utilisateur
        controller.gerer_input()
        # puis la logique du jeu
        #model.update()
        #modelZombie.update()
        i += 1
        zombie1.update()
        zombie1.modelPerso.update()
        zombie2.update()
        zombie2.modelPerso.update()
        zombie3.update()
        zombie3.modelPerso.update()
        peaShooter.update()
        peaShooter.modelPerso.update()
        tuile = zombie1.obtenir_tuile()
        if i%1000 == 0:
            
            if zombie1.obtenir_tuile() == None:
                if zombie1.obtenir_ligne() >=5:
                    zombie1.apparaitre(1)
                else:
                    zombie1.apparaitre(zombie1.obtenir_ligne()+1)
            if zombie2.obtenir_tuile() == None:
                if zombie2.obtenir_ligne() >=5:
                    zombie2.apparaitre(1)
                else:
                    zombie2.apparaitre(zombie2.obtenir_ligne()+1)
            if zombie3.obtenir_tuile() == None:
                if zombie3.obtenir_ligne() >=5:
                    zombie3.apparaitre(1)
                else:
                    zombie3.apparaitre(zombie3.obtenir_ligne()+1)
            
       # if tuile != zombie1.obtenir_tuile:
        #    print(tuile)
       #     tuile = zombie1.obtenir_tuile
            #print(zombie1.get_position())
            #print(i)
            
            
           
            
        
        zombie1.obtenir_tuile()
        # puis on affiche
        view.draw()
        #pygame.draw.line(view.screen, (255,0,0), (dictiTuile[12][0][0], dictiTuile[12][1][0]), (dictiTuile[12][0][1], dictiTuile[12][1][0]), 3)
        #pygame.draw.line(view.screen, (255,0,0), (dictiTuile[12][0][0], dictiTuile[12][1][0]), (dictiTuile[12][0][0], dictiTuile[12][1][1]), 3)

        pygame.display.flip()
       # for keys, value in dictiTuile.items():
        #    pygame.draw.line(view.screen, (255,0,0), (value[0][0], value[1][0]), (value[0][0], value[1][1]), 3)
         #   pygame.draw.line(view.screen, (255,0,0), (value[0][0], value[1][0]), (value[0][1], value[1][0]), 3)
            
          #  pygame.display.flip()

except Exception as e:
    pygame.quit()
    raise e

pygame.quit()
print("pygame_quit")