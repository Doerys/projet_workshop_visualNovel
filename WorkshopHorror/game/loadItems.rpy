# L'endroit ou l'on créer les items récupérable dans les phases Point & Click 

# -------------------- Images Clickable ------------- #
# ----------------- FLECHE DE RETOUR ---------------- #

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

    canGetItemAppart = [bouffe, telecommande, boisson, vetement, beuh, piles]

    veluxOpen = True
    tabouretClick = False
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

# -------------------- Items et Images Clickable ------------- #
# -------------------------- ... ----------------------- #
