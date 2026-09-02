## Koka — histoire

- 2012 : conçu par Daan Leijen chez Microsoft Research pour explorer la programmation fonctionnelle avec typage des effets.
- 2019 : introduction du compilateur vers C s’appuyant sur l’allocation mémoire par comptage de références avec réutilisation de mémoire (Perceus).
- 2021 : formalisation des gestionnaires d’effets algébriques (algebraic effect handlers) de premier ordre.
- 2023+ : référence internationale dans la recherche sur la gestion de mémoire sans ramasse-miettes conventionnel.
- Aujourd’hui : langage expérimental d’avant-garde ayant influencé OCaml 5, WebAssembly et les standards d’effets modernes.

## Koka — utilité

- Langage fortement typé doté d’un système d’inférence d’effets indiquant précisément dans la signature de chaque fonction les effets de bord produits.
- Intègre la technologie novatrice Perceus : libération automatique et déterministe de la mémoire sans pause de ramasse-miettes.
- Permet la réutilisation sur place (in-place mutation) automatique des structures de données fonctionnelles lorsque leur référence est unique.
- Fournit des gestionnaires d’effets algébriques permettant d’implémenter des coroutines, des exceptions et de l’asynchronisme de manière composable.
- Compilable vers du code C propre et hautement optimisé rivalisant en vitesse avec C++.

## Koka — ressources

- Site officiel : [https://koka-lang.github.io/koka/doc/index.html](https://koka-lang.github.io/koka/doc/index.html)
