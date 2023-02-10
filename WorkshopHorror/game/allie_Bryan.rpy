label suivre_Bryan:
    J "Euh... Je pense que Bryan a raison. Surtout que les secours n’arriveront pas tout de suite."
    A "Mais... Vous savez au moins ce que vous allez faire une fois que vous aurez la trousse de secours ?"
    B "On improvisera ! Il faut qu’on essaie, on ne va pas la laisser crever là dans le froid !"
    A "Non mais j’hallucine... Bon allez-y dépêchez-vous !"
    E "Sans perdre un instant, Bryan et Jason remontent les escaliers en direction de la maison de Kim."
    B "Hé, Jason... Merci de m’avoir écouté..."
    J "Anna n’a pas totalement tort, tu sais... Je ne sais pas soigner les gens."
    B "Je sais... mais je ne peux pas rester là sans rien faire. Pas pour Kim."


    if (relationJtoB > 50):
        B "Hé d’ailleurs, quand j’ai aidé Kim elle m’a donné ça... Je pense que ça pourrait nous être utile dans la cave... Prend-la, je me chargerai de la trousse de secours !"
        $ torche = True
    else :
        B "Hé, d’ailleurs... Kim m’a tendu une torche tout à l’heure... Je pense que ça pourrait nous être utile dans la cave... Je la garde. Toi, charge toi de prendre la trousse de secours."
        $ torche = False

    J "Ok, pas de soucis."
    J "Euh... Bryan... Les lumières étaient éteintes tout à l’heure ?"
    B "Je... Je ne crois pas ?"
    B "Les interrupteurs ne fonctionnent plus !"
    J "Qu’est-ce qui se passe..."


    if (torche == True):
        E "Allumant sa lampe torche, Jason passe devant, avançant doucement à pas feutré jusque dans l’entrée de la maison."

    elif (torche == False):
        E "Allumant sa lampe torche, Bryan passe devant, un peu trop sûr de lui jusque dans l’entrée de la maison."
    J "T’as une idée de qui pourrait avoir fait ça, toi ?"
    B "J’en ai aucune idée, mais c’est forcément un malade. Mon dieu... qui pourrait faire ça..."
    J "C’est une bonne chose d’avoir laissé Anna avec Kim, déjà qu’elle connait plus de choses que nous pour la soigner, tous les deux on pourra plus facilement se défendre."
    B "Ouais, il faut juste espérer qu’il y ait bien qu’une seule personne..."
    E "BRUIT DE PORTE QUI CLAQUE"
    B "Wouaw, c’était quoi ça ?"
    J "Rien, la porte vient de claquer...J’ai eu une de ces peurs !"
    B "Tu parles, j’ai carrément failli me pisser dessus !"
    B "Attends, tu sens le courant d’air ?"
    J "Ouais..."
    E "Avançant pas à pas, les deux amis suivent le vent à travers le hall d’entrée."

    #if (vu_fenetre_ouverte == True):
    B "Attends... Elle était pas fermée tout à l’heure ?"
    J "Si. Si, je crois bien. Vas-y, va la claquer, je te couvre..."
    B "Quoi ? T’as vu comment tu trembles, tu me couvres rien du tout !"
    J "Mais si... Tu sais mieux fermer les fenêtres que moi !"
    B "Je te déteste..."
    B_shout "AHHHH"
    J "Quoi, qu’est-ce qu’il y a ?"
    B "Dehors ! Dehors, j’ai vu quelque chose !"
    J "T’as vu quoi ?"
    B "Je ne sais pas, quelque chose a bougé. Oh merde..."

    # choix si on a la torche

    if (torche == True):

        menu:
            "Observer dehors":
                jump observer_dehors_torche
            "Refermer la fenêtre":
                jump fermer_fenetre_torche
            "Eteindre la lampe et se cacher":
                jump eteindre_lampe_torche


    elif (torche == False):
        J "Hé, je crois que j'ai une idée !"
        if (relationJtoB < 40):
            B "Laisse-moi faire, je vais te montrer comment on gère ce genre de chose."
            B_shout "Hé ! Je ne sais pas qui vous êtes mais je vous déconseille de vous approcher !"
            B_shout "Ouais, vous là ! On est armés ici, alors dégagez avant que je vienne vous coller une balle entre les deux yeux, c’est compris ?"
            J "Tu joues à quoi là ?"
            B "J’ai vu ça dans les films, ça marche...souvent."
            J "Ouais bah on est pas dans un film alors tais-toi avant de finir comme Kim, ok ?"
            B_murmure "Ouais... je pense que je l’ai impressionnée. C’est sûr, même."
            J "... Attends, il fait du bruit, non ?"
            E "Attentif aux bruits de l’extérieur, les deux amis tendent l’oreille... Encore... Encore..."
            jump chouette

        elif (relationJtoB >= 40):

            menu:
                "Observer dehors":
                    jump observer_dehors
                "Refermer la fenêtre":
                    jump fermer_fenetre
                "Eteindre la lampe et se cacher":
                    jump eteindre_lampe

label observer_dehors_torche:
    J "Laisse-moi voir un peu."
    B "Fais attention... On ne sait jamais..."
    E "Jason balaye le faisceau de lumière à travers la fenêtre. Rien ne semble bouger."
    J "Je ne vois rien, tu es sûr de ce que tu as vu ?"
    B "Mais quand est-ce que tu vas arrêter de douter de tout ce que je te dis !"
    jump chouette

