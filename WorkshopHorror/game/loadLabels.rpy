# Fichier permettant de créer les labels permettant
# la récupération des items, le changement de tel
# ou tel scène, ou la redirection vers d'autres scène

# GESTION INVENTAIRE =================================================
label selectCraft :

    if (act_label == 'openPlacard' or act_label == 'openAppart'):
        if (inventory.getInv().count(telecommande) > 0 and inventory.getInv().count(piles) > 0):
            jump craftTelecommande

        if liste.selected == True:
            $ listeSelect = True
        else :
            $ listeSelect = False

        if(act_label == 'openPlacard'):
            jump openPlacard
        else :
            jump openAppart
    
    if (act_label == 'openCuisine' or act_label == 'openSalon' or act_label == 'openAffairesKim') :
        if livreRecette.selected == True:
            $ livreRecetteSelect = True
            $ mdpCarnetSelect = False
            $ lettreCoquineSelect = False
        elif mdpCarnet.selected == True:
            $ mdpCarnetSelect = True
            $ livreRecetteSelect = False
            $ lettreCoquineSelect = False
        elif lettreCoquine.selected == True:
            $ lettreCoquineSelect = True
            $ mdpCarnetSelect = False
            $ livreRecetteSelect = False
        else :
            $ livreRecetteSelect = False
            $ mdpCarnetSelect = False
            $ lettreCoquineSelect = False
        if(act_label == 'openCuisine'):
            jump openCuisine
        if(act_label == 'openAffairesKim'):
            jump openAffairesKim
        else :
            jump openSalon
    
    if (act_label == 'openCave' or act_label == 'openCouloirBox' or act_label == 'openCouloir' or act_label == 'openBox') :
        if lettreSK.selected == True:
            $ lettreSKSelect = True
        else :
            $ lettreSKSelect = False

        if(act_label == 'openCouloir'):
            jump openCouloir
        if(act_label == 'openCouloirBox'):
            jump openCouloirBox
        if(act_label == 'openBox'):
            jump openBox
        else :
            jump openCave

label slotSelect0 :
    $ inventory.selectItem(0)
    jump selectCraft
    
label slotSelect1 :
    $ inventory.selectItem(1)
    jump selectCraft

label slotSelect2 :
    $ inventory.selectItem(2)
    jump selectCraft

label slotSelect3 :
    $ inventory.selectItem(3)
    jump selectCraft

label slotSelect4 :
    $ inventory.selectItem(4)
    jump selectCraft

label slotSelect5 :
    $ inventory.selectItem(5)
    jump selectCraft

label slotSelect6 :
    $ inventory.selectItem(6)
    jump selectCraft

label slotSelect7 :
    $ inventory.selectItem(7)
    jump selectCraft

# APPART PP ==========================================================



label openPlacard :

    $ act_label = 'openPlacard'

    hide screen bouffe
    hide screen boisson
    hide screen telecommande
    hide screen vetement
    hide screen placard
    hide screen tabouret
    hide screen velux

    scene placard_jason
    show screen flecheAppart

    if (canGetItemAppart.count(piles)>0):
        show screen piles
    if (canGetItemAppart.count(beuh)>0):
        show screen beuh
    call screen inventory 

label getBeuh :

    $ possible = inventory.addItem(beuh)
    if (possible and phaseTimer) :
        hide screen beuh
        $ canGetItemAppart.remove(beuh)
        $ objetTrouve += 1
        
        
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openPlacard 

label getPiles :

    $ possible = inventory.addItem(piles)
    if (possible) :
        hide screen piles
        $ canGetItemAppart.remove(piles)
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openPlacard


