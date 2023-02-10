label suivre_Bryan:

    $ relationJtoA += 1

    J "Euh... Je pense que Bryan a raison. Surtout que les secours n’arriveront pas tout de suite."
    A "Mais... Vous savez au moins ce que vous allez faire une fois que vous aurez la trousse de secours ?"
    B "On improvisera ! Il faut qu’on essaie, on ne va pas la laisser crever là dans le froid !"
    A "Non mais j’hallucine... Bon allez-y dépêchez-vous !"

    scene escalier
    with dissolve

    E "Sans perdre un instant, Bryan et Jason remontent les escaliers en direction du rez-de-chaussée."
    B "Hé, Jason... Merci de m’avoir écouté..."
    J "Anna n’a pas totalement tort, tu sais... Je ne sais pas soigner les gens."
    B "Je sais... mais je ne peux pas rester là sans rien faire. Pas pour Kim."


if (relationJtoK >= 0 and blessure_kim == 1):
    B "Hé d’ailleurs, quand j’ai aidé Kim elle m’a demandé de te donner ça... Je pense que ça pourrait nous être utile... Tiens, prends-la !"
    E "Bryan tend à Jason une lampe torche."
    $ torche = True

elif (relation JtoK < 0 and blessure_kim == 1):
    B "Hé d’ailleurs, quand j’ai aidé Kim elle m’a confié ça... Je pense que ça nous sera utile."
    E "Bryan montre une lampe torche."
    $ torche = False

elif (blessure_kim == 2) :
    B "Hé d’ailleurs, je viens de trouver ça dans la cave... Je pense que ça nous sera utile."
    E "Bryan montre une lampe torche."
    $ torche = False

J "Ok, parfait."

scene couloir_nuit
with dissolve

E "Le duo grimpe l'escalier menant hors de la cave, pour arriver dans un couloir."    
J "Euh... Bryan... Les lumières étaient éteintes tout à l’heure ?"
B "Je... Je ne crois pas ?"
E "Bryan clique sur un interrupteur, avant de le marteler avec impatience."
B "Les interrupteurs ne fonctionnent plus !"
J "Qu’est-ce qui se passe..."


if (torche == True):
    E "Allumant sa lampe torche, Jason passe devant, avançant doucement à pas feutré jusqu'au hall d'entrée de la maison."

elif (torche == False):
    E "Allumant sa lampe torche, Bryan passe devant, un peu trop sûr de lui, jusqu'au hall d'entrée de la maison."
    J "T’as une idée de qui pourrait avoir fait ça, toi ?"
    B "J’en ai aucune idée, mais c’est forcément un malade. Mon dieu... qui pourrait faire ça..."
    J "C’est une bonne chose d’avoir laissé Anna avec Kim, elle connait plus de choses que nous pour la soigner, elle sera capable de la maintenir en état jusqu'à notre retour."
    B "Ouais, il faut juste espérer qu’il y ait bien qu’une seule personne à vouloir notre peau ici..."
    E "Une porte claque violemment derrière le duo !"
    B "Wouaw, c’était quoi ça ?"
    J "Rien, la porte vient de claquer...J’ai eu une de ces peurs !"
    B "Tu parles, j’ai carrément failli me pisser dessus !"
    B "Attends, tu sens le courant d’air ?"
    J "Ouais..."
    E "Avançant pas à pas, les deux amis suivent le vent à travers le hall d’entrée."

if(vu_fenetre_ouverte == False):
    scene fenetre_nuit
    with dissolve
    
    B "Elle n’était pas fermée tout à l’heure celle-là ?"
    J "Si. Si, je crois bien." 

jump fenetre_ouverte_Bryan

if(vu_fenetre_ouverte == True):
    scene fenetre_nuit
    with dissolve

    B "Putain, c'est la même fenêtre que tout à l'heure ! Je vous l'avais dit !"
    J "Ca commence à devenir extrêmement flippant."

jump fenetre_ouverte_Bryan

