label mauve:

    scene cave_2
    with dissolve

    E "Quand Jason ouvre les yeux, il est attaché sur une chaise dans la cave. Ligoté à coup de scotch, une arme à fond est attachée dans sa main."
    E "De l’autre côté du canon, Bryan est lui aussi ligoté, pieds et poings liés."
    J "Bryan ? Qu’est-ce que..."

    if (lifeK == 0 or lifeA == 0):
        B "Jay... Je suis désolé..."
        E "Ses yeux glissent sur le sol, à côté des pieds de Jason."
        E "Jason voit alors une vision d’horreur."
        if (lifeK == 0 and lifeA == 0):
            J "Oh mon dieu... Kim ! Hé, Kim ! Putain mais qu’est-ce qu’il se passe !"
            B "Jay ! Arrête, elles sont mortes..."
            J "Quoi !? Non... Non, non, non ! Kim ! Kim réveille-toi ! Anna ! Oh putain, Anna !"
            N "Aahhh... C’est fini Jason... Elle sont parties..."
            J "Nancy ? Mais... Pourquoi ?"
            N "Pourquoi ? ... Je... je ne voulais pas. Je veux juste être libre. Je veux juste que ça s’arrête..."
            J "Que ça s’arrête ?"
            J_shout "Tu les as tués putain !"
            N "Ce n’est pas de ma faute... Ce n’est pas de ma faute, elles n’avaient qu’à pas faire ça... Il fallait qu’elles arrêtent..."
        
        elif (lifeK == 0):
            J "Kim ! Kim, réveille-toi !"
            J "Oh mon dieu, Kim !"
            E "Une grande flaque de sang s’écoule de son corps."
            J "Kim !"
            B "Jason... Elle est morte..."

            N "Oh... Oh oui... Elle est morte."
            E "Cette voix, Jason reconnaît immédiatement son amie."
            J "Nancy ? Mais... Pourquoi ?"
            N "Je... Je le devais. Il le fallait."
            N "Il fallait que ça s’arrête..."
            J "Tu l’as tué..."
            N "Non Jason... Je n’ai tué personne. Je me suis libéré. Je suis libre."
            J "Libre de quoi ? Tu l’as tué, Nancy !"
            N "Je sais ! Je sais..."
        elif (lifeA == 0):
            J "Anna ? Hé, Anna, réveille-toi !"
            N "Elle ne répondra pas... C’est fini."
            N "Oh... Oh oui... Elle est morte... oui."
            E "Cette voix, Jason reconnaît immédiatement son amie."
            J "Nancy ? Mais... Pourquoi ?"
            N "Je... Je le devais. Il le fallait."
            N "Il fallait que ça s’arrête..."
            J "Tu l’as tué..."
            N "Non Jason... Je n’ai tué personne. Je me suis libéré. Je suis libre."
            J "Libre de quoi ? Tu l’as tué, Nancy !"
            N "Je sais ! Je sais..."
    else :
        J "Qu’est-ce que... Pourquoi est-ce qu’on est là ?"
        B "C’est à cause de Nancy..."
        E "Nancy apparaît depuis le dos de Jason."
        N "Tu as tout gâché... Tout !"
        J "Nancy ? Mais à quoi est-ce que tu joues !"

    N "Il fallait que ça s’arrête... Tout ça... Je vais mieux Jason, et c’est grâce à toi !"
    J "Nancy, non mais tu t’entends ?"
    N "Oui... Oohhh oui... Je vais mieux... Ce n’est pas de ma faute..." #lent
    J_shout "Nancy, hé ! Hé !"
    J "Non mais tu t’entends ! Putain..."
    N "Ne soit pas en colère Jason... c’est de leur faute. Maintenant tout va mieux... Tout est réglé..." #lent
    B "Alors relâche nous !"
    N "Non ! Non, non, non, non, non !" #rapide
    N_shout "Toi tu la fermes !" #rapide
    J "Nancy, calme toi ! Repose ton couteau s’il te plait !"
    N "Non ! Il n’a pas le droit... Il faut... Aahhhhh." #lent
    J "Pourquoi est-ce que tu nous fais ça ?"
    N "Pourquoi ? Vas-y Bryan... Explique lui pourquoi ?" #lent
    J "Expliquer quoi ? Putain mais de quoi tu parles !"
    B "C’est à cause de ça que tu es venu nous buter !?"
    N "Il faut payer... C’est terminé Bryan... Maintenant racontes... Je veux t’entendre dire ce que tu m’a fait..." #lent
    B "T’es complètement tarée..."
    N_shout "Raconte ou je te tue !" #lent
    B "Ok ! Ok !"
    B "Putain de merde... Je n’en reviens pas..."
    N "Dis-lui ce que tu m’a fais !" #lent
    B "Je ... Je ne peux pas..."
    N "Alors je vais le faire... Tu te souviens, quand on était ensemble ? Tout allait bien... Ohhh oui... Jusqu’au jour où j’ai vu son vrai visage..." #lent
    B "Je suis désolé Nancy !"
    N "Tu te tais ! Un soir, j’ai relâché ma garde... Peut-être un peu trop... Jusqu’au moment où tu m’as sauté dessus. Tu n'aurais pas dû..."
    J "Qu’est-ce que tu as fait ?"
    B "J’avais bu... Je n’étais pas moi-même... Nancy, on en a déjà parlé !"
    N "On en a parlé, mais tu n'as jamais payé pour ce que tu m’a fait... Il est temps..."
    J "Alors... tu veux que je le tue, c’est ça ?"
    N "Tu sais... qui il est. Fais-le pour moi."


    menu:
        "Etre d'accord pour tuer Bryan":
            jump choix_tuer_Bryan
        "Raisonner Nancy":
            jump raisonner_Nancy1


