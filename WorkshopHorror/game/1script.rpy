# Vous pouvez placer le script de votre jeu dans ce fichier.

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
define N_shout = Character(kind = N, what_size = 100,what_font = 'Calvino-Regular-trial.ttf')
define I = Character('Voix inconnue', color= "#48ff00",what_font = 'Calvino-Regular-trial.ttf', who_font = 'UnfinishedScreamRegular.ttf')

define E = Character('', color= "#ffdabc", what_italic = True) # bruitage et environnement

define slowfade = Fade(3.0)

init:
    # Mettre toutes les variables ici
    $ relationJtoK = 0 #Jason to Kim
    $ relationJtoB = 0 #Jason to Bryan
    $ relationJtoA = 0 #Jason to Anna
    $ relationJtoN = 0 #Jason to Nancy

    $ lifeJ = 100 #vie Jason
    $ lifeK = 100 #vie Kim
    $ lifeB = 100 #vie Bryan
    $ lifeA = 100 #vie Anna
    $ lifeN = 100 #vie Nancy

    #variables intro
    $ traitement_conseil = False

    $ harcelement_kim_info = False

    #variables soiree

    $ vu_fenetre_ouverte = False
    $ telephone_oublie = False

    #variables exploration/confrontation psychopathe

    $ go_with_Anna = False
    $ go_with_Bryan = False
    
    $ torche = False

    $menacer_psychopathe = False

    $distraction_Bryan = False
    $trahison_Anna = False

    $ obstacles = 0

    #variables post confrontation

    $ seul = False
    $compagnie_Bryan = False
    $compagnie_Anna = False
    $police = False

    #variables de fin

    $ persuation = 0