label fenetre_ouverte_Bryan:

    J "Vas-y, va la claquer, je te couvre..."
    B "Quoi ? T’as vu comment tu trembles, tu me couvres rien du tout !"
    J "Mais si... Tu sais mieux fermer les fenêtres que moi !"
    B "Je te déteste... On voit qui est le plus courageux, ici."
    E "Bryan s'avance en direction de la fenêtre, avant de sursauter brusquement."
    B_shout "AHHHH"
    J "Quoi, qu’est-ce qu’il y a ?"
    B "Dehors ! Dehors, j’ai vu quelque chose !"
    J "T’as vu quoi ?"
    B "Je ne sais pas, quelque chose a bougé. Oh merde..."

    if (torche == True):

        menu:
            "Observer dehors":
                jump observer_dehors_torche_Bryan
            "Refermer la fenêtre":
                jump fermer_fenetre_torche_Bryan
            "Eteindre la lampe et se cacher":
                jump eteindre_lampe_torche_Bryan

    elif (torche == False):
    
        J "Hé, je crois que j’ai une idée !"
    
        if (relationJtoB >= 0):

            menu:
                "Observer dehors":
                    jump observer_dehors_Bryan
                "Refermer la fenêtre":
                    jump fermer_fenetre_Bryan
                "Eteindre la lampe et se cacher":
                    jump eteindre_lampe_Bryan

            jump chouette

        elif (relationJtoB < 0):
            
            menu:
                "Observer dehors":
                    jump initiative_Bryan
                "Refermer la fenêtre":
                    jump initiative_Bryan
                "Eteindre la lampe et se cacher":
                    jump initiative_Bryan

            jump chouette


label initiative_Bryan:

    E "Jason n'a même pas le temps de proposer sa suggestion, Bryan prend aussitôt les choses en main."
    B "Laisse-moi faire, je vais te montrer comment on gère ce genre de chose."
    B_shout "Hé ! Je ne sais pas qui vous êtes mais je vous déconseille de vous approcher !"
    B_shout "Ouais, vous là ! On est armés ici, alors dégagez avant que je vienne vous coller une balle entre les deux yeux, c’est compris ?"
    J "Tu joues à quoi là ?"
    B "J’ai vu ça dans les films, ça marche...souvent."
    J "Ouais bah on est pas dans un film alors tais-toi avant de finir comme Kim, ok ?"
    B_murmure "Ouais... je pense que je l’ai impressionnée. C’est sûr, même."
    J "... Attends, il fait du bruit, non ?"
    E "Attentifs aux bruits de l’extérieur, les deux amis tendent l’oreille... Encore... Encore..."
    jump chouette

label observer_dehors_torche_Bryan:
    J "Laisse-moi voir un peu."
    B "Fais attention... On ne sait jamais..."
    E "Jason balaye le faisceau de lumière à travers la fenêtre. Rien ne semble bouger."
    J "Je ne vois rien, tu es sûr de ce que tu as vu ?"
    B "Mais quand est-ce que tu vas arrêter de douter de tout ce que je te dis !"
    jump chouette

label fermer_fenetre_torche_Bryan:
    J "Pousse toi, je vais la refermer, si tu as si peur que ça..."
    B "Fais attention s’il te plait ! Je suis sûr de ce que j’ai vu !"
    E "Jason vient refermer la fenêtre lorsqu’il remarque un détail troublant. En effet, la poignée de la fenêtre est fracturée."
    J_murmure "Euh... Bryan ? Regarde ça..."
    B_murmure "Quoi ? Oh putain. Tu crois que quelqu’un l’a cassé ?"
    J_murmure "On dirait bien..."
    jump chouette

label eteindre_lampe_torche_Bryan:
    J "Viens vite ! Cache-toi !"
    E "Se précipitant sous le rebord de la fenêtre, les deux amis attendent en silence, cachés."
    B_murmure "On va rester ici combien de temps ?"
    J_murmure "Jusqu’à ce qu’on puisse sortir..."
    B_murmure "Alors ça risque d’être long..."
    jump chouette
    
label observer_dehors_Bryan:
    J "Jette un oeil à travers la fenêtre avec ta lampe torche."
    B "Laisse-moi voir un peu."
    J "Fais attention... On ne sait jamais..."
    E "Bryan balaye le faisceau de lumière à travers la fenêtre. Rien ne semble bouger."
    B "Je ne vois rien, tu es sûr de ce que tu as vu ?"
    J "Mais quand est-ce que tu vas arrêter de douter de tout ce que je te dis !"
    jump chouette

label fermer_fenetre_Bryan:
    J "Referme la fenêtre... C'est peut-être la personne qui a blessé Kim !"
    B "Très bien, je vais la refermer, si tu as si peur que ça..."
    E "Bryan vient refermer la fenêtre lorsqu’il remarque un détail troublant. En effet, la poignée de la fenêtre est fracturée."
    B_murmure "Euh... Jason ? Regarde ça..."
    J_murmure "Quoi ? Oh mon dieu. Tu crois que quelqu’un l’a cassé ?"
    B_murmure "On dirait bien..."
    jump chouette

