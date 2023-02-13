label scene_cave:
    if (seul == True):
        jump seul_cave
    elif (seul == False & telephone_oublie == True):
        jump tous_cave_kim_quasimorte
    elif (seul == False & telephone_oublie == False):
        jump tous_cave_kim_blesse

    pause .5

label seul_cave:

    $blessure_kim = 1

    scene escalier
    with dissolve

    J "Kim ? Qu’est-ce qu’il se passe !"
    K_shout "Aahhhhhhh"
    J "Kim ! T’es où, j’arrive !"
    J "Réponds-moi, où est-ce que tu es ?"
    E "Alors que Jason descend les escaliers, une silhouette vive disparaît au détour d’un couloir."   
    J "Kim qu’est-ce qu’il se passe ?"
    
    scene corps
    with dissolve
    
    J "Nom de Dieu, Kim ! Hé Kim ! Regarde-moi, qu’est-ce qu’il s’est passé ?"
    K "Je... je ne sais pas... Jason... J’ai mal."
    E "Une grosse plaie au couteau perce le dos de Kim. Elle perd beaucoup de sang."
    J "Ne regarde pas ! Qui t’as fait ça ?"
    K "Je... je ne sais pas... Elle semblait... masquée."

    menu:
        "Poursuivre la silhouette":
            jump poursuite
        "Rester avec Kim":
            jump rester_Kim

label poursuite:
    J "Kim, maintient ta main sur la blessure. Le plus fort possible !"
    K "Arrrrgh"
    J "Tu vas y arriver, je reviens vite !"
    E "Lâchant la main de sa petite amie, Jason poursuit la silhouette ayant disparue un instant auparavant."

    scene couloir_box
    with dissolve
    
    E "Là où la silhouette avait disparu se tient désormais une grille entrouverte. Plus aucune trace de la silhouette."
    J_think "Comment est-ce que..."
    K_shout "Jason !"

    scene corps
    with dissolve

    E "Jason revient auprès de Kim, et prend conscience qu'il ne pourra la sauver sans aide. Il grimpe les escaliers de la cave, quatre à quatre, avant d'appeler en urgence ses amis."

    scene escalier
    with dissolve

    J_shout "Bryan, Anna ! Venez vite m'aider !"

    jump suite14

label rester_Kim:
    K "J’ai mal Jason... J’ai... mal..."
    J "Je sais mon coeur, je sais. Maintient la pression sur ta plaie, je vais demander à Anna et Bryan de venir nous aider. Voilà. Tu t’en sors bien."

    scene escalier
    with dissolve

    E "Jason grimpe les escaliers de la cave, quatre à quatre, avant d'appeler en urgence ses amis."
    J_shout "Bryan, Anna ! Venez vite m'aider !"

    jump suite14


label suite14:

    scene corps
    with dissolve

    E "Une minute plus tard, Bryan et Anna ont franchi la maison en courant jusqu'à la cave, et découvre, horrifiés, l'état dans lequel se trouve Kim."
    A "Putain, qu'est-ce qu'il s'est passé ?"
    J "Kim s’est faite attaquer, elle est blessée, elle a besoin d’aide !"
    B "Oh non, non, non, non…"
    E "Anna vérifie son téléphone."
    A "Ok, on n'a pas de réseau, c’est la merde. Il faut qu’on agisse et vite."
    J "Je… je ne sais pas quoi faire."

    jump suite15


label tous_cave_kim_blesse:

    scene escalier
    with dissolve

    $blessure_kim = 1

    E "Une minute plus tard, Bryan, Anna et Jason ont franchi la maison en courant jusqu'à la cave."
    J "Kim ? Où es-tu ?"
    A "Kim ?"
    B "Kim, répond ! T'es où ?"

    scene corps
    with dissolve

    B "Les gars ? Je crois qu’elle est là !"
    A_shout "AHHHHH" #(crié rapide)
    J_shout "Putain ! Kim, Kim, hé regarde-moi !" #(crié et très rapide)
    A "Merde, elle saigne !"
    E "Une grosse plaie au couteau perce le dos de Kim. Elle perd beaucoup de sang."
    K "Jason... je... j'ai mal..."
    J "Ne bouge pas, regarde-moi. Ça va aller mon coeur. Ça va aller. Qui t’a fait ça ?"
    K "Je ne... sais pas... J’ai... Jason... j’ai mal"
    B "Les gars ! Je crois que j’ai vu quelqu’un monter les escaliers !"
    J "Choppe le !"
    E "Remontant les escaliers quatre à quatre, Bryan disparaît dans le détour d’un couloir."
    J "Aucune idée ! Hé, mon coeur, qu’est-ce qu’il s’est passé ?"
    K "Je... aucune idée. Aahh... Elle est venue dans mon dos..."
    J "Elle ?"
    K "Je... je ne sais pas..."
    E "Bryan est de retour."
    B "Putain, il s’est barré !"
    J "T’as vu qui c’était ?"
    B "Je n’ai pas eu le temps, c’était... c’était une petite silhouette..."
    E "Anna vérifie son téléphone."
    A "Ok, on n'a pas de réseau, c’est la merde. Il faut qu’on agisse et vite."
    J "Je… je ne sais pas quoi faire."

    jump suite15
 
