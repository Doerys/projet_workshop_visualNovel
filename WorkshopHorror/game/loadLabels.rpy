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
        J_think "Je ne peux pas prendre ça..." 
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
        
    
    



