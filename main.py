import pygame

pygame.init()
pygame.font.init()

from model import *
from controller import *
from view import *
from random import randint
try:

    ### Initialisation
    model = Model()
    #modelZombie = Model()
    view = View(model)
    controller = Controller(model)
    compteur = 0
    compteur1 = 0
    compteur2 = 0
    zombies_par_niveaux = {1: {"zombie1": 5}, 2:{"zombie1": 5, "zombieFootball":5}} #dictionnaire de la forme {niveau: {zombies:nombre} }. Permet de définir le nombre de zombies par niveaux.
    Nombre_zombie_par_niveaux = {1:5, 2:10}
    zombies_caracteristiques = {"zombie1":["zombie1", randint(1,5), 0.3, 0.5, 200, 100], "zombieFootball": ["zombieFootball", randint(1,5), 0.9, 0.2, 200, 100]}
    niveau_actuel = 1
    Perdu = False
    #print(map(220,  154))
    
    
    
    
    # les boutons:
    img = pygame.image.load("./ressources/boutons/Peashooter.png").convert_alpha()
    img2 = pygame.image.load("./ressources/boutons/WallNut.jpg").convert_alpha()
    img3 = pygame.image.load("./ressources/boutons/JouerBouton.png").convert_alpha()
    img4 = pygame.image.load("./ressources/boutons/pelle.png").convert_alpha()
    img5 = pygame.image.load("./ressources/boutons/sunflower.png").convert_alpha()
    #bouton1 = Bouton("bouton1", 30, 30, 100, 50, "clique")
    PeaShooterBouton = Bouton("PeaShooter", 0, 0,  img, 1)
    WallnutBouton = Bouton("Wallnut", 0, 60,  img2, 1)
    SunflowerBouton = Bouton("Sunflower", 0, 128, img5, 0.78)
    BoutonJouer = Bouton("Jouer",200, 200, img3, 1)
    BoutonEffacer = Bouton("Effacer", 125, 0, img4, 0.5)
    
    model.ajouter_bouton(BoutonJouer)

    # le personnage et son image:
    perso = Personnage(str("perso"),False) #2 attributs, nom et si NPC
    #zombie4 = Zombie("zombieX", 4, 0.7, 0.7, 200, 100) 
    #zombie4 = Zombie("zombieX", 2, 0.7, 0.7, 200, 100)
    #zombie4 = Zombie("zombieX", 1, 0.7, 0.7, 200, 100)
    #zombie5 = Zombie("zombieFootball", 1, 0.9, 0.2, 200, 100)
    #zombie6 = Zombie("zombieFootball", 5, 0.9, 0.2, 200, 100)
    #zombie6 = Zombie("zombieFootball", 4, 0.9, 0.2, 200, 100)
    #zombie7 = Zombie("zombieGargantuar", 4, 0.1, 0.2, 2000, 100)
    #zombie1 = Zombie("zombie1", 1, 0.3, 0.5, 200, 100)  
    #zombie1 = Zombie("zombie1", 4, 0.3, 0.4, 200, 100)  
    #zombie1 = Zombie("zombie1", 5, 0.3, 0.5, 200, 100)  
    #zombie1 = Zombie("zombie1", 3, 0.3, 0.45, 200, 100)  
    #zombie1 = Zombie("zombie1", 4, 0.3, 0.5, 200, 100)  
    #zombie2 = Zombie("zombie1", 2, 0.3, 0.5, 200, 100) 
    #zombie3 = Zombie("zombie1", 3, 0.3, 0.5, 200, 100) 
    
    perso.set_position((300, 300))
    model.personnage = perso
    #modelZombie.personnage = zombie1
    #modelZombie.persozombie2 = Zombie("zombie1", 2) 

    #vue_perso = ViewPersonnage(perso)
   
    #view.add_elem(vue_perso)
  
   
    ligne = 1
    clock = pygame.time.Clock()
    
    #--------------------------------Fonctions essentielles du jeu-------------------#
    
    def jouer():
        """ 
        Une fonction pour charger l'ensemble des instructions essentielles du jeu
        """
        model.ajouter_bouton(PeaShooterBouton)
        model.ajouter_bouton(SunflowerBouton)
        model.ajouter_bouton(WallnutBouton)
        model.ajouter_bouton(BoutonEffacer)
        view.Jouer = True #On active la fenêtre de jeu
        global NbPlantes
        global NbZombies
        global NbSunFlowers
        global Perdu
        if len(PlantesActuelles) > NbPlantes: #Si unne plante  a été ajoutée...
            view.add_elem(ViewPersonnage(PlantesActuelles[-1])) #Ajout du dernier PeaShooter (Pile)
            NbPlantes = len(PlantesActuelles) #on réajuste le total
        if len(ZombiesActuelles) > NbZombies: 
            view.add_elem(ViewPersonnage(ZombiesActuelles[-1])) 
            NbZombies = len(ZombiesActuelles) 
        
        for element in dico_zombies.values():
            for zombies in element.values():
                if zombies.a_Perdu:
                    Perdu = True
    

    
            
        for element in view.elems: #parcours des éléments visuels (zombies, plantes...)
            element.personnage.update() #on met à jour leur statut
            element.personnage.modelPerso.update()
            
        indice_projectile = 0
        longueur_projectile_list = len(projectiles)
        #Une boucle qui met à jour les projectiles (pea)
        while indice_projectile < longueur_projectile_list: #Une boucle pour parcourir la list contenant nos projectiles (pea)
            projectiles[indice_projectile].update()
            if (projectiles[indice_projectile].x) >= 870 or (projectiles[indice_projectile].Est_mort):  #Si le projectile sort de la map ou a touché un zombie...
                del projectiles[indice_projectile]  #on supprime le projectile de la list
                longueur_projectile_list = len(projectiles) #Mise à jour longueur list pour éviter un out of range
            indice_projectile += 1
    
    def ajouter_monnaie():
        """
        Une fonction pour ajouter de l'argent à chaque intervalle de temps.
        """
        global compteur
        compteur += 1*NbSunFlowers
     
        if compteur > 600:
            compteur = 0
            model.boutons["PeaShooter"].monnaie += 50

    def niveau():
        """ 
        Une fonction qui gère l'organisation des niveaux (difficultés, vague...)
        """
        global NbZombies
        global compteur1
        global compteur2
        global zombies_par_niveaux
        global niveau_actuel
        global zombies_caracteristiques
        for zombie, nombre in zombies_par_niveaux[niveau_actuel].items():
            if  zombies_par_niveaux[niveau_actuel][zombie] > 0:
                compteur1 += 1
                compteur2 += 1 
                if True: #nous ajoutons une condition de compteur par dessus l'autre car randint peut générer une valeur au-dessus de compteur
                    compteur2 = 0
                    Frequence = randint(400, 500)
                    if compteur1 > Frequence: 
                        
                        nom, ligne, vitesse_marche, vitesse, pv, degats = zombies_caracteristiques[zombie][0], randint(1, 5), zombies_caracteristiques[zombie][2], zombies_caracteristiques[zombie][3], zombies_caracteristiques[zombie][4], zombies_caracteristiques[zombie][5]
                        Zombie(nom, ligne, vitesse_marche, vitesse, pv, degats)
                        zombies_par_niveaux[niveau_actuel][zombie] -= 1
                        compteur1 = 0 
                        
                        #print(zombies_par_niveaux[niveau_actuel][zombie])
                        if zombies_par_niveaux[niveau_actuel][zombie] == 0:
                            niveau_actuel += 1

        
        
    
    ### Boucle du jeu
    # chaque tour de boucle est un 'pas' dans le jeux
    
    #-------------------------------Boucle de jeu---------------------------------#
    
    while not model.done:
        clock.tick(60)  #Le jeu est fait pour être joué à 60 FPS
        controller.gerer_input()
        if BoutonJouer.est_Clique:
            jouer()
            ajouter_monnaie()
            niveau()
            NbSunFlowers = 0
            if Perdu:
                BoutonJouer.est_Clique = False
                View.jouer = False
                model.reinitialiser_boutons()
                dico_zombies = {}
                dico_plantes = {}
                BoutonJouer = Bouton("Jouer",200, 200, img3, 1)

        view.draw()
        pygame.display.flip()

except Exception as e:
    pygame.quit()
    raise e

pygame.quit()
print("pygame_quit")
