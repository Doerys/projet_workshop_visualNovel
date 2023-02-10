label suivre_Anna:

    $ relationJtoA += 1

    J "Euh... Je pense qu’Anna a raison... Je ne sais pas me servir d’une trousse de secours et on a pas de temps à perdre à essayer quoi que ce soit..."
    B "T’es sérieux ? Je te jure que si jamais il lui arrive quoi que ce soit pendant qu’on attends, c’est de ta faute."
    J "Attends, sérieusement Bryan ? Tu crois vraiment que je me fiche de ce qu’il peut arriver à ma copine ? J’essaie de faire au mieux, ok ?"
    A "Jason, si tu veux m’aider, c’est maintenant ou jamais !"
    J "J’arrive ! Juste Bryan... Fais moi confiance. S’il te plait. Le temps qu’on soit parti, essaie de maintenir la pression, assure-toi qu’elle reste en sécurité ici. On va faire vite."
    B "Ouais, ouais... C’est ça... Allez-y, mais dépêchez-vous. Par pitié, grouillez-vous !"

    scene escalier
    with dissolve

    E "Anna et Jason remontent les escaliers en direction du rez-de-chaussée."
    A "Hé, Jason... Merci de m’avoir écouté..."
    J "Bryan n’a pas totalement tort, tu sais... On ne doit pas perdre de temps."
    A "Je sais... mais je ne veux pas risquer de faire une erreur. On n’a pas de deuxième chance..."

    if (relationJtoK >= 0 and blessure_kim == 1):
        A "Hé d’ailleurs, quand j’ai aidé Kim elle m’a demandé de te donner ça... Je pense que ça pourrait nous être utile... Tiens, prends-la !"
        E "Anna vous tend une lampe torche."
        $ torche = True

    elif (relationJtoK < 0 and blessure_kim == 1):
        A "Hé d’ailleurs, quand j’ai aidé Kim elle m’a confié ça... Je pense que ça nous sera utile."
        E "Anna montre une lampe torche."
        $ torche = False

    elif (blessure_kim == 2) :
        A "Hé d’ailleurs, je viens de trouver ça dans la cave... Je pense que ça nous sera utile."
        E "Anna montre une lampe torche."
        $ torche = False

    J "Ok, parfait."

    scene couloir_nuit
    with dissolve

    E "Le duo grimpe l'escalier menant hors de la cave, pour arriver dans un couloir."    
    J "Euh... Anna... ôte moi d’un doute, les lumières étaient éteintes tout à l’heure ?"
    A "Je... Je ne crois pas ?"
    E "Anna clique sur un interrupteur, avant de laisser échapper un soupir."
    A "Oh non, les interrupteurs ne fonctionnent plus !"
    J "Qu’est-ce qui se passe..."

    if (torche == True):
        E "Allumant sa lampe torche, Jason passe devant, avançant doucement à pas feutré jusqu'au hall d'entrée de la maison."

    elif (torche == False):
        E "Allumant sa lampe torche, Anna passe devant, balayant le sol de son faisceau avec une prudence exacerbée."
    
    J "T’as une idée de qui pourrait avoir fait ça, toi ?"
    A "Aucune idée. Et je n'ai pas envie de le savoir. Plus vite on sera parti d'ici, plus vite on pourra oublier ça."
    J "C’est une bonne chose d’avoir laissé Bryan avec Kim, Au cas où ils se retrouvent en danger, il pourra plus facilement la défendre..."
    A "Ouais, il faut juste espérer qu’il y ait bien qu’une seule personne à vouloir notre peau ici..."
    E "Une porte claque violemment derrière le duo !"
    A "Qu'est-ce qu'il vient de se passer ?"
    J "Rien, la porte vient de claquer...J’ai eu une de ces peurs !"
    A "Je n'aime pas du tout ça !"
    J "Attends, tu sens le courant d’air ?"
    A "Sûrement une entrée ouverte..."
    E "Avançant pas à pas, les deux amis suivent le vent à travers le hall d’entrée."

    if(vu_fenetre_ouverte == False):

        A "Elle n’était pas fermée tout à l’heure celle-là ?"
        J "Si. Si, je crois bien." 

        jump fenetre_ouverte_Anna

    if(vu_fenetre_ouverte == True):
    
        A "C'est la même fenêtre que tout à l'heure..."
        J "Ca commence à devenir extrêmement flippant."

        jump fenetre_ouverte_Anna

