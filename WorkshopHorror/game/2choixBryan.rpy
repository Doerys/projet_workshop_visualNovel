label choix_Bryan4:

    $relationJtoA -= 1
    $relationJtoB += 1
    $ vu_fenetre_ouverte = True

    J "Tu veux qu’on aille voir ce que c’était ?"

    show anna surpris2_j

    A "Ne me dites pas que vous allez le croire quand même !"
    J "On ne sait jamais... C'est peut-être un animal qui est rentré dans la maison ?"
    K "Pourtant, je crois que j'ai bien fermé l'entrée..."

    show anna jugement_j    

    A "Ouh la la, c’est peut être un fantôme !"
    J "Anna, arrête un peu. Non mais sans rire, vous pouvez pas vous tenir ne serait-ce qu’une soirée ?"

    show anna colere_j

    A "Hey, ce n’est pas à moi qu'il faut dire ça !"

    show kim pense_j

    K "Anna, laisse tomber, arrête de nous prendre la tête s’il te plaît..."

#Prévoir K_murmure

scene fenetre_jour
with dissolve

E "Ensemble, à pas feutrés, les quatres amis se rendent dans le hall d'’entrée, révélant sous leurs yeux une fenêtre légèrement entrouverte."

show anna jugement_j at center:
    xalign 0.95

A "Tu vois que ce n’était rien, juste la fenêtre ouverte..."

show kim reflechir_j at center

K_murmure "Je n’avais pas laissé la fenêtre ouverte pourtant..."

E "Kim active la lampe torche de son téléphone pour observer à travers la fenêtre ouverte, mais ne voit rien. Elle pose son téléphone sur le rebord de la fenêtre."
A "Vous flippez vraiment tous pour rien !"

show bryan surpris_j at center:
    xalign 0.05

B "Ferme-la, je te jure que j’ai entendu quelque chose... Je ne comprends pas !"
A "Qu'est-ce que tu veux qu'on te dise, quand on est à la fois con et bourré, ça donne rarement des situations convaincantes."

show bryan colere_j

B "Oh toi, tu me casses les couilles !"

show kim colere_j

K "Bon j'en ai ras le cul, de vous deux ! Puisque c'est comme ça, je me casse !" 

K "Je vais chercher une bouteille à la cave, tiens !"

hide kim colere_j

E "Kim s'en va, en laissant derrière elle son téléphone."

$ telephone_oublie = True

menu:
    "Anna et Bryan continuent de se disputer, et Kim s'éloigne."
    "Calmer la dispute":
        jump calmer_dispute

    "Accompagner Kim":
        jump Kim_couloir

label calmer_dispute:

show bryan colere_j at center:
    xalign 0.2

show anna jugement_j at center:
    xalign 0.8

J "Bon, du calme ! On peut pas passer une bon moment, pour une fois ?! C'est censé être la soirée de Kim, et regardez, elle s'est barrée !"

show bryan reflechir_j

show anna reflechir_j

E "Anna et Bryan constatent le départ de Kim, qu'ils n'avaient pas remarqué. Ils semblent gênés."
J "Elle revient avec une bouteille. Alors en attendant, calmez-vous, et soyez cool à son retour. Okay ?"

show anna normal3_j

A "Ouais... Okay. Allez, venez on retourne au salon." 
A_murmure "Mais la prochaine fois, je vous jure que je ne bouge pas mon cul du canapé si c’est pour ce genre de conneries..."

show bryan peur1_j

B "Ouais... pourtant je te jure que j’ai entendu un truc bizarre..."
E "Une marche après l’autre, le trio reprend la route en direction du salon."

jump reunion