## Datalog — histoire

- 1977–1980 : formalisé par des chercheurs en bases de données déductives comme sous-ensemble déclaratif de Prolog sans fonctions complexes.
- Années 1990 : standardisation théorique pour l’analyse statique de programmes et l’optimisation de requêtes récursives.
- 2010+ : résurgence industrielle majeure avec le moteur de base de données Datomic (Rich Hickey) et l’outil d’analyse de sécurité GitHub CodeQL.
- 2020+ : moteur sous-jacent des bases de données de graphes modernes et des moteurs d’autorisation cloud (Open Policy Agent, Oso).
- Aujourd’hui : technologie de pointe pour l’analyse de vulnérabilités logicielles et l’audit de code automatisé.

## Datalog — utilité

- Langage de requête logique déclaratif et totalement décidable (terminaison toujours garantie sur données finies).
- Prend en charge nativement les requêtes récursives complexes (fermetures transitives, graphes de dépendances).
- Moteur de requêtage de sécurité officiel de GitHub CodeQL pour détecter automatiquement des failles de sécurité dans le code source.
- Utilisé pour les bases de données immuables orientées faits (Datomic) et les moteurs de déduction de règles métier.
- Permet d’exprimer des règles d’inférence logique avec des performances d’exécution massivement parallélisables.

## Datalog — ressources

- Site officiel : [https://codeql.github.com](https://codeql.github.com)
- Dépôt GitHub : [https://github.com/souffle-lang/souffle](https://github.com/souffle-lang/souffle)