label eteindre_lampe_Bryan:
    J "Viens vite ! Cache-toi !"
    E "Se précipitant sous le rebord de la fenêtre, les deux amis attendent en silence, cachés."
    J_murmure "On va rester ici combien de temps ?"
    B_murmure "Jusqu’à ce qu’on puisse sortir..."
    J_murmure "Alors ça risque d’être long..."

label chouette:
    E "Soudain, le hululement d’une chouette résonna entre les arbres du jardin."
    B_shout "AHHHHH"
    J "Saloperie de chouette !"
    B "Je hais les chouettes... La vache, j’ai failli me faire dessus..."
    J "Ouais, mais si on voulait rester discret, maintenant c’est foutu..."
    B "C’est jamais foutu, viens, il faut qu’on y aille avant qu’il soit trop tard..."
    J_murmure "Attends ! Ne. Bouge. Surtout. Pas." #(chuchote, doucement)

    scene porte_entree
    with dissolve

    E "De l’autre côté de la porte d’entrée, des bruits de pas commencent à crisser sous des semelles de chaussures."
    B_murmure "Tu crois que c’est lui ?" 
    J_murmure "Chut ! Tais-toi !"

    menu:
        "Se cacher":
            jump se_cacher_Bryan
        "Menacer":
            jump menacer_Bryan
        "Bloquer la porte":
            jump bloquer_Bryan

label menacer_Bryan:
    E "Plus ils attendent, plus les bruits de pas commencent à s’approcher dangereusement de la porte."
    B_murmure "Il va rentrer !"
    J "Euh... N’entrez pas ! On est armés, et euh... on n’hésitera pas à vous tirer dessus !"
    B "Mais arrête Bryan, ça ne marche pas ton truc !"
    B "Arrêtez d’avancer ! Stop !"
    E "Les bruits de pas, lents et sinistres, continuaient inlassablement d’avancer jusqu’au pas de la porte."
    $menacer_psychopathe = True

    scene tueur
    with dissolve

    E "Doucement le bruit de la poignée grince dans l’entrée de la maison, laissant apparaître dans l’encadrement de la porte une jeune femme vêtue d’une robe et le visage caché par un masque blanc, tenant un couteau à la main."

    jump combat_SK

label bloquer_Bryan:
    E "Plus ils attendent, plus les bruits de pas commencent à s’approcher dangereusement de la porte."
    J_murmure "Il va rentrer !"
    J "J’ai une idée !"
    E "D’un bon, Jason jette son corps sur la porte en bois. Il peut alors sentir des coups frénétiques contre la porte, comme si la personne plantait sa lame dans l’espoir de la faire traverser."
    B "On ne va pas pouvoir rester comme ça très longtemps !"
    J "Tu vois une autre idée, toi ?"
    B "Merde... Réfléchis, réfléchis, réfléchis..."
    B "Bordel, je suis désolé Jason, mais là, Kim est en danger ! Tiens bon, je vais chercher la trousse de soin !"
    J "Quoi ?"
    B "Promets moi de sauver ta peau, s’il te plait."
    J "Qu’est-ce que tu fais ? Bryan, non !"
    E "S’élançant à travers la vitre ouverte, Bryan plonge dans l’obscurité de la nuit. Les coups continuent de résonner contre la porte, avant de cesser au bout d'une minute. Le silence."
    E "Jetant un coup d'oeil à travers la serrure de la porte, Jason ne voit personne. Il est désormais seul."

    jump pointNclicCuisineSeul #point and clic sans allié

label se_cacher_Bryan:

    J_murmure "Viens avec moi. Tout. Doucement."
    E "Le plus discrètement possible, les deux amis reculent, recroquevillés sur eux-mêmes."
    J_murmure "Va dans le couloir. Maintenant !"
    B_murmure "Mais... et si elle vient vers nous, on fait quoi ?"
    J_murmure "On improvise. Maintenant vite !"
    E "A peine ont-ils le temps de se cacher que la porte s’ouvre."

    scene tueur
    with dissolve

    pause 1

    scene cachette_placard
    with dissolve

    B_murmure "Attends, ne ferme pas la porte..."
    B_murmure "Il faut voir qui c’est !"
    J_murmure "Regarde, on dirait une femme."
    B_murmure "Une femme ? Tu connais une femme qui serai capable de planter Kim, toi ?"
    J_murmure "Non... Maintenant tais-toi, on va se faire chopper..."
    E "La tueuse continue d'arpenter le hall d'entrée, traquant, observant..."
    B_murmure "Ecoute. Il faut récupérer au plus vite la trousse de soin. Le mieux pour ça, c'est que je fasse distraction."
    J_murmure "Quoi ? Mais t’es malade !"
    B_murmure "Non mais regarde-la ! Je sais que je peux courir plus vite qu’elle. Je te jure que je peux la distancer."
    B_murmure "Et pendant ce temps-là, t’as le temps de foncer récupérer la trousse de soin."

    menu:
        "Accepter":
            jump accepter_Bryan

        "Refuser":
            jump refuser