label fenetre_ouverte_Anna:

    scene fenetre_nuit
    with dissolve

    A "Vas-y, va la fermer..."
    E "Peu rassuré, Jason s'avance vers la fenêtre." 
    E "En s'approchant de l'ouverture, il sursaute, lorsqu'il lui semble voir une ombre passer entre les arbres du jardin."
    A "Quoi, qu’est-ce qu’il y a ?"
    J "Dehors ! Dehors, j’ai vu quelque chose !"
    A "T’as vu quoi ?"
    J "Je ne sais pas, quelque chose a bougé. Oh merde..."

    if (torche == True):

            menu:
                "Observer dehors":
                    jump observer_dehors_torche_Anna
                "Refermer la fenêtre":
                    jump fermer_fenetre_torche_Anna
                "Eteindre la lampe et se cacher":
                    jump eteindre_lampe_torche_Anna

    elif (torche == False):
    
        J "Hé, je crois que j’ai une idée !"
    
        if (relationJtoA >= 0):

            menu:
                "Observer dehors":
                    jump observer_dehors_Anna
                "Refermer la fenêtre":
                    jump fermer_fenetre_Anna
                "Eteindre la lampe et se cacher":
                    jump eteindre_lampe_Anna

            jump chouette2

        elif (relationJtoA < 0):
            
            menu:
                "Observer dehors":
                    jump initiative_Anna
                "Refermer la fenêtre":
                    jump initiative_Anna
                "Eteindre la lampe et se cacher":
                    jump initiative_Anna

            jump chouette2

label initiative_Anna:

    E "Jason n'a même pas le temps de proposer sa suggestion, Anna prend aussitôt les choses en main."
    E "Anna s'empare d'une tapisserie, qu'elle vient aussitôt s'écarter de la fenêtre, pour s'emparer d'un tapis au sol."
    E "Elle place ensuite le tapis au-dessus de la fenêtre, en guise de rideau."
    A_murmure "Maintenant on ne peut plus nous voir. On attend en silence."


label observer_dehors_torche_Anna:
    J "Laisse-moi voir un peu."
    A "Fais attention... On ne sait jamais..."
    E "Jason balaye le faisceau de lumière à travers la fenêtre. Rien ne semble bouger."
    J "Je ne vois plus rien..."
    A "On devrait pas perdre plus de temps, et continuer."

    jump chouette2


label fermer_fenetre_torche_Anna:
    E "Jason vient refermer la fenêtre lorsqu’il remarque un détail troublant. En effet, la poignée de la fenêtre est fracturée."
    J_murmure "Euh... Anna ? Regarde ça..."
    A_murmure "Quoi ? Oh mon dieu. Tu crois que quelqu’un l’a cassé ?"
    J_murmure "On dirait bien..."

    jump chouette2


label eteindre_lampe_torche_Anna:
    J "Viens vite ! Cache-toi !"
    E "Se précipitant sous le rebord de la fenêtre, les deux amis attendent en silence, cachés."
    A_murmure "On va rester ici combien de temps ?"
    J_murmure "Jusqu’à ce qu’on soit sûr d'être hors de danger..."
    A_murmure "Alors ça risque d’être long... Kim est en danger."

    jump chouette2

label observer_dehors_Anna:
    J "Jette un oeil à travers la fenêtre avec ta lampe torche."
    A "T'es sûr que c'est prudent ?"
    J "Vas y."
    E "Anna balaye le faisceau de lumière à travers la fenêtre. Rien ne semble bouger."
    A "Je ne vois rien, tu es sûr de ce que tu as vu ?"
    J "Je crois..."

    jump chouette2

label fermer_fenetre_Anna:
    J "Referme la fenêtre... C'est peut-être la personne qui a blessé Kim !"
    E "Anna vient refermer la fenêtre lorsqu’elle remarque un détail troublant. En effet, la poignée de la fenêtre est fracturée."
    A_murmure "Euh... Jason ? Regarde ça..."
    J_murmure "Quoi ? Oh mon dieu. Tu crois que quelqu’un l’a cassé ?"
    A_murmure "On dirait bien..."

    jump chouette2


label eteindre_lampe_Anna:

    J "Vite ! Cache-toi !"
    E "Se précipitant sous le rebord de la fenêtre, les deux amis attendent en silence, cachés."
    A_murmure "On va rester ici combien de temps ?"
    J_murmure "Jusqu’à ce qu’on puisse sortir..."
    A_murmure "Alors ça risque d’être long..."


