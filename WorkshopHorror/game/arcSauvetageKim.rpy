J "Kim ! Regarde-moi… Bordel, Bryan vient m’aider ! Elle se vide de son sang !"
B "Appuie sur ses plaies, il faut que l’on trouve de quoi bander vite !"

if (go_with_Anna == True):
    jump postTelephone
elif (compagnie_Bryan):
    jump postSoinsBryan
else:
    jump postSoinsSeul

label postTelephone:
    #Son manquant à la sonothèque, cri d'un homme
    play sound "audio/Sounds/.mp3"
    E "Un cri résonne dans la maison."
    A "C’était quoi ça ?"
    J "Merde, c’est Bryan !"
    A "Bryan ? Il ne devait pas rester avec Kim ?"
    J "Il faut qu’on aille l’aider…"
    A "Quoi ? Tu ne vois pas que Kim se vide de son sang ? La pauvre elle s’est refaite plantée. Si on ne la sort pas de là, elle va y passer la prochaine fois !"
    menu:
        "Mettre Kim à l'abri":
            jump kimAbri
        "Aller sauver Bryan":
            jump sauvetageBryan
    jump sequence4

label kimAbri:
    J "Ok, porte la… Il faut qu’on se dépêche, avant qu’elle ne perde trop de sang !"
    A "Ça continue de couler !"
    J "Alors on la tire, vas-y dépêche toi !"
    E "Jason et Anna sortent de la maison, tirant Kim jusque dans les bois environnants."
    J "Ici, on va pouvoir la laisser."
    A "Ok, dépose-la tout doucement."
    E "Des branches craquent dans leur dos."
    N "Lâchez la… elle mérite…"
    N "Elle doit mourir…"
    A_shout "Qui êtes-vous ! Laissez-nous tranquille !"
    N "Alors, Anna ? Qu’est-ce que ça fait… de ressentir la peur ? Hein ?"
    N "De te sentir… faible. Impuissante. Hein ?"
    N "Dis le…"
    N_shout "Dis le !"
    menu:
        "Fuir ensemble":
            jump fuiteEnsemble
        
        "Confronter la tueuse":
            jump confrontationTueuse
label fuiteEnsemble:        
    J "Anna, recule ! Viens, vite !"
    E "Vous tirez Anna par le bras et vous vous enfuyez."
    E "Derrière vous, la femme se lance à votre poursuite."
    menu:
        "Porter Kim":
            jump porterKim
        
        "Faire diversion":
            jump diversionPoursuite
label porterKim:
    J "Je m’occupe de Kim, toi cours !"
    E "Devant vous, Anna commence à courir entre les arbres. Trop lourd avec Kim, vous n’arrivez pas à la rattraper."
    E "Dans votre dos, les bruits de pas se rapprochent de plus en plus, jusqu’à ce qu’un choc vous fasse perdre connaissance."   
    jump sequence4
label diversionPoursuite:
    J "Prends Kim avec toi, je vais essayer de te faire gagner du temps !"
    A "Quoi ? T’es sûr ?"
    J "Fais moi confiance, ok ? Prends la et court ! Vas-y !"
    E "Sans un mot, Anna commence à courir alors que vous faites face à la femme masquée."
    J_shout "Pourquoi ? Pourquoi est-ce que tu fais ça ?"
    E "La femme ne réponds pas."
    J "Attends… Ne me dis pas que…"
    E "D’un coup vif, elle vient planter son couteau dans votre chair avant de vous asséner un violent coup à la tête."
    jump sequence4
