## TLA+ (Leslie Lamport) — histoire

- 1999 : conçu par Leslie Lamport (prix Turing 2013) comme langage formel pour modéliser et spécifier les systèmes concurrents et distribués.
- 2002 : publication du livre fondamental "Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers".
- 2014 : publication d’un article marquant d’Amazon Web Services (AWS) révélant l’utilisation de TLA+ pour concevoir des services critiques comme S3 et DynamoDB.
- 2019 : adoption par Microsoft pour vérifier la cohérence des protocoles distribués Azure et Cosmos DB.
- Aujourd’hui : standard mondial de la spécification formelle de protocoles de consensus et d’architectures distribuées.

## TLA+ (Leslie Lamport) — utilité

- Langage de modélisation formelle basé sur la logique temporelle des actions (Temporal Logic of Actions) et la théorie des ensembles.
- Permet de décrire rigoureusement le comportement d’un système distribué avant d’écrire la moindre ligne de code applicatif.
- Fournit le vérificateur de modèles TLC (Model Checker) explorant exhaustivement tous les états possibles pour trouver les bugs de concurrence rares.
- Détecte infailliblement les interblocages (deadlocks), les corruptions de données distribuées et les violations de vivacité (liveness).
- Utilisé pour concevoir des bases de données distribuées, des algorithmes de consensus (Raft, Paxos) et des puces électroniques.

## TLA+ (Leslie Lamport) — ressources

- Site officiel : [https://lamport.azurewebsites.net/tla/tla.html](https://lamport.azurewebsites.net/tla/tla.html)
- Dépôt GitHub : [https://github.com/tlaplus/tlaplus](https://github.com/tlaplus/tlaplus)
