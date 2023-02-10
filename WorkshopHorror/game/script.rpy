﻿# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define J = Character('Jason', color="#ffffff", what_font = 'Calvino-Regular-trial.ttf', who_font = 'UnfinishedScreamRegular.ttf')
define J_think = Character(kind = J, what_italic = True, what_xalign = 0.5, what_layout ='subtitle')
define J_shout = Character(kind = J, what_bold = True, what_size = 100) # Kind permet de copier un style de perso, perso qui crie
define J_murmure = Character(kind = J, what_bold = True, what_size = 60, what_font = 'Calvino-Regular-trial.ttf')
define K = Character('Kim', color= "#ff00bf", what_font = 'Calvino-Regular-trial.ttf', who_font = 'UnfinishedScreamRegular.ttf')
define K_murmure = Character (kind = K, what_size = 60,what_font = 'Calvino-Regular-trial.ttf')
define K_shout = Character (kind = K, what_size = 100,what_font = 'Calvino-Regular-trial.ttf')
define B = Character('Bryan', color= "#ff0000",what_font = 'Calvino-Regular-trial.ttf', who_font = 'UnfinishedScreamRegular.ttf')
define B_murmure = Character(kind = B, what_size = 60,what_font = 'Calvino-Regular-trial.ttf')
define B_shout = Character(kind = B, what_size = 100,what_font = 'Calvino-Regular-trial.ttf')
define A = Character('Anna', color= "#ff9100",what_font = 'Calvino-Regular-trial.ttf', who_font = 'UnfinishedScreamRegular.ttf')
define A_shout = Character(kind = A, what_size = 100,what_font = 'Calvino-Regular-trial.ttf')
define A_murmure = Character(kind = A, what_size = 60,what_font = 'Calvino-Regular-trial.ttf')
define N = Character('Nancy', color= "#f9fd15",what_font = 'Calvino-Regular-trial.ttf', who_font = 'UnfinishedScreamRegular.ttf')
define I = Character('Voix inconnue', color= "#48ff00",what_font = 'Calvino-Regular-trial.ttf', who_font = 'UnfinishedScreamRegular.ttf')

define E = Character('', color= "#ffdabc", what_italic = True) # bruitage et environnement