label raisonner_Nancy1:
    J "T’es malade ! Nancy, écoute-moi ! Il faut que tu arrêtes, c’est terminé !"
    N "Jamais... Tu mens ! Jamais ça ne sera terminé... Il sera toujours là... Non !"
    J "Nancy ! Tu m’as appelé ce matin pour me dire que tu allais mieux ! Il faut que tu reprennes le contrôle !"
    N "Stop ! Arrête !"
    J "Nancy ! S’il te plait, regarde-moi !"
    J "Reprends-toi !"
    #Nancy se sent trahie blablabla
    N "Je le savais... Je le savais... Tu es comme eux. Tu es comme eux..."
    J "Nancy, tu ne peux pas tuer comme ça ! Merde, ouvres les yeux !"
    N "Tu m’as déçu... tu m’a profondément déçu..."
    E "Discrètement, Jason arrive à détendre les liens en faisant rouler ses poignets."

    jump Nancy_trahie



label choix_tuer_Bryan:
    J "Putain, Bryan..."
    B "Je suis désolé... Je suis vraiment désolé..."
    N_shout "Tais-toi ! Je t’ai déjà dit de te taire !"
    E "De colère, Nancy assène lui assène un violent coup au crâne."
    N "Fais-le Jason... Libère-nous... S’il te plaît..."
    J "Je... je n’ai jamais fait ça... Je ne voulais pas le faire..."

    if (lettre_coquine == True or sms_coquins == True):
        menu:
            "Lui dire qu'on est au courant de sa liaison":
                jump Bryan_trompeur
            "Être désolé":
                jump Bryan_desole
            "Garder le silence":
                jump Bryan_silence
    else :
        menu:
            "Être désolé":
                jump Bryan_desole
            "Garder le silence":
                jump Bryan_silence


label Bryan_trompeur:
    J "Bryan... Putain."
    B "Quoi ? Hé... Hé ! Regarde-moi ! Regarde-moi, Jason !"
    J "J’ai vu les messages..."
    N "Aahhh... Tu vois enfin son vrai visage..."
    B "Quels messages ? Attends... ce n’est pas ce que tu crois !"
    J "Ce n’est pas ce que je crois ? Attends, tu te fous de moi là ? Tu couches avec Kim et tu as cru que je ne le verrai jamais ?"
    B "C’était une erreur ! Ce n’est pas ce que tu crois ! Même elle, elle s’en voulait, elle t’aimait, merde !"
    J "Tu as couché avec ma meuf... Tu as abusé de Nancy, et tu as couché avec ma meuf..."
    B "Non... Hé, non ! Regarde-moi. Je suis désolé. Tu es mon frère, jamais je ne voulais te faire ça, c’était juste une erreur ! Jason !"

    jump tuer_Bryan