label tous_cave_kim_quasimorte:

    scene escalier
    with dissolve

    $blessure_kim = 2

    E "Bryan, Anna et Jason arrivent dans la cave."
    B "Bah alors, Kim, on traîne du cul ?"
    J "Kim ? Où es-tu ?"
    A "Kim ?"
    B "Kim, répond ! T'es où ?"

    scene corps
    with dissolve

    B "Les gars ? Je crois qu’elle est là !"
    A_shout "AHHHHH" #(crié rapide)
    J_shout "Putain ! Kim, Kim, hé tu m'entends !" #(crié et très rapide)
    A "Merde, elle saigne !"
    E "Une grosse plaie au couteau perce le dos de Kim. Une énorme flaque de sang recouvre le sol autour d'elle. Kim est pâle, et semble inconsciente."
    B "Bordel de merde, qui lui a fait ça ?!"
    E "Anna vérifie son téléphone."
    A "Ok, on n'a pas de réseau, c’est la merde. Il faut qu’on agisse et vite."
    J "Je… je ne sais pas quoi faire."

    jump suite15


label suite15:

    scene cave
    with dissolve

    A "Ok, d’abord, il faut que je regarde sa blessure. J’ai suivi des cours de premiers soins. Bryan il faut que tu maintienne la pression sur la plaie !"
    A "Pendant ce temps là Jason, fouilles la cave, et barricade l'accès. Qui que ce soit qui ait fait ça, il faut pas qu'il nous retombe dessus."

# séquence Point and click ?
    jump openCave

label choix_cave:

    A "Ok, les gars c’est la merde. Bryan vient voir ! J’ai regardé sa plaie, ce n’est pas joli à voir. Loin de là. je ne sais pas qui lui a fait ça, mais elle ne l’a pas raté !"
    J "Tu crois qu’elle est en danger ?"
    A "Si elle est en danger ? Mais bien sûr que oui, ducon ! Il ne faut pas que l’on perde de temps. Mais s'il y a quelqu’un qui est dans le coin et qui est capable de faire ça à Kim, ça veut dire que nous aussi on est en danger !"
    B "Hé, je te rappelle qu’on est trois ! Peu importe qui c’est, on est assez pour prendre le dessus !"
    A "Non mais tu t’écoutes ? Regarde où on en est ! Elle est en train de pisser le sang dans une cave !"
    B " Alors allons chercher de quoi la soigner ! Elle doit bien avoir une trousse de soin quelque part ! Elle en avait pas sortie une de la cuisine, l'autre soir ?"
    A "C’est débile, aucun de nous ne sait soigner ce genre de blessure, tu n’as pas vu ce que j’ai vu."
    B "Alors quoi, tu proposes quoi comme idée ?"
    A "On appelle juste les secours, on espère que la personne qui lui a fait ça ne revient pas, et on attends ! Non mais on n’est pas des héros, Bryan !"
    B "Ah bah si on reste là en espérant, c’est sûr que c’est l’idée du siècle ! Et c'est pas toi qui disait qu'il y avait pas de réseau ?"
    A "Il me semble qu'à l'étage, on peut avoir du réseau."
    B "Quitte à risquer notre peau dans cette maison, autant le faire pour chopper une trousse de soin."
    A "Ce sera clairement moins utile que d'appeler les secours !"
    B "On doit essayer ! Bon, Jason. Qu’est-ce que tu en dis ?"


menu: # GROSSE SEPARATION DU SCENARIO
    "Soutenir Bryan":
        $ go_with_Bryan = True
        jump suivre_Bryan
    "Soutenir Anna":
        $ go_with_Anna = True
        jump suivre_Anna