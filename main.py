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
    
    dictiTuile = map(220,  155) #génération d'une matrice
    for key, value in dictiTuile.items():  #On réarrange les imperfection causé par les irrégularités du terrain
        if key >= 45:
            dictiTuile[key][0][1] += 40
            dictiTuile[key][0][0] += 40
        elif key >= 44:
            dictiTuile[key][0][1] += 30
            dictiTuile[key][0][0] += 30
        elif key >= 43:
            dictiTuile[key][0][1] += 25
            dictiTuile[key][0][0] += 25
        elif key >= 42:
            dictiTuile[key][0][1] += 20
            dictiTuile[key][0][0] += 20
        elif key >= 41:
            dictiTuile[key][0][1] += 15
            dictiTuile[key][0][0] += 15
        elif key >= 40:
            dictiTuile[key][0][1] += 10
            dictiTuile[key][0][0] += 10
        elif key >= 38:
            dictiTuile[key][0][1] += 10
            dictiTuile[key][0][0] += 10
            
        elif key >= 37:
            dictiTuile[key][0][1] -= 10
            dictiTuile[key][0][0] -= 10
            
        elif key >= 36:
            dictiTuile[key][0][1] += 40
            dictiTuile[key][0][0] += 40
        elif key >= 33:
            dictiTuile[key][0][1] += 25
            dictiTuile[key][0][0] += 25
            
        elif key >= 31:
            dictiTuile[key][0][1] += 20
            dictiTuile[key][0][0] += 20
        elif key >= 29:
            dictiTuile[key][0][1] += 10
            dictiTuile[key][0][0] += 10
        elif key >= 28:
            dictiTuile[key][0][1] -= 5
            dictiTuile[key][0][0] -= 5
        elif key >= 25:
            dictiTuile[key][0][1] += 35
            dictiTuile[key][0][0] += 35
        elif key >=24:
            dictiTuile[key][0][1] += 20
            dictiTuile[key][0][0] += 20
        elif key >=22:
            dictiTuile[key][0][1] += 20
            dictiTuile[key][0][0] += 20
        elif key >= 21:
            dictiTuile[key][0][1] += 5
            dictiTuile[key][0][0] += 5
            
        elif key >= 20:
            dictiTuile[key][0][1] += 7
            dictiTuile[key][0][0] += 7
            
            
        elif key >= 19:
            dictiTuile[key][0][1] -= 5
            dictiTuile[key][0][0] -= 5
        
        elif key >=18:
            dictiTuile[key][0][1] += 28
            dictiTuile[key][0][0] += 28
        
        elif key >=15:
            dictiTuile[key][0][1] += 25
            dictiTuile[key][0][0] += 25
        
        
        elif key >= 13:
            dictiTuile[key][0][1] += 15
            dictiTuile[key][0][0] += 15
        
        elif key >= 12:
            dictiTuile[key][0][1] += 5
            dictiTuile[key][0][0] += 5
        elif key >= 10:
            dictiTuile[key][0][1] -= 2
            dictiTuile[key][0][0] -= 2
        elif key >= 5:
            dictiTuile[key][0][1] += 25
            dictiTuile[key][0][0] += 25
            
        elif key >= 3:
            dictiTuile[key][0][1] += 10
            dictiTuile[key][0][0] += 10
        
    dictiTuile[2][0][1] += 10
    dictiTuile[4][0][1] += 15
    dictiTuile[11][0][1] = 353
    dictiTuile[12][0][1] = 427
    dictiTuile[14][0][1] = 565
    dictiTuile[17][0][1] = 760
    #dictiTuile[18][0][1] = 215
    dictiTuile[19][0][1] = 291
    dictiTuile[20][0][1] = 353
    dictiTuile[21][0][1] = 432
    dictiTuile[24][0][1] = 639
    #dictiTuile[27][0][1] = 215
    dictiTuile[28][0][1] = 294
    dictiTuile[30][0][1] = 432
    dictiTuile[32][0][1] = 565
    dictiTuile[35][0][1] = 772
    #dictiTuile[36][0][1] = 210
    dictiTuile[37][0][1] = 294
    dictiTuile[40][0][1] = 491
    dictiTuile[41][0][1] = 560
    dictiTuile[42][0][1] = 629
    dictiTuile[43][0][1] = 698
    dictiTuile[44][0][1] = 772
  
    print(dictiTuile)
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
        #model.update()
        #modelZombie.update()
        # puis on affiche
        view.draw()
        #pygame.draw.line(view.screen, (255,0,0), (dictiTuile[18][0][0], dictiTuile[18][1][0]), (dictiTuile[18][0][1], dictiTuile[18][1][0]), 3)
        #pygame.draw.line(view.screen, (255,0,0), (dictiTuile[18][0][0], dictiTuile[18][1][0]), (dictiTuile[18][0][0], dictiTuile[18][1][1]), 3)

        pygame.display.flip()
        for keys, value in dictiTuile.items():
            pygame.draw.line(view.screen, (255,0,0), (value[0][0], value[1][0]), (value[0][0], value[1][1]), 3)
            pygame.draw.line(view.screen, (255,0,0), (value[0][0], value[1][0]), (value[0][1], value[1][0]), 3)
            
            pygame.display.flip()

except Exception as e:
    pygame.quit()
    raise e

pygame.quit()
print("pygame_quit")
