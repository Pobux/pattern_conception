#Strategy pattern
Le pattern "Strategy" permet de :

1. Encapsulé différentes familles d'algorithme
2. Gérer plusieurs comportements qui peuvent ou changeront dans le temps
3. S'adapter à une utilisation du client dynamiquement

Vous utilisez le pattern "Strategy" lorsque certains comportements évolueront ou changeront à travers le temps.

#Symptômes
1. Une classe abstraite comporte des méthodes qui doivent être nullifié lorsque que certaines sous-classes en hérite.
2. Vous vous retrouvez avec une quantité importante d'interface pour chaque comportement

#Idée générale
Des familles de comportements seront encapsulées afin de composer l'élément primaire.

#Exemple
Un programme doit copier un fichier dans un dossier. Ce dossier peut être local, sur le réseau interne de l'entreprise ou sur le web.
Les comportements du programme varie en fonction de la localisation où il est appelé.

Localement : Le programme ne fait aucune modification et copie le fichier au chemin demandé
Intranet : Le programme se connecte en SSH et ensuite copie le fichier au chemin demandé
Web : Le programme envoie au serveur le fichier et c'est celui-ci qui s'occupera de gérer la copie 

#Note
Suite à la compréhension vous pouvez constater que stratégie peut modéliser des objets dynamiquement en les adaptant à la demande.
Dans ce cas-ci avec une classe ModelProgram par exemple.

Il y a des liens et des affinités avec le pattern Factory.