label Bryan_desole:
    J "Bryan... Bryan !"
    B "Quoi ? Hé ? Jason, tu ne vas quand même pas le faire !"
    J "Putain Bryan, je suis désolé..."
    B "Quoi !? Non mais hé, regarde-moi ! Tu ne vas quand même pas me tuer ?"
    J "Je ne veux pas faire ça !"

    jump tuer_Bryan

label Bryan_silence:
    J "..."
    B "Hé, putain Jason ? Réponds-moi ! Tu joues à quoi là ?"
    J "..."
    B "Bordel, je savais que t’allais finir par me la faire à l’envers ! Espèce de connard ! Ose au moins me regarder, assume ce que tu fais !"

    

label tuer_Bryan:
    menu:
        "Tuer Bryan":
            jump tuer_Bryan2
        "Ne pas tirer":
            J "Je... je suis désolé."
            B "Hé, pitié arrête ! Tu n’as pas besoin de faire ça ! Jason pitié !"
            E "Vous placez votre doigt sur la détente."
            J "Ahhhhh."
            J "Je ne peux pas faire ça !"
            N "Quoi !? Non ! Non, non, non !"

            jump Nancy_trahie


label tuer_Bryan2:
    J "Je suis désolé..."
    E "Jason presse la détente, tirant une première balle sur Bryan. Puis une seconde. Bryan, touché au thorax, meurt en quelques secondes."
    N "Je le savais ! Je savais que tu me comprenais !"
    J "Qu’est-ce que je viens de faire..."
    N "Il faut qu’on y aille maintenant. Ensemble."

    if (police == True):
        E "Nancy s’empresse de détacher les liens de Jason. Encore sous le choc du coup de feu, ses mains tremblent, ses jambes se dérobent sous son poids."
        E "C’est à cet instant qu’ils entendent les sirènes retentir dans le jardin de la maison. La police arrive, ils n’ont pas le temps de sortir d’ici. Paniquée, Nancy regarde Jason, les yeux écarquillés."
        E "À ses pieds, le cadavre de vos amis jonchent le sol, où les pieds trempent dans une mare de sang visqueuse et putride."
        E "Au loin, la police enfonce la porte. Bientôt, elle arrivera dans la cave. Bientôt, il sera trop tard."
        E "..."
        E "FIN" #fin prison
        return

    else :
        N "Je le savais ! Je le savais, je le savais !"
        J "Qu’est-ce que..."
        N "Aller, il faut qu’on y aille... Je... je suis si fière de toi..."
        J "Pourquoi est-ce que j’ai fait ça..."
        N "Jason, il faut qu’on y aille ! Viens avec moi... Ils... méritaient... Tu n’as rien fait de mal... Tu m’as sauvé !"
        E "..."
        E "FIN" #fin psychopathe
        return



label Nancy_trahie:
    N "Je le savais... Je le savais... Tu es comme eux. Tu es comme eux..."
    J "Nancy, tu ne peux pas tuer comme ça ! Merde, ouvres les yeux !"
    N "Tu m’as déçu... tu m’a profondément déçu..."
    E "Discrètement, Jason arrive à détendre les liens en faisant rouler ses poignets."

$ persuasion_Nancy = 0

