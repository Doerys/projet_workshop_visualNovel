label suivre_Bryan:

    $ relationJtoA += 1

    J "Euh... Je pense que Bryan a raison. Surtout que les secours n’arriveront pas tout de suite."
    A "Mais... Vous savez au moins ce que vous allez faire une fois que vous aurez la trousse de secours ?"
    B "On improvisera ! Il faut qu’on essaie, on ne va pas la laisser crever là dans le froid !"
    A "Non mais j’hallucine... Bon allez-y dépêchez-vous !"
    E "Sans perdre un instant, Bryan et Jason remontent les escaliers en direction du rez-de-chaussée."
    B "Hé, Jason... Merci de m’avoir écouté..."
    J "Anna n’a pas totalement tort, tu sais... Je ne sais pas soigner les gens."
    B "Je sais... mais je ne peux pas rester là sans rien faire. Pas pour Kim."


if (relationJtoK >= 0 and blessure_kim = 1):
        B "Hé d’ailleurs, quand j’ai aidé Kim elle m’a demandé de te donner ça... Je pense que ça pourrait nous être utile... Tiens, prends-la !"
        E "Bryan tend à Jason une lampe torche."
        $ torche = True

    else if (relation JtoK < 0 and blessure_kim = 1):
        B "Hé d’ailleurs, quand j’ai aidé Kim elle m’a confié ça... Je pense que ça nous sera utile."
        E "Bryan montre une lampe torche."
        $ torche = False

    else if (blessure_kim = 2) :
        B "Hé d’ailleurs, je viens de trouver ça dans la cave... Je pense que ça nous sera utile."
        E "Bryan montre une lampe torche."
        $ torche = False

    J "Ok, parfait."

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
    B "Elle n’était pas fermée tout à l’heure celle-là ?"
    J "Si. Si, je crois bien." 

    jump fenetre_ouverte_Bryan

    if(vu_fenetre_ouverte == True):
    B "Putain, c'est la même fenêtre que tout à l'heure ! Je vous l'avais dit !"
    J "Ca commence à devenir extrêmement flippant."

    jump fenetre_ouverte_Bryan

label fenetre_ouverte_Bryan:

    B "Attends... Elle était pas fermée tout à l’heure ?"
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
    J_murmure "Il va rentrer !"
    B "Euh... Vous n’entrez pas ! Je vous ai dit qu’on est armés, et euh... on n’hésitera pas à vous tirer dessus !"
    J "Mais arrête Bryan, ça ne marche pas ton truc !"
    B "Arrêtez d’avancer ! Stop !"
    E "Les bruits de pas, lents et sinistres, continuaient inlassablement d’avancer jusqu’au pas de la porte."
    J "Tu vois que ça ne sert à rien..."
    E "Doucement le bruit de la poignée grince dans l’entrée de la maison, laissant apparaître dans l’encadrement de la porte une jeune femme vêtue d’une robe et le visage caché par un masque blanc."

    jump combat_SK

label bloquer_Bryan:
    E "Plus ils attendent, plus les bruits de pas commencent à s’approcher dangereusement de la porte."
    J_murmure "Il va rentrer !"
    B "J’ai une idée ! Fais comme moi, vite !"
    E "D’un bon, Bryan jeta son corps sur la porte en bois. Faisant de même, Jason pouvait sentir contre la porte quelques coups, comme si la personne plantait sa lame dans l’espoir de la faire traverser."
    B "On ne va pas pouvoir rester comme ça très longtemps !"
    J "Tu vois une autre idée, toi ?"
    B "Merde... Réfléchis, réfléchis, réfléchis..."
    B "Hé Jason ? Si je te laisse du temps pour régler tous les problèmes, tu m’assures que tu y arriveras ?"
    J "Quoi ?"
    B "Promets moi que tu vas sauver Kim, s’il te plait."
    J "Qu’est-ce que tu fais ? Bryan, non !"
    E "S’élançant à travers la vitre ouverte, Bryan plonge dans l’obscurité de la nuit, entraînant derrière lui l’agresseur. Seul, Jason se précipite alors vers la cuisine, où par chance, il pourrait trouver de quoi sauver sa petite-amie."

    jump on_continu #point and clic sans allié

