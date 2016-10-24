#Decorator pattern
Le pattern "Decorator" permet de :

1. Met de l'avant le principe suivant : Ouvert à l'extension, fermé à la modification.
2. Ajouter au comportement d'une classe (ou de ses méthodes), avant ou après, lorsque celle-ci est appelée

Vous utilisez le pattern "Decorator" lorsque certains comportements doivent être décoré (modifié à l'exécution). 

#Symptômes
1. Vous avez une classe qui a plusieurs  
2. Vous vous retrouvez avec une quantité importante d'interface pour chaque comportement et ce nombre augmente à chaque nouvelle demande.

#Idée générale
Des familles de comportements seront encapsulées afin de composer l'élément qui les utilisera.

#Exemple
Un programme doit copier un fichier dans un dossier. Ce dossier peut être local, sur le réseau interne de l'entreprise ou sur le web.
Les comportements du programme varie en fonction de la localisation où il est appelé.

Localement : Le programme ne fait aucune modification et copie le fichier au chemin demandé

Intranet : Le programme se connecte en SSH et ensuite copie le fichier au chemin demandé

Web : Le programme envoie au serveur le fichier et c'est celui-ci qui s'occupera de gérer la copie 

#Note
Suite à la compréhension vous pouvez constater que "Strategy" peut modéliser des objets dynamiquement en les adaptant à la demande.
Dans ce cas-ci avec une classe ModelProgram par exemple.

Il y a des liens et des affinités à proposer avec le pattern Factory.