if (lettre_Nancy == True):
    menu:
        "Gagner du temps":
            J "Hé, non ! Je ne voulais pas te décevoir !"
            N "Tu refuses de m’aider... Tu ne vaux pas mieux qu’eux..."
            J "Nancy, hé ! Je te jure que je suis totalement avec toi, d’accord ? C’est juste que... qu’on ne peut pas faire ça ici ! Imagine que quelqu'un nous entende, imagine que la police arrive !"
            N "Non, impossible... C’est... impossible. Tu mens."
            N_shout "Tu mens !"
            J "Nancy, non ! Calme-toi, s’il te plait !"
            jump suite_Nancy

        "Raisonner Nancy":
            J "Hé, non ! Nancy, écoute-moi, s’il te plaît !"
            N "Non !"
            N "Tu n’es qu’un menteur. Menteur ! Menteur !"
            J " S’il te plaît, Nancy ! Ce n’est pas toi, ça !"
            N "Tu ne sais rien de moi ! Arrête de vouloir entrer dans ma tête !"
            J "Je te connais, Nancy. Je sais qui tu es. S’il te plaît, il faut que tu te calmes !"
            jump suite_Nancy

        "Lui parler de sa lettre":
            $ persuasion_Nancy += 1
            J "Nancy ! Hé, je sais ce que tu as traversé !"
            N "Non ! Tu ne sais rien... Tu t’en ai toujours foutu..."
            J "C’est faux ! Nancy, tu es mon amie ! S’il te plaît, ne fais pas plus d’erreurs que ça. Ne fais pas cette erreur..."
            N "Une erreur ? Tu ne sais rien... Tu n’es... même pas au courant de tout ce qu’il m’a fait subir !"
            J "Si ! J’ai lu ta lettre ! Je n’avais pas compris de qui elle venait, mais maintenant tout est plus clair ! Le poids qui écrase ta poitrine, ta peau qui te brûle, c’est bien toi qui a écrit ça, non ?"
            N "Comment est-ce que tu..."
            J "Nancy... Je tiens à toi. Je veux savoir ce que tu traverses, mais s’il te plait, ne va pas trop loin. Il faut que tu te calmes."
            jump suite_Nancy

else :
    menu:
        "Gagner du temps":
            J "Hé, non ! Je ne voulais pas te décevoir !"
            N "Tu refuses de m’aider... Tu ne vaux pas mieux qu’eux..."
            J "Nancy, hé ! Je te jure que je suis totalement avec toi, d’accord ? C’est juste que... qu’on ne peut pas faire ça ici ! Imagine que quelqu'un nous entende, imagine que la police arrive !"
            N "Non, impossible... C’est... impossible. Tu mens."
            N_shout "Tu mens !"
            J "Nancy, non ! Calme-toi, s’il te plait !"
            jump suite_Nancy

        "Raisonner Nancy":
            J "Hé, non ! Nancy, écoute-moi, s’il te plaît !"
            N "Non !"
            N "Tu n’es qu’un menteur. Menteur ! Menteur !"
            J " S’il te plaît, Nancy ! Ce n’est pas toi, ça !"
            N "Tu ne sais rien de moi ! Arrête de vouloir entrer dans ma tête !"
            J "Je te connais, Nancy. Je sais qui tu es. S’il te plaît, il faut que tu te calmes !"
            jump suite_Nancy

