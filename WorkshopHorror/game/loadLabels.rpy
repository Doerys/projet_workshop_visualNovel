# Fichier permettant de créer les labels permettant
# la récupération des items, le changement de tel
# ou tel scène, ou la redirection vers d'autres scène

# GESTION INVENTAIRE =================================================
label selectCraft :

    if (act_label == 'openPlacard' or act_label == 'openAppart'):
        if (inventory.getInv().count(telecommande) > 0 and inventory.getInv().count(piles) > 0):
            jump craftTelecommande
        else :
            jump openAppart
    
    if (act_label == 'openCuisine' or act_label == 'openSalon' or act_label == 'openAffairesKim') :
        if (livreRecette.selected == True):
            show livreRecetteContenu
        if (mdpCarnet.selected == True):
            show mdpCarnetContenu
        else :
            if(act_label == 'openCuisine'):
                jump openCuisine
            if(act_label == 'openAffairesKim'):
                jump openAffairesKim
            else :
                jump openSalon

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

        J_think "Oulah, il est déjà l'heure! Si je me dépêche assez, j'ai moyen d'arriver à temps'."

        # De quoi j'ai besoin déjà ?
        # Affichage liste d'objet

        # Possibilité de partir à tout moment de la séquence, 3 répliques selon le nb d'objet pris
        if (objetTrouve == 0):
            J_think "Hé merde, j'espère que Kim ne m'en voudras pas de venir les mains vides..."
        elif (objetTrouve >= 1 or objetTrouve <= 3):
            J_think "Bon, au moins je n'arriverai pas les mains vides !"
        elif (objetTrouve == 4):
            J_think "Ok, je pense que je suis bon pour ce soir !"

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

        $ act_label = 'openTiroirCasse'

        hide screen partir
        hide screen tiroirCasse
        hide screen affairesKim

        scene tiroir_casse
        show screen flecheSalon

        if (canGetItemSoin.count(mdpCarnet)>0):
            show screen mdpCarnet

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
    
    
    call screen inventory



label openTiroirCuisine :

    $ act_label = 'openTiroirCuisine'

    hide screen tiroirCuisine
    hide screen livreRecette
    hide screen partir
    hide screen infirmerie
    hide screen flecheSalon

    if (canGetItemSoin.count(ciseaux) > 0):

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
        $ act_label = 'openInfirmerie'

        hide screen tiroirCuisine
        hide screen livreRecette
        hide screen partir
        hide screen infirmerie

        scene infirmerie

        if (canGetItemSoin.count(trousse) > 0):

            $ possible = inventory.addItem(trousse)
            if (possible) :
                $ canGetItemSoin.remove(trousse)
            else :
                J_think "Je ne peux pas prendre ça..."
        else :
            J_think "J'ai déjà tout récupéré..."

        call screen inventory
        jump openCuisine
         

    else :

        show cadena
        python :
            code = renpy.input("Quel est le code", length=4)

        if (code == "1234") :
            $ cadenaOpen = True 
            $ inventory.removeItem(mdpCarnet)
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
    

    scene cuisine_nuit
        
    show screen infirmerie
    show screen tiroirCuisine
    show screen livreRecette
    show screen partir
    show screen flecheSalon
    
    call screen inventory