label chouette2:
    E "Soudain, le hululement d’une chouette résonna entre les arbres du jardin."
    A_shout "AHHHHH"
    J "Saloperie de chouette !"
    A_shout "Non... Non, non, non !"
    J "Qu’est-ce que tu as ?"
    A "Cette putain de chouette m’a fait faire tomber mon téléphone !"
    J "Quoi !?"
    J "Attends, ne me dis pas que..."
    A "Si ! Non mais c’est une blague ! Mon téléphone est complètement explosé !"
    J "Il ne fonctionne plus ?"
    A "Ahhh... non. Non, non, non, allez rallume toi, par pitié... Ton téléphone, Jason !"
    E "Jason tente d'allumer à son tour son téléphone, avant de constater qu'il n'a plus de batterie."
    J "Merde, on va faire comment ?"
    A "... Okay, c'est pas foutu. Kim doit bien avoir un autre appareil chez elle, elle change de téléphone tous les mois !"
    A "Il faut qu'on atteigne sa chambre, à l'étage. On pourra appeler les secours avec ce téléphone."
    J "Ok, allons voir ça !"
    A_murmure "Attends ! Ne. Bouge. Surtout. Pas." #(chuchote, doucement)

    scene porte_entree
    with dissolve

    E "De l’autre côté de la porte d’entrée, des bruits de pas commencent à crisser sous des semelles de chaussures."
    J_murmure "Tu crois que c’est lui ?" 
    A_murmure "Chut ! Tais-toi !"

    menu:
        "Se cacher":
            jump se_cacher_Anna
        "Menacer":
            jump menacer_Anna
        "Bloquer la porte":
            jump bloquer_Anna

label menacer_Anna:
    E "Plus ils attendent, plus les bruits de pas commencent à s’approcher dangereusement de la porte."
    A_murmure "Il va rentrer !"
    J "Euh... N’entrez pas ! On est armés, et euh... on n’hésitera pas à vous tirer dessus !"
    A_murmure "Mais arrête Bryan, ça ne marche pas ton truc !"
    J "Arrêtez d’avancer ! Stop !"
    E "Les bruits de pas, lents et sinistres, continuaient inlassablement d’avancer jusqu’au pas de la porte."

    $menacer_psychopathe = True

    scene tueur
    with dissolve

    E "Doucement le bruit de la poignée grince dans l’entrée de la maison, laissant apparaître dans l’encadrement de la porte une jeune femme vêtue d’une robe et le visage caché par un masque blanc, tenant un couteau à la main."

    jump combat_SK_Anna

label bloquer_Anna:

    E "Plus ils attendent, plus les bruits de pas commencent à s’approcher dangereusement de la porte."
    J_murmure "Il va rentrer !"
    J "J’ai une idée !"
    E "D’un bon, Jason jette son corps sur la porte en bois. Il peut alors sentir des coups frénétiques contre la porte, comme si la personne plantait sa lame dans l’espoir de la faire traverser."
    A "On ne va pas pouvoir rester comme ça très longtemps !"
    J "Tu vois une autre idée, toi ?"
    A "Merde... Réfléchis, réfléchis, réfléchis..."
    A "Je vois pas d'autres solutions, mais Kim est en danger ! On doit appeler les secours au plus vite ! Je vais te devoir te laisser."
    J "Quoi ?"
    A " Tiens bon, je vais les contacter !"
    J "Qu’est-ce que tu fais ? Anna, non !"
    E "Enjambant la fenêtre ouverte, Anna plonge dans l’obscurité de la nuit. Les coups continuent de résonner contre la porte, avant de cesser au bout d'une minute. Le silence."
    E "Jetant un coup d'oeil à travers la serrure de la porte, Jason ne voit personne. Il est désormais seul."

    jump pointNclicChambreSeul #point and clic sans allié