label se_cacher_Bryan:
    J_murmure "Viens avec moi. Tout. Doucement."
    E "Le plus discrètement possible, les deux amis reculent, recroquevillés sur eux-mêmes."
    J_murmure "Va dans le couloir. Maintenant !"
    B_murmure "Mais... et si elle vient vers nous, on fait quoi ?"
    J_murmure "On improvise. Maintenant vite !"
    E "A peine ont-ils le temps de s’enfermer que la poignée de la porte s’ouvre."
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
        J "Je peux pas te laisser faire ça, c'est trop dangereux."
        B "Ecoute mec, je vais me passer de ton avis pour le moment, désolé."
        E "Sans plus de débat, Bryan se faufile hors du couloir, se place au milieu de l’entrée et hurle à plein poumons avant de sortir en courant de la maison."
        E "Dans son dos, la femme s’est lancée à sa poursuite."

    if(relationJtoB >= 0):
        J "Je peux pas te laisser faire ça, c'est trop dangereux."
        B "Très bien. C'est toi le chef."


label accepter_Bryan:
    J_murmure "Bon, ok. Mais fais attention à toi !"
    B_murmure "Ne t’inquiète pas pour moi, inquiète-toi plus pour Kim maintenant"
    E "Sans un bruit, Bryan se faufile hors du couloir, se place au milieu de l’entrée et hurle à plein poumons avant de sortir en courant de la maison."
    E "Dans son dos, la femme s’est lancée à sa poursuite."

    jump Bryan_distraction


label refuser1:
    J_murmure "Mais t’es malade ! Ne fais pas ça, tu ne sais pas de quoi elle est capable !"
    B_murmure "Alors quoi, tu veux qu’on reste ici pendant que Kim se vide de son sang ? Fais moi confiance, je suis en train de sauver ta meuf !"
    E "Sans un bruit, Bryan se faufile hors du couloir, se place au milieu de l’entrée et hurle à plein poumons avant de sortir en courant de la maison."
    E "Dans son dos, la femme s’est lancée à sa poursuite."

    jump Bryan_distraction

label refuser3:
    J_murmure "Mais t’es pas bien ! Si ça se trouve elle court beaucoup plus vite que toi ! Tu vas faire quoi face à une arme blanche ?"
    B_murmure "Hmmmm."
    B_murmure "Dans ce cas, il faut qu’on s’arme, et vite"
    J "Ah, là je suis d’accord avec toi, mais pour l’instant reste caché et ferme-la !"
    E "Accroupis dans la pénombre du couloir, Jason et Bryan observent la jeune femme passer devant eux, vêtue d’une longue robe et d’un masque blanc, cachant son visage aux deux jeunes hommes."
    E "Malheureusement pour eux, plus temps avance, plus la femme se dirige dans leur direction."

    jump combat_SK

label combat_SK:

    if (torche == True):
        menu:
            "Rester caché":
                jump rester_cache
            "Aveugler avec la lampe":
                jump aveugler_Bryan
            "Fuir":
                jump fuite_Bryan
    else : 
        menu:
            "Rester caché":
                jump rester_cache
            "Fuir":
                jump fuite_Bryan

        
label rester_cache:
    E "Malgré tout, elle s’arrête à quelques mètres de la porte. Jetant un œil par-dessus son épaule, elle se décide à faire demi-tour, s’engouffrant sans un bruit dans la pénombre du couloir du salon."
    B_murmure "Où est-ce qu’elle va ?"
    J_murmure "Elle doit nous chercher dans le salon, elle ne doit pas penser qu’on se trouve ici..."

    jump pointNclicAllie

label aveugler_Bryan:
    B_murmure "Hé, j’ai une idée débile, mais ça peut marcher ! Utilise ta lampe torche pour l’aveugler, ça nous laissera peut-être assez de temps pour lui en coller une ou l’attirer plus loin des filles !"
    J_murmure "Ok, bonne idée ! A trois !"
    J_murmure  "Un"
    J_murmure  "Deux"
    J_shout  "Trois !"
    E "Le faisceau de lumière planté sur la femme, les deux garçons en profitent pour foncer à travers l’entrée en direction du salon."
    J_shout "Cours ! Elle est derrière toi !"
    B_shout "Va dans le salon, j’ai une idée !"
    B_shout "Viens avec moi, on va la bloquer !"
    E "Alors que les deux garçons continuent de courir dans le couloir, la femme qui les poursuit commence à les rattraper."
    B_shout "Jay ! Maintenant !"

    menu:
        "Bloquer la porte":
            $ obstacles +=1
            jump suite21
        "Foncer à travers le couloir":
            jump suite21


