
E "Alors que Jason regarde dans le téléphone pour appeler les secours, un message attire son attention."
J_think "Attends, qu’est-ce que c’est que ça…"
J_think "Kim ? Mais qu’est-ce que ?"
E "“Tu dis qu j’ai que de la gueule ms le jour ou on va te retrouver crevée ds le canal tu rigolera plus, sale chienne. Essaye même pas de te plaindre à quelquun, personne écoutera ta sale gueule de pute.”"
E "“Alors vas y continu de faire la meuf quand y a du monde autour, je sais que tout ce que tu veux cest te tirer une balle pour arreter ta vie de merde”"

if (go_with_Anna == True):
    jump policecallAnna
else:
    jump policeCallAlone

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

    menu:
        "Parler de la tueuse":
            J "Si vous nous entendez, on est en train de se faire attaquer ! Allô ?"
        "Dire que vous êtes en danger":
            J "On est en danger, venez vite !"
        "Réclamer de l'aide pour Kim":
            J "Mon amie est blessée, on a besoin d’aide, s’il vous plaît !"

    E "Aucune réponse"
    A "Donne leur l'adresse"
    J "On est au 18 Stanway Road! Dépêchez vous!"

    play sound "audio/Sounds/Phone Off.mp3"

    A "Ils arrivent quand?"
    J "Je ne sais pas. Le téléphone adu mal à passer, j'espère qu'ils ont réussi à m'entendre."

    N_shout "Anna ! Je sais que t’es dans la maison !"
    N_shout "Oooooooh… Aahh… Viens là !"

    J "C’était quoi ça ?"
    A "Elle arrive ! Oh mon dieu, elle arrive !"

    play sound "audio/Sounds/Cri Kim2.mp3"
    E "Un cri aigu retentit dans la maison."

label policeCallAlone:

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
    E "Jason se jette sous le lit, espérant être assez caché de la tueuse."

    menu:
        "Se taire":
            E "La personne entre dans la chambre, fouillant les meubles, tournant en rond"
            E "Elle a le souffle court, des mouvements erratiques"
            E "Puis soudain, plus rien. Plus un geste, plus un souffle."
            menu:                    
                "Sortir de la cachette pour fuir":
                    A "Ah! Jason tu m'as fait peur!"
                    J "Moi aussi, Anna"
                "Rester caché":
                    jump findingAnna
        "Dire l'adresse":
            J_murmure "Si vous m’entendez…"
            J_murmure "Je suis au 18 Stanway… Road. Venez vite, par pitié venez vite !"
            jump findingAnna

label findingAnna:
    A "Jason, t’es là ?"
    J_murmure "Anna ? Tu m’as fait peur !"
    J "Oh mon dieu, c’est toi ! Je… Je ne savais pas où tu étais passée…"
    A "Je… j’ai vu la tueuse… Bordel Jason, tu aura vu son couteau… Pourquoi nous ?"

N_shout "Annaaaaaa ! Je sais que t’es dans la maison !"
N_shout "Oooooooh… Aahh… Viens là !"
J "C’était quoi ça ?"
A "Elle arrive ! Oh mon dieu, elle arrive !"
jump kimHurlement

label kimHurlement:
    E "Un cri aigu retentit dans la maison."
    J "Kim ! Nom de Dieu."
    J_shout "T’as pas intérêt à la toucher !"
    E "Vous courez en direction de la cave avec Anna, où vous aviez laissé Kim blessée."
    E "Vous retrouvez Kim, seule, ensanglantée, sur le sol de l’entrée."


jump arcSauvetageKim