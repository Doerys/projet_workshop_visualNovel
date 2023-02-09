J "Kim ! Regarde-moi… Bordel, Bryan vient m’aider ! Elle se vide de son sang !"
B "Appuie sur ses plaies, il faut que l’on trouve de quoi la bander !"

if (troussedeSoin = 1):
    jump postTelephone
else:
    jump postSoins

label postTelephone:
    #Son manquant à la sonothèque
    play sound "audio/Sounds/.mp3"

    E "Le cri d’un homme résonne dans la maison."
    A "C’était quoi ça ?"
    J "Merde, c’est Bryan !"
    A "Bryan ? Il ne devait pas rester avec Kim ?"
    J "Il faut qu’on aille l’aider…"
    A "Quoi ? Tu ne vois pas que Kim se vide de son sang ? La pauvre elle s’est refaite plantée. Si on ne la sort pas de là, elle va y passer la prochaine fois !"

    menu:
        "Mettre Kim à l'abri":
            jump kimAbri
        "Aller sauver Bryan":
            jump sauvetageBryan


label kimAbri:
    J "Ok, porte la… Il faut qu’on se dépêche, avant qu’elle ne perde trop de sang !"
    A "Ça continue de couler !"
    J "Alors on la tire, vas-y dépêche toi !"
    E "Jason et Anna sortent de la maison, tirant Kim jusque dans les bois environnants."
    J "Ici, on va pouvoir la laisser."
    A "Ok, dépose-la tout doucement."
    E "Des branches craquent dans leur dos."

    N "Lâchez la… elle mérite…"


label sauvetageBryan:
    

label postSoins:

    play sound "audio/Sounds/Cri Kim 1.mp3"

    E "Le cri de femme rententit."
    B "C’était quoi ça ?"
    J "Merde, c’est Anna !"
    B "Anna ? Où est-ce qu’elle est partie ?"
    J "Il faut qu’on aille l’aider…"
    B "Quoi ? Tu ne vois pas que Kim se vide de son sang ? Elle s’est refaite planter ! Si on ne la sort pas de là, elle va y passer la prochaine fois !"
    J "On ne va pas la laisser crever !"
    B "Alors vas y, fonce ! Je m’occupe de Kim, toi, vas aider Anna !"
    E "Jason se précipite dans les escaliers"


