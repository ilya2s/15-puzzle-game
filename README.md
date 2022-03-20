# tp1-ift1015 - Jeu de Taquin

Jeu de Taquin en python dans le cadre du cours IFT1015

## 1. Introduction

Le jeu se joue sur une grille carrée de tuiles. Chaque tuile est une petite image de 16x16 pixels. Voici un exemple de ce qui pourrait être affiché au début du jeu :

Avant d'expliquer le fonctionnement du jeu il faut comprendre comment l'affichage des tuiles se fait.

Sur le plan matériel, l'affichage d'images (et aussi de texte) à l'écran d'un ordinateur se fait en contrôlant le contenu d'une grille rectangulaire de pixels carrés. La grille a une largeur et hauteur qui dépend de la résolution de l'écran (par exemple 1600 colonnes par 1200 rangées). Chaque pixel a une coordonnée X-Y qui indique sa position dans la grille. Par convention, le pixel le plus en haut à gauche a la coordonnée (0,0) et le pixel le plus en bas à droite a la coordonnée (largeur-1,hauteur-1).

Chaque pixel est une cellule qui a une couleur spécifiée par ses composantes rouge, vert et bleu, qui sont des nombres entiers entre 0 et une valeur maximale qui dépend de la configuration de l'écran (par exemple 15, 255 ou 65535). Les trois composantes sont combinées pour déterminer la couleur finale du pixel. Nous utiliserons la valeur 15 comme valeur maximale. Plus une composante est élevée (jusqu'au maximum de 15), plus cette couleur sera présente dans la couleur finale du pixel. On peut donc se servir d'un enregistrement à trois champs pour représenter une couleur. Nous utiliserons les noms de champs r, g et b (pour red, green et blue). Voici comment on pourrait définir quelques couleurs :

    noir  = struct(r= 0, g= 0, b= 0)
    blanc = struct(r=15, g=15, b=15)
    vert  = struct(r= 0, g=15, b= 0)
    jaune = struct(r=15, g=15, b= 0)

Sous les ordres du pilote d'écran du système d'exploitation, le processeur graphique de l'ordinateur (le GPU), stocke dans chaque pixel les composantes r, g et b nécessaires pour afficher l'image voulue. Pour faire un affichage à l'écran, un programme doit envoyer des requêtes appropriées au système d'exploitation, dont le pilote d'écran traduira ces requêtes en commandes pour le GPU.

Dans l'environnement codeBoot l'écran graphique est simulé par une fenêtre qui apparait à la droite de la console (au même endroit que la fenêtre de dessins tortue, mais les dessins ne se font pas de la même façon). Chaque pixel de cet écran simulé peut être modifié pour y afficher une certaine couleur. Quelques procédures et fonctions prédéfinies de codeBoot qui contrôlent cet écran graphique simulé seront utiles pour ce travail :

    setScreenMode(largeur, hauteur) : Conceptuellement, cette procédure établit la résolution de l'écran (comme une requête de changement de mode graphique envoyée au GPU). Dans codeBoot, cette opération est simulée en ajoutant à la droite de la console une grille de la largeur et de la hauteur demandées. Chaque carré de la grille représente un pixel de l'écran simulé. Pour faciliter la visualisation de l'écran simulé et le débogage, dans les faits un pixel simulé est un carré de quelques vrais pixels et il y a une bordure grise autour des pixels simulés afin de bien les distinguer. S'il y a un grand nombre de pixels la bordure grise disparait pour qu'on voit uniquement les pixels simulés.
    getScreenWidth() : Cette fonction retourne la largeur de l'écran simulé (le nombre de colonnes de pixels).
    getScreenHeight() : Cette fonction retourne la hauteur de l'écran simulé (le nombre de rangées de pixels).
    setPixel(x, y, couleur) : Change le contenu du pixel à la coordonnée (x,y) de l'écran simulé pour que sa couleur soit couleur (une structures avec trois champs r, g et b contenant des entiers entre 0 et 15).
    getMouse() : Retourne un enregistrement indiquant la position du curseur de souris et l'état du bouton de souris. L'enregistrement contient les champs : x, y, button, shift, ctrl et alt. Les champs x et y indiquent la coordonnée du pixel de l'écran simulé qui est pointé par le curseur de souris. Le champ button est un entier qui indique quel bouton de souris est présentement appuyé (0 = aucun bouton, 1 = bouton principal, 2 = bouton secondaire). Les champs shift, ctrl et alt ont une valeur booléenne qui indique si les touches Shift, Control, et Alt étaient appuyée au moment du dernier clic de bouton.
    exportScreen() : Cette fonction retourne un texte qui encode le contenu de tous les pixels de l'écran créé par setScreenMode. Chaque pixel est représenté par un texte de 3 caractères donnant la valeur de chaque composante RGB en hexadécimal, préfixé par le caractère #. Le caractère de fin-de-ligne \n sépare les rangées de pixels. Cette fonction est principalement utile pour écrire des tests unitaires. Voici un exemple d'utilisation à la console de codeBoot :

        >>> setScreenMode(4,3)
        >>> setPixel(2, 1, struct(r=15, g=8, b=1))
        >>> exportScreen()
            '#000#000#000#000\n#000#000#f81#000\n#000#000#000#000'
        >>> print(exportScreen())
            #000#000#000#000
            #000#000#f81#000
            #000#000#000#000