label suite_Nancy:
    N "Il ne peut pas comprendre... Il ne peut pas... C’est ton meilleur ami, après tout... Il est trop tard !"
    J "Trop tard pour quoi ? Nancy s’il te plaît, il faut que tu me parles !"
    N "Tu ne me crois pas ! Tu ne sais rien !"
    E "Alors que Nancy fait les cents pas, Jason en profite pour agrandir le mouvement de ses poignets, arrachant encore un peu plus sa main qui était prisonnière de l’arme à feu."


    if (lettre_coquine == True):
        menu:
            "Lui dire que Bryan doit finir en prison":
                J "Ecoute Nancy ! Je sais que Bryan est un connard. Je le sais !"
                B "Quoi ?"
                J "Toi, ferme-la. J’ai vu ce qu’il a envoyé à Kim. Je sais ce qu’il se passe entre eux."
                N "Aahhh... tu ne peux pas t’en... empêcher, hein Bryan ?"
                B "S’il vous plaît vous deux, ce n’est pas ce que vous croyez !"
                J "Ah ouais ? Je ne dois pas croire que tu te tapes Kim dans mon dos ?"
                B "C’était une erreur !"
                J "Espèce de connard... Tu vois Nancy, crois-moi je ne veux pas essayer de le sauver lui."
                J "Rien ne me ferait plus plaisir que de le buter, mais ça ne marche pas comme ça Nancy !"
                J "On ne peut pas faire comme ça ! Il faut que tu laisses la justice se faire !"
                B "Quoi, la justice ? Hé, Jason tu me fais quoi là ?"
                J "Ce connard a abusé de toi ? Alors il faut qu’il finisse en taule. Sinon, c’est toi qui risque ta peau."
                N "La justice..."
                J "S’il te plaît, fais-moi confiance."
                $persuation +=1
                jump suite_Nancy2
            "Raisonner Nancy":
                J "Nancy ! Bien sûr que je te crois ! Regarde-nous, je ne serais jamais resté près de toi si je ne te faisais pas confiance."
                N "Tu es resté près de moi ... ?"
                J "Bien sûr ! Tu es mon amie, Nancy. Alors si tu me dis que Bryan a fait tout ça, je te crois !"
                N "Tu me crois..."
                J "Oui ! C’est pour ça que je ne veux pas que tu fasses plus de victimes, parce que je sais que tu es la victime. Ce sont eux qui doivent payer, pas toi !"
                jump suite_Nancy2

            "Lui dire qu'on se soucis de tout le monde":
                J "Je te crois ! Bien sûr que je te crois !"
                N "Non ! Tu préfères lui faire confiance plutôt qu’à moi !"
                J "Ce n’est pas ça Nancy, regarde-moi ! Je n’étais pas au courant de ce qu’il s’est passé ce soir là. Je ne le savais pas."
                J "Alors imagine-toi à ma place. Je suis face à mes deux amis, c’est dur pour moi d’entendre tout ça !"
                N "Aahhh parce qu’il est encore ton ami après tout ce qu’il m’a fait ?"
                J "Non ! Non ce n’est pas ce que je voulais dire !"
                jump suite_Nancy2

    else :
        menu:
            "Raisonner Nancy":
                J "Nancy ! Bien sûr que je te crois ! Regarde-nous, je ne serais jamais resté près de toi si je ne te faisais pas confiance."
                N "Tu es resté près de moi ... ?"
                J "Bien sûr ! Tu es mon amie, Nancy. Alors si tu me dis que Bryan a fait tout ça, je te crois !"
                N "Tu me crois..."
                J "Oui ! C’est pour ça que je ne veux pas que tu fasses plus de victimes, parce que je sais que tu es la victime. Ce sont eux qui doivent payer, pas toi !"
                jump suite_Nancy2

            "Lui dire qu'on se soucis de tout le monde":
                J "Je te crois ! Bien sûr que je te crois !"
                N "Non ! Tu préfères lui faire confiance plutôt qu’à moi !"
                J "Ce n’est pas ça Nancy, regarde-moi ! Je n’étais pas au courant de ce qu’il s’est passé ce soir là. Je ne le savais pas."
                J "Alors imagine-toi à ma place. Je suis face à mes deux amis, c’est dur pour moi d’entendre tout ça !"
                N "Aahhh parce qu’il est encore ton ami après tout ce qu’il m’a fait ?"
                J "Non ! Non ce n’est pas ce que je voulais dire !"
                jump suite_Nancy2

