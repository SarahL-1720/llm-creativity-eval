# Exercice 0



## Famille A
6.	Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?
7.	Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.
8.	Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).
9.	Proposez une pondération justifiée pour les combiner en un Creativity Index (CI). Validez-la en la corrélant au compar:IA Creative Score (colonne creative / conv_creative_*).
---

## Famille B

### 6. Dimension théorique de la créativité capturée

Chaque métrique peut être reliée à une dimension classique de la créativité issue de la psychologie cognitive :

- **Perplexité interne**
  - Dimension : *Fluidité*
  - Interprétation : capacité à produire un texte grammaticalement correct et fluide
  - Limite : ne capture pas la créativité en tant que telle, seulement une condition de base

- **Cohérence locale (LC)**
  - Dimension : *Cohérence*
  - Interprétation : continuité logique entre idées successives
  - Lien théorique : créativité comme exploration structurée de l’espace des idées

- **ROUGE-L (vs consigne)**
  - Dimension : *Adéquation*
  - Interprétation : respect de la consigne
  - Lien théorique : une production créative doit être adaptée, pas seulement nouvelle

- **BERTScore**
  - Dimension : *Richesse sémantique*
  - Interprétation : qualité et profondeur du contenu
  - Lien théorique : créativité comme recombinaison sémantique riche

---

### 7. Protocole expérimental de validation

#### Objectif
Valider que chaque métrique mesure bien la dimension qu’elle prétend capturer.

#### 1. Construction du dataset

Créer un corpus contrôlé avec 4 conditions :

| Condition | Description |
|----------|------------|
| A | Créatif + cohérent |
| B | Créatif + incohérent |
| C | Non créatif + cohérent |
| D | Non créatif + incohérent |

---

#### 2. Annotation humaine

- Minimum 3 annotateurs
- Échelles (1–5) :
  - créativité
  - cohérence
  - pertinence
- Calcul de l’accord inter-annotateurs (κ ou α)

---

#### 3. Calcul des métriques

Pour chaque texte :
- Perplexité (PP)
- Cohérence locale (LC)
- ROUGE-L
- BERTScore

---

#### 4. Analyse statistique

- Corrélations (Pearson / Spearman)
- Régression :
  - prédire les scores humains à partir des métriques
- Analyse factorielle :
  - vérifier si les métriques capturent des dimensions distinctes

---

#### 5. Tests d’ablation

- Retirer une métrique du modèle
- Observer la baisse de performance

---

#### Critères de validation

- Corrélation significative avec la dimension cible
- Faible corrélation avec dimensions non pertinentes
- Robustesse sur différents types de textes

---

### 8. Cas d’échec (faux positifs / faux négatifs)

#### Perplexité

- Faux positifs :
  - texte fluide mais banal ou cliché
- Faux négatifs :
  - texte créatif avec structure atypique (ex : poésie expérimentale)

---

#### Cohérence locale (LC)

- Faux positifs :
  - texte répétitif mais cohérent
- Faux négatifs :
  - texte créatif avec ruptures narratives intentionnelles

---

#### ROUGE-L

- Faux positifs :
  - copie ou paraphrase du prompt
- Faux négatifs :
  - réponse pertinente mais reformulée de manière originale

---

#### BERTScore

- Faux positifs :
  - texte sémantiquement proche mais peu original
- Faux négatifs :
  - idées nouvelles ou métaphores mal capturées par les embeddings

---

### 9. Proposition d’un Creativity Index (CI)

#### Formule

CI basé sur une combinaison pondérée :

CI = 0.15 × (1 − norm_PP) + 0.25 × LC + 0.20 × ROUGE-L + 0.40 × BERTScore

---

#### Justification des poids

- **BERTScore (0.40)** :
  - capture la richesse sémantique, plus le vocabulaire est riche plus l'espace des idées est grand. Dimension centrale de la créativité

- **Cohérence locale (0.25)** :
  - garantit la structure du texte

- **ROUGE-L (0.20)** :
  - assure le respect de la consigne. Si le respect de la consigne est trop stricte, cela nuit à la créativité

- **Perplexité (0.15)** :
  - nécessaire

---

#### Normalisation

- Toutes les métriques sont ramenées dans [0,1]
- Perplexité inversée :
  - (1 − norm_PP)

---

#### Validation empirique (compar:IA)

##### Protocole

1. Calculer le CI pour chaque réponse
2. Extraire les scores humains :
   - `creative`
   - `conv_creative_*`
3. Tester :

- Corrélation de Spearman entre CI et scores humains
- Régression linéaire

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