label openAppart :

    $ act_label = 'openAppart'

    hide screen flecheAppart
    hide screen beuh
    hide screen piles

    if (veluxOpen) :
        scene chambre_jason
      
        if (canGetItemAppart.count(bouffe)>0):
            show screen bouffe
        if (canGetItemAppart.count(telecommande)>0):
            show screen telecommande
        if (canGetItemAppart.count(boisson)>0):
            show screen boisson
        if (canGetItemAppart.count(vetement)>0):
            show screen vetement
        
        show screen placard
        show screen velux

        if (not tabouretClick) :
            show screen tabouret
    
        if (piles.getSelected() and inventory.getInv().count(telecommande)>0):
            jump craftTelecommande
 

    else :
        scene chambre_jason_sombre

        J_think "Oula, il est déjà l'heure ! Si je me dépêche, j'ai moyen d'arriver juste à temps !"

        # De quoi j'ai besoin déjà ?
        # Affichage liste d'objet

        # Possibilité de partir à tout moment de la séquence, 3 répliques selon le nb d'objet pris
        if (objetTrouve == 0):
            J_think "Hé merde, j'espère que Kim ne m'en voudras pas de venir les mains vides..."
        elif (objetTrouve >= 1 or objetTrouve <= 3):
            J_think "Bon, au moins je n'arriverai pas les mains vides !"
        elif (objetTrouve == 4):
            J_think "Ok, je pense que je suis bon !"

        J_think "Maintenant, il reste plus qu'à espérer que rien de mal n'arrive ce soir..."

        hide screen bouffe
        hide screen boisson
        hide screen telecommande
        hide screen vetement
        hide screen placard
        hide screen tabouret
        hide screen velux

        if (inventory.getInv().count(bouffe) > 0):
            $ inventory.removeItem(bouffe)
        if (inventory.getInv().count(boisson) > 0):
            $ inventory.removeItem(boisson)
        if (inventory.getInv().count(telecommande) > 0):
            $ inventory.removeItem(telecommande)
        if (inventory.getInv().count(vetement) > 0):
            $ inventory.removeItem(vetement)
        if (inventory.getInv().count(beuh) > 0):
            $ inventory.removeItem(beuh)
        if (inventory.getInv().count(liste) > 0):
            $ inventory.removeItem(liste)

        jump chezKim
    
    call screen inventory

label toTabouret :

    $ tabouretClick = True
    hide screen tabouret 
 
    J_think "Ça pourrait me servir..."
    
    jump openAppart

label toVelux :

    if (inventory.getInv().count(telecommande)>0 and telecommande.specialAttribute == True):
        $ veluxOpen = False
    else :
        J_think "J'ai besoin d'une télécommande qui marche..."

    jump openAppart

label getBouffe :

    $ possible = inventory.addItem(bouffe)
    if (possible and phaseTimer) :
        hide screen bouffe
        $ canGetItemAppart.remove(bouffe)
        $objetTrouve += 1
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openAppart

label getBoisson :

    $ possible = False
    if (tabouretClick) :
        $ possible = inventory.addItem(boisson)
    if (possible and phaseTimer and tabouretClick) :
        hide screen boisson
        $ canGetItemAppart.remove(boisson)
        $ objetTrouve += 1
    else :
        J_think "Je ne peux pas l'atteindre..." 
    call screen inventory
    jump openAppart

label getTelecommande :

    $ possible = inventory.addItem(telecommande)
    if (possible) :
        hide screen telecommande
        $ canGetItemAppart.remove(telecommande)
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openAppart

label getVetement :

    $ possible = inventory.addItem(vetement)
    if (possible and phaseTimer) :
        hide screen vetement
        $ canGetItemAppart.remove(vetement)
        $ objetTrouve += 1
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openAppart

label craftTelecommande:
    #call screen inventory
    menu:
        "Voulez vous mettre les piles dans la telecommande ?"
        "Oui":
            $ telecommande.specialAttribute = True
            $ inventory.selectItem(inventory.getInv().index(telecommande))
            $ inventory.removeItem(piles)
            call screen inventory
            jump openAppart
        "Non":
            $ inventory.selectItem(inventory.getInv().index(telecommande))
            call screen inventory
            jump openAppart
        
    

# TROUSSE DE SOIN (Cuisine, Salon) ==========================================================

