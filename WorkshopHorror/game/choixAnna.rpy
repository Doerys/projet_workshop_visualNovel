label choix_Anna4:
    
    J "Ouais, donc t’es vraiment parti dans un bad trip. Lâche tes verres sinon demain tu vas finir avec un putain de mal de crâne."
    B "Ah donc même toi tu ne me crois pas ?"
    A "Mais sans déconner, comment tu veux qu'on te crois ? T'es en train de finir ton cinquième verre et la soirée vient à peine de commencer !"
    B "Mais ta gueule toi ! Ce n'est pas de ma faute si t'es pas capable de te retirer le balai que t'as de coincé !"
    K "Hé Bryan calme-toi !"
    B "Non j’en ai marre que personne ne me croit jamais. Vous me dites que vous êtes mes potes mais quand je parle avec vous j’ai juste l’impression d’être le con de service qui se met des caisses à chaque fois qu’on fait une soirée..."
    J "En même temps, mon pote..."
    B "Oh c’est bon vous me soulez tous."
    E "Bryan se lève du canapé énervé, et disparaît dans le coin d’un couloir."
    K "Je ne sais pas ce qu’il a, mais il va falloir qu’il apprenne à se calmer 'ton pote'... Bon, aller. Je vais descendre chercher une autre bouteille, avant qu’il ne vide toutes celles qu’on a avant qu’on puisse y toucher."
    A "Tu crois que c’est une bonne idée de ramener une nouvelle bouteille après le cinéma qu’il vient de nous faire ?"
    K "On aura qu’à la lui cacher... Je n’ai pas envie de passer une soirée coincée du cul parce que 'monsieur' ne sait pas se tenir."
    E "Kim sort de la maison, laissant derrière ses amis, mais attirant Jason d’un léger clin d’oeil."

    menu:
        "Aller voir Bryan dans la cuisine":
            jump Bryan_cuisine

        "Rester dans le salon avec Anna":
            jump Anna_salon

    label Bryan_cuisine:

        J "Hé Bryan ?"
        B "Quoi tu veux encore te foutre de ma gueule c’est ça ?"
        J "Oh arrête un peu, tu sais que je rigole. T’as l’air à cran aujourd’hui, on voulait juste rigoler un peu avec les autres. Tout va bien ?"
        B "C’est à vous de demander ça ! Je vous jure que j’entends quelque chose et la seule réponse que vous avez c’est vous foutre de ma gueule ! Tout ça parce qu’Anna est trop conne pour me croire."
        J "Hé, lâche un peu l’affaire... Vous n’avez pas réussi à vous parler depuis votre embrouille de la dernière fois ?"
        A "Tu parles... J’ai essayé, mais la seule chose que je me prends c’est soit des critiques soit un vent."
        J "Alors arrête d’aller la voir ! Laisse couler !"

        menu:
            "La situation est inssuportable...":
                jump situation_inssup

            "Vous êtes tous les deux inssuportables...":
                jump deux_inssup

            "Tu es inssuportable...":
                jump Bryan_inssup


    label situation_inssup:
        J "Là, la seule chose que vous faites c’est vous engueuler en boucle. Vous tournez en rond et pour nous c’est insupportable."
        B "Pourquoi tu me dis ça à moi ? Va voir Anna, va lui dire tout ça, c’est elle qui doit se calmer !"
        J "Ne t’inquiète pas, je vais le faire. Il faut que Kim aille lui en parler parce qu’elle commence aussi à lui faire perdre ses nerfs, mais en attendant, évite d’aller la chercher, sinon on avancera jamais."

        jump suite7

    label deux_inssup:
        B "J’aimerai bien laisser couler, mais hé, comment veux-tu que je fasse quand elle est là en boucle à venir me faire chier ?"
        J "Dans ce cas arrête d’aller la faire chier aussi ! Tu te plains mais t’es pas vraiment mieux qu’elle !"
        B "Hé je t’emmerde !"

        jump suite7

    label Bryan_inssup:
        J "Regarde l’ambiance que t’as foutu ! Arrête d’aller la voir, sinon on avancera jamais !"
        B "Hé, c’est à elle de dire ça ! C’est elle qui..."
        J "Non, arrête de faire genre que c’est elle qui vient toujours te faire chier ! Ce soir c’est de ta faute si la soirée est gâchée !"

    label suite7:
        J "Bon, viens on va voir où en est Anna, mais s'il te plait, ne fais pas de conneries d'accord ?"
        E "Bryan gromelle en suivant Jason à travers la maison."

        jump reunion





    label Anna_salon:
        E "Kim s’en va dans la cave, laissant Jason et Anna seuls dans le salon"
        J "Je suis désolé pour le comportement de Bryan... Je ne sais pas ce qui lui prend, il n’est pas comme ça d’habitude."
        A "Ouais... tu sais, je ne suis pas contre lui. J’ai essayé d’aller le voir, mais il est toujours renfermé sur lui-même, il refuse de me parler."
        J "Il ne t’a jamais expliqué pourquoi ?"
        A "Non, jamais ! Après je m’en fous hein, à la base ce n’est pas mon pote, mais pour Kim j’aimerai bien qu’on arrive enfin à passer une soirée tous ensemble sans aucune embrouilles."

        menu:
            "Approuver":
                jump approuver
            "Tous les deux coupables":
                jump deux_coupables
            "Désapprouver":
                jump desapprouver


    label approuver:
        J "Tu sais, c’est le genre de mec à s’emporter toujours trop vite, il est sanguin..."
        A "Ouais bah faudrait que tu ailles lui parler parce qu’à terme on va juste tous finir par péter un plomb."
        J "J'essaierai. Il est parti dans la cuisine, il faut lui laisser du temps, il va se calmer tout seul."
        A "C’est bien, qu’il décuve un peu..."
        J "C’est ça. Tu sais, je sais comment il fonctionne maintenant. Laisse-lui cinq minutes et il reviendra calme quand il verra qu’il est en train de gâcher la soirée de Kim."

        jump suite8

    label deux_coupables:
        J "Dans ce cas, évite aussi d’aller le chercher quand tu vois qu’il est en train de se chauffer tout seul. Ça ne sert à rien, au contraire..."
        A "Je veux juste qu’il se rende compte de ses erreurs."
        J "Arrête, ce n’est pas en l’énervant que tu vas lui faire comprendre ses conneries. Tout ce que tu vas réussir à faire c’est le braquer davantage."
        A "Ça ce n’est pas mon problème ! Il n’a pas à réagir comme ça..."
        J "Anna, s’il te plaît, arrête d’envenimer la situation, par pitié... La soirée de Kim est déjà bien assez gâchée comme ça..."

        jump suite8

    label desapprouver:
        J "Dans ce cas arrête d’aller le faire chier."
        A "Hé, j’essaie juste de l’aider ! Je ne comprends pas pourquoi Kim s’entête à l’inviter si c’est tout la même chose."
        J "Mais il n’a pas besoin d’aide ! Il veut juste que tu le laisses tranquille !"
        A "Parce que tu trouves que je suis trop sur ses côtes ?"
        J "Tu rigoles j’espère ? T’es tout le temps en train de le critiquer. Enfin... merde Anna... T’es bien plus intelligente que ça !"


    label suite8:
        A "Ok, ok... je veux bien essayer de faire des efforts. Pour ce soir au moins, et pour Kim."
        J "Merci. Hé, d’ailleurs en parlant de Kim, elle va bien ?"
        A "Euh, oui ? Pourquoi est-ce que tu me demandes ça ?"
        J "Bah je ne sais pas, regarde-la. Elle a l’air moins enjouée que d’habitude. Rien qu’hier, elle est venue me prendre la tête sur des détails à la con, je n’ai pas compris pourquoi."
        A "Et tu lui as demandé ?"
        J "Ouais, mais pour elle tout est normal, sauf que je la connais assez pour savoir que c’est faux. Quelque chose ne tourne pas rond."
        A "Je suis désolé pour toi, mais je ne peux pas vraiment te donner mon avis là-dessus, elle ne m’a pas parlé de la dispute avec toi, du coup je ne sais pas ce qu’elle t’a dit..."
        J "Elle ne t’en a pas parlé ?"
        A "Non. Tu sais, elle est plus du genre à garder les choses pour elle. Ça ne me regarde pas vraiment, elle ne va pas venir m’en parler d'elle-même..."


        menu:
            "Elle cache quelque chose ?":
                jump secret

            "S'excuser":
                jump excuser2

    label secret:
        J "Tu sais, j’ai peur qu’elle me cache quelque chose, c’est la première fois que je la vois comme ça..."
        A "Après c’est Kim, ça ne me choque pas d’elle."
        J "Vraiment ?"
        A "C’est toujours la même histoire avec elle, il y a toujours un moment où tout n’est pas rose avec elle et elle finit par se renfermer sur elle-même. La seule chose que je peux te dire c’est de lui laisser du temps..."
        J "Mais toi, tu n’es pas au courant de quelque chose ? Elle va vraiment bien ?"
        A "Laisse lui du temps, vraiment... Si elle doit te dire quelque chose, elle le fera d’elle-même mais insister c’est risquer de la brusquer..."

        jump suite9

    label excuser2:
        J "Ouais, je comprends. Je suis désolé de te faire entrer dans cette histoire débile, je pensais que tu saurai au moins si je dois m’inquiéter ou non..."
        A "Tu connais Kim, tu sais comment gérer, tu sauras mieux que moi comment gérer..."
        J "J’espère..."


    label suite9:
        J "Bon aller, viens voir, peut-être que Bryan a fini par se calmer."



    label reunion:

        # Kim a son téléphone
        E "Ensemble, les trois amis finissent par se retrouver sur le canapé du salon, bière à la main, essayant tant bien que mal d’enterrer la hache de guerre."
        B "Du coup, il faut que je vous raconte ! J’ai rencontré quelqu’un !"
        J "Pardon ? Depuis quand ?"
        B "Ça fait quelques semaines, mais je crois que c’est bien parti entre nous !"
        A "Trop bien, je suis contente pour toi !"
        J "Il faut que tu me la montre que je…"
        E "Soudain le téléphone de Jason se met à sonner. Sur l’écran, le nom de Kim apparaît."
        J "Kim ? Pourquoi est-ce que tu…"
        K_shout "Jason !"
        K_shout "Jason ! Elle… !"
        E "Le téléphone se coupe, un message d’erreur de réseau apparaît."
        J "Les gars ! Putain de merde !"
        B "Quoi ? Qu’est-ce qu’il se passe ?"
        J "Kim a un problème. Putain de… putain !"
        E "Ensemble, les trois amis sortent de la maison en trombe en direction de la cave."
        
        $ seul = False

        jump scene_cave

        #Résultat final ???