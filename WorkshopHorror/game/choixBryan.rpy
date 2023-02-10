label choix_Bryan4:

    $relationJtoA -= 1
    $relationJtoB += 1
    $ vu_fenetre_ouverte = True
    
    J "Tu veux qu’on aille voir ce que c’était ?"
    A "Ne me dites pas que vous allez le croire quand même !"
    J "On ne sait jamais... Et puis si jamais c’est juste un courant d’air on n’aura qu’à fermer la porte."
    K "Pourtant je crois que je n’ai ouvert aucune fenêtre..."
    A "Ouh la la, c’est peut être un fantôme !"
    J "Anna arrête un peu. Non mais sans rire vous pouvez pas vous tenir ne serait-ce qu’une soirée tous les deux ?"
    A "Hé ce n’est pas à moi de dire ça !"
    K "Anna, laisse tomber, arrête de nous prendre la tête s’il te plaît..."

#Prévoir K_murmure

E "Ensemble, à pas feutrés, les quatres amis se rendent sur le palier de l’entrée, dévoilant sous leurs yeux une fenêtre légèrement entrouverte."
A "Tu vois que ce n’était rien, juste la fenêtre ouverte..."
K_murmure "Je n’avais pas laissé la fenêtre ouverte pourtant..."
E "Kim active la lampe torche de son téléphone pour observer à travers la fenêtre ouverte, mais ne voit rien. Elle pose son téléphone sur le rebord de la fenêtre."
A "Vous flippez vraiment tous pour rien !"
B "Ferme-la, je te jure que j’ai entendu quelque chose... Je ne comprends pas !"
K "Bon j'en ai ras le cul ! Je me casse, je vais chercher une bouteille à la cave, tiens !"
E "Kim s'en va, en laissant derrière elle son téléphone."

$ telephone_oublie = True

    menu:
        "Calmer la dispute entre Bryan et Anna":
            jump calmer_dispute

        "Accompagner Kim":
            jump Kim_couloir

label calmer_dispute:

J "Bon, du calme ! On peut pas passer une bonne soirée là ?! C'est censé être la soirée de Kim, et regardez, elle s'est barrée !"
E "Anna et Bryan constatent le départ de Kim, qu'ils n'avaient pas."
J "Elle revient avec une bouteille. En attendant, calmez-vous, et soyez cool à son retour. Okay ?"
A "Ouais... Aller, venez on retourne au salon. La prochaine fois je vous jure que je ne bouge pas mon cul du canapé si c’est pour ce genre de connerie..."
B "Ouais... pourtant je te jure que j’ai entendu un truc bizarre..."
E "Une marche après l’autre, le trio reprend la route en direction du salon."

jump reunion