label openAffairesKim :

    $ act_label = 'openAffairesKim'

    hide screen partir
    hide screen tiroirCasse
    hide screen affairesKim

    scene affaire_kim
    show screen flecheSalon

    if (canGetItemSoin.count(photoNancy)>0):
        show screen photoNancy
    if (canGetItemSoin.count(lettreCoquine)>0):
        show screen lettreCoquine

    if (livreRecetteSelect == True) :
        hide screen mdpCarnetContent
        hide screen lettreCoquineContent
        hide screen photoNancy
        show livreRecetteContent :
            xpos 0
            ypos 400
    else :
        hide livreRecetteContent

    if (mdpCarnetSelect == True) :
        hide screen livreRecetteContent
        hide screen lettreCoquineContent
        
        show mdpCarnetContent :
            xpos 600
            ypos 500
    else :
        hide mdpCarnetContent

    if (lettreCoquineSelect == True) :
        hide screen livreRecetteContent
        hide screen mdpCarnetContent
        hide screen photoNancy
        show lettreCoquineContent :
            xpos 350
            ypos 1000

        J_think "Qu'est-ce que c'est que ça ?! 'B' ? Est-ce que ce serait... ?"

    else :
        hide lettreCoquineContent

    call screen inventory 

label openTiroirCasse :

    if (inventory.getInv().count(ciseaux) > 0 and ciseaux.selected == True) :
        menu:
            "Utiliser les ciseaux pour forcer le tiroir ?"
            "Oui":
                $ inventory.removeItem(ciseaux)
                $ tiroirForce = True
                call screen inventory
                jump openSalon
            "Non":
                call screen inventory
                jump openSalon

    elif(tiroirForce == True):

        if (canGetItemSoin.count(mdpCarnet) > 0):

            $ possible = inventory.addItem(mdpCarnet)
            if (possible) :
                $ canGetItemSoin.remove(mdpCarnet)
                J_think "Un carnet de mots de passe..."
            else :
                J_think "Je ne peux pas prendre ça..." 
        else :
            J_think "J'ai déjà tout récupéré..."

        jump openSalon

    else :
        J_think "Je dois pouvoir forcer ce tiroir..."
        jump openSalon
        
    call screen inventory 

label getPhotoNancy :

    $ possible = inventory.addItem(photoNancy)
    if (possible) :
        hide screen photoNancy
        $ canGetItemSoin.remove(photoNancy)     
        
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openAffairesKim

label getLettreCoquine :

    $ possible = inventory.addItem(lettreCoquine)
    if (possible) :
        hide screen lettreCoquine
        $ canGetItemSoin.remove(lettreCoquine)
        $ lettre_coquine = True  
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openAffairesKim

label getMdpCarnet :

    $ possible = inventory.addItem(mdpCarnet)
    if (possible) :
        hide screen mdpCarnet
        $ canGetItemSoin.remove(mdpCarnet)
        J_think "Ça pourrait me servir..." 
        
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openTiroirCasse

label openSalon :

    $ act_label = 'openSalon'
    
    hide screen flecheSalon
    hide screen lettreCoquine
    hide screen photoNancy
    hide screen mdpCarnet
    hide screen tiroirCuisine
    hide screen livreRecette
    hide screen infirmerie

    
    scene salon
    
    show screen affairesKim
    show screen tiroirCasse
    show screen partir

    show screen flecheCuisine

    if (livreRecetteSelect == True) :
        hide screen mdpCarnetContent
        hide screen lettreCoquineContent
        hide screen tiroirCasse
        show livreRecetteContent :
            xpos 0
            ypos 400
    else :
        hide livreRecetteContent

    if (mdpCarnetSelect == True) :
        hide screen livreRecetteContent
        hide screen lettreCoquineContent
        hide screen tiroirCasse
        show mdpCarnetContent :
            xpos 600
            ypos 500
    else :
        hide mdpCarnetContent

    if (lettreCoquineSelect == True) :
        hide screen livreRecetteContent
        hide screen mdpCarnetContent
        hide screen tiroirCasse
        show lettreCoquineContent :
            xpos 350
            ypos 1000

        J_think "Qu'est-ce que c'est que ça ?! 'B' ? Est-ce que ce serait... ?"

    else :
        hide lettreCoquineContent
    
    
    call screen inventory



label openTiroirCuisine :

    if (canGetItemSoin.count(ciseaux) > 0):

        hide screen tiroirCuisine
        hide screen livreRecette
        hide screen partir
        hide screen infirmerie
        hide screen flecheSalon

        scene tiroir_cuisine

        $ possible = inventory.addItem(ciseaux)
        if (possible) :
            $ canGetItemSoin.remove(ciseaux)
            J_think "Ces ciseaux peuvent me servir..."
        else :
            J_think "Je ne peux pas prendre ça..." 
    else :
        J_think "J'ai déjà tout récupéré..."
    
    jump openCuisine