label se_cacher_Anna:

    J_murmure "Viens avec moi. Doucement."
    E "Le plus discrètement possible, les deux amis reculent, recroquevillés sur eux-mêmes."
    J_murmure "On n’a pas le choix, va dans le couloir. Maintenant !"
    A_murmure "Non ! Si elle nous entend, on peut être sûr qu’elle finira par buter Kim !"
    J_murmure "Fais moi confiance, je sais ce que je fais, Jason ! Vite !"
    E "A contre-coeur, Anna accepte et suit les instructions de Jason. A peine ont-ils le temps de se cacher que la porte s’ouvre."

    scene tueur
    with dissolve

    pause 1

    scene cachette_placard
    with dissolve

    A_murmure "Attends, ne ferme pas la porte..."
    A_murmure "Il faut voir qui c’est !"
    J_murmure "Regarde, on dirait une femme."
    A_murmure "Une femme ? Tu connais une femme qui serai capable de planter Kim, toi ?"
    J_murmure "Non... Maintenant tais-toi, on va se faire chopper..."
    A_murmure "Pourquoi, t’as un plan de génie pour nous sortir de la maison, peut-être ?"
    J_murmure "Sortir peut-être pas, mais oui j’ai un plan !"

    if (relationJtoA < 0):
        
        menu:
            "Distaire la femme":
                jump plan_fuite_Anna
            "Foncer vers la porte":
                jump plan_fuite_Anna
            "Rester caché":
                jump plan_fuite_Anna
    else :
        menu:
            "Distaire la femme":
                jump distraction_Anna
            "Foncer vers la porte":
                jump fuite_Anna
            "Rester caché":
                jump rester_cache_Anna

label plan_fuite_Anna:
    J_murmure "Alors voilà mon plan ! Si tu..."
    J "Héééééééééé !" # cri
    E "Anna pousse Jason contre la porte, faisant tomber son ami dans le hall d’entrée. Au-dessus de lui, la femme est entrée."

    scene entree_nuit
    with dissolve

    if (torche  == True):
        menu:
            "Fuir":
                jump vase
            "Eblouir avec la lampe torche":
                E "Au sol, Jason n’a pas le temps de se relever lorsque la femme vient se placer au-dessus de lui."
                E "Fouillant le sol de sa main, ses doigts rencontrent sa lampe torche."
                J_shout "Mange toi ça salope !"
                E "La femme est aveuglée ! Profitant des quelques secondes de répit, Jason se relève et court aussi vite que possible dans la maison."
                jump pointNclicChambreSeul
    else :
        jump vase

label vase:
    E "Poussant sur ses bras pour se relever, Jason tombe nez à nez face à la femme. Plus petite que lui, plus frêle. Tétanisé, il n’a pas le temps de s’échapper avant que la femme n’abatte un énorme vase sur sa tête. Inconscient, il tombe au sol."
    #FONDU AU NOIR
    E "Lorsqu’il se réveille, l’entrée est vide. Plus aucune trace de la femme, ni d’Anna."
    jump pointNclicChambreSeul

label distraction_Anna:

    J_chuchote "Ok, voilà mon plan… Il faut faire diversion pour pouvoir se glisser derrière elle."
    A_chuchote "J'ai peut-être une idée pour ça, mais je ne suis pas sûr que ça va marcher..."
    J_chuchote "On n’a pas le choix, vas-y !"
    E "Anna décroche sa montre, calibre une sonnerie et attends que la femme ait le dos tourné pour la lancer lancer à travers la fenêtre ouverte."
    E "Après quelques secondes, une mélodie retentit à l’extérieur, poussant la femme à sortir."
    A_chuchote "Tu me dois une montre, Jason."
    J_chuchote "Maintenant ! On court vers la chambre !"

    jump pointNclicChambreAllie

label fuite_Anna:

    A_murmure "Jason, elle arrive vers nous..."
    A_murmure "Merde... qu’est-ce qu’on fait ?"
    J_murmure "Il faut qu’on se sépare, on n’a pas le choix. Si elle nous attrape tous les deux, on est foutu."
    A_murmure "Quoi ? Tu veux vraiment risquer de te faire attraper ?"
    J_murmure "Avec un peu de chance, je vais pouvoir la retenir assez longtemps que pour que tu contactes les secours."
    A_murmure "T’es sûr de ton coup ?"
    J_murmure "On n’a pas d’autre choix, Anna. Tu veux sauver Kim ? Alors plus le temps de réfléchir."
    A_murmure "Très bien... Mais ne prends pas de risque, s’il te plait !"
    E "Poussant doucement la porte, Anna se faufile dans l’entrée avant de détaler en direction de l’extérieur."
    E "Jason fait de même, essayant d'attirer davantage l'attention de la femme." 
    E "Malheureusement, malgré leur plan, la femme semble prendre en chasse Anna, laissant Jason désormais seul."

    jump pointNclicChambreSeul

