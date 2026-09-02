import os
import json

# Comprehensive encyclopedia catalog for 500+ additional languages
# Structured by domain / era / paradigms

LANGUAGES_PART1 = [
    # --- Letter A ---
    ("a-plus", "A+", [
        "1988 : développé par Arthur Whitney chez Morgan Stanley pour les applications financières exigeantes.",
        "1992 : diffusion interne intensive pour l'analyse boursière haute fréquence et l'évaluation d'actifs.",
        "2001 : Morgan Stanley libère A+ sous licence open source GNU GPL.",
        "2010+ : reconnu comme l'un des dialectes APL les plus influents ayant directement inspiré K et Q.",
        "Aujourd’hui : monument historique de l'informatique financière de Wall Street."
    ], [
        "Langage de programmation matriciel (array programming) descendant direct d'APL.",
        "Intègre nativement un jeu complet de primitives graphiques et d'interfaces utilisateur (X11).",
        "Optimisé pour manipuler des tableaux multidimensionnels et séries temporelles massives.",
        "Utilisé historiquement pour le trading d'actions, la gestion des risques et l'analyse quantitative.",
        "Assure une exécution vectorielle ultra-véloce avec une empreinte mémoire compacte."
    ], "http://www.aplusdev.org", "Scientifiques, Mathématiques & Finance", "00599C", "dyalog"),

    ("abc", "ABC", [
        "1980–1985 : conçu au CWI (Centrum Wiskunde & Informatica) à Amsterdam par Leo Geurts, Lambert Meertens et Steven Pemberton.",
        "1985–1989 : développé pour remplacer le BASIC par un langage d'apprentissage élégant et structuré.",
        "1989 : Guido van Rossum s'inspire directement d'ABC (notamment l'indentation significative et les types de haut niveau) pour créer Python.",
        "1991 : diffusion académique en Europe comme modèle d'ergonomie syntaxique.",
        "Aujourd’hui : célèbre pour avoir posé les fondations syntaxiques directes du langage Python."
    ], [
        "Langage de programmation impératif et interactif conçu pour l'enseignement et le prototypage rapide.",
        "Pionnier mondial de l'indentation significative pour la structuration des blocs de code.",
        "Fournit cinq types de données de très haut niveau : nombres à précision infinie, textes, listes, tables et composés.",
        "Intègre un environnement de développement interactif avec éditeur syntaxique dédié.",
        "Conçu pour rendre la programmation accessible aux non-programmeurs et scientifiques."
    ], "https://homepages.cwi.nl/~steven/abc/", "Langages Historiques & Pionniers", "1976D2", "python"),

    ("action", "Action!", [
        "1983 : créé par Clinton Parker pour Action Computer Services sur la famille d'ordinateurs 8-bit Atari.",
        "1984 : commercialisé par Optimized Systems Software (OSS) sous forme de cartouche ROM pour Atari 400/800/XL/XE.",
        "1985–1990 : langage de prédilection pour développer des jeux commerciaux et utilitaires rapides sur micro-ordinateurs Atari.",
        "2015 : libéré dans le domaine public par son auteur original.",
        "Aujourd’hui : vénéré par la communauté rétro-gaming Atari pour sa vitesse de compilation foudroyante sur matériel 6502."
    ], [
        "Langage procédural compilé produisant du code machine natif pour le microprocesseur 6502.",
        "Compilait des programmes entiers en moins d'une seconde directement dans la mémoire vive de 64 Ko.",
        "Offrait des performances d'exécution jusqu'à 200 fois supérieures à l'Atari BASIC standard.",
        "Permettait l'accès direct aux registres matériels graphiques (ANTIC, GTIA) et sonores (POKEY).",
        "Utilisé pour programmer des jeux d'arcade fluides et des démos sur ordinateurs 8-bit."
    ], "https://github.com/pfusik/action", "Langages Historiques & Pionniers", "E01A22", "atari"),

    ("actor", "Actor", [
        "1986 : développé par Charles Duff chez The Whitewater Group pour la plateforme Windows 1.0/2.0.",
        "1988 : adoption massive pour le prototypage rapide d'applications sous Windows 3.0.",
        "1990 : élu meilleur environnement de développement logiciel par le magazine PC World.",
        "1992 : rachat par Symantec Corporation.",
        "Aujourd’hui : pionnier historique de la programmation orientée objet pure pour l'interface graphique Windows."
    ], [
        "Langage purement orienté objet combinant l'architecture de Smalltalk avec une syntaxe de type Pascal/C.",
        "Intégrait un ramasse-miettes automatique et un environnement interactif avec navigateur de classes.",
        "Facilitait grandement la création d'interfaces graphiques complexes pour Windows 3.x.",
        "Générait des applications fenêtrées performantes via une machine virtuelle optimisée.",
        "A largement contribué à la démocratisation de l'orienté objet dans l'écosystème PC professionnel."
    ], "https://winworldpc.com/product/actor/4x", "Langages Historiques & Pionniers", "00549D", "windows"),

    ("apex", "Apex (Salesforce)", [
        "2006 : développé par Salesforce pour permettre l'exécution de logique métier personnalisée sur la plateforme Force.com.",
        "2010 : intégration avec Visualforce pour bâtir des interfaces CRM sur mesure.",
        "2016 : intégration avec Lightning Component Framework et Lightning Web Components (LWC).",
        "2020+ : enrichissement avec le compilateur Apex moderne et des outils de CI/CD cloud native.",
        "Aujourd’hui : langage d'entreprise incontournable gérant les processus CRM de centaines de milliers de multinationales."
    ], [
        "Langage orienté objet fortement typé s'exécutant entièrement côté serveur dans le cloud multilocataire de Salesforce.",
        "Syntaxe très proche de Java et C# avec intégration native des requêtes SOQL (Salesforce Object Query Language) et SOSL.",
        "Garantit l'intégrité de la plateforme grâce à des limites d'exécution strictes imposées par conception (Governor Limits).",
        "Moteur de déclencheurs automatiques (Triggers) sur les opérations de bases de données et les flux métiers.",
        "Exige un taux de couverture de tests unitaires minimum de 75 % avant tout déploiement en production."
    ], "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/", "Entreprise, ERP & 4GL Métier", "00A1E0", "salesforce"),

    ("arc", "Arc", [
        "2001 : conçu par Paul Graham (cofondateur de Y Combinator) et Robert Morris au MIT comme dialecte Lisp idéal.",
        "2008 : publication officielle de la première version publique d'Arc.",
        "2008 : Hacker News (news.ycombinator.com) est écrit et mis en ligne entièrement en langage Arc.",
        "2014 : développement d'implémentations communautaires comme Anarki.",
        "Aujourd’hui : célèbre pour motoriser le forum Hacker News et pour ses idées sur la concision expressive."
    ], [
        "Dialecte Lisp épuré conçu pour maximiser la densité d'expression et la rapidité de développement web.",
        "Traite les requêtes web et l'état des sessions de manière transparente via des continuations de première classe.",
        "Offre une syntaxe ultra-concise réduisant au strict minimum le nombre de parenthèses et de symboles.",
        "Motorise la plateforme communautaire mondiale de développeurs Hacker News.",
        "Conçu pour le prototypage ultra-véloce de startups technologiques et de serveurs web légers."
    ], "http://arclanguage.org", "Langages Fonctionnels & Déclaratifs", "FF6600", "ycombinator"),

    ("arexx", "ARexx", [
        "1987 : développé par William S. Hawes pour le système d'exploitation AmigaOS de Commodore.",
        "1990 : Commodore intègre officiellement ARexx au cœur d'AmigaOS 2.0 en tant que protocole d'automatisation système universel.",
        "Années 1990 : permet l'interconnexion transparente entre logiciels de PAO, vidéo, audio et 3D sur Amiga.",
        "2000+ : inspiration majeure pour les mécanismes d'automatisation inter-processus et D-Bus sous Linux.",
        "Aujourd’hui : standard légendaire d'interopérabilité et de communication inter-applications."
    ], [
        "Implémentation du langage REXX d'IBM pour l'architecture multitâche préemptive de l'Amiga.",
        "Permettait à des logiciels totalement indépendants (ex: un séquenceur musical et un logiciel 3D) de se piloter mutuellement via des ports de messages.",
        "Fournissait une syntaxe accessible et puissante pour l'automatisation système et le scripting de bureau.",
        "Intégrait la gestion des bibliothèques de fonctions partagées dynamiques (ARexx function libraries).",
        "A fait de l'Amiga la station de travail vidéo et multimédia la plus automatisable de son époque."
    ], "http://aminet.net/package/util/rexx/ARexxGuide", "Langages Historiques & Pionniers", "FF4400", "amigaos"),

    ("autoit", "AutoIt", [
        "1999 : créé par Jonathan Bennett pour automatiser l'installation silencieuse de logiciels sous Windows 95/NT.",
        "2004 : refonte majeure avec AutoIt v3, apportant une syntaxe structurée inspirée du BASIC et l'orientation objet.",
        "2010+ : adoption massive par les équipes d'administration système et d'assistance informatique d'entreprise.",
        "2020+ : maintien actif avec support 64 bits et intégration de l'interface graphique Windows moderne.",
        "Aujourd’hui : outil de référence sous Windows pour l'automatisation de tâches bureautiques et la création d'installateurs."
    ], [
        "Langage de script de type BASIC conçu pour simuler des frappes clavier, mouvements de souris et fenêtres sous Windows.",
        "Pilote directement l'ensemble des contrôles graphiques Win32 (boutons, champs, listes, menus).",
        "Permet de compiler les scripts en fichiers exécutables autonomes (.exe) sans nécessiter de runtime préinstallé.",
        "Dispose d’outils intégrés puissants pour concevoir des interfaces graphiques (Koda FormDesigner).",
        "Utilisé pour les déploiements de parcs informatiques, les tests de régression GUI et les outils utilitaires."
    ], "https://www.autoitscript.com", "Automatisation Desktop & Web Scripting", "0078D7", "windows"),

    # --- Letter B ---
    ("b-lang", "B", [
        "1969 : conçu par Ken Thompson et Dennis Ritchie aux laboratoires Bell d’AT&T pour le premier système Unix sur PDP-7.",
        "1970 : adaptation sur machine PDP-11 pour le développement des premiers utilitaires Unix.",
        "1971–1972 : Dennis Ritchie fait évoluer B en ajoutant les types de données, donnant naissance au langage C.",
        "Aujourd’hui : ancêtre direct du C et de toute la famille des langages à accolades modernes."
    ], [
        "Langage système typeless (non typé) dérivé de BCPL, où chaque variable correspondait à un mot mémoire de la machine.",
        "A introduit les opérateurs d'incrémentation (++) et de décrémentation (--) devenus universels.",
        "Premier langage de haut niveau utilisé pour prototyper des composants du système d'exploitation Unix.",
        "Fournissait une syntaxe compacte convenant aux ressources extrêmement réduites des mini-ordinateurs PDP.",
        "A posé les fondations lexicales et syntaxiques fondamentales de la programmation moderne."
    ], "https://www.bell-labs.com/usr/dmr/www/bintro.html", "Langages Historiques & Pionniers", "000000", "c"),

    ("bcpl", "BCPL", [
        "1967 : conçu par Martin Richards à l’Université de Cambridge pour écrire des compilateurs portables.",
        "1969 : utilisé pour développer le système d'exploitation TRIPOS (qui devint plus tard le noyau AmigaDOS).",
        "1970 : inspire directement Ken Thompson pour concevoir le langage B aux laboratoires Bell.",
        "Aujourd’hui : monument historique de l'ingénierie des compilateurs et de la programmation système."
    ], [
        "Langage de programmation système impératif non typé (Basic Combined Programming Language).",
        "A inventé la célèbre convention d'exemple 'Hello, World!' devenue la tradition universelle de l'informatique.",
        "A popularisé l'utilisation des accolades ({ et }) pour délimiter les blocs d'instructions.",
        "Utilisait une machine virtuelle intermédiaire (O-code) pour garantir une portabilité pionnière sur diverses architectures.",
        "Moteur historique de multiples systèmes d'exploitation pionniers des années 1970."
    ], "https://www.cl.cam.ac.uk/users/mr/BCPL.html", "Langages Historiques & Pionniers", "00599C", "cambridge"),

    ("beanshell", "BeanShell", [
        "1997–2000 : créé par Patrick Niemeyer comme interpréteur de script Java léger et dynamique.",
        "2005 : standardisé via la JSR 274 au sein du Java Community Process.",
        "2010+ : intégré comme moteur de script dans des logiciels d'entreprise majeurs (Apache JMeter, OpenOffice, Eclipse).",
        "Aujourd’hui : solution éprouvée pour injecter et exécuter dynamiquement du code Java sans étape de compilation."
    ], [
        "Interpréteur et langage de script exécutant du code source Java standard de manière totalement dynamique.",
        "Permet d'ajouter du typage dynamique optionnel et des fermetures (closures) au code Java classique.",
        "Accède directement et de façon transparente à tous les objets et bibliothèques de la JVM.",
        "Utilisé massivement dans Apache JMeter pour l'écriture de scénarios de tests de charge et d'assertions complexes.",
        "Idéal pour intégrer un terminal de commande interactif ou un moteur d'extension dans des applications Java."
    ], "https://github.com/beanshell/beanshell", "Langages Applicatifs & Entreprise", "007396", "java"),

    ("bliss", "BLISS", [
        "1970 : conçu par W.A. Wulf, D. Russell et A.N. Habermann à l’Université Carnegie Mellon.",
        "1975–1985 : adopté par Digital Equipment Corporation (DEC) comme langage système principal pour PDP-10, PDP-11 et VAX.",
        "1978 : le système d'exploitation historique VMS (OpenVMS) de DEC est écrit en grande majorité en BLISS-32.",
        "Aujourd’hui : référence majeure dans l'histoire des compilateurs à optimisation globale agressive."
    ], [
        "Langage système non typé (Basic Language for Implementation of System Software) orienté expression.",
        "Considérait chaque construction de programme (y compris les blocs et boucles) comme une expression retournant une valeur.",
        "Rejetait explicitement l'instruction goto pour forcer une programmation structurée rigoureuse.",
        "Pionnier de l'allocation automatique des registres processeurs par analyse de flux de données.",
        "Utilisé pour bâtir des systèmes d'exploitation industriels d'une fiabilité légendaire (OpenVMS)."
    ], "https://en.wikipedia.org/wiki/BLISS", "Langages Historiques & Pionniers", "002D62", "digital"),

    # --- Letter C ---
    ("c-minus-minus", "C--", [
        "1997 : conçu par Norman Ramsey et Simon Peyton Jones (créateur de GHC Haskell) comme langage d'assemblage portable de haut niveau.",
        "2000–2004 : utilisé pour concevoir le backend de génération de code natif du compilateur GHC (Glasgow Haskell Compiler).",
        "2008 : influence majeure sur la conception des représentations intermédiaires modernes (LLVM IR).",
        "Aujourd’hui : jalon fondamental de la recherche sur la compilation et la gestion du déroulement de pile (stack unwinding)."
    ], [
        "Langage intermédiaire de bas niveau conçu pour servir de cible commune aux compilateurs de langages de haut niveau.",
        "Fournit des abstractions portables pour les registres processeur, les appels de fonctions et la disposition en mémoire.",
        "Intègre nativement le support pour les ramasse-miettes précis et la gestion des exceptions matérielles.",
        "A servi de cible de génération de code pour les compilateurs fonctionnels avancés.",
        "A posé les principes de séparation moderne entre frontend linguistique et backend d'optimisation machine."
    ], "https://www.cs.tufts.edu/~nr/c--/", "Langages Systèmes & Bas Niveau", "5D4F85", "haskell"),

    ("cecil", "Cecil", [
        "1992 : conçu par Craig Chambers à l’Université de Washington pour explorer le multi-dispatching dynamique.",
        "1995 : publication de Vortex, compilateur optimisant le polymorphisme et l'inlining de méthodes virtuelles.",
        "Aujourd’hui : référence théorique majeure ayant influencé CLOS, Dylan, Julia et Swift."
    ], [
        "Langage orienté objet pur multi-paradigme basé sur le multi-dispatch dynamique (multimethods).",
        "Sépare strictement la définition des structures de données de leurs méthodes de traitement.",
        "Permet d'étendre des types de données existants sans modifier leur code source d'origine.",
        "Intègre à la fois le typage statique optionnel et le typage dynamique flexible.",
        "Pionnier des techniques d'analyse statique pour la dévirtualisation d'appels de méthodes à l'exécution."
    ], "https://www.cs.washington.edu/research/projects/cecil/www/cecil.html", "Langages Hybrides & Spécifiques", "3C5CAA", "openaccess"),

    ("cfml", "ColdFusion (CFML)", [
        "1995 : créé par Jeremy et Joseph Allaire chez Allaire Corporation pour dynamiser les pages web avec des balises simples.",
        "2001 : racheté par Macromedia, puis par Adobe Systems en 2005.",
        "2002 : réécriture du moteur ColdFusion au-dessus de la machine virtuelle Java (JVM).",
        "2010+ : émergence de moteurs open source performants alternatifs (Lucee).",
        "Aujourd’hui : technologie web d'entreprise mature motorisant de nombreuses plateformes gouvernementales et bancaires."
    ], [
        "Langage de script web dynamique utilisant une syntaxe basée sur des balises (similaire au HTML/XML) et du scripting (CFScript).",
        "Exécuté sur la machine virtuelle Java (JVM) avec accès direct à toutes les classes et bibliothèques Java.",
        "Simplifie à l'extrême l'interrogation de bases de données relationnelles (<cfquery>) et l'envoi de courriels.",
        "Intègre des fonctionnalités natives de génération de PDF, de manipulation d'images et de tâches planifiées.",
        "Utilisé pour le développement rapide d'applications intranet d'entreprise et de portails sécurisés."
    ], "https://www.adobe.com/products/coldfusion-family.html", "Langages Web & Scripting Dynamique", "FF0000", "adobe"),

    ("clean", "Clean", [
        "1987 : développé par l’Université Radboud de Nimègue aux Pays-Bas pour explorer la programmation fonctionnelle pure.",
        "1995 : introduction pionnière du système de types d'unicité (Uniqueness Types) pour gérer les entrées/sorties sans monades.",
        "Aujourd’hui : référence académique ayant directement inspiré le système de possession (ownership) de Rust."
    ], [
        "Langage purement fonctionnel à évaluation paresseuse basé sur la réécriture de graphes (Graph Rewriting).",
        "Pionnier du système de types d'unicité garantissant qu'une valeur n'a qu'une seule référence, permettant la mutation en place sûre.",
        "Génère du code machine natif ultra-rapide rivalisant directement en performance avec le code C compilé.",
        "Fournit une inférence de types complète (système Hindley-Milner étendu).",
        "Utilisé pour la recherche sur la concurrence formelle, le parallélisme et la sémantique de graphes."
    ], "https://clean.cs.ru.nl", "Langages Fonctionnels & Déclaratifs", "00599C", "haskell"),

    ("clu", "CLU", [
        "1974–1975 : conçu par Barbara Liskov (prix Turing 2008) et ses étudiants au MIT.",
        "1979 : formalisation des types de données abstraits (Abstract Data Types) et du polymorphisme paramétrique.",
        "Années 1980–1990 : influence directe et déterminante sur la conception de C++, Java, Python, Ruby et Rust.",
        "Aujourd’hui : monument absolu du génie logiciel ayant inventé les itérateurs, les génériques et le principe de substitution de Liskov."
    ], [
        "Langage procédural ayant inventé le concept moderne de types de données abstraits encapsulés (clusters).",
        "A introduit pour la première fois dans l'histoire les itérateurs et le mot-clé yield.",
        "Pionnier de la gestion structurée des exceptions et de l'affectation multiple de variables.",
        "Fondement sur lequel repose le célèbre principe de substitution de Liskov (le 'L' des principes SOLID).",
        "A servi de modèle direct pour l'implémentation des génériques en C++ et Java."
    ], "https://pmg.csail.mit.edu/CLU.html", "Langages Historiques & Pionniers", "1F2937", "mit"),

    ("comal", "COMAL", [
        "1973 : créé par Børge R. Christensen et Benedict Løfstedt au Danemark (Common Algorithmic Language).",
        "1980–1990 : adopté officiellement par les ministères de l'Éducation au Danemark, en Irlande et au Royaume-Uni (BBC Micro, Commodore 64).",
        "Aujourd’hui : référence historique de l'enseignement de la programmation structurée dans les écoles européennes."
    ], [
        "Langage éducatif combinant la simplicité interactive du BASIC avec la rigueur structurée d'ALGOL et Pascal.",
        "Éliminait les numéros de ligne obligatoires et les sauts GOTO anarchiques au profit de blocs IF, WHILE et REPEAT indentés.",
        "Fournissait des structures de contrôle complètes et des procédures paramétrées à portée locale.",
        "A permis à des millions d'élèves d'apprendre la pensée algorithmique moderne sur micro-ordinateurs 8-bit.",
        "Intégrait des modules graphiques de commande pour le tracé de figures et la tortue Logo."
    ], "https://en.wikipedia.org/wiki/COMAL", "Langages Historiques & Pionniers", "D42428", "commodore"),

    ("cython", "Cython", [
        "2007 : initié par Robert Bradshaw et Stefan Behnel comme fork optimisé du projet Pyrex.",
        "2011 : adoption comme moteur d'accélération central des bibliothèques scientifiques majeures (NumPy, SciPy, Pandas, Scikit-learn).",
        "2023 : sortie historique de Cython 3.0 avec support complet de Python 3.12+ et typage pur sans syntaxe propriétaire.",
        "Aujourd’hui : passerelle incontournable reliant la simplicité de Python aux performances brutes du C/C++."
    ], [
        "Sur-ensemble compilé de Python permettant d'écrire des extensions C natives ultra-performantes.",
        "Permet d'ajouter des annotations de types C statiques (cdef) pour multiplier la vitesse d'exécution par 100 à 1 000.",
        "Interagit sans surcoût avec les structures de données natives, tableaux de mémoire brute et bibliothèques C/C++ externes.",
        "Moteur sous-jacent garantissant la rapidité fulgurante de l'ensemble de l'écosystème de Data Science et Machine Learning en Python.",
        "Prend en charge la libération du verrou global (GIL - Global Interpreter Lock) pour le parallélisme multithread natif."
    ], "https://cython.org", "Langages Web & Scripting Dynamique", "3776AB", "python")
]

print(f"Dataset Part 1 ready: {len(LANGUAGES_PART1)} languages.")