label openInfirmerie :

    if (cadenaOpen):

        if (canGetItemSoin.count(trousse) > 0):

            $ possible = inventory.addItem(trousse)
            if (possible) :
                $ canGetItemSoin.remove(trousse)
                $ troussedeSoin = 1
                J_think "J'ai trouvé la trousse de soin !"
            else :
                J_think "Je ne peux pas prendre ça..."
        else :
            J_think "J'ai déjà tout récupéré..."

        call screen inventory
        jump openCuisine
         

    else :

        show cadena :
            xpos 800
            ypos 400

        J_think "Le premier est chiffre est bloqué sur 0, il doit faire partie du code..." 

        python :
            code = renpy.input("Code du cadenas", length=5, default='0')

        if (code == "09201") :
            $ cadenaOpen = True 
            if (inventory.getInv().count(mdpCarnet)>0):
                $ inventory.removeItem(mdpCarnet)
            if (inventory.getInv().count(livreRecette)>0):
                $ inventory.removeItem(livreRecette)

            J_think "Ça a marché !" 
            jump openCuisine
        else :
            J_think "Ce n'est pas le bon code..." 
            jump openCuisine

    call screen inventory  

label getLivreRecette:
    $ possible = inventory.addItem(livreRecette)
    if (possible) :
        hide screen livreRecette
        $ canGetItemSoin.remove(livreRecette)
        J_think "Ça pourrait me servir..." 
        
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openCuisine

label openCuisine :

    $ act_label = 'openCuisine'
    
    hide screen flecheCuisine
    hide screen trousse
    hide screen tiroirCasse
    hide screen partir
    hide screen affairesKim
    hide livreRecetteContent
    

    scene cuisine_nuit
    
    show screen infirmerie
    show screen tiroirCuisine
    if (canGetItemSoin.count(livreRecette)>0):
        show screen livreRecette
    show screen partir
    show screen flecheSalon

    if (livreRecetteSelect == True) :
        hide screen tiroirCuisine
        hide screen mdpCarnetContent
        hide screen lettreCoquineContent
        show livreRecetteContent :
            xpos 0
            ypos 400
    else :
        hide livreRecetteContent

    if (mdpCarnetSelect == True) :
        hide screen tiroirCuisine
        hide screen livreRecetteContent
        hide screen lettreCoquineContent
        hide screen livreRecette
        show mdpCarnetContent :
            xpos 600
            ypos 500
    else :
        hide mdpCarnetContent

    if (lettreCoquineSelect == True) :
        hide screen tiroirCuisine
        hide screen livreRecetteContent
        hide screen mdpCarnetContent
        hide screen livreRecette
        show lettreCoquineContent :
            xpos 350
            ypos 1000

        J_think "Qu'est-ce que c'est que ça ?! 'B' ? Est-ce que ce serait... ?"
        
    else :
        hide lettreCoquineContent
    
    call screen inventory


# Cave ===========================================================================

# Cave
label openCave :

    $ act_label = 'openCave'
    
    hide screen cle
    hide screen planches
    hide screen flecheCave
    hide screen partirCave
    
    scene cave
    
    show screen kimDead

    show screen partirCave
    show screen flecheCouloirBox

    if (lettreSKSelect == True) :
        show lettreSKContent :
            xpos 300
            ypos 350
    else :
        hide lettreSKContent
    
    call screen inventory

label toKimDead :
    
    J_think "On va trouver du soin Kim..." 

    jump openCave

# CouloirBox
label openCouloirBox :

    $ act_label = 'openCouloirBox'
    
    hide screen kimDead
    hide screen marteau
    hide screen flecheCouloirBox
    hide screen partirCave

    scene couloir_box
    
    show screen porteBarricade1
    show screen porteBarricade2
    show screen porteBox

    if (canGetItemCave.count(clou)>0):
        show screen clou
    if (canGetItemCave.count(lettreSK)>0):
        show screen lettreSK

    show screen partirCave
    show screen flecheCouloir

    if (lettreSKSelect == True) :

        hide screen clou
        hide screen porteBarricade1
        hide screen porteBarricade2

        show lettreSKContent :
            xpos 300
            ypos 350
    else :
        hide lettreSKContent
    
    call screen inventory

