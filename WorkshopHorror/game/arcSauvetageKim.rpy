<<<<<<< HEAD
@@ -1,174 +1,150 @@
label lectureMessage:

E "Alors que Jason regarde dans le téléphone pour appeler les secours, un message attire son attention."
J_think "Attends, qu’est-ce que c’est que ça…"
J_think "Kim ? Mais qu’est-ce que ?"
E "“Kimou : Tu dis qu j’ai que de la gueule ms le jour ou on va te retrouver crevée ds le canal tu rigolera plus, sale chienne. Essaye même pas de te plaindre à quelquun, personne écoutera ta sale gueule de pute.”"
E "“Kimou : Alors vas y continu de faire la meuf quand y a du monde autour, je sais que tout ce que tu veux cest te tirer une balle pour arreter ta vie de merde”"
J_think "Je reconnais ce numéro... C'est adressé à Nancy ! Quelle horreur... Kim, qu'est-ce qui t'a pris ?"

J_think "Attend, et qu'est-ce que c'est que ça ?"
E "D'autres séries de messages apparaissent dans la messagerie du téléphone."
E "CONTACT : B <3"
E "Kim : ct trop bien hier soir, on refait sa quand tu veux <3"
E "B : c'est vrai, ta kiffé ?"
E "Kim : fais pas genre, mdr, le gars veut satisfaire son ego"
E "B : je peux te satisfaire autant que tu veux, tkt"
E "Kim : mdr, tg, t'es trop con"
E "B : coquine"
E "Kim : lov <3" 

J_think : "Putain, c'est quoi cette merde ? ''B'' ? Non... me dis pas que..."

if (compagnie_Anna == True):
E "“Tu dis qu j’ai que de la gueule ms le jour ou on va te retrouver crevée ds le canal tu rigolera plus, sale chienne. Essaye même pas de te plaindre à quelquun, personne écoutera ta sale gueule de pute.”"
E "“Alors vas y continu de faire la meuf quand y a du monde autour, je sais que tout ce que tu veux cest te tirer une balle pour arreter ta vie de merde”"

if (go_with_Anna == True):
    jump policecallAnna
=======
J "Kim ! Regarde-moi… Bordel, Bryan vient m’aider ! Elle se vide de son sang !"
B "Appuie sur ses plaies, il faut que l’on trouve de quoi bander vite !"

if (troussedeSoin =False):
    jump postTelephone
elif (truc on est avec bryan):
    jump postSoinsBryan
>>>>>>> 0c41905118cfb3e0c557b8550c36ac88eb193ce0
else:
    jump policeCallAlone

<<<<<<< HEAD
label policecallAnna:
    J "Hé, regarde ça !"
    A "Ce n’est pas ce que tu crois…"
    J "Parce que tu le savais ? Anna ! Je vous avais demandé d’arrêter !"
    A "Hé ! Ce n’est pas moi qui ai envoyé ce message, c’est à Kim qu’il faut te plaindre !"
    J "Et tu sais à qui elle envoie des messages ?"
    A "Jason calme-toi, on va se faire attraper…”"
    J "Non ! Parles-moi !"
    A "Elle… elle ne m’a jamais dit qui c’est… Je suis désolée Jason, elle m’avait promis de t’en parler…"
    J "C’est pas possible… T’as de la chance qu’on doit partir d’ici, mais crois-moi qu’on va en reparler !"
    E "Jason compose le numéro de secours."

    play sound "audio/Sounds/Phone Calling.mp3"
    
    J "Allô ?"
    E "Le téléphone grésille…"
    J "Allô, vous m’entendez ?"
    A "Moins fort, tu vas nous faire repérer !"

=======
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
    jump mauve

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
>>>>>>> 0c41905118cfb3e0c557b8550c36ac88eb193ce0
    menu:
        "Parler de la tueuse":
            J "Si vous nous entendez, on est en train de se faire attaquer ! Allô ?"
        "Dire que vous êtes en danger":
            J "On est en danger, venez vite !"
        "Réclamer de l'aide pour Kim":
            J "Mon amie est blessée, on a besoin d’aide, s’il vous plaît !"

<<<<<<< HEAD
    E "Un bruit sourd résonne à l'intérieur de la maison."
    A "Donne leur l'adresse."
    E "Aucune réponse"
    A "Donne leur l'adresse"
    J "On est au 18 Stanway Road! Dépêchez vous!"

    play sound "audio/Sounds/Phone Off.mp3"

    A "Ils arrivent quand?"
    J "Je ne sais pas. Le téléphone adu mal à passer, j'espère qu'ils ont réussi à m'entendre."

    E "Le hurlement de Kim résonne à l'intérieur de la maison."
    N_shout "Anna ! Je sais que t’es dans la maison !"
    N_shout "Oooooooh… Aahh… Viens là !"

    J "C’était quoi ça ?"
    A "Elle arrive ! Oh mon dieu, elle arrive !"

    play sound "audio/Sounds/Cri Kim2.mp3"
    E "Un cri aigu retentit dans la maison."

