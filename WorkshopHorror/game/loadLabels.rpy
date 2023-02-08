# Fichier permettant de créer les labels permettant
# la récupération des items, le changement de tel
# ou tel scène, ou la redirection vers d'autres scène

# GESTION INVENTAIRE =================================================

label slotSelect0 :
    $ inventory.selectItem(0)
    call screen inventory

label slotSelect1 :
    $ inventory.selectItem(1)
    call screen inventory

label slotSelect2 :
    $ inventory.selectItem(2)
    call screen inventory

label slotSelect3 :
    $ inventory.selectItem(3)
    call screen inventory

label slotSelect4 :
    $ inventory.selectItem(4)
    call screen inventory

label slotSelect5 :
    $ inventory.selectItem(5)
    call screen inventory

label slotSelect6 :
    $ inventory.selectItem(6)
    call screen inventory

label slotSelect7 :
    $ inventory.selectItem(7)
    call screen inventory

# APPART PP ==========================================================

label openPlacard :

    scene bg placard
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
        $ objetTrouve = objetTrouve + 1
        $ canGetItemAppart.remove(beuh)
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

    if (veluxOpen) :
        scene bg appartLight

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

        if (tabouretClick) :
            show screen tabouretClick
        else :
            show screen tabouret
 

    else :
        scene bg appartDark

        J_think "C'est bon je suis prêt."

label toTabouret :

    if (tabouretClick == False) :
        $ tabouretClick = True
        hide screen tabouret
        show screen tabouretClick
    else :
        J_think "Ça pourrait me servir..."
    
    jump openAppart

label toVelux :

    if (inventory.count(telecommande)>0 and telecommande.specialAttribute == True):
        $ veluxOpen = True
    else :
        J_think "J'ai besoin d'une télécommande qui marche..."

    jump openAppart

label getBouffe :

    $ possible = inventory.addItem(bouffe)
    if (possible and phaseTimer) :
        hide screen bouffe
        $ objetTrouve = objetTrouve + 1
        $ canGetItemAppart.remove(bouffe)
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openPlacard

label getBoisson :

    $ possible = inventory.addItem(boisson)
    if (possible and phaseTimer and tabouretClick) :
        hide screen boisson
        $ objetTrouve = objetTrouve + 1
        $ canGetItemAppart.remove(boisson)
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openPlacard

label getTelecommande :

    $ possible = inventory.addItem(telecommande)
    if (possible) :
        hide screen telecommande
        $ canGetItemAppart.remove(telecommande)
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openPlacard

label getVetement :

    $ possible = inventory.addItem(vetement)
    if (possible and phaseTimer and tabouretClick) :
        hide screen vetement
        $ objetTrouve = objetTrouve + 1
        $ canGetItemAppart.remove(vetement)
    else :
        J_think "Je ne peux pas prendre ça..." 
    call screen inventory
    jump openPlacard
        
    
    



