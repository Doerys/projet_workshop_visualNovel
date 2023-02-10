label Kim_couloir:

E "Kim se trouve un peu plus loin, dans un couloir non loin de la cave, l'air d'attendre Jason."
K "Ah, te voilà enfin !"
J "Bien sûr que je suis là."
K "Enfin débarrassés des deux cons. Je n’arrive pas à croire qu’ils n’arrivent pas à se tenir pour au moins une soirée..."
J "Ça leur passera, ne t'inquiète pas pour eux."
K "Bon aller, viens, j’ai une petite surprise à te donner... Si tu vois ce que je veux dire ?"

menu:
    "Rentrer dans le jeu de Kim":
        jump accepter2

    "Ne pas rentrer dans son jeu":
        jump refuser2

label accepter2:
    J "Hmmm... non je ne sais pas, dis-m'en plus ?"
    K "Oh si tu vois très bien... Tu m'as manqué tu sais ?"
    J "Toi aussi tu m'as manqué mon coeur..."

    $relationJtoK += 1

    jump suite10

label refuser2:
    J "Kim, arrête... arrête !"
    K "Quoi, qu’est-ce qui t’arrives ?"

    if (harcelement_kim_info = True)

    menu:
        "Inquiet":
            jump inquiet2
        "Pourquoi les avoir invité ?":
            jump pourquoi_invite
        "Nancy":
            jump discussion_Nancy

    if (harcelement_kim_info = False)

    menu:
    "Inquiet":
        jump inquiet2
    "Pourquoi les avoir invité ?":
        jump pourquoi_invite

    label inquiet2:
        J "Arrête, ce n’est pas le moment..."
        K "Ce n’est pas le moment ?"
        J "On vient à peine de laisser Bryan et Anna alors qu’ils étaient sur le point de se taper dessus. Tu veux vraiment faire ça là, maintenant ?"
        K "Oh là là, ce que tu peux être coincé des fois..."
        jump suite10

    label pourquoi_invite:
        J "Kim, pourquoi est-ce que tu les as invité en fait ? Tu savais que ça allait mal finir, à quoi est-ce que tu pensais ?"
        K "Je te demande pardon ?"
        J "Pourquoi est-ce que tu cherches les problèmes comme ça ?"
        K "Quoi ? Je cherche les problèmes ? J’ai invité ton meilleur pote pour te faire plaisir !"

        $relationJtoK -= 1
        jump suite10

    label discussion_Nancy:
        J "J’ai parlé avec Nancy tout à l’heure..."
        K "Pardon ? Pourquoi est-ce que tu lui parles encore à celle-la ?"
        J "Parce que c’est mon amie !"
        K "T’as vraiment des amis de merde, tu sais..."
        J "Kim, stop. Elle m’a dit que tu continuais de la chercher. Tu m’avais promis !"
        K "Quoi ? Mais quelle garce ! Elle te ment Jay', c’est elle qui continue de m’harceler !"
        J "Kim... juste laisse-la tranquille. S’il te plait..."
        K "Parce que tu la crois ? Plus que moi ?"
        
        $relationJtoK -= 1
        jump suite10

    label suite10:
        E "Soudain, le téléphone de Jason se met à sonner."
        J_think "Nancy ? Pourquoi est-ce qu’elle me rappelle ?"
        K "Qui c'est...?"

    menu:
        "Être honnête":
            jump honnete2
        "Mentir":
            jump mentir2

    label honnete2:
        J "Ouais, c’est Nancy, je ne sais pas pourquoi elle m’appelle..."
        K "Je ne te comprends pas, je ne comprends pas comment t’arrive encore à lui parler à cette bouffonne."
        J "Tssss... laisse tomber Kim, je n’ai pas envie de me battre avec toi..."
        K "Ouais, c’est ça, aller, répond lui, je vais chercher la bouteille !"
        jump suite11

    label mentir2:
        J "C’est... c’est Bryan. Je pense qu’il doit s’inquiéter de ne pas nous voir revenir..."
        K "Bryan ? C’est bizarre, pourquoi est-ce qu’il vient pas nous voir, il est juste à côté ?"
        J "Je... je ne sais pas, il doit peut-être avoir la flemme... Vas-y, pars devant, je te rejoins après !"

    label suite11:
        J "Allô ?"
        N "Ja-Jason ? C’est moi... je..."
        J "Nancy ? Hé, qu’est-ce qu’il se passe ?"
        N "Je ne sais pas... Jason, j’ai du mal à respirer. Je crois que... j’ai besoin d’aide."
        J "Hé, calme-toi où est-ce que tu es ?"
        N "Jay, j’ai peur... Je... arrêter. Aahhh putain... J’ai mal..."
        J "Mal ? Nancy dis-moi où tu es je viens te chercher tout de suite ! Il n’y a personne autour de toi ?"
        N "C’est... trop tard. Je... aahh... trop tard. Respirer... Jason, respirer."

        menu:
            "Demander ce qu'il se passe":
                jump demander2

            "Dire de respirer":
                jump respire

            "Demander sa localisation":
                jump localisation

            
        label demander2:
            J "Nancy calme-toi et dis-moi ce qu’il se passe. Il faut que tu me le dises si tu veux que je t’aide d’accord ? Nancy ?"
            jump suite12

        label respire:

            J "Ok Nancy, tu dois faire une crise de panique. Il faut que tu respires. Allonge-toi, ça va aller d’accord. Je sais que ça fait mal mais il faut que tu respires..."
            jump suite12

        label localisation:

            J "Ok Nancy, il faut que tu me dises où tu es ? Je ne suis pas loin de chez toi, dis-moi où tu te trouves. Nancy ?"
            jump suite12

        label suite12:
            N "Jay'... Tout est... ma faute. Tout est de ma faute... Depuis le début."
            J "Nancy, écoute-moi. Tout va bien. Il y a quelqu’un autour de toi ?"
            N "Non... non, non... Je le mérite."
            J "Nancy, s’il te plait..."
            N  "C’est trop tard, c’est fini."

            menu:
                "Où es tu ???":
                    jump suite13
                "Tu es en pleine crise":
                    jump suite13
                "La rejoindre":
                    jump suite13

        label suite13:
            N "Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non. Non." #(de plus en plus vite) 
            J "Nancy ?"
            N "C’est trop tard Jason. Bien trop tard." #(tres lent et en gras)
            J "Nancy ? Nancy !"
            E "L'appel prend fin."

            #Bruitage tonalité

            J "Nancy ! Merde !"

            J_think "Elle avait l'air en danger. Ca m'inquiète..."

            E "Jason tente de recontacter Nancy."

            J_think "Il n’y a plus de réseau... C'est bien le moment ! Foutue maison de campagne !"

            E "Un cri résonne en direction de la cave." 

            J "Kim ?!"

            $ seul = True

            jump scene_cave
