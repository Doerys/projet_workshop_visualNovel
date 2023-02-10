# Les screen permettent d'afficher des éléments supplémentaires à l'écran, c'est ici que l'on va
# load les screens permettant d'afficher l'inventaire, mais aussi les différents items récupérables
# lors des Passages point & Click. 


# Modifie la taille des images pour l'inventaire
transform inv :
    size(300,300)


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
        xpos 1983
        ypos 1303
        idle "placard"
        action Jump("openPlacard")
#Load Velux
screen velux:
    imagebutton:
        xpos 0
        ypos -39
        idle "velux"
        action Jump("toVelux")
#Load Tabouret
screen tabouret:
    imagebutton:
        xpos 1250
        ypos 1567
        idle "tabouret"
        action Jump("toTabouret")
#Load Tabouret cliqué
screen tabouretClick: 
    imagebutton:
        xpos 800
        ypos 2000
        idle "tabouret"
        action Jump("toTabouret")
    #Load Bouffe
screen bouffe:
    imagebutton:
        xpos 1820
        ypos 1215
        idle "bouffe"
        action Jump("getBouffe")
    #Load Boisson
screen boisson:
    imagebutton:
        xpos 2900
        ypos 10
        idle "boisson"
        action Jump("getBoisson")
    #Load Telecommande
screen telecommande:
    imagebutton:
        xpos 350
        ypos 1840
        idle "telecommande"
        action Jump("getTelecommande")
    #Load vêtement
screen vetement:
    imagebutton:
        xpos 3030
        ypos 1825
        idle "vetement"
        action Jump("getVetement")

# Placard -----------------------------------------

    #Load Flêche de retour
screen flecheAppart:
    imagebutton:
        xpos 200
        ypos 1600
        idle "fleche"
        hovered (SetVariable("directionGauche", "Vers l'appartement"))
        unhovered (SetVariable("directionGauche", " "))
        action [SetVariable("directionGauche", ""),Jump("openAppart")]
    text directionGauche size 80 :
        xpos 200
        ypos 1450
    #Load Piles
screen piles:
    imagebutton:
        xpos 1450
        ypos 1880
        idle "piles"
        action Jump("getPiles")
    #Load beuh
screen beuh:
    imagebutton:
        xpos 2665
        ypos 300
        idle "beuh"
        action Jump("getBeuh")


# CUISINE - SALON ==========================================================

screen partir:
    imagebutton:
        xpos 3000
        ypos 1600
        idle "partir"
        hovered (SetVariable("directionDroit", "Partir"))
        unhovered (SetVariable("directionDroit", " "))
        action [SetVariable("directionDroit", ""),Jump("versCriCave")]
    text directionDroit size 80 :
        xpos 3000
        ypos 1450

# Salon -----------------------------------------
screen affairesKim:
    imagebutton:
        xpos 2166
        ypos 1053
        idle "affairesKim"
        action Jump("openAffairesKim")

screen tiroirCasse:
    imagebutton:
        xpos 0
        ypos 475
        idle "tiroirCasse"
        action Jump("openTiroirCasse")

# Tiroir Cassé ----------------------------------
screen mdpCarnet:
    imagebutton:
        xpos 1983
        ypos 1303
        idle "mdpCarnet"
        action Jump("getMdpCarnet")

# Affaires Kim ----------------------------------
screen photoNancy:
    imagebutton:
        xpos 1800
        ypos 1500
        idle "photoNancy"
        action Jump("getPhotoNancy")

screen lettreCoquine:
    imagebutton:
        xpos 1100
        ypos 1200
        idle "lettreCoquine"
        action Jump("getLettreCoquine")

# Cuisine ---------------------------------------
screen infirmerie:
    imagebutton:
        xpos 2100
        ypos 1340
        idle "infirmerie"
        action Jump("openInfirmerie")

screen tiroirCuisine:
    imagebutton:
        xpos 1125
        ypos 1622
        idle "tiroirCuisine"
        action Jump("openTiroirCuisine")

screen livreRecette:
    imagebutton:
        xpos 1400
        ypos 1500
        idle "livreRecette"
        action Jump("getLivreRecette")

screen flecheSalon:
    imagebutton:
        xpos 200
        ypos 1600
        idle "fleche"
        hovered (SetVariable("directionGauche", "Vers le Salon"))
        unhovered (SetVariable("directionGauche", " "))
        action [SetVariable("directionGauche", ""),Jump("openSalon")]
    text directionGauche size 80 :
        xpos 200
        ypos 1450


    #Load Flêche de retour
screen flecheCuisine:
    imagebutton:
        xpos 200
        ypos 1600
        idle "fleche"
        hovered (SetVariable("directionGauche", "Vers la Cuisine"))
        unhovered (SetVariable("directionGauche", " "))
        action [SetVariable("directionGauche", ""),Jump("openCuisine")]
    text directionGauche size 80 :
        xpos 200
        ypos 1450