label getLettreSK :

    $ possible = inventory.addItem(lettreSK)
    if (possible) :
        hide screen lettreSK
        $ canGetItemCave.remove(lettreSK)
        $ lettre_Nancy = True
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openCouloirBox

label getClou :

    $ possible = inventory.addItem(clou)
    if (possible) :
        hide screen clou
        $ canGetItemCave.remove(clou)
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openCouloirBox

label toBarricade :

    if (inventory.getInv().count(marteau) > 0 and inventory.getInv().count(planches) > 0 and inventory.getInv().count(clou) > 0) :
        menu:
            "Utiliser le martaux, les planches et les clous pour barricader ?"
            "Oui":
                $ inventory.removeItem(marteau)
                $ inventory.removeItem(planches)
                $ inventory.removeItem(clou)
                $ barricade = True
                call screen inventory
                jump openCouloirBox
            "Non":
                call screen inventory
                jump openCouloirBox

    elif(barricade == True):

        J_think "Belle barricade"

        jump openCouloirBox

    else :
        J_think "Je dois barricader ce passage..."
        jump openCouloirBox
        
    call screen inventory 

label toPorteBox :

    if (inventory.getInv().count(cle) > 0 ) :
        menu:
            "Utiliser la clé pour ouvrir le box ?"
            "Oui":
                $ inventory.removeItem(cle)
                $ boxOpen = True
                call screen inventory
                jump openCouloirBox
            "Non":
                call screen inventory
                jump openCouloirBox

    elif(boxOpen == True):

        jump openBox

    else :
        J_think "C'est fermé à clé..."
        jump openCouloirBox
        
    call screen inventory 


# Couloir
label openCouloir :

    $ act_label = 'openCouloir'
    
    hide screen clou
    hide screen lettreSK
    hide screen flecheCouloir
    hide screen porteBarricade1
    hide screen porteBarricade2
    hide screen porteBox
    hide screen partirCave

    scene couloir

    if (canGetItemCave.count(planches)>0):
        show screen planches
    if (canGetItemCave.count(cle)>0):
        show screen cle

    show screen partirCave
    show screen flecheCave

    if (lettreSKSelect == True) :

        show lettreSKContent :
            xpos 300
            ypos 350
    else :
        hide lettreSKContent
    
    call screen inventory

label getCle :

    $ possible = inventory.addItem(cle)
    if (possible) :
        hide screen cle
        $ canGetItemCave.remove(cle)   
        J_think "Des clés... que peuvent-t-elles bien ouvrir ?"  
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openCouloir

label getPlanches :

    $ possible = inventory.addItem(planches)
    if (possible) :
        hide screen planches
        $ canGetItemCave.remove(planches)     
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openCouloir


# Box
label openBox :

    $ act_label = 'openBox'
    
    hide screen clou
    hide screen lettreSK
    hide screen flecheCouloir
    hide screen porteBarricade1
    hide screen porteBarricade2
    hide screen porteBox
    hide screen partirCave

    scene box

    if (canGetItemCave.count(marteau)>0):
        show screen marteau

    show screen partirCave
    show screen flecheCouloirBox

    if (lettreSKSelect == True) :
        show lettreSKContent :
            xpos 300
            ypos 400
    else :
        hide lettreSKContent
    
    call screen inventory

label getMarteau :

    $ possible = inventory.addItem(marteau)
    if (possible) :
        hide screen marteau
        $ canGetItemCave.remove(marteau)     
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openBox

label hideCuisine:

    hide screen flecheSalon
    hide screen lettreCoquine
    hide screen photoNancy
    hide screen mdpCarnet
    hide screen tiroirCuisine
    hide screen livreRecette
    hide screen infirmerie
    hide screen affairesKim
    hide screen mdpCarnetContent
    hide screen lettreCoquineContent

    jump kimHurlement

label hideCave:
    hide screen clou
    hide screen lettreSK
    hide screen cle
    hide screen planches
    hide screen marteau
    hide screen kimDead
    hide screen flecheCouloir
    hide screen partirCave
    hide screen flecheCave
    hide screen flecheCouloirBox
    hide screen porteBarricade1
    hide screen porteBarricade2
    hide screen porteBox

    jump choix_cave
