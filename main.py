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
    img = pygame.image.load("./ressources/boutons/Peashooter.png").convert_alpha()
    #bouton1 = Bouton("bouton1", 30, 30, 100, 50, "clique")
    PeaShooterBouton = Bouton("PeaShooter", 75, 75,  img, 1)
    model.ajouter_bouton(PeaShooterBouton)
    #model.ajouter_bouton()

    # le personnage et son image:
    perso = Personnage(str("perso"),False) #2 attributs, nom et si NPC
    zombie1 = Zombie("zombie1", 1, 0.20, 200, 100)  
    zombie2 = Zombie("zombie1", 2, 0.67, 200, 100) 
    zombie3 = Zombie("zombie1", 3, 0.67, 200, 100) 
    perso.set_position((300, 300))
    model.personnage = perso
    #modelZombie.personnage = zombie1
    #modelZombie.persozombie2 = Zombie("zombie1", 2) 

    #vue_perso = ViewPersonnage(perso)
   
    #view.add_elem(vue_perso)
    view.add_elem(ViewPersonnage(zombie1))
    view.add_elem(ViewPersonnage(zombie2))
    view.add_elem(ViewPersonnage(zombie3))
    i = 1
   
    ligne = 1
    clock = pygame.time.Clock()
    ### Boucle du jeu
    # chaque tour de boucle est un 'pas' dans le jeux
    while not model.done:
        clock.tick(60)  #Le jeu est fait pour être joué à 60 FPS
        # d'abord les entrées utilisateur
        controller.gerer_input()
        # puis la logique du jeu
        if len(PeaShooterActuelles) > NbPlantes: #Si une plante a été ajoutée...
           
            view.add_elem(ViewPersonnage(PeaShooterActuelles[-1])) #Ajout de la dernière plante (Pile)
            NbPlantes = len(PeaShooterActuelles) #on réajuste le total
        i += 1
        for element in view.elems:
            element.personnage.update()
            element.personnage.modelPerso.update()
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
        view.draw()
        pygame.display.flip()

except Exception as e:
    pygame.quit()
    raise e

pygame.quit()
print("pygame_quit")
