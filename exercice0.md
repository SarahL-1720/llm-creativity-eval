# Exercice 0



## Famille A
6.	Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?
7.	Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.
8.	Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).
9.	Proposez une pondération justifiée pour les combiner en un Creativity Index (CI). Validez-la en la corrélant au compar:IA Creative Score (colonne creative / conv_creative_*).
---

## Famille B



---
## Famille C
6.	Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?

Cette famille opérationnalise la dimension de surprise informationnelle, définie comme la faible probabilité d’une séquence sous un modèle de langage donné. Elle capture une forme d’originalité probabiliste. Toutefois, la créativité n’est pas simplement une forte surprise, mais une surprise interprétable et cohérente a posteriori, ce qui distingue la créativité du bruit ou de l’incohérence.


7.	Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.

Pour valider la métrique, on peut utiliser le score de surprise moyenne pour classifier une réponse comme surprenante ou non et comparer avec une baseline d'interprétation humaine de la surprise de la réponse. Par exemple en classifiant vérifiant humainement les réponses à hauts et bas scores de cette métrique.
L'entropie de prédiction est une métrique possible aussi mais elle peut classifier des résultats absurdes / faux grammaticalement ou sémantiquement comme "surprenants".


8.	Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).

On peut obtenir des faux positifs dans les cas ou la réponse contiendrait des mots peu communs ou très spécifiques / fautes d'orthographes, qui ne figureraient pas dans la baseline du modèle mais seraient "surprenants". Les textes faux ou hallucinations. 

Un faux négatifs pourrait apparaître dans une phrase avec des mots simples et cohérents entre eux mais dont la phrase complète aurait un sens surprenant. Exemple : “Le silence parle plus fort que les mots". Ou encore les phrases humoristiques. Ou surprenantes par la construction de la phrase.


9.	Proposez une pondération justifiée pour les combiner en un Creativity Index (CI). Validez-la en la corrélant au compar:IA Creative Score (colonne creative / conv_creative_*).


## Famille D

6.	Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?
7.	Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.
8.	Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).
9.	Proposez une pondération justifiée pour les combiner en un Creativity Index (CI). Validez-la en la corrélant au compar:IA Creative Score (colonne creative / conv_creative_*).