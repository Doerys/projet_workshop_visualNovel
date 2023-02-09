label scene_cave:
    if (seul == True):
        jump seul_cave
    elif (seul == False):
        jump tous_cave



label seul_cave:

    J "Kim ? Qu’est-ce qu’il se passe !"
    K_shout "Aahhhhhhh"
    J "Kim ! T’es où, j’arrive !"
    J "Réponds-moi, où est-ce que tu es ?"
    E "Alors que Jason descend les escaliers, une silhouette vive disparaît au détour d’un couloir."
    J "Kim qu’est-ce qu’il se passe ?"
    J "Nom de Dieu, Kim ! Hé Kim ! Regarde-moi, qu’est-ce qu’il s’est passé ?"
    K "Je... je ne sais pas... Jason... J’ai mal."
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
    E "Lâchant la main de sa petite amie, Jason les escaliers quatre à quatre."
    E "Là où la silhouette avait disparu se tient désormais porte entrouverte."
    E "Sans y réfléchir, Jason y entra, mais découvrit une salle vide."
    J_think "Comment est-ce que..."
    J "Bryan, Anna ! Venez vite m'aider !"

    jump suite15



label rester_Kim:
    K "J’ai mal Jason... J’ai... mal..."
    J "Je sais mon coeur, je sais. Maintient la pression sur ta plaie, je vais demander à Anna et Bryan de venir nous aider. Voilà. Tu t’en sors bien."

    #Appel Bryan

    B "Allô ? T’es... avec... long !"
    J "Allô ? Bryan ? Si tu m’entends, viens à la cave. Tout de suite ! Kim s’est faite attaquée !"
    B "C’est... je le dis... arrive !"
    J_think "Putain de réseau..."
    J "Continue comme ça Kim, c’est parfait. Respire. Doucement, voilà, comme ça. On va t’aider, tu vas t’en sortir, d’accord ?"



label suite14:
    A "Hé, oh qu’est-ce qu’il se passe ici ?"
    J "Kim s’est faite attaquer, elle est blessée, elle a besoin d’aide !"
    B "Oh non, non, non, non…"
    A "Ok, on a pas de réseau, c’est la merde. Il faut qu’on agisse et vite."
    J "Je… je ne sais pas quoi faire."

    jump suite15


label tous_cave:

    J "Kim ? Où es-tu ?"
    A "Kim ?"
    B "Kim, répond ! T'es où ?"


# Si Kim a son tel
    B "Les gars ? Je crois qu’elle est là !"
    A "AHHHHH" #(crié rapide)
    J_shout "Putain ! Kim, Kim, hé regarde-moi !" #(crié et très rapide)
    A "Merde, elle saigne !"
    K "Jason... je... j'ai mal..."
    J "Ne bouge pas, regarde-moi. Ça va aller mon coeur. Ça va aller. Qui t’a fait ça ?"
    K "Je ne... sais pas... J’ai... Jason... j’ai mal"
    B "Les gars ! Je crois que j’ai vu quelqu’un monter les escaliers !"
    J "Choppe le !"
    E "Remontant les escaliers quatre à quatre, Bryan disparaît dans le détour d’un couloir."
    A "Il nous faut une trousse de secours, tu sais où il y en a ?"
    J "Aucune idée ! Hé, mon coeur, qu’est-ce qu’il s’est passé ?"
    K "Je... aucune idée. Aahh... Elle est venue dans mon dos..."
    J "Elle ?"
    K "Je... je ne sais pas..."
    B "Putain, il s’est barré !"
    J "T’as vu qui c’était ?"
    B "Je n’ai pas eu le temps, c’était... c’était une petite silhouette..."



    label suite15:
        A "Ok fouilles la cave, et pendant ce temps là Bryan il faut que tu maintienne la pression sur la plaie !"
        A "Bon, donc on n’a pas de réseau. Si on doit la soigner, il va falloir qu’on se bouge, d’accord ? D’abord, il faut que je regarde sa blessure. J’ai eu des cours de premiers soins."


    # séquence Point and click ?

        A "Ok, les gars c’est la merde. Bryan vient voir ! J’ai regardé sa plaie, ce n’est pas joli à voir. Loin de là. je ne sais pas qui lui a fait ça, mais elle ne l’a pas raté !"
        J "Tu crois qu’elle est en danger ?"
        A "Si elle, elle est en danger ? Oui, il ne faut pas que l’on perde de temps. Mais s'il y a quelqu’un qui est dans le coin et qui est capable de faire ça à Kim, ça veut dire que nous aussi on est en danger !"
        B "Hé, je te rappelle qu’on est trois ! Peu importe qui c’est, on est assez pour prendre le dessus !"
        A "Non mais tu t’écoutes ? Regarde où on en est ! Elle est en train de pisser le sang dans une cave !"
        B " Alors allons chercher de quoi la soigner ! Elle doit bien avoir une trousse de soin quelque part !"
        A "C’est débile, aucun de nous ne sait soigner ce genre de blessure, tu n’as pas vu ce que j’ai vu."
        B "Alors quoi, tu proposes quoi comme idée ?"
        A "On appelle juste les secours, on espère que la personne qui lui a fait ça ne revient pas, et on attends ! Non mais on n’est pas des héros, Bryan !"
        B "Ah bah si on reste là en espérant, c’est sûr que c’est l’idée du siècle ! Anna, quand Jason a essayé de m’appeler, le réseau était tellement pourri qu’on ne se comprenait pas !"
        A "On doit essayer ! Bon, Jason. Qu’est-ce que tu en dis ?"


    menu: # GROSSE SEPARATION DU SCENARIO
        "Suivre Bryan":
            $ go_with_Bryan = True
            jump suivre_Bryan
        "Suivre Anna":
            $ go_with_Anna = True
            jump suivre_Anna
 

    