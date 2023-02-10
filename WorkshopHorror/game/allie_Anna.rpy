label suivre_Anna:

    $ relationJtoA += 1

    J "Euh... Je pense qu’Anna a raison... Je ne sais pas me servir d’une trousse de secours et on a pas de temps à perdre à essayer quoi que ce soit..."
    B "T’es sérieux ? Je te jure que si jamais il lui arrive quoi que ce soit pendant qu’on attends, c’est de ta faute."
    J "Attends, sérieusement Bryan ? Tu crois vraiment que je me fiche de ce qu’il peut arriver à ma copine ? J’essaie de faire au mieux, ok ?"
    A "Jason, si tu veux m’aider, c’est maintenant ou jamais !"
    J "J’arrive ! Juste Bryan... Fais moi confiance. S’il te plait. Le temps qu’on soit parti, essaie de maintenir la pression, assure-toi qu’elle reste en sécurité ici. On va faire vite."
    B "Ouais, ouais... C’est ça... Allez-y, mais dépêchez-vous. Par pitié, grouillez-vous !"
    E "Sans perdre un instant, Anna et Jason remontent les escaliers en direction du rez-de-chaussée."
    A "Hé, Jason... Merci de m’avoir écouté..."
    J "Bryan n’a pas totalement tort, tu sais... On ne doit pas perdre de temps."
    A "Je sais... mais je ne veux pas risquer de faire une erreur. On n’a pas de deuxième chance..."

    if (relationJtoK >= 0 and blessure_kim = 1):
        A "Hé d’ailleurs, quand j’ai aidé Kim elle m’a demandé de te donner ça... Je pense que ça pourrait nous être utile... Tiens, prends-la !"
        E "Anna tend à Jason une lampe torche."
        $ torche = True

    else if (relation JtoK < 0 and blessure_kim = 1):
        A "Hé d’ailleurs, quand j’ai aidé Kim elle m’a confié ça... Je pense que ça nous sera utile."
        E "Anna montre une lampe torche."
        $ torche = False

    else if (blessure_kim = 2) :
        A "Hé d’ailleurs, je viens de trouver ça dans la cave... Je pense que ça nous sera utile."
        E "Anna montre une lampe torche."
        $ torche = False

    J "Ok, parfait."

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
    E "Soudain, le cri hululement d’une chouette résonna entre les arbres du jardin."
    A_shout "AHHHHH"
    J "Saloperie de chouette !"
    A_shout "Non... Non, non, non !"
    J "Qu’est-ce que tu as ?"
    A "Cette putain de chouette m’a fait faire tomber mon téléphone !"
    J "Quoi !?"
    J "Attends, ne me dis pas que..."
    A "Si ! Non mais c’est une blague ! Mon téléphone est complètement explosé !"
    J "Il ne fonctionne plus ?"
    A "Ahhh... non. Non, non, non, allez rallume toi, par pitié..."
    J "Merde, on va faire comment ?"
    A "... Kim doit bien avoir un autre appareil chez elle, elle change de téléphone tous les mois !"
    J "Ok, allons voir ça !"




