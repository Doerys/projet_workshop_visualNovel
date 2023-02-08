# L'endroit ou l'on créer les items récupérable dans les phases Point & Click 

# -------------------- Images Clickable ------------- #
# ----------------- FLECHE DE RETOUR ---------------- #

image fleche = "fleche.png" 

# -------------------- Items et Images Clickable ------------- #
# -------------------------- APPART PP ----------------------- #

init python :

    # Ici on load le nom de l'item, l'image de l'item puis l'image en version selectioné

        # Principale
    bouffe = Item("Bouffe", "bouffeItem.png", "bouffeItemSelect.png",False)
    telecommande = Item("Télécommande", "telecommandeItem.png", "telecommandeItemSelect.png",False)
    boisson = Item("Boisson", "boissonItem.png", "boissonItemSelect.png",False)
    vetement = Item("Vêtement", "vetementItem.png", "vetementItemSelect.png",False)
        # Placard
    beuh = Item("Sachet de Beuh", "beuhItem.png", "beuhItemSelect.png",False)
    piles = Item("Piles", "pilesItem.png", "pilesItemSelect.png",False)

    canGetItemAppart = [bouffe, telecommande, boisson, vetement, beuh, piles] 

    veluxOpen = False
    tabouretClick = False
    phaseTimer = False
    phaseCraft = False

    objetTrouve = 0


# Ici, on load les images utilisable par renPy (ça fait un peu un double mais pas grave) 

image bouffe = "bouffe.png"
image boisson = "boisson.png"
image telecommande = "telecommande.png"
image vetement = "vetement.png"
image tabouret = "tabouret.png"
image velux = "velux.png"
image placard = "placard.png"

image beuh = "beuh.png"
image piles = "piles.png"


# -------------------- Items et Images Clickable ------------- #
# -------------------------- ... ----------------------- #