label suite21:
    B "Fonce dans la cuisine, je vais te rattraper ! Vas y tant que je peux tenir la porte du salon !"
    E "Hésitant quelques instants à aider son ami, Jason continu son chemin jusque dans la cuisine."

    menu:
        "Faire tomber un meuble":
            $ obstacles+=1
            E "Passant entre les meubles du salon, Jason pousse une commode de toutes ses forces, obstruant le passage qui pouvait mener jusqu’à la cuisine"
            B "Putain Jason, elle me rattrape !"
            jump suite22
        "Foncer":
            E "Sans réfléchir, Jason passe entre les allées du salon. Connaissant la maison par cœur, il est facile pour lui de s’y repérer, la pièce est remplie d’obstacles."
            jump suite22
        "Se cacher":
            E "Courant à travers le salon, Jason a trop peur pour écouter son ami. Fouillant la pièce du regard, il trouve rapidement un moyen de fuir en grimpant les marches des escaliers deux par deux."
            E "Il devait se rendre dans la salle de bain. C’est le seul endroit où il connaît une cachette assez grande pour rester planqué."
            jump on_continu

label suite22:
    J "Et maintenant, on fait quoi ?"
    B "A l’étage ! On va pouvoir se cacher, vite !"
    E "Continuant la poursuite jusqu’à l’étage, Jason commence petit à petit à distancer Bryan."
    
   

    menu:
        "Renverser un seau d'eau":
            $ obstacles +=1
            E "Sur le palier de l’étage, un seau d’eau est posé contre l’un des murs."
            E "Dans un éclair de lucidité, Jason l’attrape et jette son contenu à travers les escaliers."
            B "Hé Jason, qu’est-ce que tu fais ?"
            jump suite23
        "Foncer":
            E "L’étage est constitué de quelques pièces. Certes, la maison de Kim n’est pas grande, mais c’est suffisant pour se cacher."
            E "Fonçant dans le couloir, il ouvre la première porte trouvée, et s’engouffre dans ce qui semble être la salle de bain."
            jump suite23


label suite23:
    if (obstacles ==3):
        E "Jason entre en trombe dans la chambre. Balayant la pièce des yeux, il n’avait pas beaucoup de choix pour se cacher."
        E "Après s’être assuré que la porte est fermée, il se précipite dans une petite cachette, lorsqu’il entend Bryan passer devant la porte avant de disparaître un peu plus loin."
        jump on_continu
    else :
        B_murmure "Jason ! Jason ! Jason !"
        J_murmure "Chut, tais-toi ! Elle t’a vu rentrer ?"
        B_murmure "Je ne crois pas ! Elle avait beaucoup trop de retard sur moi dans les escaliers."
        E "De l’autre côté du mur, les bruits de pas commencent à se faire entendre de plus en plus fort."
        E "Plongés dans une pièce sombre les deux amis ne bougent pas d’un cil jusqu’au moment où les bruits de pas de la femme semblent enfin s’éloigner."
        jump pointNclicAllie



label pointNclicAllie:
    ""



label on_continu:



label fuite_Bryan:
    J_murmure "Elle arrive vers nous..."
    B_murmure "Merde... qu’est-ce qu’on fait ?"
    J_murmure "Je ne sais pas... Elle arrive..."
    B_murmure "Il faut qu’on se sépare, on n’a pas le choix. Tu sais quoi, tant pis. Je vais courir, toi pendant ce temps là, cours dans l’autre direction."
    B_murmure "Avec un peu de chance, je vais pouvoir la retenir assez longtemps que pour que t’aille chercher du soin, ou un téléphone peu importe."
    J_murmure "T’es sûr de ton coup ?"
    B_murmure "Ne t’en fais pas pour moi, on n’a pas d’autre choix... Au pire, je vais essayer de trouver de l’aide dehors, d’accord ? Aller."
    B_shout "Maintenant !"
    E "Poussant la porte de toutes ses forces, Bryan réussi presque à renverser la femme lorsqu’il l’attira à l’extérieur. Attendant que la femme passe la porte, Jason se précipite dans la maison, avec comme objectif en tête de s’enfermer dans la cuisine."



label Bryan_distraction:

