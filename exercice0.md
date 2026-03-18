# Exercice 0



## Famille A - Métriques de nouveauté lexicale et 

> NB : deux grandes familles :
> - une plus grande de diversité de vocabulaire pure (polysémie des mots non prise en compte)
> - mesure 

### Type-Token Ratio (TTR)

6. **Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?**  
TTR = |V| / N  (V = vocabulaire unique, N = tokens totaux)  
→ Dimension : **nouveauté lexicale (diversité)**  
Mesure la diversité lexicale et donc une forme de nouveauté sémantique superficielle.  
Ne capture ni la créativité conceptuelle, ni la structure syntaxique, ni la cohérence globale.

7. **Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.**  
Objectif : vérifier que TTR corrèle avec la nouveauté perçue.

- Sélectionner plusieurs tâches contrôlées :
  - traduction (faible créativité attendue)
  - paraphrase
  - génération créative (histoires, poésie)

- Pour chaque tâche :
``` pour texte in corpus :
    output = LLM(texte)
    TTR = calcul_TTR(output)
    liste_TTR.append(TTR)
```

8.	**Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).**

*faux négatifs* : une très longue réponse, un roman \
*faux positifs* : une réponse très courte, un seul mot


- En parallèle :
    - faire annoter les sorties par des humains (score de nouveauté perçue)
    - calculer la corrélation (Spearman/Pearson) entre TTR et jugements humains

- Contrôle : normaliser la longueur des textes (ou comparer par tranches de longueur)

Validation réussie si :
→ corrélation positive significative entre TTR et nouveauté perçue

8. **Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).**

- Faux négatifs :
texte long et riche mais avec répétitions nécessaires (roman, narration cohérente)
- texte technique utilisant un vocabulaire spécialisé mais répétitif

- Faux positifs :
texte très court (1–5 mots)
ou liste aléatoire de mots sans cohérence ("chat lune fractale cuivre")


---

### TTR corrigé (MATTR)

6. **Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?**  
→ Dimension : **nouveauté lexicale robuste à la longueur**  
MATTR (Moving-Average TTR) mesure la diversité lexicale localement, en réduisant le biais lié à la longueur du texte.  
Elle capture mieux la variation lexicale continue, mais reste limitée à la surface lexicale.

7. **Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.**

Objectif : montrer que MATTR est plus stable et plus fiable que TTR.

- Générer des textes de longueurs variées pour une même tâche
- Calculer TTR et MATTR :
```
pour texte in corpus :
    TTR = calcul_TTR(texte)
    MATTR = calcul_MATTR(texte, window=k)
```


- Étapes :
    - mesurer la variance de TTR vs MATTR selon la longueur
    - corréler MATTR avec jugements humains de nouveauté
    - comparer MATTR vs TTR (robustesse + corrélation)

Validation :
→ MATTR doit être :
    - moins sensible à la longueur
    - mieux corrélé à la nouveauté perçue

8. **Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).**

- Faux négatifs :
    - créativité conceptuelle avec vocabulaire stable (ex : idées originales exprimées simplement)
    - textes stylistiquement répétitifs mais conceptuellement innovants

- Faux positifs :
    - variation lexicale artificielle (synonymes forcés)
    - texte incohérent mais lexicalement diversifié


---

### N-gramme Rarity Score

6. **Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?**  
→ Dimension : **originalité statistique (syntaxique + sémantique locale)**  
Mesure la rareté des séquences de n-grammes par rapport à un corpus de référence.  
Capture la surprise statistique, donc une forme d’originalité formelle.

7. **Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.**

- Construire un corpus de référence (ex : Wikipédia, Common Crawl)
- Pour chaque output :
```
    extraire n-grammes
    calculer fréquence dans corpus_ref
    score = moyenne(-log(freq))
```

- Expérimentation :
    - comparer : outputs standards(traduction, résumé) et outputs créatifs (poèmes, histoires absurdes)

- Évaluation :
    - annotation humaine de l’originalité
    - corrélation avec le score de rareté

- Test critique : injecter du bruit aléatoire pour vérifier que le score augmente (sanity check)

**Validation :
→ score élevé pour textes perçus comme originaux mais cohérents**


8. **Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).**

- Faux positifs :
    - texte incohérent ou bruité ("zxqv blargh syntaxis rupture")
    - erreurs grammaticales rares

- Faux négatifs :
    - idées très originales exprimées avec phrases communes
    - reformulations créatives mais avec n-grammes fréquents


---

### Self-BLEU

6. **Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?**  
→ Dimension : **diversité inter-générations (variété)**  
Self-BLEU mesure la similarité entre plusieurs outputs du modèle.  
Faible Self-BLEU = forte diversité → proxy de créativité exploratoire.

7. **Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.**

- Pour un même prompt :
    ```
    outputs = [LLM(prompt) for i in range(K)]
    pour chaque output_i :
    BLEU_i = BLEU(output_i, outputs \ {output_i})
    self_bleu = moyenne(BLEU_i)
    ```


- Expériences :
    - varier température / top-k
    - comparer tâches :
    - factuelles (faible diversité attendue)
    - créatives (forte diversité attendue)

- Validation :
    - corréler diversité perçue (annotations humaines) avec Self-BLEU
    - vérifier que :
    - haute température → Self-BLEU bas

8. **Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).**

- Faux positifs (diversité ≠ créativité) :
    - outputs incohérents mais différents
    - réponses aléatoires

- Faux négatifs :
    - créativité dans une structure stable (ex : haïkus avec même forme)
    - réponses différentes mais partageant beaucoup de n-grammes


---

### Distance d'embedding

6. **Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?**  
→ Dimension : **nouveauté sémantique / distance conceptuelle**  
Mesure la distance entre embeddings (entre outputs ou vs corpus de référence).  
Capture la différence de sens plutôt que de surface.

7. **Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.**

- Encoder textes avec un modèle d’embedding (ex : sentence-transformers)

- Deux configurations :
1. Distance à un corpus de référence
2. Distance entre outputs générés
```
    emb_output = encode(output)
    emb_ref = encode(corpus_ref)
    score = distance(emb_output, centroid(emb_ref))
```


- Expérimentation :
    - comparer tâches (traduction vs génération créative)
    - annotations humaines de nouveauté sémantique

- Tests :
    - paraphrases → faible distance attendue
    - idées originales → grande distance

**Validation :
→ corrélation entre distance et nouveauté perçue**

8. **Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).**

- Faux positifs :
    - texte hors sujet (grande distance mais pas créatif)
    - incohérence sémantique

- Faux négatifs :
    - créativité locale (jeu de mots, style) sans changement sémantique global
    - innovations subtiles proches du sens initial

---

## Famille B

6.	Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?
7.	Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.
8.	Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).
9.	Proposez une pondération justifiée pour les combiner en un Creativity Index (CI). Validez-la en la corrélant au compar:IA Creative Score (colonne creative / conv_creative_*).
---
## Famille C
6.	Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?
7.	Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.
8.	Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).
9.	Proposez une pondération justifiée pour les combiner en un Creativity Index (CI). Validez-la en la corrélant au compar:IA Creative Score (colonne creative / conv_creative_*).
---


## Famille D

6.	Quelle dimension théorique de la créativité cette métrique opérationnalise-t-elle ?
7.	Proposez un protocole expérimental pour valider que la métrique mesure bien ce qu’elle prétend mesurer.
8.	Identifiez au moins deux cas où la métrique échouerait (faux positifs et faux négatifs).
9.	Proposez une pondération justifiée pour les combiner en un Creativity Index (CI). Validez-la en la corrélant au compar:IA Creative Score (colonne creative / conv_creative_*).