# Le jeu commence ici
label start:

    play music "audio/Music/Prologue1.mp3" loop

    J_think "Aujourd'hui, c'est le grand jour." 
    J_think "Il ne me reste plus beaucoup de temps avant de partir pour la soirée."
    J_think "Il faut que tout soit parfait, sinon Kim ne me le pardonnera jamais."
    J_think "Depuis le temps qu'elle s'embête à tout bien organiser, la moindre petite erreur pourrait me coûter très cher."
    J_think "Ca fait des années qu'on se connaît, je sais comment elle réagira... surtout depuis la dispute d’hier."

    scene chambre_jason
    with dissolve

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

    J_think "Au moins, ce sera l'occasion de revoir Bryan. Ça fait plusieurs semaines que je ne l’ai pas revu."
    J_think "Je crois que Kim a décidé d’inviter Anna aussi. J’espère que tout va bien se passer malgré ses différends avec Bryan."
    J_think "Bon, je dois finir de me préparer avant d’arriver en retard. Je ne suis pas très convaincu par ma tenue mais tant pis, plus de temps à perdre."
    
    
    play sound "audio/Sounds/Phone Ringing.mp3" 
    
    # son de vibration, clic sur le portable mis en évidence en arrière plan

    # ouverture interface portable OU fondu au noir avec scène scindé, chaque perso sur son téléphone

    show telephone_appel:
        xalign 1.5 yalign 9
        linear 0.8 xalign 0.9

    E "Le téléphone de Jason sonne."
    J "Hey Nancy !"
    N "Salut Jason, je te dérange pas ?"
    J "Bien sûr que non."
    N "Je voulais juste t'appeler parce que je sors de chez le psy. J'avais rendez-vous cet après-midi..."
    J "Déjà ? Ton dernier rendez-vous était il y a à peine deux semaines... Pourquoi te revoir si tôt ?"
    N "Je n'ai pas non plus compris pourquoi. Mais mes parents ont insisté pour que je le vois..."
    N "Pourtant, ça fait des mois maintenant... J'aimerais qu'ils passent à autre chose."
    J "Je vois. Mais toi, comment tu te sens ?"
    N "Honnêtement, ça va bien ! J'en ai juste un peu marre de ces medocs qui me shootent complètement..."
    N "Je pense peut-être arrêter mon traitement. Je suis certaine que sans ça, ça ira encore mieux."
    N "Tu ne crois pas ?"

    menu:
        "Lui conseiller de continuer son traitement ou la rassurer sur son choix ?"
        "Continuer le traitement":
            jump continuer
        "La rassurer":
            jump rassurer

    label continuer:
        J "Ton psy serait d'accord avec ça ?"
        N "Je ne pense pas... mais je n'ai pas l'impression qu'il comprenne vraiment... Ni lui, ni mes parents."
        J "Hé, s'ils sentent que tu as besoin de continuer ton traitement, il faut que tu leur fasse confiance Nancy..."
        J "Ça ne va pas durer, tu vas y arriver."
        N "Tu crois ?"
        J "Fais moi confiance Nan'... Je suis ton ami, je te dis pas ça à la légère."
        N "..."
        E "Nancy s'en souviendra."

        $ traitement_conseil = True;

        jump suite
        
    label rassurer:
        J "Je suis pas le plus désigné pour te conseiller, par rapport à ça..."
        J "Mais effectivement, j'ai vraiment l'impression que tu vas mieux."
        N "Tu trouves aussi ? J'avais peur de me tromper mais je me sens bien en ce moment."
        J "T'es beaucoup plus souriante, t'as l'air de revivre."
        N "Je suis contente que tu le remarques ! Tu es le premier à me le dire, ça fait du bien !"
        N "Merci Jason. T'es un véritable ami !"
        E "Nancy s'en souviendra."

    label suite:
        N "... Hé dis-moi, ça te dit de sortir ce soir ? J'ai envie de prolonger l'euphorie pour la soirée avant que ça retombe..."
        J "Oh, euh... je ne vais pas pouvoir ce soir, malheureusement. Je dois aller chez Kim, on va enfin se voir avec les autres, depuis le temps."
        N "Les autres ?"
        J "Ouais, Bryan et Anna. Même si je ne comprends pas pourquoi on insiste à les faire venir ensemble, vu l'ambiance que ça donne."
        N "Hum..."
        J "Dis-moi... ça te tenterait pas de venir ?"
        J "Ce serait peut-être l'occasion d'enterrer la hache de guerre, et de passer une soirée tous ensemble, comme au bon vieux temps."
        N "Ouais, non... je pense pas que ce soit une bonne idée, Jason."
        N "Je suis pas la bienvenue, tu le sais bien."
        J "Tu es sûre ? J'ai l'impression qu'Anna et Kim se sont calmées avec toi, depuis le temps."
        N "N-non... Pas vraiment. C'est juste que... bref, t'en fais pas. Profite de ta soirée, tout ira bien !"

        menu :
            "En savoir plus":
                jump en_parler

            "Ne pas insister":
                jump desole

            "Dédramatiser":
                jump passer

    label en_parler:
      
        J "Attends, elles continuent de te faire chier ?"
        N "Ca... ça arrive... Elles sont juste plus discrètes qu'avant..."
        J "Putain ! J'avais fait jurer à Kim de te laisser tranquille ! Merde !"
        N "Oui... Je... Je pense pas que ce soit le genre de personnes qu'on peut raisonner, de ce côté-là..."
        J "Bon, je vais essayer de lui en parler ce soir. Je ne comprends pas ce qu'il se passe entre vous, mais il faut que vous arriviez à vous reparler un jour toutes les trois."
        N "Je ne suis pas sûre que ça change grand chose. C'est trop tard maintenant."
        J "Je vais gérer ça avec elles. Fais-moi confiance, et ne pense plus à ça. Profite de ta soirée, tu le mérites."
        N "M-merci Jason... Ca me touche énormément."
        E "Nancy s'en souviendra."

        $ relationJtoN += 1
        $ harcelement_kim_info = True

        jump suite2

    label desole:
        J "Je vois... Comme tu le sens, je ne vais pas t'obliger à y aller."
        N "Oui, je préfère rester chez moi."
        J "Désolé quand même de pas pouvoir sortir ce soir !"
        N "Je trouverai bien de quoi m'occuper, t'en fais pas pour ça."
        J "On se fera ça une autre fois ! Promis !"
        N "Comme tu voudras !"

        jump suite2

    label passer:
        J "Nancy, arrête de jouer les martyres... Kim fait parfois des plaisanteries un peu vaches, mais c'est pas pour être méchante..."
        N "Pardon ? Tu ne l'as jamais vue quand elle est avec Anna, ce n'est pas 'juste pour rigoler' Jason."
        J "Non mais... ce n'est pas ce que je voulais dire..." 
        J "Juste, ne prends pas à cœur tout ce qu'elle te dit, elle veut juste s'amuser avec toi. C'est toi qui empires la situation, en réagissant comme ça..."
        N "Tu sais quoi, va te faire foutre Jay ! Il faut que tu ouvres les yeux sur elle, ou elle va finir par t'avoir toi aussi !"
        J "Laisse tomber, Nancy. On en reparlera une autre fois."
        E "Nancy s'en souviendra."

        $ relationJtoN -= 1

    label suite2:
        J "Bon. Je vais devoir te laisser, sinon je vais être en retard. En tous cas, ça m'a fait plaisir de te parler."
        N "Ouais... Moi aussi..."
        J "Bisous !"

        play sound "audio/Sounds/Phone off.mp3"

        hide telephone_appel with dissolve

        J_think "Bon, il ne me reste plus beaucoup de temps."         
        
        show liste:
            xalign 0.5 yalign 0.3

        J_think "Kim m’a filé cette liste. Si j’oublie la moindre chose, c’est un coup à ce que la soirée parte en vrille."

        jump openAppart

    label chezKim:

        scene titre
        with fade

        pause 5

        scene fond_noir
        with dissolve

        E "Depuis l'extérieur, les fenêtres de la maison de Kim semblent éclairées. Quelques ombres témoignent de la présence de certaines personnes. La soirée a déjà commencé."
        J_think "Merde, je suis le dernier. J'espère que je n'ai pas raté grand chose."

        play sound "audio/Sounds/Carillon.mp3"
        E "Ding dong !"
        play music "audio/Music/Soiree1.mp3" loop fadeout 1

        E "Des pas précipités se font entendre derrière la porte d'entrée."

        #porte d'entrée qui s'ouvre

        scene entree
        with dissolve
        show kim surpris_j at center

        K "Ah bah te voilà enfin !"

        show kim drague3_j

        E "Kim plonge dans les bras de Jason, et l'embrasse langoureusement."

        K "T'es le dernier à arriver, on a cru que tu allais oublier la soirée !"
        J "Désolé, j'ai pris trop de temps sur le chemin, le bus a fait un détour."
        
        show kim gentil_j

        K "Ne t'en fais pas, va ! Alors, tu as pensé à ce que tu devais ramener ?"

        if (objetTrouve == 0 ):
            jump mainsvides
        elif (objetTrouve >=1 and objetTrouve <= 3) :
            jump moitie
        elif (objetTrouve == 4) :
            jump tout

        label mainsvides : 

            J "Merde, je suis désolé j'ai complètement oublié ce que tu voulais que je prenne..."

            show kim colere_j

            K "Tu te moques de moi là j'espère ? Non mais, tu espères vraiment me faire croire que tu as complètement oublié et tu ne m'as même pas envoyé un message pour me prévenir ?"
            K "Jay... Je... Tu m'énerves ! Viens, sinon je vais finir par t'étriper avant même que tu rentres..."

            $ relationJtoK -= 1

            E "Kim s'en souviendra."

            jump suite3
        
        label moitie :

            show kim choque_j

            J "Euh non, je crois qu'il fallait que je prenne un truc en plus, mais je ne me souviens plus quoi."
            K "Oh t'es lourd ! Je n'ai pas prévu que tu allais oublier de ramener les affaires de ce soir. Il va nous manquer de quoi passer la soirée !"
            K "Bon viens, sinon en plus d'être con tu vas vraiment être en retard."

            jump suite3

        label tout :

            J "Ouais, j'ai pensé à ce que tu m'avais dit, normalement je n'ai rien oublié."
            
            show kim heureux_j

            K "Incroyable ! Je ne pensais pas que tu te souviendrais de tout. T'es vraiment parfait mon coeur !"

            show kim drague3_j

            E "Kim s'en souviendra."

            K "Bon, allons dans le salon, on était en train de jouer et... Ne t'inquiètes pas, j'ai une petite surprise pour toi après la soirée, une petite récompense..."
            E "Un clien d'oeil plus tard, Kim invite Jason à le suivre jusqu'au salon, où ils retrouvent Bryan et Anna autour d'une table de jeu dans le salon."

            $ relationJtoK += 1

        label suite3 :
            scene salon_jour
            with dissolve
            show kim normal2_j at center
            show anna normal_j at center:
                xalign 0.95
            show bryan dragueur_j at center:
                xalign 0.05

            E "Dans le salon, Bryan et Anna sont tous les deux assis autour d'une table où quelques bouteilles d'alcool ont déjà été vidées."

            show bryan rire_j

            B "Hééééé ! Mais c'est l'autre qui se décide enfin à arriver ! Viens dépêches-toi, je te sers un verre, il faut que tu me rattrapes !"

            show anna surpris2_j

            A "Tu vas vraiment continuer de boire toute la soirée ? T'es déjà explosé..."

            show kim choque_j

            K "Ouais, s'il te plait, calme toi un peu... Je n'ai pas envie de te récupérer en train de dormir sur le sol parce que tu t'es enquillé trop de verres d'alcool..."  

            B "Mais fermez là... Il va falloir qu'on apprenne à vous décoincer un peu, un jour... Pas vrai Jason ?"

            show bryan normal_j   
            show kim normal2_j

            B "Bon d'ailleurs, on était dans un débat : est-ce que tu penses que tu peux compter sur moi en cas de problèmes ou pas ?"
            J "Heu... C'est quoi cette question ?"

            show anna normal_j

            A "On s'ennuyait en t'attendant du coup, Kim a décidé de nous lancer une série de questions pour savoir qui on préférait dans le groupe."
            A "On en était à 'Sur qui tu peux compter ?' là."

            menu:
                "Sur qui peux-tu compter ?"

                "{color=#ff0000}Bryan{/color}, mon ami d'enfance":
                    jump choix_Bryan

                "{color=#ff00bf}Kim{/color}, ma petite amie":
                    jump choix_Kim

                "{color=#ff9100}Anna{/color}, la plus intelligente":
                    jump choix_Anna
        
        label choix_Bryan:
            J "Elle est nulle la question… Pour moi ça restera toujours Bryan. Il a beau être un peu con, il me colle au train depuis trop longtemps pour que je le laisse de côté."
            show bryan rire_j

            B "Ah ! Vous voyez je vous l’avais dit ! Il fait passer la famille avant le coeur !"
            
            show kim choque_j

            K "Ouais, je vois ça… Je vois surtout qu’il va finir par dormir tout seul ce soir..."

            $relationJtoB += 1

            E "Bryan s'en souviendra."

            jump suite4

        label choix_Anna:
            J "En vrai, si je devais choisir entre vous trois... je pense que je prendrais Anna."

            show bryan surpris_j

            show anna surpris_j

            B "Hé ! C’est quoi ce choix de merde là !"
            J "Non mais juste réfléchis un peu : elle est la plus calme, elle est la plus réfléchie d’entre nous, si il y a bien une personne qui peut me sauver le cul sans trembler c’est bien elle !"

            show anna content_j

            A "Stop la jalousie, Bryan. Ta côte baisse, accepte-le, Jason préfère se tourner vers des gens plus intéressants que toi, c'était prévisible."

            $relationJtoA += 1

            E "Anna s'en souviendra."

            jump suite4

        label choix_Kim:
            
            J "Ca paraît évident, non ? Je suis en couple, donc si je dois appeler l'un de vous trois, c’est forcément Kim, je sais que je peux lui faire confiance."

            show bryan surpris_j

            show kim content_j

            A "Ah ! Tu vois Bryan, c’était évident. Son couple passera toujours devant toi, c'est pas la peine de chialer."

            $relationJtoK += 1

            E "Kim s'en souviendra."

            jump suite4
        
        label suite4:

            J "Bon bon, du calme ! Vous en avez une autre ?"

            show kim normal2_j

            K "On a eu plein tout à l’heure, mais on est à court d'idées."
            K "Il y avait celle-ci, par exemple :"
            K "''Si jamais on devait vivre pendant une apocalypse, lequel mourrait le premier ?''"

            menu:
                "Qui mourrait le premier ?"

                "{color=#ff0000}Bryan{/color}":
                    jump choix_Bryan2
                "{color=#ff00bf}Kim{/color}":
                    jump choix_Kim2
                "{color=#ff9100}Anna{/color}":
                    jump choix_Anna2

        label choix_Bryan2:

            show bryan confiant_j

            B "Arrête de me regarder en rigolant, tu sais très bien que je serai le best survivor !"
            J "Je suis désolé mais celui d’entre nous qui durera le moins longtemps, c’est toi."
            
            show bryan colere_j

            B "Mais n’importe quoi ! Je suis le seul qui fait du sport, vous serez tellement lent qu'en moins de deux, vous finirez crevé dans la gueule d'un zombie."
            B "Regarde Anna, elle met trente ans à prendre une décision, alors je te dis pas s'il faut qu’elle court !"
            
            show anna jugement_j
            
            A "Hé ! Va te faire ! Assume-le, t’es juste trop con, tu tomberais dans tous les pièges."
            B "Humpf… Je savais que ça allait être un jeu de merde de toute manière..."

            $relationJtoB -= 1

            E "Bryan s'en souviendra."

            jump suite5

        label choix_Anna2:

            J "Bah, écoute..."

            show anna colere_j

            A "Hé, arrête de me fixer comme ça, s'il y en a bien une qui peut survivre c’est bien moi !"
            J "Alors oui, mais tu n’es pas assez sportive. Si on se fait attaquer, je pense que celle qui a le moins de chance..."
            A "Sans moi vous ne durerez pas plus de quelques jours."

            show bryan perdu_j

            B_murmure "Tu parles, sans toi, putain, on serait tranquille..."

            show anna surpris2_j

            A "Tu viens de dire quoi là ?"

            show kim pense_j

            K "Bryan laisse-la tranquille un peu, tu veux ?"

            $relationJtoA -= 1

            E "Anna s'en souviendra."

            jump suite5
        
        label choix_Kim2:

            J "Si il faut réfléchir en terme de vulnérabilité, la première personne qui serait visée en cas d’attaque, ce serait Kim. T’as l’air sans défense..."

            show kim choque_j

            K "Pardon ? J’ai l’air faible, moi ?"
            J "Non, je dis pas ça. Mais comparé à Bryan, s’il y a bien quelqu’un qui paraît moins dangereux, c’est toi quoi..."

            show bryan perdu_j

            B_murmure "Ah c’est marrant, j’aurai plutôt dis Anna avec sa gueule de première de classe..."

            show anna surpris2_j

            A "Hé mais va te faire foutre !"

            show kim colere_j            

            K "Tu veux que je t’en colle une, pour voir si je suis si faible que ça ?"
            J "Non mais le prends pas comme ça mon coeur, hé !"

            $relationJtoK -= 1

            E "Kim s'en souviendra."

            jump suite5

        label suite5:

            show kim reflechir_j
            show anna jugement_j
            show bryan normal_j

            K "Bon, je change de question avant que ça parte encore plus en couilles. Si l’un d’entre nous était un dangereux psychopathe, qui ce serait ?"
            B "Elle est dure, ta question..."

            menu:
                "Qui serait un psychopathe ?"
                "{color=#ff0000}Bryan{/color}":
                    jump choix_Bryan3
                "{color=#ff00bf}Kim{/color}":
                    jump choix_Kim3
                "{color=#ff9100}Anna{/color}":
                    jump choix_Anna3

        label choix_Bryan3:
            J "Moi je pense que ça pourrait être Bryan. Regarde-le, c’est le seul qui pourrait avoir assez de force pour..."
            jump suite6

        label choix_Anna3:
            J "Moi je pense que ça pourrait être Anna. Regarde-la, c’est la seule qui pourrait être assez intelligente pour..."
            jump suite6

        label choix_Kim3:
            J "Moi je pense que ce serait toi, Kim. De nous tous, t’es la plus fourbe, tu pourrais..."
            jump suite6


        label suite6:
            play sound "audio/Sounds/Bruit Sourd.mp3"

            show bryan peur1_j

            B "Vous avez entendu ?"

            A "Quoi ?"
            B "Je ne sais pas, ça vient de l’entrée... Kim, tu n’as pas de chat ?"

            show kim choque_j

            K "Non... Arrête, tu commences à me faire flipper !"

            show anna persuasion_j

            A "Non mais laisse tomber, regarde tout ce qu’il a bu, il est encore en train d'halluciner."
            B "Anna, arrête. Je suis sûr de ce que j’ai entendu..."
            K "Mais c’était quoi, une voix, un bruit de pas... ?"
            B "Je n’en sais rien..."
            K "Je commence à avoir peur..."
            A "Vous paniquez pour que dalle, y'a vraiment rien à craindre à part le coma éthylique de Bryan."
            play music "audio/Music/Tension Nonstop - Myuu.mp3" loop fadeout 1
            menu:
                "Croire Bryan : aller inspecter":
                    jump choix_Bryan4
                "Croire Anna : rassurer Kim":
                    jump choix_Anna4