label rester_cache_Anna:
    E "Anna reste cachée derrière Jason. Les yeux rivés sur la femme masquée."
    E "Celle-ci avance d'un pas lent vers eux, avant de s'arrêter brusquement, puis faire demi-tour, s’engouffrant sans un bruit à travers la fenêtre ouverte."
    A_murmure "Où est-ce qu’elle va ?"
    J_murmure "Elle doit nous chercher dans le jardin, elle ne doit pas penser qu’on se trouve ici..."
    J_murmure "Perdons pas plus de temps, allons-y."
    E "Jason et Anna quittent leur cachette, franchissant le reste de la maison en silence jusqu'à leur destination."

    jump pointNclicChambreAllie

label combat_SK_Anna:

    if (menacer_psychopathe):
        if (torche):
            menu:
                "L'aveugler avec la lampe":
                    jump aveugler_Anna
                "Fuir":
                    jump fuite_Anna
        else : 
            jump fuite_Anna

    elif (menacer_psychopathe == False):
        if (torche):
            menu:
                "Rester caché":
                    jump rester_cache_Anna
                "L'aveugler avec la lampe":
                    jump aveugler_Anna
                "Fuir":
                    jump fuite_Anna
        else : 
            menu:
                "Rester caché":
                    jump rester_cache_Anna
                "Fuir":
                    jump fuite_Anna

label aveugler_Anna:

    J_murmure "Hé, j’ai une idée débile, mais ça peut marcher ! Je vais utiliser ma lampe torche pour l’aveugler."
    A_murmure "Bonne idée ! Ca nous laissera peut-être assez de temps de la semer !"
    J_murmure "Ok, bonne idée ! A trois !"
    J_murmure  "Un"
    J_murmure  "Deux"
    J_shout  "Trois !"
    E "Le faisceau de lumière planté sur la femme, Anna et Jason en profitent pour foncer à travers le hall d'entrée en direction d'un corridor."

    scene entree_ouverte
    with dissolve

    J_shout "Cours ! Elle est derrière toi !"
    
    menu:
        "Bloquer la porte":
            $ obstacles +=1
            jump poursuite1
        "Foncer à travers le couloir":
            jump poursuite1

label poursuite1:

    scene couloir_choix
    with dissolve

    E "A travers le corridor, Anna fonce à vive allure, et disparaît dans un angle. Mais la tueuse talonne non loin le duo."
    B_shout "Fonce !"
    E "Une pièce cachée dans l'ombre se révèle sur la droite de Jason."

    menu:
        "Faire tomber un meuble":
            $ obstacles+=1
            E "Passant entre les meubles du corridor, Jason pousse une commode de toutes ses forces, obstruant le passage qui pouvait mener jusqu’à la suite du passage."
            A "Jason, dépêche toi !"
            jump poursuite2
        "Foncer":
            E "Sans réfléchir, Jason court à toute vitesse à travers le corridor pour rattraper son retard sur Anna."
            jump poursuite2
        "Se cacher":
            E "Courant à travers le corridor, Jason plonge dans la pièce tapie dans l'ombre. Il entend la tueuse passer en coup de vent dans le corridor sans s'arrêter, avant de faire place au silence."
            jump pointNclicChambreSeul

label poursuite2:

    scene sceau
    with dissolve

    J "Et maintenant, on fait quoi ?"
    A "Par là ! Vite !"
    E "Continuant la fuite, Anna commence petit à petit à distancer Bryan."

    menu:
        "Renverser un seau d'eau":
            $ obstacles +=1
            E "Un seau d’eau est posé contre l’un des murs."
            E "Dans un éclair de lucidité, Jason l’attrape et jette son contenu qui se déverse sur le sol."
            jump poursuite3
        "Foncer":
            E "Fonçant, Jason arrive enfin au bout de cette série de couloirs."
            jump poursuite3
    
label poursuite3:

    scene porte_fin
    with dissolve

    if (obstacles ==3):
        E "Jason arrive en trombe dans le séjour. Les bruits de pas de la tueuse ne se font plus entendre, mais Anna a disparu, l'ayant visiblement distancé."
        jump pointNclicChambreSeul
    else :
        E "Jason arrive en trombe dans le séjour en compagnie d'Anna. Les bruits de pas de la tueuse ne se font plus entendre : les différents obstacles ont dû suffir à la ralentir suffisamment pour la semer."
        J_murmure "On s'en est sorti !"
        A_murmure "Chut, tais-toi ! Allons vite dans la chambre de Kim."
        E "Tous deux franchissent grimpent en silence de escaliers menant à l'étage."

        $compagnie_anna = True

        jump pointNclicChambreAllie

label pointNclicChambreSeul:

label pointNclicChambreAllie: