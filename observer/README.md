#Observer pattern
Le pattern "Observer" permet de :

1. Suivre les changements ou s'inscrire aux changements d'un sujet, se désinscrire aussi. 
2. De pousser (push) les informations aux observateurs ou de tirer (pull) les informations du sujet
3. De créer une relation un à plusieurs sans se soucier de modifier du code lorsque l'on veut suivre un sujet 

Vous utilisez le pattern "Observer" lorsque certains comportements d'un sujet nécessite que des objets réagissent.
Le pattern "Observer" est souvent utilisé dans les services tranversaux. Ces services comme le nommage, la journalisation, l'authentification, la messagerie sont des services que toutes les couches (présentation, aiguilleur, métier, persistance et BD) utilisent ou pourraient utiliser.

#Symptômes
1. Une classe (le sujet) est modifié à chaque fois qu'un de ses comportements nécessite d'avertir une autre classe 
2. Ce qui doit être mis à jour nécessite crée des effets de bord sur les autres objets qui suivent cette même mise à jour. 

#Idée générale
Une relation un à plusieurs où les observeurs s'inscrivent ou se désinscrivent à un sujet.

#Exemple
Vous faites pousser des fines herbes et vous souhaitez être avertit de l'humidité en temps réel.
Trois éléments doivent réagir lorsque qu'un changement d'humidité se produit :
1. Votre siteweb
2. L'avertisseur par e-mail lorsqu'un certain seuil est atteint
3. La petite pompe qui permet d'arroser automatiquement

Il serait tentant de mettre dans le capteur d'humidité une section comme suit par exemple: 
```
if taux < TAUX_MIN :
    #avertir
    
```
Mais ce serait une erreur. Ce n'est pas le rôle du capteur que d'avertir, son rôle est d'informer en recueillant une information. Constatez aussi qu'il faudrait pour chaque nouvelle condition ajouté une condition supplémentaire d'avertissement.

#Note
Le modèle utilisé ici sera celui basé sur le "push". Ce n'est pas toujours le meilleur puisqu'on force les observeurs à gober de l'information. Ceci dit, c'est le plus simple à démontrer. La différence est que lors d'une conception "pull" la fonction `update` du sujet ne comprends aucun paramètre. Celle-ci lance seulement un signal et les observeurs décident ou non d'agir en fonction de celui-ci. La fonction `update` reste donc plus flexible. 