# Le jeu commence ici
label start:


    # Mettre toutes les variables ici
    $ relationJtoK = 0 #Jason to Kim
    $ relationJtoB = 0 #Jason to Bryan
    $ relationJtoA = 0 #Jason to Anna
    $ relationJtoN = 0 #Jason to Nancy
    $ relationKtoB = 0 #Kim to Bryan
    $ relationKtoA = 0 #Kim to Anna
    $ relationKtoN = 0 #Kim to Nancy
    $ relationBtoA = 0 #Bryan to Anna
    $ relationBtoN = 0 #Bryan to Nancy
    $ relationAtoN = 0 #Anna to Nancy

    $ lifeJ = 100 #vie Jason
    $ lifeK = 100 #vie Kim
    $ lifeB = 100 #vie Bryan
    $ lifeA = 100 #vie Anna
    $ lifeN = 100 #vie Nancy

    $ harcelement_kim_info = False

    $ obstacles = 0
    $ seul = False
    $ torche = False
    $ vu_fenetre_ouverte = False
    $ go_with_Anna = False
    $ go_with_Bryan = False
    $ telephone_oublie = False
    $compagnie_bryan = False
    $compagnie_anna = False
    $menacer_psychopathe = False


    $ traitement_conseil = False

    play music "audio/Music/Prologue1.mp3" loop

    J_think "Aujourd'hui, c'est le grand jour. Il ne me reste plus beaucoup de temps avant de devoir partir, et il ne faut pas que je gâche la soirée, sinon Kim ne me le pardonnera jamais."
    J_think " Depuis le temps qu'elle s'embête à tout bien organiser, la moindre petite faute de goût pourrait me coûter très cher."
    J_think "On se connait déjà depuis plusieurs années, et je n'ai pas envie de savoir comment elle réagira... Surtout depuis la dispute d’hier."

    scene chambre_jason

    # Chargement des items dans la scène
    show bouffe:
        xpos 1820
        ypos 1215
    show telecommande:
        xpos 350
        ypos 1840
    show boisson:
        xpos 2900
        ypos 10
    show vetement:
        xpos 3030
        ypos 1825
    show placard:
        xpos 1983
        ypos 1303
    show velux:
        xpos 0
        ypos -39
    show tabouret:
        xpos 1250
        ypos 1567

    J "Ca sera l'occasion de revoir Bryan. Ça fait plusieurs semaines que je ne l’ai pas revu. Je crois que Kim a décidé d’inviter Anna aussi. J’espère que tout va bien se passer malgré leurs différends."
    J "Bon, je dois finir de me préparer avant d’arriver en retard. Je ne suis pas très convaincu de ma tenue mais tant pis, plus de temps à perdre."
    
    
    play sound "audio/Sounds/Phone Ringing.mp3" 
    
    # son de vibration, clic sur le portable mis en évidence en arrière plan

    # ouverture interface portable OU fondu au noir avec scène scindé, chaque perso sur son téléphone

    show nancy_normal:
        xalign 1.5 yalign -0.5
        linear 0.8 xalign 0.9

    E "Le téléphone de Jason sonne."
    N "Hey Jason ! Comment tu vas ?"
    J "Salut Nancy, ça va et toi ?"
    N "Ouais ça va, je voulais juste t'appeler parce que je sors de chez le psy, j'avais rendez-vous cet après-midi..."
    J "Déjà ? Ton dernier rendez-vous était il y a à peine deux semaines, pourquoi voulait-il te revoir si vite ?"
    N "Honnêtement je n'ai pas compris pourquoi mais mes parents ont insisté pour que je le voie alors que..."
    N "..."
    N "Ca fait... je ne sais combien de mois maintenant ! Il faut qu'ils passent à autre chose."
    J "Toi, comment tu te sens ?"
    N "Ca va ! J'en ai juste marre de ces medocs qui me shootent complètement..."
    N "Mon psy serait pas d'accord, mais je pense peut-être arrêter mon traitement."

    menu:
        "Lui conseiller de continuer son traitement ou la rassurer sur son choix ?"
        "Continuer le traitement":
            jump continuer
        "La rassurer":
            jump rassurer

    label continuer:
        J "Hé, s'ils sentent que tu as besoin de continuer ton traitement, il faut que tu leur fasse confiance Nancy..."
        J "Ça ne va pas durer, tu vas y arriver. Dans le pire des cas, va à tes rendez-vous, et raconte n'importe quoi, ils seront contents."
        N "Tu crois ?"
        J "Fais moi confiance Nan'..."
        N "..."

        $ traitement_conseil = True;

        jump suite
        
    label rassurer:
        J "Après tu sais, j'ai vraiment l'impression que tu vas mieux."
        N "Tu trouves aussi ? J'avais peur de me tromper mais je me sens bien en ce moment."
        J "Bah, tu es plus souriante, tu as l'air de revivre."
        N "Merci ! Je suis contente que tu le remarques ! Tu es le premier à me le dire, ça fait du bien !"
        J "Tu vas continuer de suivre le traitement ?"
        N "Pourquoi, tu crois que je devrais arrêter ?"
        J "Je ne sais pas, mais je te vois guérir, tu pourrais peut-être en parler à tes parents."

    label suite:
        N "... Hé dis-moi, ça te dit de sortir ce soir ? J'ai envie de prolonger l'euphorie pour la soirée avant que ça retombe..."
        J "Oh, euh, je ne vais pas pouvoir ce soir. Je dois aller chez Kim, on va enfin se voir avec les autres, depuis le temps."
        N "Les autres ?"
        J "Ouais, Bryan et Anna. Même si je ne comprends pas pourquoi on insiste à les faire venir ensemble, vu l'ambiance que ça donne."
        N "Ouais, non... si c'est pour être avec eux, je préfère dire non... Je suis pas la bienvenue, tu le sais bien."

        menu :
            "En demander plus":
                jump en_parler

            "Être désolé":
                jump desole

            "Dédramatiser":
                jump passer

    label en_parler:
        J "Attends, Kim et Anna continuent de te faire chier ? J'avais fait jurer à Kim de te laisser tranquille. Merde."
        N "Ouais, bah, comme quoi, on ne peut pas lui faire confiance..."
        J "Bon, je vais essayer de lui en parler ce soir, je ne comprends pas ce qu'il se passe entre vous, mais il faut que vous arriviez à vous parler un jour toutes les trois."
        N "Je ne suis pas sûre que ça change grand chose, c'est trop tard maintenant."
        J "Je vais gérer ça avec eux. Fais-moi confiance, et ne pense plus à ça. Profite de ta soirée, tu le mérites."

        $ relationJtoN += 1
        $ harcelement_kim_info = True

        jump suite2

    label desole:
        J "Je suis désolé que tu aies à vivre ça, Kim m'avait promis d'arrêter pourtant..."
        N "Mouais, bah si elle était du genre à respecter ses promesses, on le saurait..."
        J "Arrête Nancy..."

        jump suite2

    label passer:
        J "Arrête, tu sais que Kim disait ça pour rigoler..."
        N "Pardon ? Tu ne l'a jamais vue quand elle est avec Anna, ce n'est pas 'juste pour rigoler' Jason."
        J "Non mais ce n'est pas ce que je voulais dire... Juste, ne prends pas à cœur tout ce qu'elle te dit, elle veut juste s'amuser avec toi, c'est toi qui empires la situation..."
        N "Tu sais quoi, va te faire foutre Jay ! Il faut que tu ouvres les yeux sur elle, ou elle va finir par t'avoir toi aussi."
        J "Ouais, ouais... Je sais..."

        $ relationJtoN -= 1

    label suite2:
        J "Je vais devoir te laisser Nancy, sinon je vais être en retard. Ça m'a fait plaisir de t'entendre ce soir."
        N "Ouais... Moi aussi..."
        J "Bisous !"

        play sound "audio/Sounds/Phone off.mp3"

        hide nancy_normal with dissolve

        J_think "Bon, il ne me reste plus beaucoup de temps. Kim m’a donné sa liste, si j’oublie le moindre objet, c’est un coup à ce que la soirée parte en vrille. J’espère juste que Bryan et Anna arriveront à se tenir."

        jump openAppart
        


    label chezKim:
        scene fond_noir
        with dissolve

        E "Depuis l'extérieur, les fenêtres de la maison de Kim semblent éclairées. Quelques ombres témoignent de la présence de certaines personnes. La soirée a déjà commencé."
        J_think "Merde, je suis le dernier. J'espère que je n'ai pas raté grand chose."

        play sound "audio/Sounds/Carillon.mp3"
        E "Ding dong"
        play music "audio/Music/Soiree1.mp3" loop fadeout 1

        scene entree
        show kim_content:
            yalign -0.5

        K "Ah bah enfin te voilà ! T'es le dernier à arriver, on a cru que tu allais oublier la soirée !"
        J "Désolé, j'ai pris trop de temps sur le chemin, le bus a fait un détour."
        K "Ne t'en fais pas va ! Alors, tu as pensé à ce que tu devais ramener ?"

        if (objetTrouve == 0 ):
            jump mainsvides
        elif (objetTrouve >=1 and objetTrouve <= 3) :
            jump moitie
        elif (objetTrouve == 4) :
            jump tout

        label mainsvides : 
            J "Merde, je suis désolé j'ai complètement oublié ce que tu voulais que je prenne..."
            K "Tu te moques de moi là j'espère ? Non mais, tu espères vraiment me faire croire que tu as complètement oublié et tu ne m'as même pas envoyé un message pour me prévenir ?"
            K "Jay... Je... Tu m'énerves ! Viens, sinon je vais finir par t'étriper avant même que tu rentres..."

            $ relationJtoK -= 1

            jump suite3
        
        label moitie :
            J "Euh non, je crois qu'il fallait que je prenne un truc en plus, mais je ne me souviens plus quoi."
            K "Oh t'es lourd ! Je n'ai pas prévu que tu allais oublier de ramener les affaires de ce soir. Il va nous manquer de quoi passer la soirée !"
            K "Bon viens, sinon en plus d'etre con tu vas vraiment être en retard."

            jump suite3

        label tout :
            J "Ouais, j'ai pensé à ce que tu m'avais dit, normalement je n'ai rien oublié."
            K "Incroyable ! Je ne pensais pas que tu te souviendrais de tout. T'es vraiment parfait mon coeur."
            K "Bon, allons dans le salon, on était en train de jouer et... Ne t'inquiètes pas, j'ai une petite surprise pour toi après la soirée, une petite récompense..."
            E "Un clien d'oeil plus tard, Kim invite Jason à le suivre dans l'appartement où ils retrouvent Bryan et Anna autour d'une table de jeu dans le salon."

            $ relationJtoK += 1

        label suite3 :
            scene salon_jour
            with dissolve
            show kim_normal:
                xalign 0.5
            show bryan_drague:
                xalign 0.9
            show anna_normal:
                xalign 0.1
            E "Dans le salon, Bryan et Anna sont tous les deux assis autour d'une table où quelques bouteilles d'alcool ont déjà été vidées."
            B "Hééééé ! Mais c'est l'autre qui se décide enfin à arriver ! Viens dépêches-toi, je te sers un verre, il faut que tu me rattrapes !"
            A "Tu vas vraiment continuer de boire toute la soirée ? T'es déjà explosé..."
            K "Ouais, s'il te plait, calme toi un peu... Je n'ai pas envie de te récupérer en train de dormir sur le sol parce que tu t'es enquillé trop de verres d'alcool..."
            B "Mais fermez là... Il va falloir qu'on apprenne à vous décoincer un peu, un jour... Pas vrai Jason ?"
            B "Bon d'ailleurs, on était dans un débat : est-ce que tu penses que tu peux compter sur moi en cas de problèmes ou pas ?"
            J "C'est quoi cette question ?"
            A "On s'ennuyait en t'attendant du coup, Kim a décidé de nous lancer une série de questions pour savoir qui on préférait dans le groupe."
            A "On en était à 'Sur qui tu peux compter ?' là."

            menu:
                "Sur qui compter ?"
                "Bryan, mon ami d'enfance":
                    jump choix_Bryan
                "Anna, la plus intelligente":
                    jump choix_Anna
                "Kim, ma petite amie":
                    jump choix_Kim
        
        label choix_Bryan:
            J "Elle est nulle la question… Pour moi ça restera toujours Bryan. Il a beau être un peu con, il me colle au train depuis trop longtemps pour que je le laisse de côté."
            hide bryan_drague
            show bryan_content:
                xalign 0.9
            hide kim_normal
            show kim_colere:
                xalign 0.5
            B "Ah ! Vous voyez je vous l’avais dit ! Il fait passer la famille avant le coeur !"
            K "Ouais, je vois ça… Je vois surtout qu’il va finir par dormir tout seul ce soir..."

            $relationJtoB += 1
            hide bryan_content
            hide kim_colere
            hide anna_normal

            jump suite4

        label choix_Anna:
            J "En vrai, si je dois choisir entre vous trois… je pense que je prendrai Anna."
            B "Hé ! C’est quoi ce choix de merde là !"
            hide bryan_drague
            show bryan_colere:
                xalign 0.9
            hide anna_normal
            show anna_contente:
                xalign 0.1
            J "Non mais juste réfléchis un peu : elle est la plus calme, elle est la plus réfléchie d’entre nous, si il y a bien une personne qui peut me sauver le cul sans trembler c’est bien elle !"
            A "Et faut arrêter d’être jaloux Bryan. Elle baisse ta cote, assume-le, il préfère passer par d’autres gens que par toi."

            $relationJtoA += 1
            hide bryan_colere
            hide anna_contente
            hide kim_normal
            jump suite4

        label choix_Kim:
            
            J "Non mais ne me posez pas la question, je suis le seul en couple. Si je dois appeler quelqu’un entre vous trois, c’est forcément Kim, je sais que je peux lui faire confiance."
            hide kim_normal
            show kim_content:
                xalign 0.5
            A "Ah ! Tu vois Bryan, c’était évident. Son couple passera toujours devant toi, ne viens pas chialer."

            $relationJtoK += 1
            hide kim_content
            hide anna_normal
            hide bryan_drague
            jump suite4
        
        label suite4:
            show bryan_drague:
                xalign 0.9
            show kim_normal:
                xalign 0.5
            show anna_normal:
                xalign 0.1
            J "Forcément, elle était trop simple cette question... Vous en avez une autre ?"
            K "On a eu plein tout à l’heure mais on est à court d'idées. Genre par exemple, si jamais on devait vivre pendant une apocalypse, tu penses que lequel d’entre nous finirai par mourir en premier ?"

            menu:
                "Qui mourrait en premier ?"

                "Bryan":
                    jump choix_Bryan2
                "Anna":
                    jump choix_Anna2
                "Kim":
                    jump choix_Kim2

        label choix_Bryan2:
            B "Arrête de me regarder en rigolant, tu sais très bien que je serai le best survivor !"
            J "Je suis désolé mais celui d’entre nous qui durera le moins longtemps, c’est toi."
            hide bryan_drague
            show bryan_colere:
                xalign 0.9
            B "Mais n’importe quoi ! Je suis le seul qui fait du sport, vous allez être tellement lent que vous allez crever en moins de deux."
            B "Regarde Anna, même réfléchir ça lui prend du temps, alors je te dis pas si il faut qu’elle court !"
            A "Hé ! Va te faire ! Assume-le, t’es juste trop con, tu tomberais dans tous les pièges."
            hide anna_normal
            show anna_colere:
                xalign 0.1
            B "Humpf… Je savais que ça allait être un jeu de merde de toute manière..."
            hide bryan_colere
            hide anna_colere
            $relationJtoB -= 1

            jump suite5

        label choix_Anna2:
            J "Bah, écoute..."
            A "Hé, arrête de me fixer comme ça, si il y en a bien une qui peut survivre c’est bien moi !"
            J "Alors oui, mais tu n’es pas assez sportive. Si on se fait attaquer, je pense que celle qui a le moins de chance..."
            hide anna_normal
            show anna_colere:
                xalign 0.1
            A "Sans moi vous ne durerez pas plus de quelques jours."
            B_murmure "Tu parles, sans toi, putain, on serait tranquille..."
            A "Tu viens de dire quoi là ?"
            K "Bryan laisse-la tranquille un peu, tu veux ?"
            hide anna_colere
            $relationJtoA -= 1

            jump suite5
        
        label choix_Kim2:
            J "Si il faut réfléchir en terme de défense, le premier qui se ferait viser en cas d’attaque, c’est Kim. T’as trop l’air sans défense..."
            K "Pardon ? J’ai l’air faible ?"
            J "Non, je dis pas ça. Mais comparé à Bryan, s’il y a bien quelqu’un qui peut paraître moins dangereux, c’est bien toi quoi..."
            B_murmure "Ah c’est marrant, j’aurai plutôt dis Anna avec sa gueule de première de classe..."
            A "Hé mais vas te faire foutre !"
            K "Tu veux que je t’en colle une, voir si je suis si faible que ça ?"
            J "Non mais le prends pas comme ça mon coeur, hé !"

            $relationJtoK -= 1
            jump suite5

        label suite5:
            K "Bon, je change de question avant que ça parte encore plus en couilles. Si l’un d’entre nous était un dangereux psychopathe, vous pensez que ça serait qui ?"
            B "Elle est dure ta question..."

            menu:
                "Qui serait un psychopathe ?"
                "Bryan":
                    jump choix_Bryan3
                "Anna":
                    jump choix_Anna3
                "Kim":
                    jump choix_Kim3

        label choix_Bryan3:
            J "Moi je pense que ça pourrait être Bryan, regarde-le c’est le seul qui pourrait avoir assez de force pour..."
            jump suite6

        label choix_Anna3:
            J "Moi je pense que ça pourrait être Anna. Regarde-la c’est la seule qui pourrait être assez intelligente pour..."
            jump suite6

        label choix_Kim3:
            J "Moi je pense que je te dirai, toi. Entre nous tous, je suis sûr que t’es la plus fourbe, tu pourrais..."
            jump suite6


        label suite6:
            play sound "audio/Sounds/Bruit Sourd.mp3"
            B "Vous avez entendu ?"
            A "Quoi ?"
            B "Je ne sais pas, ça vient de l’entrée... Kim, tu n’as pas de chat ?"
            K "Non, non… Arrête tu commences à me faire flipper..."
            A "Non mais laisse tomber, regarde tout ce qu’il a bu, il est encore en train d’avoir des hallucinations."
            B "Anna, arrête. Je suis sûr de ce que j’ai entendu..."
            K "Mais c’était quoi, une voix, un bruit de pas... ?"
            B "Je n’en sais rien..."
            K "Je commence à avoir peur..."
            A "Vous paniquez pour que dalle, y'a vraiment rien à craindre à part le coma éthylique de Bryan."

            menu:
                "Croire Bryan : aller inspecter":
                    jump choix_Bryan4
                "Croire Anna : rassurer Kim":
                    jump choix_Anna4


    return # Quitte la partie, partie terminée