label fermer_fenetre_torche:
    J "Pousse toi, je vais la refermer, si tu as si peur que ça..."
    B "Fais attention s’il te plait ! Je suis sûr de ce que j’ai vu !"
    E "Jason vient refermer la fenêtre lorsqu’il remarque un détail troublant. En effet, la poignée de la fenêtre est fracturée."
    J_murmure "Euh... Bryan ? Regarde ça..."
    B_murmure "Quoi ? Oh mon dieu. Tu crois que quelqu’un l’a cassé ?"
    J_murmure "On dirait bien..."
    jump chouette

label eteindre_lampe_torche:
    J "Viens vite ! Cache-toi !"
    E "Se précipitant sous le rebord de la fenêtre, les deux amis attendent en silence, cachés."
    B_murmure "On va rester ici combien de temps ?"
    J_murmure "Jusqu’à ce qu’on puisse sortir..."
    B_murmure "Alors ça risque d’être long..."
    jump chouette
    
label observer_dehors:
    B "Laisse-moi voir un peu."
    J "Fais attention... On ne sait jamais..."
    E "Bryan balaye le faisceau de lumière à travers la fenêtre. Rien ne semble bouger."
    B "Je ne vois rien, tu es sûr de ce que tu as vu ?"
    J "Mais quand est-ce que tu vas arrêter de douter de tout ce que je te dis !"
    jump chouette

label fermer_fenetre:
    B "Pousse toi, je vais la refermer, si tu as si peur que ça..."
    J "Fais attention s’il te plait ! Je suis sûr de ce que j’ai vu !"
    E "Bryan vient refermer la fenêtre lorsqu’il remarque un détail troublant. En effet, la poignée de la fenêtre est fracturée."
    B_murmure "Euh... Jason ? Regarde ça..."
    J_murmure "Quoi ? Oh mon dieu. Tu crois que quelqu’un l’a cassé ?"
    B_murmure "On dirait bien..."
    jump chouette

label eteindre_lampe:
    B "Viens vite ! Cache-toi !"
    E "Se précipitant sous le rebord de la fenêtre, les deux amis attendent en silence, cachés."
    J_murmure "On va rester ici combien de temps ?"
    B_murmure "Jusqu’à ce qu’on puisse sortir..."
    J_murmure "Alors ça risque d’être long..."

label chouette:
    E "Soudain, le cri hululement d’une chouette résonna entre les arbres du jardin."
    B_shout "AHHHHH"
    J "Saloperie de chouette !"
    B "Je hais les chouettes... La vache, j’ai failli me faire dessus..."
    J "Ouais, mais si on voulait rester discret, maintenant c’est foutu..."
    B "C’est jamais foutu, viens, il faut qu’on y aille avant qu’il soit trop tard…"
    J_murmure "Attends ! Ne. Bouge. Surtout. Pas." #(chuchote, doucement)
    E "Bruit de pas"
    B_murmure "Tu crois que c’est lui ?" 
    J_murmure "Chut  ! Tais-toi !"

    menu:
        "Se cacher":
            jump se_cacher_Bryan
        "Menacer":
            jump menacer_Bryan
        "Bloquer la porte":
            jump bloquer_Bryan

label se_cacher_Bryan:
    E "De l’autre côté de la porte d’entrée, des bruits de pas commencent à crisser sous des semelles de chaussures."
    J_murmure "Viens avec moi. Tout. Doucement."
    E "Le plus discrètement possible, les deux amis reculent, recroquevillés sur eux-mêmes."
    J_murmure "Vas dans le couloir de la cave. Maintenant !"
    B_murmure "Mais… et si elle vient vers nous, on fait quoi ?"
    J_murmure "On improvise. Maintenant vite !"
    E "A peine eurent-ils le temps de s’enfermer que la poignée de la porte s’ouvrit. Doucement, comme si elle n’avait jamais été fermée."
    B_murmure "Attends, ne ferme pas la porte…"
    B_murmure "Il faut voir qui c’est !"
    J_murmure "Regarde, on dirait une femme."
    B_murmure "Une femme ? Tu connais une femme qui serai capable de planter Kim, toi ?"
    J_murmure "Non… Maintenant tais-toi, on va se faire chopper…"
    B_murmure "Attends, je crois que je peux être capable de l’empêcher de venir par ici."
    J_murmure "Quoi ? Mais t’es malade !"
    B_murmure "Non mais regarde-la ! Je sais que je peux courir plus vite qu’elle. Je te jure que je peux la distancer, comme ça t’as le temps de monter récupérer une arme ou de quoi appeler les flics"

    #menu:
        #"Accepter"
            #jump accepter_Bryan
        #if (relationJtoB < 40):
            #"Refuser":
            #    jump



#label accepter_Bryan:
    #J_murmure “Bon, ok. Mais fais attention à toi !”
    #B_murmure “Ne t’inquiète pas pour moi, inquiète-toi plus pour Kim maintenant”
    #E “Sans un bruit, Bryan se faufile hors du couloir, se place au milieu de l’entrée et hurle à plein poumons avant de sortir en courant de la maison.”
    #E “Dans son dos, la femme s’est lancée à sa poursuite.”