Dans le processus de développement, pour faciliter le débogage, il est conseillé d'utiliser une faible résolution d'écran simulé pour bien voir chaque pixel. C'est également utile pour faire des tests unitaires.

## 2. Jeu

Le jeu de taquin est un jeu de réflexion qui consiste à déplacer par "glissement" des tuiles carrées pour les placer dans un ordre précis. Si la grille est N par N alors il y a N*N-1 tuiles numérotées de 1 à N*N-1 et une des cases de la grille est vide. Le jeu débute avec les N*N-1 tuiles dans un état de désordre. Le joueur peut uniquement glisser une (ou des) tuile(s) vers la case vide pour changer la position de ces tuiles et indirectement de la case vide. Le jeu se termine lorsque les tuiles sont en ordre numérique de gauche à droite et haut en bas avec la case vide en bas à droite de la grille.

Le joueur doit cliquer le bouton de souris sur une tuile qui est sur la même rangée ou colonne que la case vide (autrement le clic n'a aucun effet). La tuile cliquée sera déplacée vers la case vide par glissement, ce qui entraine aussi le déplacement des tuiles entre la case vide et la tuile cliquée s'il y en a. Pour simplifier, ce glissement doit se faire d'un seul coup (sans animation).

Par exemple, voici la grille de tuiles dans l'état initial du jeu (tuiles en désordre) à gauche, et à droite l'état du jeu après avoir cliqué sur la tuile numérotée 13 :
   

Lorsque le jeu se termine un message est affiché avec alert pour féliciter le joueur. Après un clic sur OK une nouvelle partie recommence automatiquement avec un nouveau placement aléatoire des tuiles.

Le programme doit utiliser la fonction random pour placer les tuiles en désordre au début d'une partie. Il est important de noter que les tuiles ne sont pas positionnées complètement aléatoirement car certaines configurations de tuiles sont impossibles à résoudre. Vous devez utiliser l'algorithme expliqué ci-dessous pour faire le placement initial (donc un placement invalide mènera à une perte de points).
3. Spécification

Vous devez concevoir et coder les procédures spécifiées ci-dessous en respectant le nom spécifié exactement pour qu'on puisse les tester plus facilement. Vous aurez sûrement à définir des fonctions et procédures auxiliaires (utilisez des noms appropriés de votre choix en camelCase). Votre code doit être dans un fichier nommé taquin.py.

Nous vous fournissons sur Studium le fichier tuiles.py qui contient les définitions des images des 16 tuiles possibles (case vide et les 15 nombres 1 à 15). Ce fichier contient la déclaration de 2 variables globales ayant comme valeur des tableaux : colormap et images. Le tableau colormap contient la définition des 5 couleurs qui sont utilisées dans les images de tuiles. Chaque élément du tableau colormap est une structure avec des champs r, g et b spécifiant la couleur. Le tableau images contient 16 éléments, chacun représentant une image. Une image est un tableau de 16 éléments, chaque élement représente une rangée de pixels de l'image et est un tableau contenant 16 entiers de 0 à 4 qui indiquent l'index de la couleur dans le tableau colormap. Chaque image contient donc 256 pixels (16x16 pixels). Les pixels sont disposés de haut en bas et de gauche à droite. Le tableau images est donc un tableau à 3 dimensions.

Le fichier tuiles.py doit être copié dans codeBoot (avec un glisser-déposer), et votre fichier taquin.py doit importer le fichier de tuiles avec l'énoncé import tuiles pour avoir accès à ses définitions. Dans taquin.py vous pourrez par la suite faire tuiles.images et tuiles.colormap pour lire le contenu des variables définies dans tuiles.py.

## 3.1 Procédure afficherImage(x, y, colormap, image)

Cette procédure affiche à la coordonnée (x,y) de la grille de pixels l'image indiquée par le paramètre image qui utilise des couleurs définies par le paramètre colormap. Ce dernier doit être un tableau de tableaux d'entiers entre 0 et la longueur du tableau colormap dont les éléments sont des structures avec des champs r, g et b spécifiant des couleurs. La longueur du tableau image est la hauteur de l'image (en nombre de rangées de pixels) et la longueur des éléments du tableau image est la largeur de l'image (en nombre de colonnes de pixels). Les entiers contenus dans l'image sont donc des entiers qui sont l'index de la couleur du pixel dans le tableau colormap. L'image n'a pas nécessairement une taille 16x16 (en d'autres termes c'est une procédure générale pour afficher des images de n'importe quelle taille contenant n'importe quelles couleurs).

## 3.2 Procédure afficherTuile(x, y, tuile)

Cette procédure affiche à l'écran à la coordonnée (x,y) de la grille de tuiles l'image de la tuile indiquée par le paramètre tuile (un entier de 0 à 15). Cette procédure doit appeler la procédure afficherImage.

## 3.3 Fonction attendreClic()

Cette fonction attend que le bouton de souris soit relaché, puis attend que le bouton de souris soit appuyé. La fonction retourne un enregistrement contenant les champs x et y qui indiquent la coordonnée de la tuile sur laquelle le joueur a cliqué.

L'implantation de cette fonction doit se faire avec une boucle qui fait appel à la fonction getMouse et la fonction sleep avec un paramètre égal à 0.01 . L'appel à la fonction sleep permet de ne pas demander trop souvent l'état de la souris car ça pourrait gaspiller inutilement l'énergie (et chauffer le processeur).

## 3.4 Fonction permutationAleatoire(n)

La fonction permutationAleatoire retourne un nouveau tableau de longueur n contenant les entiers de 0 à n-1 dans un ordre aléatoire. Un algorithme simple pour le faire consiste à créer un tableau contenant les entiers de 0 à n-1. Puis pour chaque index i de ce tableau choisir aléatoirement un index j ≥ i et échanger les éléments aux indices i et j.

## 3.5 Fonction inversions(tab, x)

La fonction inversions prends deux paramètres : un tableau tab de longueur n contenant les entiers de 0 à n-1 (dans un ordre quelconque), et un entier x entre 1 et n-1. La fonction retourne le nombre d'éléments dans le tableau tab qui suivent la valeur x et qui sont une des valeurs de 1 à x-1. Le nombre retourné indique à quel point la valeur x n'est pas bien ordonnée dans le tableau tab. En effet pour un tableau tab contenant des valeurs ordonnées la fonction inversions retournera 0 pour toute valeur x (c'est-à-dire aucune valeur n'est "inversée").

## 3.6 Fonction soluble(tab)

La fonction soluble prends comme unique paramètre un tableau tab de longueur n contenant les entiers de 0 à n-1 (dans un ordre quelconque). La longueur de tab doit être un carré parfait. La valeur de retour est un booléen qui indique si cette séquence de tuiles placées sur la grille de gauche à droite et de haut en bas est une configuration du jeu qui a une solution. L'élément du tableau contenant la valeur 0 indique la position de la case vide. Donc l'appel soluble([3,5,6,7,10,14,11,9,4,13,2,0,8,1,12,15]) retourne True car cette séquence correspond à la configuration des tuiles donnée dans l'introduction qui a une solution.

Pour calculer le résultat de la fonction il n'est pas nécessaire de trouver la solution. Il y a un algorithme simple qui permet de le déterminer directement. Si r est la rangée où se trouve la case vide (la rangée du haut correspond à r=1), alors il y a une solution si la somme de r et inversions(tab,x) pour tous les x entre 1 et n-1 donne un nombre pair. Pour la configuration de tuiles donnée dans l'introduction on a que :

    3 = r
    0 = inversions(tab,1)
    1 = inversions(tab,2)
    2 = inversions(tab,3)
    2 = inversions(tab,4)
    3 = inversions(tab,5)
    3 = inversions(tab,6)
    3 = inversions(tab,7)
    1 = inversions(tab,8)
    4 = inversions(tab,9)
    5 = inversions(tab,10)
    5 = inversions(tab,11)
    0 = inversions(tab,12)
    4 = inversions(tab,13)
    8 = inversions(tab,14)
    0 = inversions(tab,15)
 ----
   44 = somme (qui est un nombre pair donc soluble)

## 3.7 Fonction initial(largeur)

La fonction initial prends comme unique paramètre un entier positif largeur qui est la largeur (et hauteur) de la grille de jeu. La fonction retourne un tableau de longeur largeur*largeur contenant les entiers de 0 à largeur*largeur-1 qui correspond à une configuration de tuile qui est soluble.

L'algorithme suivant permet de trouver une configuration soluble. On fait un appel de permutationAleatoire(largeur*largeur) pour générer une configuration candidate c. Si soluble(c) est vrai alors on a trouvé une configuration soluble. Sinon on tente avec une nouvelle permutation aléatoire jusqu'à ce qu'on trouve une configuration soluble. Généralement il faut un petit nombre de tentatives pour trouver une configuration acceptable.

## 3.8 Procédure taquin(largeur)

Cette procédure est la procédure principale du jeu. L'unique paramètre largeur indique la largeur de la grille et est un entier entre 2 et 4. Vous devez faire le codage de votre programme pour qu'il n'y ait pas de limite supérieure au paramètre largeur, mais pour le TP1 une valeur de largeur plus grande que 4 est interdite car il y a seulement 16 images de tuiles définies dans tuiles.py.

La procédure taquin s'occupe du déroulement du jeu. L'état initial est déterminé par un appel à la fonction initial puis cette configuration de tuiles est affichée. Le jeu réagit aux clics du joueur et déplace les tuiles en conséquence. Lorsque toutes les tuiles sont en ordre avec la case vide dans le coin inférieur droit, alors le programme félicite le joueur avec un message affiché avec alert puis recommence une nouvelle partie.

Votre programme ne doit pas faire un appel à la procédure taquin car c'est le correcteur qui le fera. Pour votre phase de test, il est suggéré d'utiliser au tout début une petite grille, par exemple 2x2. Ça permet de trouver les erreurs plus facilement et de tester la fin de partie sans avoir à passer un temps fou à cliquer des tuiles. L'utilisation d'une petite grille peut également être utile pour faire des tests unitaires.

## 3.9 Procédure testTaquin()

Cette procédure effectue les tests unitaires des procédures afficherImage et afficherTuile et les fonctions permutationAleatoire, inversions, soluble et initial. Pour tester les procédures afficherImage et afficherTuile il faudra utiliser la fonction exportScreen afin de pouvoir tester avec assert que le résultat est bon. Faites des appels à setScreenMode avec des petits entiers (pas plus grands que 32) pour ne pas avoir des tests unitaires trop longs. N'oubliez pas que vous pouvez briser les longs textes litéraux sur plusieurs lignes en utilisant le caractère d'échappement \ à la fin des lignes. Vous devez avoir de 5 à 10 tests par fonction et procédure. La procédure testTaquin() peut contenir des tests unitaires pour les autres abstractions procédurales que vous avez définies, mais ce n'est pas requis (utilisez votre jugement sur la pertinence de faire des tests de ces abstractions procédurales).

Votre programme doit faire un appel à la procédure testTaquin pour lancer les tests. Aucun des tests ne doit faire une interaction avec l'utilisateur ni afficher quoi que ce soit à la console (sauf la grille de pixels bien entendu). 
