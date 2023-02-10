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
    A "Oh non, les interrupteurs ne fonctionnent plus !"
    J "Qu’est-ce qui se passe..."


    if (torche == True):
        E "Allumant sa lampe torche, Jason passe devant, avançant doucement à pas feutré jusque dans l’entrée de la maison."

    elif (torche == False):
        E "Allumant sa lampe torche, Anna passe devant, balayant le sol de son faisceau tant il est impossible d’y voir à plus de 2 mètres."
    
    J "T’as une idée de qui pourrait avoir fait ça, toi ?"
    A "J’en ai aucune idée, mais c’est forcément un malade. Mon dieu... qui pourrait faire ça..."
    J "C’est une bonne chose d’avoir laissé Bryan avec Kim, Au cas où ils se retrouvent en danger, il pourra plus facilement la défendre..."
    A "Ouais, il faut juste espérer qu’il y ait bien qu’une seule personne..."
    E "BRUIT DE PORTE QUI CLAQUE"
    A "Wouaw, c’était quoi ça ?"
    J "Rien, la porte vient de claquer...J’ai eu une de ces peurs !"
    A "Tu parles, j’ai carrément failli me pisser dessus !"
    J "Attends, tu sens le courant d’air ?"
    A "Ouais..."
    E "Avançant pas à pas, les deux amis suivent le vent à travers le hall d’entrée."

    if(vu_fenetre_ouverte = True):

    A "Elle n’était pas close tout à l’heure celle-là ?"
    J "Si. Si, je crois bien. Vas-y, va la fermer, je te couvre..."
    A "Quoi ? T’as vu comment tu trembles, tu me couvres rien du tout !"
    J "Mais si... Tu sais mieux fermer les fenêtres que moi !"
    A "Je te déteste..."
    A_shout "AHHHH"
    J "Quoi, qu’est-ce qu’il y a ?"
    A "Dehors ! Dehors, j’ai vu quelque chose !"
    J "T’as vu quoi ?"
    A "Je ne sais pas, quelque chose a bougé. Oh merde..."

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
        if (relationJtoA < 40):

            A "Laisse-moi faire, je vais te montrer comment on gère ce genre de chose."
            A_shout "Hé ! Je ne sais pas qui vous êtes mais je vous déconseille de vous approcher !"
            A_shout "Ouais, vous là ! On est armés ici, alors dégagez avant que je vienne vous coller une balle entre les deux yeux, c’est compris ?"
            J "Tu joues à quoi là ?"
            A "J’ai vu ça dans les films, ça marche...souvent."
            J "Ouais bah on est pas dans un film alors tais-toi avant de finir comme Kim, ok ?"
            A_shout "Ouais... je pense que je l’ai impressionnée. C’est sûr, même."
            J "... Attends, il fait du bruit, non ?"
            E "Attentif aux bruits de l’extérieur, les deux amis tendent l’oreille... Encore... Encore..."


            jump chouette2

        elif (relationJtoA >= 40):

            menu:
                "Observer dehors":
                    jump observer_dehors_Anna
                "Refermer la fenêtre":
                    jump fermer_fenetre_Anna
                "Eteindre la lampe et se cacher":
                    jump eteindre_lampe_Anna

label observer_dehors_torche_Anna:
    J "Laisse-moi voir un peu."
    A "Fais attention... On ne sait jamais..."
    E "Jason balaye le faisceau de lumière à travers la fenêtre. Rien ne semble bouger."
    J "Je ne vois rien, tu es sûr de ce que tu as vu ?"
    A "Mais quand est-ce que tu vas arrêter de douter de tout ce que je te dis !"


    jump chouette2


label fermer_fenetre_torche_Anna:
    J "Pousse toi, je vais la fermer, si tu as si peur que ça..."
    A "Fais attention s’il te plait ! Je suis sûr de ce que j’ai vu !"
    E "Jason vient refermer la fenêtre lorsqu’il remarque un détail troublant. En effet, la poignée de la fenêtre est fracturée."
    J_murmure "Euh... Bryan ? Regarde ça..."
    A_murmure "Quoi ? Oh mon dieu. Tu crois que quelqu’un l’a cassé ?"
    J_murmure "On dirait bien..."

    jump chouette2


label eteindre_lampe_torche_Anna:
    J "Viens vite ! Cache-toi !"
    E "Se précipitant sous le rebord de la fenêtre, les deux amis attendent en silence, cachés."
    A_murmure "On va rester ici combien de temps ?"
    J_murmure "Jusqu’à ce qu’on puisse sortir..."
    A_murmure "Alors ça risque d’être long..."

    jump chouette2

label observer_dehors_Anna:
    A "Laisse-moi voir un peu."
    J "Fais attention... On ne sait jamais..."
    E "Bryan balaye le faisceau de lumière à travers la fenêtre. Rien ne semble bouger."
    A "Je ne vois rien, tu es sûr de ce que tu as vu ?"
    J "Mais quand est-ce que tu vas arrêter de douter de tout ce que je te dis !"

    jump chouette2

label fermer_fenetre_Anna:
    A "Pousse toi, je vais la refermer, si tu as si peur que ça..."
    J "Fais attention s’il te plait ! Je suis sûr de ce que j’ai vu !"
    E "Bryan vient refermer la fenêtre lorsqu’il remarque un détail troublant. En effet, la poignée de la fenêtre est fracturée."
    A_murmure "Euh... Jason ? Regarde ça..."
    J_murmure "Quoi ? Oh mon dieu. Tu crois que quelqu’un l’a cassé ?"
    A_murmure "On dirait bien..."

    jump chouette2


label eteindre_lampe_Anna:

    A "Viens vite ! Cache-toi !"
    E "Se précipitant sous le rebord de la fenêtre, les deux amis attendent en silence, cachés."
    J_murmure "On va rester ici combien de temps ?"
    A_murmure "Jusqu’à ce qu’on puisse sortir..."
    J_murmure "Alors ça risque d’être long..."


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