label confrontationTueuse:
    J "Prends Kim avec toi, je vais essayer de te faire gagner du temps !"
    A "Quoi !? Mais qu’est-ce que tu fais ?"
    J "J’essaie de sauver Kim… Laisse-moi, vas-y !"
    E "Anna s’en va, prenant Kim avec elle."
    J_shout "Pourquoi ? Pourquoi est-ce que tu fais ça ?"
    E "La femme ne réponds pas."
    J "Pourquoi est-ce que tu nous fais ça ? Tu es qui?"
    J "Réponds-moi ! Qu’est-ce que tu veux de nous ?"
    E "Elle avance."
    J "Arrête d’avancer ! Dis-moi qui tu es ? Laisse-nous tranquille !"
    J "La police va arriver, ok ? Alors tire-toi putain !"
    E "Reculant dans les arbres, vous vous cognez à l’un d’entre eux."
    E "La femme se rapproche, tend le bras, et vous assène un violent coup. Vous vous effondrez, inconscient."
    jump sequence4
    #if (relationJtoA >= 100):
        #Anna et Kim survivent
    #else:
        #Anna survit, Kim meurt

label sauvetageBryan:
    J "Prends Kim avec toi…"
    A "Quoi ? T’es sérieux là ?"
    J "Je ne peux pas laisser Bryan tout seul, il est en danger !"
    A "Alors que Kim, tu t’en fous, c’est ça ?"
    J "Je suis désolé… Je te fais confiance, je reviens vite !"
    J_shout "Bryan ? Où es-tu ?"
    J_think "J’espère qu’il n’est pas trop tard…"
    E "Dans la cave, Bryan est à genoux, de large coupures sur les bras et le visage tuméfié."
    jump lamentationNancy

label postSoinsBryan:

    play sound "audio/Sounds/Cri Kim 1.mp3"

    E "Un cri retentit."
    B "C’était quoi ça ?"
    J "Merde, c’est Anna !"
    B "Anna ? Où est-ce qu’elle est partie ?"
    J "Il faut qu’on aille l’aider…"
    B "Quoi ? Tu ne vois pas que Kim se vide de son sang ? Elle s’est refaite planter ! Si on ne la sort pas de là, elle va y passer la prochaine fois !"
    J "On ne va pas la laisser crever !"
    B "Alors vas y, fonce ! Je m’occupe de Kim, toi, vas aider Anna !"
    E "Vous vous précipitez dans les escaliers"
    E "Dans la cave, Anna est à genoux, de larges coupures sur les bras et le visage tuméfié."
    jump lamentationNancy
    jump sequence4

label lamentationNancy:
    N "Jamais… Jamais… C’est terminé, maintenant."
    J "Hé, laisse-le partir !"
    N "Non..."
    N "Non..."
    N "Non !"
    N "Je dois le faire… Je dois…"
    E "La femme baisse la tête. Vous en profitez pour lui bondir dessus."
    E "Dans l'action, sa lame glisse contre vos côtes."
    E "Vous vous effondrez de douleur avant de recevoir un grand coup sur le crâne"

label postSoinsSeul:
    menu:
        "Sauver Kim":
            jump saveKim
        "Sauver Anna":
            jump saveAnna
    jump sequence4

label saveKim:
    J "Hé, je reste avec toi alors ne me laisse pas, ok ?"
    E "Vous utilisez le contenu de la trousse pour sauver Kim."
    J "J’irai aider Anna plus tard, pour l’instant, il faut que je te sauve toi."
    E "Après avoir soigné votre petite amie, vous vous assurez que sa situation est stable, puis partez en direction de la cave."
    J_shout "Anna ! Tu es où ?"
    J_shout "Anna !"
    E "La cave est silencieuse. Pas un bruit."
    J "Anna ? Oh non… Non, mon Dieu… Non, Anna !"
    E "Dans la pièce, seul le cadavre d’Anna repose."
    J "Ce n’est pas possible… Je suis désolé… Je suis si désolé…"
    J "Je… putain… Anna !"
    E "Penché sur le cadavre de son ami, vous n'entendez pas les bruits de pas arriver dans votre dos."


label saveAnna:
    J "Hé mon coeur, je vais revenir, d’accord ?"
    J "Je vais juste aider Anna, d’accord. Je vais revenir, je te le promet. Je t’aime."
    E "Laissant Kim derrière lui, vous retournez dans la cave d’où vient le cri."
    J_shout "Anna? T'es où?"
    J_think "J’espère qu’il n’est pas trop tard…"
    E "Dans la cave, Anna est à genoux, de larges coupures sur les bras et le visage tuméfié."
    jump lamentationNancy

