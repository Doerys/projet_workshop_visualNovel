# L'endroit ou l'on créer les items récupérable dans les phases Point & Click 

# -------------------- Images Clickable ------------- #
# ----------------- FLECHE DE RETOUR ---------------- #

image partir = "items/partir.png"
image fleche = "items/fleche.png" 

# -------------------- Items et Images Clickable ------------- #
# -------------------------- APPART PP ----------------------- #

init python :

    # Ici on load le nom de l'item, l'image de l'item puis l'image en version selectioné

        # Principale
    bouffe = Item("Bouffe", "items/bouffeItem.png", "items/bouffeItemSelect.png",False)
    telecommande = Item("Télécommande", "items/telecommandeItem.png", "items/telecommandeItemSelect.png",False)
    boisson = Item("Boisson", "items/boissonItem.png", "items/boissonItemSelect.png",False)
    vetement = Item("Vêtement", "items/vetementItem.png", "items/vetementItemSelect.png",False)
        # Placard
    beuh = Item("Sachet de Beuh", "items/beuhItem.png", "items/beuhItemSelect.png",False)
    piles = Item("Piles", "items/pilesItem.png", "items/pilesItemSelect.png",False)

    liste = Item("Liste", "items/listeItem.png", "items/listeItemSelect.png", False)
    inventory.addItem(liste)

    canGetItemAppart = [bouffe, telecommande, boisson, vetement, beuh, piles]

    veluxOpen = True
    tabouretClick = False
    listeSelect = False

    phaseTimer = True
    phaseCraft = False

    objetTrouve = 0


# Ici, on load les images utilisable par renPy (ça fait un peu un double mais pas grave) 

image bouffe = "items/bouffe.png"
image boisson = "items/boisson.png"
image telecommande = "items/telecommande.png"
image vetement = "items/vetement.png"
image tabouret = "items/tabouret.png"
image velux = "items/velux.png"
image placard = "items/placard.png"

image beuh = "items/beuh.png"
image piles = "items/piles.png"

image liste = "items/liste.png"

# -------------------- Items et Images Clickable ------------- #
# -------------------------- Cuisine - Salon ----------------------- #

init python :

    # Ici on load le nom de l'item, l'image de l'item puis l'image en version selectioné

        # Cuisine
    livreRecette = Item("Livre de Recette", "items/livreRecetteItem.png", "items/livreRecetteItemSelect.png",False)
        # Sac de Nancy
    lettreCoquine = Item("Lettre Coquine", "items/lettreCoquineItem.png", "items/lettreCoquineItemSelect.png",False)
    photoNancy = Item("Photo de Nancy", "items/photoNancyItem.png", "items/photoNancyItemSelect.png",False)
        # Tiroir cassé
    mdpCarnet = Item("Carnet de mot de passe", "items/mdpCarnetItem.png", "items/mdpCarnetItemSelect.png",False)
        # Infirmerie    
    trousse = Item("Trousse de soin", "items/trousseItem.png", "items/trousseItemSelect.png",False)
        # Tiroir Cuisine
    ciseaux = Item("Ciseaux", "items/ciseauxItem.png", "items/ciseauxItemSelect.png",False)

    canGetItemSoin = [trousse, mdpCarnet, photoNancy, lettreCoquine, livreRecette, ciseaux]

    cadenaOpen = False
    tiroirForce = False

    livreRecetteSelect = False
    mdpCarnetSelect = False
    lettreCoquineSelect = False

    phaseTimerSoin = True
    phaseCraftSoin = False

    troussedeSoin = 0

    directionGauche = ' '
    directionDroit = ' '

# Ici, on load les images utilisable par renPy (ça fait un peu un double mais pas grave) 

image livreRecette = "items/livreRecette.png"
image lettreCoquine = "items/lettreCoquine.png"
image photoNancy = "items/photoNancy.png"
image mdpCarnet = "items/mdpCarnet.png"
image trousse = "items/trousse.png"
image infirmerie = "items/infirmerie.png"
image tiroirCuisine = "items/tiroirCuisine.png"
image tiroirCasse = "items/tiroirCasse.png"
image affairesKim = "items/affairesKim.png"

image livreRecetteContent = "items/livreRecetteContenu.png"
image mdpCarnetContent = "items/mdpCarnetContenu.png"
image lettreCoquineContent = "items/lettreCoquineContenu.png"

image cadena = "items/cadena.png"

# -------------------- Items et Images Clickable ------------- #
# -------------------------- Cave ---------------------------- #

init python :

    # Ici on load le nom de l'item, l'image de l'item puis l'image en version selectioné

        # Cave
        # Couloir Box
    clou = Item("Boîte de clou", "items/boiteClouItem.png", "items/boiteClouItemSelect.png",False)
    lettreSK = Item("Lettre de Nancy", "items/lettreSKItem.png", "items/lettreSKItemSelect.png",False)
        # Couloir
    cle = Item("Clé du box", "items/cleItem.png", "items/cleItemSelect.png",False)
    planches = Item("Planches", "items/planchesItem.png", "items/planchesItemSelect.png",False)
        # Box 
    marteau = Item("Marteau", "items/marteauItem.png", "items/marteauItemSelect.png",False)

    canGetItemCave = [clou, lettreSK, cle, planches, marteau]

    boxOpen = False
    barricade = False

    lettreSKSelect = False

    phaseTimerSoin = True
    phaseCraftSoin = False

# Ici, on load les images utilisable par renPy (ça fait un peu un double mais pas grave) 

image clou = "items/boiteClou.png"
image lettreSK = "items/lettreSK.png"
image cle = "items/cle.png"
image planches = "items/planches.png"
image marteau = "items/marteau.png"

image kimDead = "items/kimDead.png"
image porteBarricade1 = "items/porteBarricade1.png"
image porteBarricade2 = "items/porteBarricade2.png"
image porteBox = "items/porteBox.png"

image lettreSKContent = "items/lettreSKContent.png"