label suite_Nancy2:
    N "Non, tu mens encore ! Tu n’es qu’un menteur ! je... Tu n’essaie que de sauver sa peau..."
    J "Non, Nancy."
    J "Putain, écoute moi !"
    N "Tu crois que je suis folle..."

    if (traitement_conseil == True):
        menu:
            "Lui parler de son traitement":
                J "Si je pensais que tu étais folle, jamais je ne ferai attention à toi !"
                J "Arrête de croire que je suis contre toi, j’essaie de faire mon maximum pour que tu ailles mieux !"
                N "Conneries ! Je... arrête !"
                J "Tu te souviens de l’appel que tu m'as passé ce matin ? Celui où tu m’a dit que tu allais bien ?"
                J "Tu te souviens de ce que je t’ai dis ?"
                J "Il fallait que tu continues ton traitement. Je veux que tu ailles mieux. Je veux te montrer que je tiens à toi. S’il te plaît. Je t’aime et tu es mon amie, tu crois que ça me fait plaisir de te voir comme ça ?"
                N "Quoi ? Je..."
                J "S’il te plaît..."
                $ persuation += 1
                jump suite_Nancy3
            "Lui dire qu'on ne l'a pas abandonné":
                J "Bien sûr que non ! Nancy, hé !"
                J "Tu ne te souviens pas que je suis resté là, avec toi depuis tout ce temps ?"
                N "Tu me mentais..."
                J "Non ! Je ne te mentais pas ! Tu es mon amie ! Alors si je dois rester ici à te parler pendant des heures pour t’éviter de faire une connerie, je le ferai. Il faut que tu me crois, Nancy."
                N "Tu me manipules..."
                J "Non ! Je ne te manipule pas ! Putain... Nancy, je t’aime et tu es mon amie, et tu l’as toujours été !"
                N "Quoi ? Je..."
                J "S’il te plaît..."
                jump suite_Nancy3
            "Lui assurer qu'elle compte beaucoup":
                J "Je ne sais pas ce qu’il se passe. Tu sais que je n’arrive pas à comprendre ce qu’il se passe dans ta tête, mais j’aime ça."
                J "Alors non, tu n’es pas folle. Tu es drôle, intelligente, mais tu n’es pas folle."
                J "Personne n’a le droit de te dire ça, personne n’a le droit de penser ça."
                N "Je ne suis pas folle..."
                J "Non tu n’es pas folle. Tu es mon amie, et tu comptes beaucoup pour moi. Alors s’il te plaît, calme-toi et laisse tomber. Je ne veux pas te voir sombrer, Nancy... S’il te plaît."

                jump suite_Nancy3

    else :
        menu:
            "Lui dire qu'on ne l'a pas abandonné":
                J "Bien sûr que non ! Nancy, hé !"
                J "Tu ne te souviens pas que je suis resté là, avec toi depuis tout ce temps ?"
                N "Tu me mentais..."
                J "Non ! Je ne te mentais pas ! Tu es mon amie ! Alors si je dois rester ici à te parler pendant des heures pour t’éviter de faire une connerie, je le ferai. Il faut que tu me crois, Nancy."
                N "Tu me manipules..."
                J "Non ! Je ne te manipule pas ! Putain... Nancy, je t’aime et tu es mon amie, et tu l’as toujours été !"
                N "Quoi ? Je..."
                J "S’il te plaît..."
                jump suite_Nancy3

            "Lui assurer qu'elle compte beaucoup":
                J "Je ne sais pas ce qu’il se passe. Tu sais que je n’arrive pas à comprendre ce qu’il se passe dans ta tête, mais j’aime ça."
                J "Alors non, tu n’es pas folle. Tu es drôle, intelligente, mais tu n’es pas folle."
                J "Personne n’a le droit de te dire ça, personne n’a le droit de penser ça."
                N "Je ne suis pas folle..."
                J "Non tu n’es pas folle. Tu es mon amie, et tu comptes beaucoup pour moi. Alors s’il te plaît, calme-toi et laisse tomber. Je ne veux pas te voir sombrer, Nancy... S’il te plaît."

                jump suite_Nancy3