label policeCallAlone:

    J_think : "Non, Jason, reste concentrée, t'es en danger de mort. Aller, appeler les secours."
=======
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

>>>>>>> 0c41905118cfb3e0c557b8550c36ac88eb193ce0

    E "Vous composez le numéro de secours."
    J "Allô ?"
    E "Le téléphone grésille…"
    J "Allô, vous m’entendez ?"
    menu:
        "Parler de la tueuse":
            J "Si vous nous entendez, on est en train de se faire attaquer ! Allô ?"
        "Dire que vous êtes en danger":
            J "On est en danger, venez vite !"
        "Réclamer de l'aide pour Kim":
            J "Mon amie est blessée, on a besoin d’aide, s’il vous plaît !"

    E "Des bruits de pas semblent se rapprocher de la porte."
    J_murmure "Allô?"
    E "La personne s’approche encore un peu plus, tournant la poignée pour ouvrir la porte."
    E "Jason se jette derrière un placard, espérant être assez caché de la tueuse."

    scene cachette_chambre
    with dissolve

    E "Un bruit de clé dans la serrure de la chambre se fait entendre. Une voix résonne à l'intérieur du téléphone. La police nous demande notre emplacement."
    E "Jason se jette sous le lit, espérant être assez caché de la tueuse."

    menu:
        "Se taire":
            E "La personne entre dans la chambre, fouillant les meubles, tournant en rond."
            E "Elle a le souffle court, des mouvements erratiques."
            E "La personne entre dans la chambre, fouillant les meubles, tournant en rond"
            E "Elle a le souffle court, des mouvements erratiques"
            E "Puis soudain, plus rien. Plus un geste, plus un souffle."
            menu:                    
                "Sortir de la cachette pour fuir":
                    A "Ah! Jason tu m'as fait peur!"
                    J "Moi aussi, Anna"
                    jump findingAnna
                "Rester caché":
                    jump findingAnna
        "Dire l'adresse":
            J_murmure "Si vous m’entendez…"
            J_murmure "Je suis au 18 Stanway… Road. Venez vite, par pitié venez vite !"
            jump findingAnna

label findingAnna:

    scene chambre_pnc_objet
    with dissolve

    A "Ah ! Jason tu m'as fait peur!"
    E "Anna se trouve dans la chambre. Elle tremble encore de peur."
    J_murmure "Putain, tu m'as foutu la frousse!"
    J "Je… Je ne savais pas où tu étais passée…"
    A "Jason, t’es là ?"
    J_murmure "Anna ? Tu m’as fait peur !"
    J "Oh mon dieu, c’est toi ! Je… Je ne savais pas où tu étais passée…"
    A "Je… j’ai vu la tueuse… Bordel Jason, tu aura vu son couteau… Pourquoi nous ?"

E "Un bruit sourd résonne à l'intérieur de la maison."
N_shout "Annaaaaaa ! Je sais que t’es dans la maison !"
N_shout "Oooooooh… Aahh… Viens là !"
J "C’était quoi ça ?"
A "Elle arrive ! Oh mon dieu, elle arrive !"
jump kimHurlement_Anna
jump kimHurlement

label kimHurlement:

    if (compagnie_Bryan):
        jump kimHurlement_Bryan
    else:
        jump kimHurlement_seul

label kimHurlement_Anna:
    E "Un cri aigu retentit dans la maison."
    A "Kim ! Nom de Dieu."
    J_shout "T’as pas intérêt à la toucher !"
    E "Vous courez en direction de la cave avec Anna, où vous aviez laissé Kim blessée."

    scene entree_nuit
    with dissolve

    E "Vous retrouvez Kim, seule, ensanglantée, sur le sol du hall d'entrée."

jump arcSauvetageKim

label kimHurlement_Bryan:
    E "Un cri aigu retentit dans la maison."
    B "Kim ! Nom de Dieu."
    J_shout "T’as pas intérêt à la toucher !"
    E "Vous courez en direction de la cave avec Bryan, où vous aviez laissé Kim blessée."

    scene entree_nuit
    with dissolve

    E "Vous retrouvez Kim, seule, ensanglantée, sur le sol du hall d'entrée."

jump arcSauvetageKim

label kimHurlement_seul:
    E "Un cri aigu retentit dans la maison."
    J "Kim ! Nom de Dieu."
    J_shout "T’as pas intérêt à la toucher !"
    E "Vous courez en direction de la cave, où vous aviez laissé Kim blessée."

    scene entree_nuit
    with dissolve

    E "Vous retrouvez Kim, seule, ensanglantée, sur le sol du hall d'entrée."

jump arcSauvetageKim