label refuser:

    if(relationJtoB < 0):

        jump refuser1

    if(relationJtoB >= 0):

        jump refuser3


label accepter_Bryan:
    J_murmure "Bon, ok. Mais fais attention à toi !"
    B_murmure "Ne t’inquiète pas pour moi, inquiète-toi plus pour Kim maintenant"
    E "Sans un bruit, Bryan se faufile hors du couloir, se place au milieu de l’entrée et hurle à plein poumons avant de sortir en courant de la maison."
    E "Dans son dos, la femme s’est lancée à sa poursuite."

    jump pointNclicCuisineSeul


label refuser1:
    J_murmure "Mais t’es malade ! Ne fais pas ça, tu ne sais pas de quoi elle est capable !"
    B_murmure "Alors quoi, tu veux qu’on reste ici pendant que Kim se vide de son sang ? Fais moi confiance, je suis en train de sauver ta meuf !"
    J_murmure "Bryan, non... !"
    E "Sans plus de débat, Bryan se faufile en silence hors du couloir, se place au milieu de l’entrée et hurle à plein poumons avant de sortir en courant de la maison."
    E "Dans son dos, la femme s’est lancée à sa poursuite."

    $distraction_Bryan = False

    jump pointNclicCuisineSeul

label refuser3:
    J_murmure "Mais t’es pas bien ! Si ça se trouve elle court beaucoup plus vite que toi ! Tu vas faire quoi face à une arme blanche ?"
    B_murmure "Hmmmm."
    B_murmure "Dans ce cas, il faut qu’on s’arme, et vite"
    J "Ah, là je suis d’accord avec toi, mais pour l’instant reste caché et ferme-la !"
    E "Accroupis dans la pénombre du couloir, Jason et Bryan observent la jeune femme passer dans la pièce, vêtue d’une longue robe et d’un masque blanc, cachant son visage aux deux jeunes hommes."
    E "Malheureusement pour eux, plus temps avance, plus la femme se rapproche de leur emplacement."

    jump combat_SK

label combat_SK:

    scene entree_nuit
    with dissolve

    if (menacer_psychopathe):
        if (torche):
            menu:
                "L'aveugler avec la lampe":
                    jump aveugler_Bryan
                "Fuir":
                    jump fuite_Bryan
        else : 
            jump fuite_Bryan

    elif (menacer_psychopathe == False):
        if (torche):
            menu:
                "Rester caché":
                    jump rester_cache
                "L'aveugler avec la lampe":
                    jump aveugler_Bryan
                "Fuir":
                    jump fuite_Bryan
        else : 
            menu:
                "Rester caché":
                    jump rester_cache
                "Fuir":
                    jump fuite_Bryan
    
label fuite_Bryan:
    J_murmure "Elle arrive vers nous..."
    B_murmure "Merde... qu’est-ce qu’on fait ?"
    J_murmure "Je ne sais pas... Elle arrive..."
    B_murmure "Il faut qu’on se sépare, on n’a pas le choix. Tu sais quoi, tant pis. Je vais courir, toi pendant ce temps là, cours dans l’autre direction."
    B_murmure "Avec un peu de chance, je vais pouvoir la retenir assez longtemps que pour que t’aille chercher du soin."
    J_murmure "T’es sûr de ton coup ?"
    B_murmure "Ne t’en fais pas pour moi, on n’a pas d’autre choix... Au pire, je vais essayer de trouver de l’aide dehors, d’accord ? Aller."
    B_shout "Maintenant !"
    E "Poussant la porte de toutes ses forces, Bryan réussi presque à renverser la femme lorsqu’il l’attira à l’extérieur. Attendant que la femme passe la porte, Jason se précipite dans la maison."

    jump pointNclicCuisineSeul
        
