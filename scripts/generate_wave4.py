import os

WAVE4_DB = {
    'ceylon': {
        'name': 'Ceylon',
        'histoire': [
            '2011 : dévoilé par Gavin King (créateur d’Hibernate) chez Red Hat pour corriger les faiblesses du système de types de Java.',
            '2013 : publication de la version 1.0 "Guanabara" avec compilateur vers bytecode JVM et JavaScript.',
            '2017 : transfert officiel du projet à la fondation Eclipse, devenant Eclipse Ceylon.',
            '2019+ : ses innovations sur les types d’union et d’intersection ont directement influencé TypeScript et Scala 3.',
            'Aujourd’hui : jalon majeur dans l’histoire des systèmes de types élégants pour plateformes d’entreprise.'
        ],
        'utilite': [
            'Langage orienté objet et fonctionnel fortement typé conçu pour la lisibilité et l’architecture logicielle d’équipe.',
            'Introduit un système de types basé sur la théorie des ensembles avec types d’union (A|B) et d’intersection (A&B).',
            'Élimine totalement les pointeurs nuls grâce à la gestion explicite du type Nullable (Null|T).',
            'Permet l’exécution transparente et le partage de code entre la machine virtuelle Java (JVM) et les moteurs JavaScript.',
            'Intègre un système de modules rigoureux vérifié dès la compilation avec métadonnées hermétiques.'
        ],
        'url': 'https://ceylon-lang.org',
        'badge': ('Ceylon', 'https://img.shields.io/badge/Ceylon-D9531E?style=for-the-badge&logo=eclipseide&logoColor=white', 'Langages Hybrides & Spécifiques')
    },
    'fantom': {
        'name': 'Fantom',
        'histoire': [
            '2005 : créé par Brian et Andy Frank sous le nom initial de Fan pour unifier les mondes Java et .NET.',
            '2009 : renommage en Fantom et stabilisation de l’architecture multiplateforme native.',
            '2015+ : moteur de développement des systèmes de gestion intelligente de bâtiments (Smart Buildings via SkyFoundry).',
            'Aujourd’hui : langage pragmatique conçu pour s’exécuter indifféremment sur la JVM, le CLR (.NET) et les navigateurs Web.'
        ],
        'utilite': [
            'Langage orienté objet portable conçu pour éliminer les disparités entre les plateformes d’exécution JVM et .NET.',
            'Fournit une bibliothèque standard unifiée et indépendante masquant les détails des machines virtuelles sous-jacentes.',
            'Gère les conversions de types avec un compromis élégant entre typage statique strict et typage dynamique optionnel (->).',
            'Intègre nativement l’immutabilité des objets pour garantir la concurrence sans verrous complexes.',
            'Utilisé pour les plateformes industrielles IoT, l’analyse énergétique de bâtiments et les passerelles multiplateformes.'
        ],
        'url': 'https://fantom.org',
        'badge': ('Fantom', 'https://img.shields.io/badge/Fantom-2B579A?style=for-the-badge&logo=java&logoColor=white', 'Langages Hybrides & Spécifiques')
    },
    'nemerle': {
        'name': 'Nemerle',
        'histoire': [
            '2003 : conçu à l’Université de Wrocław par Kamil Skalski, Michal Moskal, Pawel Olszta et Jacek Srebrny pour la plateforme .NET.',
            '2008 : acquisition de l’équipe de développement principale par la société de logiciels JetBrains.',
            '2012 : inspiration directe pour la conception du système de macros et d’analyseurs de code de JetBrains et de C# Roslyn.',
            'Aujourd’hui : pionnier historique de la métaprogrammation par macros avancées au sein de l’écosystème .NET.'
        ],
        'utilite': [
            'Langage multi-paradigme (objet et fonctionnel) statiquement typé s’exécutant sur le Common Language Runtime (.NET CLR).',
            'Dispose du système de macros à la compilation le plus puissant jamais conçu pour la plateforme .NET.',
            'Permet d’étendre la syntaxe du langage lui-même et de générer du code typé vérifié lors de la phase de compilation.',
            'Intègre le pattern matching expressif, les types algébriques et l’inférence complète de types à la manière d’OCaml.',
            'Garantit une interopérabilité totale et sans coût avec les bibliothèques C# et VB.NET.'
        ],
        'url': 'http://nemerle.org',
        'badge': ('Nemerle', 'https://img.shields.io/badge/Nemerle-007ACC?style=for-the-badge&logo=dotnet&logoColor=white', 'Langages Hybrides & Spécifiques')
    },
    'boo': {
        'name': 'Boo',
        'histoire': [
            '2003 : initié par Rodrigo Barreto de Oliveira pour apporter la concision et l’élégance de Python sur la plateforme Microsoft .NET.',
            '2005–2014 : intégré comme l’un des trois langages de script officiels du moteur de jeu vidéo Unity (aux côtés de C# et UnityScript).',
            '2014 : dépréciation progressive dans Unity au profit de l’unification autour de C# moderne.',
            'Aujourd’hui : langage historique ayant initié toute une génération de créateurs de jeux vidéo à la programmation sur .NET.'
        ],
        'utilite': [
            'Langage à typage statique doté d’une syntaxe claire et épurée basée sur l’indentation inspirée de Python.',
            'Dispose d’un pipeline de compilation ouvert et hautement extensible via des macros d’arbres syntaxiques (AST Macros).',
            'Permet l’écriture de DSLs (Domain-Specific Languages) personnalisés pour la configuration et la logique métier.',
            'Produit du bytecode .NET ultra-rapide sans interpréteur dynamique intermédiaire.',
            'A servi de langage d’écriture de gameplay pour de nombreux jeux vidéo indépendants et simulations 3D.'
        ],
        'url': 'https://github.com/boo-lang/boo',
        'badge': ('Boo', 'https://img.shields.io/badge/Boo-000000?style=for-the-badge&logo=unity&logoColor=white', 'Langages Hybrides & Spécifiques')
    },
    'pike': {
        'name': 'Pike',
        'histoire': [
            '1994 : développé par Fredrik Hübinette et l’Université de Linköping en Suède, issu des travaux sur le langage LPC des MUDs.',
            '1996 : création de Roxen Internet Software, utilisant Pike comme moteur du serveur web haute performance Roxen WebServer.',
            '2000+ : évolution vers un langage interprété multiplateforme riche doté d’une bibliothèque standard exhaustive.',
            'Aujourd’hui : langage dynamique performant réputé pour son moteur de machine virtuelle en C ultra-optimisé.'
        ],
        'utilite': [
            'Langage interprété dynamique à syntaxe proche du C/C++ doté d’un typage fort et d’un ramasse-miettes automatique.',
            'Intègre des structures de données natives avancées (tableaux, mappings, multisets) et un support graphique et réseau complet.',
            'Moteur de serveurs web, de proxy de mise en cache et d’applications multimédias temps réel.',
            'Dispose d’une machine virtuelle hautement optimisée avec compilation à la volée du bytecode.',
            'Facilite le développement rapide d’applications réseau et d’outils d’administration système.'
        ],
        'url': 'https://pike.lysator.liu.se',
        'badge': ('Pike', 'https://img.shields.io/badge/Pike-2C3E50?style=for-the-badge&logo=cplusplus&logoColor=white', 'Langages Hybrides & Spécifiques')
    },
    'io': {
        'name': 'Io',
        'histoire': [
            '2002 : créé par Steve Dekorte pour explorer le minimalisme conceptuel de la programmation orientée prototype pure.',
            '2008 : mis en lumière mondiale dans le livre culte "Seven Languages in Seven Weeks" de Bruce Tate.',
            '2010+ : référence pédagogique pour comprendre les mécanismes fondamentaux des prototypes et des acteurs concurrents.',
            'Aujourd’hui : modèle d’élégance et de simplicité radicale dans la théorie des langages objets dynamiques.'
        ],
        'utilite': [
            'Langage purement orienté prototype où tout élément (y compris les blocs de code et les activateurs) est un objet clonable.',
            'Élimine la distinction rigide entre classes et instances au profit du clonage dynamique et de la délégation différentielle.',
            'Intègre le modèle de concurrence par acteurs légers (coroutines et fibres asynchrones natives).',
            'Dispose d’une syntaxe homoiconique ultra-épurée où chaque instruction est un simple envoi de message.',
            'Utilisé pour l’apprentissage conceptuel des systèmes objets réflexifs et la recherche en sémantique logicielle.'
        ],
        'url': 'https://iolanguage.org',
        'badge': ('Io', 'https://img.shields.io/badge/Io-1E1E1E?style=for-the-badge&logo=ghost&logoColor=white', 'Langages Hybrides & Spécifiques')
    },
    'ring': {
        'name': 'Ring',
        'histoire': [
            '2016 : conçu par Mahmoud Fayed et publié en open source comme langage innovant à multi-paradigmes extensibles.',
            '2018–2022 : développement d’un écosystème complet clé en main comprenant IDE (Ring Notepad), moteur de jeu 2D et bindings GUI (Qt).',
            '2024+ : enrichissement des outils de programmation déclarative et de traitement du langage naturel (NLP).',
            'Aujourd’hui : langage polyvalent et autonome conçu pour l’apprentissage, les jeux vidéo et le développement rapide.'
        ],
        'utilite': [
            'Langage multi-paradigme (impératif, fonctionnel, déclaratif, orienté objet) à syntaxe flexible et paramétrable.',
            'Permet de choisir son style de syntaxe (avec ou sans accolades, ou style naturel sans symboles stricts).',
            'Fournit des bibliothèques prêtes à l’emploi pour créer des applications graphiques Qt, des jeux 2D/3D et des applications web.',
            'Machine virtuelle autonome ultra-légère écrite en C ANSI sans dépendances externes lourdes.',
            'Utilisé pour l’éducation, le prototypage rapide de logiciels de bureau et la création de DSLs déclaratifs.'
        ],
        'url': 'https://ring-lang.github.io',
        'badge': ('Ring', 'https://img.shields.io/badge/Ring-18BC9C?style=for-the-badge&logo=c&logoColor=white', 'Langages Hybrides & Spécifiques')
    },
    'ur-web': {
        'name': 'Ur/Web',
        'histoire': [
            '2010–2015 : conçu par Adam Chlipala au MIT pour concevoir des applications web complètes mathématiquement garanties sans failles de sécurité.',
            '2016+ : utilisé comme référence académique pour la preuve formelle de sécurité des applications web fullstack.',
            'Aujourd’hui : pionnier mondial de la sécurité web totale garantie par le système de types à la compilation.'
        ],
        'utilite': [
            'Langage fonctionnel fortement typé compilant simultanément le code serveur, le code client JS, le schéma SQL et les styles CSS.',
            'Garantit à la compilation l’absence totale d’injections SQL, d’attaques XSS (Cross-Site Scripting) et de liens hypertextes brisés.',
            'Encapsule les transactions de base de données dans un modèle monadique rigoureux.',
            'Produit des binaires serveurs natifs ultra-rapides consommant une fraction infime des ressources de serveurs traditionnels.',
            'Idéal pour les applications financières, médicales et administratives où la sécurité web ne tolère aucun compromis.'
        ],
        'url': 'http://www.impredicative.com/ur/',
        'badge': ('Ur/Web', 'https://img.shields.io/badge/Ur_Web-1A365D?style=for-the-badge&logo=mit&logoColor=white', 'Langages Hybrides & Spécifiques')
    },
    'curry': {
        'name': 'Curry',
        'histoire': [
            '1995 : conçu par un comité international de chercheurs pour fusionner la programmation fonctionnelle pure (Haskell) et logique (Prolog).',
            '2000–2010 : formalisation du modèle de réduction paresseuse et de recherche non déterministe (Lazy Functional Logic Programming).',
            '2020+ : développement des compilateurs modernes PAKCS et KiCS2 générant du code Haskell natif.',
            'Aujourd’hui : standard mondial de la programmation fonctionnelle-logique intégrée.'
        ],
        'utilite': [
            'Langage multi-paradigme unifiant harmonieusement les fonctions d’ordre supérieur, l’évaluation paresseuse et les variables logiques.',
            'Permet d’appeler des fonctions avec des arguments inconnus (libres) que le système résout automatiquement par unification.',
            'Intègre la recherche de solutions multiples et la résolution de contraintes sans quitter le paradigme fonctionnel.',
            'Élimine la frontière artificielle entre calcul fonctionnel déterministe et recherche logique exploratoire.',
            'Utilisé dans la recherche sur la transformation de programmes, la vérification formelle et l’intelligence artificielle symbolique.'
        ],
        'url': 'https://curry-lang.org',
        'badge': ('Curry', 'https://img.shields.io/badge/Curry-5D4F85?style=for-the-badge&logo=haskell&logoColor=white', 'Langages Logiques & Formels')
    },
    'alice-ml': {
        'name': 'Alice ML',
        'histoire': [
            '2000–2006 : développé à l’Université de la Sarre par l’équipe de programming systems lab sous la direction de Gert Smolka.',
            '2007 : pionnier de l’intégration des composants logiciels de première classe et du typage dynamique sécurisé.',
            'Aujourd’hui : jalon fondamental de la recherche en concurrence fonctionnelle et calcul distribué sur machine virtuelle.'
        ],
        'utilite': [
            'Extension fonctionnelle de Standard ML intégrant nativement la concurrence concurrente par promesses (futures) et paquets de types.',
            'Permet l’évaluation paresseuse et concurrente transparente grâce aux futures de première classe.',
            'Intègre la programmation par contraintes sur domaines finis au sein d’un langage fonctionnel typé.',
            'Fournit un mécanisme de paquets (packages) pour le chargement et la sérialisation sécurisée de code sur le réseau.',
            'Utilisé dans la recherche sur les architectures distribuées résilientes et les systèmes concurrents avancés.'
        ],
        'url': 'https://www.ps.uni-saarland.de/alice/',
        'badge': ('Alice ML', 'https://img.shields.io/badge/Alice_ML-4B32C3?style=for-the-badge&logo=edx&logoColor=white', 'Langages Fonctionnels & Déclaratifs')
    },
    'shen': {
        'name': 'Shen',
        'histoire': [
            '2011 : conçu par Mark Tarver comme successeur de Qi II pour offrir un langage fonctionnel typé par calcul des séquents.',
            '2015 : architecture ultra-portable basée sur la machine virtuelle primitive K Lambda (KL) composée de seulement 43 fonctions.',
            '2020+ : portage sur plus d’une dizaine de plateformes hôtes (C, JavaScript, Python, CL, JVM, WebAssembly).',
            'Aujourd’hui : technologie unique offrant l’un des systèmes de types les plus expressifs et prouvables du monde Lisp.'
        ],
        'utilite': [
            'Dialecte Lisp intégrant la logique formelle du calcul des séquents pour définir des règles de typage arbitraires.',
            'Permet au développeur de programmer son propre système de types et de vérifier des propriétés mathématiques à la compilation.',
            'Intègre nativement un moteur de programmation logique Prolog complet et un moteur de grammaires PEG.',
            'Extrêmement portable grâce à sa compilation vers une machine virtuelle minimale de 43 fonctions primitives.',
            'Idéal pour l’intelligence artificielle symbolique, la démonstration automatique de théorèmes et la recherche en typage.'
        ],
        'url': 'https://shenlanguage.org',
        'badge': ('Shen', 'https://img.shields.io/badge/Shen-2C3E50?style=for-the-badge&logo=lisp&logoColor=white', 'Langages Fonctionnels & Déclaratifs')
    },
    'carp': {
        'name': 'Carp',
        'histoire': [
            '2016–2018 : initié par Erik Svedäng pour combiner la syntaxe expressive de Lisp avec la gestion mémoire sans GC de Rust.',
            '2020 : formalisation du système d’emprunt et de possession (borrowing/ownership) adapté à la syntaxe Lisp.',
            '2023+ : optimisations pour le développement de jeux vidéo 2D natifs et la synthèse sonore temps réel.',
            'Aujourd’hui : langage pionnier démontrant la faisabilité d’un Lisp purement statique et sans ramasse-miettes.'
        ],
        'utilite': [
            'Dialecte Lisp statiquement typé compilé directement vers du code C natif sans machine virtuelle ni ramasse-miettes (GC).',
            'Utilise un modèle de possession et d’emprunt similaire à Rust pour garantir la sûreté mémoire à la compilation.',
            'Permet la métaprogrammation par macros exécutées lors de la compilation pour générer du code hautement optimisé.',
            'Garantit une allocation mémoire déterministe et une empreinte minimale idéale pour le temps réel critique.',
            'Conçu spécifiquement pour les jeux vidéo, le traitement audio temps réel et les systèmes embarqués.'
        ],
        'url': 'https://github.com/carp-lang/Carp',
        'badge': ('Carp', 'https://img.shields.io/badge/Carp-663399?style=for-the-badge&logo=rust&logoColor=white', 'Langages Fonctionnels & Déclaratifs')
    },
    'kql': {
        'name': 'KQL (Kusto)',
        'histoire': [
            '2014 : développé en interne chez Microsoft pour analyser les pétaoctets de logs télémétriques des services Azure.',
            '2018 : adoption comme langage d’interrogation officiel d’Azure Data Explorer, Azure Monitor et Microsoft Sentinel (SIEM).',
            '2021+ : standard de l’industrie de la cybersécurité pour la détection de menaces (Threat Hunting) et l’analyse de logs cloud.',
            'Aujourd’hui : référence mondiale pour le requêtage ultra-rapide de données télémétriques et de sécurité à grande échelle.'
        ],
        'utilite': [
            'Langage de requête en pipeline conçu pour analyser rapidement de gigantesques volumes de données chronologiques et de logs.',
            'Utilise l’opérateur de tuyau (| pipe) pour enchaîner les transformations de manière fluide, lisible et intuitive.',
            'Optimisé pour scanner des milliards d’enregistrements en quelques secondes avec indexation automatique de texte et de colonnes.',
            'Moteur de détection de sécurité et d’investigation médico-légale (forensics) dans les centres opérationnels de sécurité (SOC).',
            'Fournit des fonctions natives de machine learning, de détection d’anomalies temporelles et de prévisions statistiques.'
        ],
        'url': 'https://learn.microsoft.com/azure/data-explorer/kusto/query/',
        'badge': ('KQL', 'https://img.shields.io/badge/KQL_Kusto-0089D6?style=for-the-badge&logo=microsoftazure&logoColor=white', 'Requêtes de Données & Graphes')
    },
    'prql': {
        'name': 'PRQL',
        'histoire': [
            '2022 : initié comme projet open source pour moderniser et simplifier l’écriture de requêtes relationnelles complexes (Pipelined Relational Query Language).',
            '2023 : adoption rapide par les analystes de données recherchant une alternative lisible et composable au SQL verbeux.',
            '2024+ : intégration avec Python (PyPRQL), dbt, DuckDB, PostgreSQL et les outils modernes de BI.',
            'Aujourd’hui : alternative montante au SQL apportant une approche fluide et fonctionnelle à la manipulation de données.'
        ],
        'utilite': [
            'Langage relationnel basé sur des pipelines de transformation séquentiels se compilant directement en requêtes SQL valides.',
            'Élimine la syntaxe non linéaire historique du SQL (SELECT écrit avant FROM et WHERE) au profit d’une lecture naturelle de haut en bas.',
            'Permet la réutilisation et la composition aisée de fonctions et de variables de transformation de données.',
            'Compatible avec l’ensemble des moteurs SQL existants (PostgreSQL, ClickHouse, BigQuery, Snowflake, DuckDB).',
            'Idéal pour l’ingénierie de données moderne, les pipelines analytiques et l’analyse exploratoire.'
        ],
        'url': 'https://prql-lang.org',
        'badge': ('PRQL', 'https://img.shields.io/badge/PRQL-F15A24?style=for-the-badge&logo=postgresql&logoColor=white', 'Requêtes de Données & Graphes')
    },
    'xpath': {
        'name': 'XPath',
        'histoire': [
            '1999 : standardisé par le W3C (XPath 1.0) comme langage universel d’adressage et de navigation dans les arbres XML.',
            '2007 : publication de XPath 2.0 enrichissant le système de types et les séquences ordonnées.',
            '2014–2017 : standardisation de XPath 3.0 et 3.1 avec intégration des fonctions d’ordre supérieur et du support JSON.',
            'Aujourd’hui : norme mondiale incontournable utilisée dans tous les frameworks d’automatisation de tests web (Selenium, Playwright).'
        ],
        'utilite': [
            'Langage d’expression permettant de sélectionner et de localiser précisément des nœuds ou ensembles de nœuds dans un arbre hiérarchique (DOM, XML, HTML).',
            'Utilise une notation par chemins d’accès compacte (/noeud/enfant[@attribut="valeur"]) avec prédicats logiques et axes de navigation.',
            'Standard universel pour le scraping de données web, le parsing documentaire et les tests automatisés d’interfaces.',
            'Moteur d’extraction de données au cœur des technologies XSLT, XQuery et des parseurs XML/HTML de tous les langages.',
            'Permet d’écrire des sélections structurelles complexes basées sur la parenté, la descendance et les conditions sémantiques.'
        ],
        'url': 'https://www.w3.org/TR/xpath-31/',
        'badge': ('XPath', 'https://img.shields.io/badge/XPath-005A9C?style=for-the-badge&logo=w3c&logoColor=white', 'Requêtes de Données & Graphes')
    }
}

def run():
    target_dir = os.path.join(os.path.dirname(__file__), '..', 'languages')
    os.makedirs(target_dir, exist_ok=True)
    
    count = 0
    for slug, data in WAVE4_DB.items():
        filepath = os.path.join(target_dir, f'{slug}.md')
        name = data['name']
        lines_hist = '\n'.join([f'- {b}' for b in data['histoire']])
        lines_util = '\n'.join([f'- {b}' for b in data['utilite']])
        url = data['url']
        content = f'''## {name} — histoire

{lines_hist}

## {name} — utilité

{lines_util}

## {name} — ressources

- Site officiel : [{url}]({url})
'''
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
    print(f'Vague 4 terminée : {count} nouvelles fiches écrites !')

if __name__ == '__main__':
    run()
