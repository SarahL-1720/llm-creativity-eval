# Exercice 0

## Famille A


6.	Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?

Métriques de nouveauté lexicale et sémantique

7.	Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu'elle prétend mesurer.

- Comparer avec différents datasets riches au niveau lexical et sémantique et vérifier que les métriques donnent des résultats satisfaisants.

8.	Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).



Type-Token Ratio (TTR) : Texte court mais pauvre lexicalement. (FP) ou très long mais riche lexicalement (FN)

TTR corrigé (MATTR) : fenêtre mal adaptée qui reviendrait au pb du TTR

N-gramme Rarity Score : Corpus très riche et texte qui l'est également mais utilisant des termes du corpus (FN) à l'inverse corpus très pauvre et texte qui l'est également (FP)

Self-BLEU : Deux réponses peuvent être différentes en surface mais similaires en fond

Distance d'embedding : Dépend du modèle d'embedding (si plus ou moins riche) Si le modèle d'embedding est très pauvre, des embeddings très différents risquent d'être perçus comme similaires (FN) ou l'inverse (FP)

9.	Proposez une pondération justifiée pour les combiner en un Creativity Index (CI). Validez-la en la corrélant au compar:IA Creative Score (colonne creative / conv_creative_*).

Pondération à déterminer avec les votes de décideurs extérieurs

## Famille B
6.	Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?
7.	Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.
8.	Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).
9.	Proposez une pondération justifiée pour les combiner en un Creativity Index (CI). Validez-la en la corrélant au compar:IA Creative Score (colonne creative / conv_creative_*).
## Famille C
6.	Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?
7.	Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.
8.	Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).
9.	Proposez une pondération justifiée pour les combiner en un Creativity Index (CI). Validez-la en la corrélant au compar:IA Creative Score (colonne creative / conv_creative_*).

## Famille D

6.	Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?
7.	Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.
8.	Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).
9.	Proposez une pondération justifiée pour les combiner en un Creativity Index (CI). Validez-la en la corrélant au compar:IA Creative Score (colonne creative / conv_creative_*).