label rester_cache:
    E "Malgré tout, elle s’arrête à quelques mètres de la porte. Jetant un œil par-dessus son épaule, elle se décide à faire demi-tour, s’engouffrant sans un bruit à travers la fenêtre ouverte."
    B_murmure "Où est-ce qu’elle va ?"
    J_murmure "Elle doit nous chercher dans le jardin, elle ne doit pas penser qu’on se trouve ici..."
    J_murmure "Perdons pas plus de temps, allons-y."
    E "Les deux garçons quittent leur cachette, franchissant le reste de la maison en silence jusqu'à leur destination."

    $compagnie_Bryan = True

    jump pointNclicCuisineAllie

label aveugler_Bryan:
    J_murmure "Hé, j’ai une idée débile, mais ça peut marcher ! Je vais utilise ma lampe torche pour l’aveugler."
    B_murmure "Bonne idée ! Ca nous laissera peut-être assez de temps pour lui en coller une ou l’attirer plus loin des filles !"
    J_murmure "Ok, bonne idée ! A trois !"
    J_murmure  "Un"
    J_murmure  "Deux"
    J_shout  "Trois !"
    E "Le faisceau de lumière planté sur la femme, les deux garçons en profitent pour foncer à travers le hall d'entrée en direction d'un corridor."

    scene entree_ouverte
    with dissolve

    J_shout "Cours ! Elle est derrière toi !"
    
    menu:
        "Bloquer la porte":
            $ obstacles +=1
            jump suite21
        "Foncer à travers le couloir":
            jump suite21


label suite21:

    scene couloir_choix
    with dissolve

    E "A travers le corridor, Bryan fonce à vive allure, et disparaît dans un angle. Mais la tueuse talonne non loin le duo."
    B_shout "Fonce !"
    E "Une pièce cachée dans l'ombre se révèle sur la droite de Jason."

    menu:
        "Faire tomber un meuble":
            $ obstacles+=1
            E "Passant entre les meubles du corridor, Jason pousse une commode de toutes ses forces, obstruant le passage qui pouvait mener jusqu’à la suite du passage."
            B "Putain Jason, dépêche toi !"
            jump suite22
        "Foncer":
            E "Sans réfléchir, Jason court à toute vitesse à travers le corridor pour rattraper son retard sur Bryan."
            jump suite22
        "Se cacher":
            E "Courant à travers le corridor, Jason plonge dans la pièce tapie dans l'ombre. Il entend la tueuse passer en coup de vent dans le corridor sans s'arrêter, avant de faire place au silence."
            jump pointNclicCuisineSeul

label suite22:

    scene sceau
    with dissolve
    
    J "Et maintenant, on fait quoi ?"
    B "Par là ! Vite !"
    E "Continuant la fuite, Bryan commence petit à petit à distancer Bryan."

    menu:
        "Renverser un seau d'eau":
            $ obstacles +=1
            E "Un seau d’eau est posé contre l’un des murs."
            E "Dans un éclair de lucidité, Jason l’attrape et jette son contenu qui se déverse sur le sol."
            jump suite23
        "Foncer":
            E "Fonçant, Jason arrive enfin au bout de cette série de couloirs."
            jump suite23


label suite23:

    scene porte_fin
    with dissolve

    if (obstacles ==3):
        E "Jason arrive en trombe dans le séjour. Les bruits de pas de la tueuse ne se font plus entendre, mais Bryan a disparu, l'ayant visiblement distancé."
        jump pointNclicCuisineSeul
    else :
        E "Jason arrive en trombe dans le séjour en compagnie de Bryan. Les bruits de pas de la tueuse ne se font plus entendre : les différents obstacles ont dû suffir à la ralentir suffisamment pour la semer."
        B_murmure "Putain, c'était flippant !"
        J_murmure "Chut, tais-toi ! Allons vite dans le salon."
        E "Tous deux franchissent la porte les menant au salon."

        $compagnie_Bryan = True

        jump pointNclicCuisineAllie

label pointNclicCuisineAllie:

    scene salon_nuit_objet
    with dissolve

    E "Après avoir franchi la maison, Jason et Anna arrivent dans le salon, concomittant à la cuisine. Bryan ferme la porte à clé derrière eux."
    B "Je surveille l'entrée. Trouve cette trousse de soin."
    J_think "Bien. Commençons les recherches."

    jump openCuisine

label pointNclicCuisineSeul:

    scene salon_nuit_objet
    with dissolve

    if (distraction_Bryan == True):
        J_think "Putain, Bryan, qu'est-ce que tu peux être con quand tu t'y mets ! Jamais capable d'appliquer un plan !"
    else:
        J_think "'Chier. J'espère que Bryan va bien... Trouvons cette trousse au plus vite."
    
    jump openCuisine