label suite_Nancy3:
    if (persuation >= 2):
        N "Je suis... ton... amie..."
        J "Oui. Mais il faut que tu arrêtes maintenant. Tu as fait trop de dégâts autour de toi."
        J "S’il te plaît... Laisse tomber. Tu te souviens de ce que je t’ai dis au téléphone cet après-midi ?"
        N "Que je... devais te faire confiance..."
        J "Alors s’il te plait... Je suis ton ami, je ne te veux que du bien... Lâche ta lame, s’il te plaît."
        N "Non. Non, je ne peux pas... je ne peux pas !"
        N_shout "Arrête !"
        J "Nancy, hé Nancy !"
        N "Je suis désolée... Je suis si désolée... Je ne sais pas ce qui m’a pris..."
        E "Regardant ses mains et sa lame pleine de sang, Nancy fond en larme."
        N "Je ne voulais... Ils devaient payer, tous autant qu’ils sont..."
        J "Et ils payeront ! Maintenant il faut que tu lâches ton couteau."
        N "Non... Ce ne sera jamais fini... C’est trop tard maintenant..."
        E "Le visage baigné de larmes, Nancy jette son couteau avant de remonter les escaliers de la cave et de disparaître dans la pénombre, laissant les deux amis seuls, dans l’obscurité."
        E "..."
        E "FIN" #fin persuasion / bonus
        return


    else :
        N "Non... Non. Non. Non. Non. Non. Non. Ce n’est pas possible."
        J "Nancy, hé ! Qu’est-ce que tu fais !"
        N "Non, non tu mens... Tu mens... Je ne suis pas folle. Tu essaies de me manipuler."
        J "C’est faux, Nancy ! Je suis là pour toi !"
        N "Alors dans ce cas, tue-le pour moi... Vas-y... Tire !"
        N_shout "Tire..." #lent
        E "Alors que Nancy fait face à Jason, le couteau pointé vers son visage, le scotch qui le maintenait finit par lâcher."
        E "La main sur la crosse de l’arme, Jason retrouve l’entièreté de ses mouvements."


        menu:
            "Tirer sur Bryan":
                jump tuer_Bryan2
            "Tirer sur Nancy":
                E "Tenant le pistolet à la main, Jason hésite une seconde avant de tourner l’arme de direction de la jeune femme. Lorsqu’elle voit l’arme se tourner vers elle, la surprise lui fait lâcher son arme, qui tombe lourdement au sol."
                N "Jason... Qu’est-ce que tu..."
                E "Le premier coup de feu retentit. Puis un second. Puis un dernier."
                E "Lourdement, la jeune femme tombe à genou, le visage s’éteignant petit à petit, avant de tomber dans une boue noirâtre et putride de sang et de poussière. "
                B "Jason ! Putain, sors moi de là, par pitié !"
                E "Arrachant les liens de Bryan, Jason en profite pour jeter un œil au corps de son ancienne amie. Elle est là, allongée sur le sol, son couteau posé à ses pieds."
                J "Je suis désolé..."
                E "..."
                E "FIN" #SURVIE
                return
            "Refuser de tirer":
                N "Quoi ? Qu’est-ce que... Qu’est-ce que tu fais ? Non, non !"
                J "C’est fini Nancy..."
                N "Non ! Ce n’est pas ce que tu devais faire !"
                J "Je dois faire ce qui est juste..."
                jump fin_Nancy

label fin_Nancy:
    if (police == True):
        E "Au loin, des sirènes de police commencent à résonner."
        N "Pourquoi est-ce que tu fais ça..."
        J "Parce qu’il est temps de mettre fin à cette folie, Nancy..."
        J "Il faut que tu abandonnes, c’est terminé..."
        N "Je pensais qu’on était amis..."
        N "Tu étais mon ami..."
        E "..."
        E "FIN" # prison
        return

    else :
        E "Alors que Jason jette son arme au sol, la tension semble monter d’un cran."
        N "Je pensais que tu étais mon ami..."
        J "Je le suis... mais tu as besoin d’aide, Nancy..."
        N "Tu m’as menti... Tu m’as menti !"
        N_shout "Tu m’as menti !"
        E "Dans un élan de folie, Nancy se jette sur Jason. Sans pouvoir réagir, la lame se plante alors au creux de son abdomen, lui coupant le souffle instantanément."
        N "Tu n’aurais jamais dû me mentir... C’est fini maintenant. Personne ne me mentira. Plus jamais."
        E "Elle lui assène alors un deuxième coup de couteau, avant de se retourner en direction de Bryan."
        B "Non ! Pitié Nancy, non !"
        E "D’un geste vif, sa lame glissa sur le coup du jeune homme, projetant un flot de sang vif sur plusieurs mètres autour de lui."
        N "Plus personne ne me fera de mal... C’est... fini..."
        E "Debout, seule au centre des cadavres jonchant le sol, Nancy retourne alors la lame contre sa propre gorge, avant de l’y enfoncer d’un seul coup."
        E "..."
        E "FIN" # suicide
        return








