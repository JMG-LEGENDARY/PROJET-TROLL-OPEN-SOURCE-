# PROJET-TROLL-OPEN-SOURCE-
Le plus gros projet de troll par les élèves de l'esgi pour mettre gentiment à genoux win defender



explications :
    le script python main.py est le cheval de Troie, c'est lui qui va tout orchestrer à travers la class Launcher() :
        os_finder() va analyser l'os sur lequel il est installé (win 11, win 10 et pk pas linux) ainsi que les antivirus installés, puis il va appeler la fonction correspondante pour lancer le virus
        win_installer() va s'occuper d'extraire les fichiers puis de les introduire dans des répertoires cachés de windows avec les privilèges admin
        sounds() va jouer les sons au volume maximum et en boucle.
        screen() va afficher une plaque noire tout devant le reste avec pk pas un message empechant toute intéraction avec le bureau ou les applications
        regedit() va s'occuper de modifier les registres pour lancer main.py au démarrage du pc (avant même la session)
        isolation() va couper et ejecter en boucle tous les périfériques, sauf la carte son, de sorte à ne pas pouvoir intéragir à partir d'une clé externe, il devra aussi couper le wifi et le partage d'écran pour éviter les commandes SSH  
        pour le fun on peut aussi ajouter sript qui sature la mémoire et le processeur pour faire ramer le pc pour chaque essai de désactivation, mais c'est à lancer en dernier pour éviter que le virus ne se lance pas bien.
    le fichier block_keyboard.ahk va empêcher l'utilisation du clavier. ATTENTION, les raccourcis comme ctrl+alt+sup sont géré depuis le noyau et très difficilent à couper
    un fichier .bat ou en rust va devoir être appelé en premier pour virer le win defender et le gestionnaire des taches
    un autre fichier (c'est jouable en python) devra s'occuper de vérifier l'installation et devra pouvoir cloner les fichiers installés pour les réinstaller à d'autres endroits pour complexifier la désinstallation ATTENTION WINDEFENDER DEVRA ETRE DESACTIVE SINON LE PROGRAMME VA SE FAIRE DEGAGE !!!




autres fonctionnalités possibles:
    modifier la fonction du bouton power pour qu'il ne fasse rien.



# ajoutez vos idées.
Les chatbots ne sont pas autorisées (elles vont faire de la merde car c'est illégal)
Cependant, la completion de texte est autorisée pour aller plus vite du moment que c'est ce que vous alliez taper et que votre modèle tourne de préférence en local ou au moins qu'il ne soit pas censuré.
