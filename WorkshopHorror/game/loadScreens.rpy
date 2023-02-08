# Les screen permettent d'afficher des éléments supplémentaires à l'écran, c'est ici que l'on va
# load les screens permettant d'afficher l'inventaire, mais aussi les différents items récupérables
# lors des Passages point & Click. 


# Modifie la taille des images pour l'inventaire
transform inv :
    size(55,55)


# INVENTAIRE
# Screen qui load l'inventaire
screen inventory:
    vbox:
        for i in inventory.getInv():
            frame:
                xpadding 10
                ypadding 10
                xmargin 30
                ymargin 15
                imagebutton :
                    xpos 0
                    ypos 0
                    if (i.selected == True) :
                        idle i.selectImage
                        at inv
                    else :
                        idle i.image
                        at inv
                    action Jump("slotSelect"+str(inventory.getInv().index(i)))


# POINT & CLICK

# open[lieu] -> On clique pour aller à cet emplacement
# get[item] -> On clique pour récuperer l'item 
# to[objet] -> Le clique apport des modifications à la scène 



# APPART PP ==========================================================

# Principale -----------------------------------------
#Load Placard
screen placard:
    imagebutton:
        xpos 180
        ypos 450
        idle "placard"
        action Jump("openPlacard")
#Load Velux
screen velux:
    imagebutton:
        xpos 180
        ypos 450
        idle "velux"
        action Jump("toVelux")
#Load Tabouret
screen tabouret:
    imagebutton:
        xpos 500
        ypos 450
        idle "tabouret"
        action Jump("toTabouret")
#Load Tabouret cliqué
screen tabouretClick:
    imagebutton:
        xpos 500
        ypos 450
        idle "tabouret"
        action Jump("toTabouret")
    #Load Bouffe
screen bouffe:
    imagebutton:
        xpos 500
        ypos 450
        idle "bouffe"
        action Jump("getBouffe")
    #Load Boisson
screen boisson:
    imagebutton:
        xpos 500
        ypos 450
        idle "boisson"
        action Jump("getBoisson")
    #Load Telecommande
screen telecommande:
    imagebutton:
        xpos 500
        ypos 450
        idle "telecommande"
        action Jump("getTelecommande")
    #Load vêtement
screen vetement:
    imagebutton:
        xpos 500
        ypos 450
        idle "vetement"
        action Jump("getVetement")

# Placard -----------------------------------------

    #Load Flêche de retour
screen flecheAppart:
    imagebutton:
        xpos 500
        ypos 450
        idle "fleche"
        action Jump("openAppart")
    #Load Piles
screen piles:
    imagebutton:
        xpos 500
        ypos 450
        idle "piles"
        action Jump("getPiles")
    #Load beuh
screen beuh:
    imagebutton:
        xpos 500
        ypos 450
        idle "beuh"
        action Jump("getBeuh")



