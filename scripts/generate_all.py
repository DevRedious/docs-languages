import os
import json

# Comprehensive database of languages
LANG_DB = {
    'c': {
        'name': 'C',
        'histoire': [
            '1972 : créé par Dennis Ritchie aux laboratoires Bell pour réécrire le système d’exploitation Unix.',
            '1978 : publication du livre de référence "The C Programming Language" par Brian Kernighan et Dennis Ritchie (K&R C).',
            '1989 : première standardisation officielle par l’ANSI (ANSI C / C89), suivie par l’ISO en 1990 (C90).',
            '1999–2011 : évolutions normatives majeures avec C99 et C11 (tableaux à taille variable, types booléens, support multithread natif).',
            'Aujourd’hui : norme C23 finalisée, langage système le plus influent et omniprésent dans l’histoire de l’informatique.'
        ],
        'utilite': [
            'Langage impératif et procédural de bas niveau offrant un contrôle direct sur la mémoire et le processeur.',
            'Sert de fondation aux systèmes d’exploitation (noyaux Linux, Windows, macOS), pilotes matériels et systèmes embarqués.',
            'Conçu pour une efficacité d’exécution maximale et une empreinte mémoire minimale.',
            'Utilisé pour les moteurs de bases de données, interpréteurs de langages (CPython, Ruby) et logiciels temps réel critique.',
            'Standard universel d’interopérabilité binaire (ABI C) servant de passerelle entre quasiment tous les langages modernes.'
        ],
        'url': 'https://www.iso.org/standard/74528.html',
        'badge': ('C', 'https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black', 'Langages Systèmes & Bas Niveau')
    },
    'cpp': {
        'name': 'C++',
        'histoire': [
            '1979–1985 : conçu par Bjarne Stroustrup aux laboratoires Bell sous le nom initial de "C with Classes" pour ajouter l’abstraction objet au C.',
            '1998 : première standardisation ISO internationale (C++98) introduisant la bibliothèque standard et la STL d’Alexander Stepanov.',
            '2011 : tournant majeur avec C++11 ("Modern C++"), apportant la sémantique de déplacement, les lambdas et la gestion automatique de mémoire.',
            '2014–2020 : modernisations continues avec C++14, C++17 et C++20 (concepts, modules, coroutines, plages).',
            'Aujourd’hui : langage standardisé en cycle triennal (C++23/C++26), pilier des industries de la haute performance.'
        ],
        'utilite': [
            'Langage multi-paradigme (orienté objet, générique, fonctionnel) appliquant le principe d’abstraction à coût nul (zero-cost abstractions).',
            'Permet de combiner manipulation matérielle de bas niveau et constructions logicielles de très haut niveau.',
            'Privilégie le déterminisme des performances et la gestion des ressources via l’idiome RAII.',
            'Moteur de référence pour les jeux vidéo AAA (Unreal Engine), navigateurs web (Chromium, Firefox) et trading haute fréquence (HFT).',
            'Indispensable dans le calcul scientifique lourd, les frameworks d’apprentissage profond (TensorFlow, PyTorch) et la robotique.'
        ],
        'url': 'https://isocpp.org',
        'badge': ('C++', 'https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white', 'Langages Systèmes & Bas Niveau')
    },
    'rust': {
        'name': 'Rust',
        'histoire': [
            '2006 : projet personnel initié par Graydon Hoare, rapidement sponsorisé par Mozilla Research dès 2009.',
            '2015 : sortie de la version stable 1.0 garantissant la stabilité de l’API sans rupture rétrocompatible.',
            '2018–2021 : éditions 2018 et 2021 apportant la syntaxe async/await, une ergonomie accrue du compilateur et un écosystème mature.',
            '2021+ : création de la Rust Foundation par Mozilla, AWS, Google, Microsoft et Huawei ; intégration progressive dans le noyau Linux 6.1+.',
            'Aujourd’hui : référence mondiale de la programmation système sécurisée par conception (memory safety sans garbage collector).'
        ],
        'utilite': [
            'Langage système compilé garantissant la sûreté mémoire et la concurrence sans corruption de données à la compilation.',
            'Utilise un modèle novateur de possession (ownership), d’emprunt (borrowing) et de durées de vie (lifetimes).',
            'Fournit des abstractions à coût nul comparables à C++ tout en éliminant les vulnérabilités de type use-after-free et buffer overflow.',
            'Utilisé pour les moteurs de rendu, l’outillage web haute performance, les systèmes cloud-native et la blockchain.',
            'Soutenu par un gestionnaire de paquets et outil de build unifié de premier ordre (Cargo).'
        ],
        'url': 'https://www.rust-lang.org',
        'badge': ('Rust', 'https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white', 'Langages Systèmes & Bas Niveau')
    },
    'zig': {
        'name': 'Zig',
        'histoire': [
            '2015–2016 : créé par Andrew Kelley comme remplaçant moderne et pragmatique du C sans complexité superflue.',
            '2019 : adoption du compilateur Zig comme compilateur C/C++ universel (capable de cross-compiler clé en main sans dépendance externe).',
            '2020 : création de la Zig Software Foundation (organisation à but non lucratif) pour pérenniser le développement open source.',
            '2022+ : adoption industrielle notable dans des projets d’infrastructure haute performance (Bun runtime, TigerBeetle DB).',
            'Aujourd’hui : langage en marche vers sa version 1.0, reconnu pour sa clarté, sa métaprogrammation à la compilation et son interop C directe.'
        ],
        'utilite': [
            'Langage système sans flux de contrôle caché, sans préprocesseur et sans allocation mémoire implicite.',
            'Remplace les macros par l’évaluation de code à la compilation via la directive puissante comptime.',
            'Fournit une gestion explicite des allocateurs de mémoire passés en paramètres de fonctions.',
            'Sert à la fois de langage système ultra-rapide et de chaîne de compilation C/C++ cross-plateforme complète.',
            'Utilisé pour les bases de données financières distribuées, les moteurs de jeux et les runtimes JavaScript légers.'
        ],
        'url': 'https://ziglang.org',
        'badge': ('Zig', 'https://img.shields.io/badge/Zig-F7A41D?style=for-the-badge&logo=zig&logoColor=black', 'Langages Systèmes & Bas Niveau')
    },
    'nim': {
        'name': 'Nim',
        'histoire': [
            '2008 : créé par Andreas Rumpf sous le nom initial de Nimrod, avec une syntaxe élégante inspirée de Python et la rapidité du C.',
            '2014 : renommage officiel du projet en Nim et refonte de l’écosystème.',
            '2019 : publication de la version stable Nim 1.0 marquant l’engagement de stabilité à long terme.',
            '2023 : publication de Nim 2.0 introduisant la gestion mémoire déterministe ORC/ARC par comptage de références avec cycle collection.',
            'Aujourd’hui : langage système polyvalent compilé vers C, C++, JavaScript et WebAssembly.'
        ],
        'utilite': [
            'Langage compilé statiquement typé combinant une syntaxe expressive et concise avec des performances natives pures.',
            'Dispose d’un système de macros basé sur les arbres syntaxiques abstraits (AST) permettant de transformer le code à la compilation.',
            'Offre plusieurs stratégies de gestion de mémoire configurables, du mode sans GC au mode temps réel déterministe (ARC/ORC).',
            'Permet la cross-compilation facile et une interopérabilité sans surcoût (zero-overhead) avec les bibliothèques C/C++.',
            'Utilisé en bioinformatique, développement de jeux vidéo, cybersécurité (outils d’audit) et passerelles réseau.'
        ],
        'url': 'https://nim-lang.org',
        'badge': ('Nim', 'https://img.shields.io/badge/Nim-FFE953?style=for-the-badge&logo=nim&logoColor=black', 'Langages Systèmes & Bas Niveau')
    },
    'd': {
        'name': 'D',
        'histoire': [
            '1999–2001 : conçu par Walter Bright (ingénieur chez Digital Mars et auteur de compilateurs C/C++) pour réinventer le C++.',
            '2007 : Andrei Alexandrescu rejoint le projet et impulse la spécification de D2 (D version 2) axée sur la métaprogrammation et la pureté fonctionnelle.',
            '2018 : intégration du frontend D (GDC) dans la suite officielle de compilateurs GNU GCC 9.',
            '2020+ : développement des modes sans garbage collector (BetterC) et d’extensions pour la sûreté mémoire (DIP1000).',
            'Aujourd’hui : langage système mature, combinant productivité expressive et performances natives.'
        ],
        'utilite': [
            'Langage système multi-paradigme offrant une métaprogrammation par gabarits (templates) et introspection puissante.',
            'Permet l’exécution de fonctions arbitraires à la compilation (CTFE - Compile-Time Function Execution).',
            'Dispose d’une compatibilité binaire directe avec le C et partielle avec le C++ sans couche de glue manuelle.',
            'Prend en charge la programmation par contrat (pre/post-conditions, invariants de classe) intégrée au langage.',
            'Utilisé dans l’analyse financière quantitative, les moteurs de recherche, la simulation physique et les jeux vidéo.'
        ],
        'url': 'https://dlang.org',
        'badge': ('D', 'https://img.shields.io/badge/D-B03931?style=for-the-badge&logo=d&logoColor=white', 'Langages Systèmes & Bas Niveau')
    },
    'assembly': {
        'name': 'Assembly',
        'histoire': [
            '1947–1950 : formalisé par Kathleen Booth et les pionniers de l’informatique pour remplacer le code machine binaire brut par des mnémoniques textuels.',
            'Années 1960–1970 : langage de prédilection pour l’écriture des premiers systèmes d’exploitation et logiciels commerciaux sur mainframes.',
            'Années 1980–1990 : standardisation d’assembleurs populaires comme MASM, TASM, NASM et GAS sur architectures x86 et 68000.',
            'Années 2000–2020 : diversification avec l’essor mondial des architectures ARM, RISC-V et des bytecodes virtuels.',
            'Aujourd’hui : outil indispensable pour l’initialisation de processeurs (bootloaders), l’ingénierie inverse et les micro-optimisations critiques.'
        ],
        'utilite': [
            'Représentation symbolique textuelle directe des instructions exécutées par une architecture matérielle spécifique (x86, ARM, RISC-V).',
            'Accès direct et absolu aux registres du processeur, aux interruptions matérielles et à l’adressage mémoire physique.',
            'Permet la programmation des routines d’amorçage (boot sequence, BIOS/UEFI) et des barrières de synchronisation atomique de bas niveau.',
            'Indispensable en rétro-ingénierie, analyse de logiciels malveillants, audit de sécurité et exploitation de vulnérabilités.',
            'Utilisé pour les micro-noyaux temps réel et les noyaux de calcul vectoriel ultra-optimisés (SIMD/AVX).'
        ],
        'url': 'https://www.nasm.us',
        'badge': ('Assembly', 'https://img.shields.io/badge/Assembly-6E4C13?style=for-the-badge&logo=assemblyscript&logoColor=white', 'Langages Systèmes & Bas Niveau')
    },
    'fortran': {
        'name': 'Fortran',
        'histoire': [
            '1957 : créé par John Backus et son équipe chez IBM comme le tout premier langage de haut niveau commercialisé (FORmula TRANslating System).',
            '1966–1977 : standardisations FORTRAN 66 et FORTRAN 77 établissant les règles du calcul numérique mondial.',
            '1990–1995 : Fortran 90 et Fortran 95 introduisent les opérations vectorielles sur tableaux, l’allocation dynamique et la modularité.',
            '2003–2018 : ajouts de la programmation orientée objet, de l’interopérabilité native avec le C et des co-tableaux pour le parallélisme massif (Coarray Fortran).',
            'Aujourd’hui : norme Fortran 2023 active, moteur incontesté du calcul haute performance (HPC) et des supercalculateurs.'
        ],
        'utilite': [
            'Langage compilé impératif spécifiquement optimisé pour le calcul numérique intensif, matriciel et scientifique.',
            'Permet aux compilateurs d’appliquer des optimisations vectorielles agressives grâce à l’absence stricte d’aliasing de pointeurs par défaut.',
            'Prend en charge nativement les calculs sur tableaux multidimensionnels et les nombres complexes.',
            'Moteur historique des prévisions météorologiques, simulations astrophysiques, dynamique des fluides (CFD) et fusion nucléaire.',
            'Dispose de bibliothèques mathématiques éprouvées depuis des décennies (BLAS, LAPACK) sur lesquelles reposent NumPy et SciPy.'
        ],
        'url': 'https://fortran-lang.org',
        'badge': ('Fortran', 'https://img.shields.io/badge/Fortran-734F96?style=for-the-badge&logo=fortran&logoColor=white', 'Langages Systèmes & Bas Niveau')
    },
    'ada': {
        'name': 'Ada',
        'histoire': [
            '1980 : conçu par l’équipe de Jean Ichbiah (CII Honeywell Bull) pour répondre à un appel d’offres strict du Département de la Défense américain (DoD).',
            '1983 : normalisation officielle ANSI/MIL-STD-1815A, nommé en hommage à Ada Lovelace, première programmeuse de l’histoire.',
            '1995 : Ada 95 devient le premier langage orienté objet officiellement standardisé par l’ISO.',
            '2012–2022 : Ada 2012 et Ada 2022 introduisent la vérification par contrats intégrée (aspects pré/post-conditions) et le parallélisme fin.',
            'Aujourd’hui : langage de référence absolue pour les systèmes embarqués critiques à haute intégrité (avionique, ferroviaire, spatial).'
        ],
        'utilite': [
            'Langage structuré à typage statique très strict conçu pour la fiabilité, la maintenabilité et la détection d’erreurs à la compilation.',
            'Intègre nativement les mécanismes de concurrence sécurisée (tâches et objets protégés) sans dépendance à une bibliothèque externe.',
            'Prend en charge la programmation par contrats et la vérification formelle de code via le sous-ensemble prouvable SPARK.',
            'Utilisé dans le contrôle de vol (Airbus, Boeing), les métros automatiques sans conducteur, les satellites et centrales nucléaires.',
            'Élimine par construction des catégories entières de bugs critiques grâce à un contrôle sévère des plages de valeurs et de types.'
        ],
        'url': 'https://www.adacore.com',
        'badge': ('Ada', 'https://img.shields.io/badge/Ada-02F0C2?style=for-the-badge&logo=ada&logoColor=black', 'Langages Systèmes & Bas Niveau')
    },
    'pascal': {
        'name': 'Pascal',
        'histoire': [
            '1970 : créé par le professeur Niklaus Wirth à l’ETH Zurich pour enseigner la programmation structurée et la conception rigoureuse.',
            '1983 : lancement de Turbo Pascal par Philippe Kahn chez Borland, révolutionnant le développement sur PC par sa vitesse de compilation fulgurante.',
            '1995 : évolution vers Object Pascal avec la sortie de Borland Delphi, apportant la conception visuelle d’interfaces (RAD).',
            'Années 2000 : émergence de projets open source majeurs comme Free Pascal et l’environnement de développement Lazarus.',
            'Aujourd’hui : utilisé dans les systèmes industriels, l’éducation et les applications de gestion natives multiplateformes.'
        ],
        'utilite': [
            'Langage impératif et structuré favorisant une syntaxe claire, lisible et un typage fort pour prévenir les erreurs.',
            'Compilateur extrêmement rapide produisant des binaires natifs compacts et autonomes sans dépendance externe lourde.',
            'Dispose de capacités orientées objet complètes via Object Pascal / Free Pascal.',
            'Permet le développement rapide d’applications de bureau riches (desktop GUI) avec Lazarus et Delphi.',
            'Apprécié pour la stabilité logicielle à très long terme et la maintenance de code patrimonial.'
        ],
        'url': 'https://www.freepascal.org',
        'badge': ('Pascal', 'https://img.shields.io/badge/Pascal-00549D?style=for-the-badge&logo=delphi&logoColor=white', 'Langages Systèmes & Bas Niveau')
    },
    'odin': {
        'name': 'Odin',
        'histoire': [
            '2016 : initié par Ginger Bill comme langage système alternatif au C, inspiré des principes de programmation orientée données (Data-Oriented Design).',
            '2020 : adoption croissante au sein des communautés de développement de moteurs de jeux vidéo indépendants et de graphisme.',
            '2023 : choix d’Odin pour le développement de logiciels commerciaux notables (notamment le moteur du jeu vidéo Emberward).',
            '2024+ : enrichissement continu de la bibliothèque standard (fonctions mathématiques SIMD, bindings Vulkan/DirectX/Metal natifs).',
            'Aujourd’hui : langage système apprécié pour sa simplicité radicale, sa transparence et son adéquation avec les architectures modernes de processeurs.'
        ],
        'utilite': [
            'Langage de programmation système moderne pensé pour la haute performance et le contrôle précis de la mémoire.',
            'Refuse la complexité orientée objet au profit de structures de données explicites et de procédures composables.',
            'Offre des fonctionnalités de programmation contextuelle (allocateur passé implicitement via context).',
            'Conçu sur mesure pour les moteurs de jeux vidéo, le rendu graphique 3D temps réel et les outils de création numérique.',
            'Intègre nativement les types matriciels, les tableaux dynamiques légers et la manipulation de mémoire brute.'
        ],
        'url': 'https://odin-lang.org',
        'badge': ('Odin', 'https://img.shields.io/badge/Odin-1A2B3C?style=for-the-badge&logo=odin&logoColor=white', 'Langages Systèmes & Bas Niveau')
    },
    'v': {
        'name': 'V',
        'histoire': [
            '2019 : créé par Alexander Medvednikov pour développer le client de messagerie Volt, puis publié en open source.',
            '2020 : montée en popularité rapide grâce à ses promesses de compilation ultra-rapide (plus d’un million de lignes/seconde) et d’absence de dépendances.',
            '2022 : ajout d’un traducteur automatique C vers V et amélioration du modèle de gestion de mémoire automatique sans GC.',
            '2024+ : expansion de l’écosystème d’interface graphique multiplateforme native (V UI / Véditor).',
            'Aujourd’hui : langage compilé simple et rapide, combinant syntaxe épurée et génération de binaires C/natifs.'
        ],
        'utilite': [
            'Langage statiquement typé visant une simplicité syntaxique proche de Go avec la rapidité d’exécution du C.',
            'Garantit l’immutabilité des variables et la non-nullité des pointeurs par défaut.',
            'Propose une gestion mémoire sans garbage collector basée sur l’analyse statique autofree et le comptage de références.',
            'Permet la compilation vers du C lisible, des binaires natifs ou du code JavaScript.',
            'Utilisé pour les outils en ligne de commande (CLI), les applications graphiques légères et les microservices réseau.'
        ],
        'url': 'https://vlang.io',
        'badge': ('V', 'https://img.shields.io/badge/V-4F80AA?style=for-the-badge&logo=v&logoColor=white', 'Langages Systèmes & Bas Niveau')
    },
    'java': {
        'name': 'Java',
        'histoire': [
            '1995 : créé par James Gosling chez Sun Microsystems avec la promesse "Write Once, Run Anywhere" (WORA) via la machine virtuelle JVM.',
            '1999–2004 : essor de Java 2 Enterprise Edition (J2EE) et Java 5 (génériques, annotations, énumérations, boucle for-each).',
            '2010 : rachat de Sun Microsystems par Oracle Corporation.',
            '2014–2017 : Java 8 révolutionne le langage (lambdas, Streams API) et Java 9 adopte le système de modules (Project Jigsaw).',
            'Aujourd’hui : cycle de publication semestriel stable avec versions LTS régulières (Java 17, Java 21+ avec threads virtuels Project Loom).'
        ],
        'utilite': [
            'Langage orienté objet fortement typé exécuté sur la JVM, garantissant portabilité, gestion automatique de mémoire (GC) et sécurité.',
            'Épine dorsale des systèmes d’information bancaires, des infrastructures d’entreprise et du commerce électronique mondial.',
            'Dispose du plus vaste écosystème de bibliothèques et frameworks d’entreprise (Spring Boot, Quarkus, Micronaut).',
            'Moteur de référence pour le Big Data et le traitement distribué à grande échelle (Apache Hadoop, Spark, Kafka, Flink).',
            'Reste le socle historique du développement d’applications mobiles natives pour la plateforme Android.'
        ],
        'url': 'https://www.oracle.com/java/',
        'badge': ('Java', 'https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=java&logoColor=white', 'Langages Applicatifs & Entreprise')
    },
    'csharp': {
        'name': 'C#',
        'histoire': [
            '2000–2002 : conçu par Anders Hejlsberg chez Microsoft comme langage phare du framework .NET.',
            '2007 : C# 3.0 introduit LINQ (Language Integrated Query) et les expressions lambdas, transformant la manipulation de données.',
            '2014 : virage stratégique vers l’open source avec le compilateur Roslyn et l’annonce du runtime multiplateforme .NET Core.',
            '2020–2023 : unification de l’écosystème avec .NET 5 à .NET 8 (records, pattern matching avancé, performances d’exécution records).',
            'Aujourd’hui : langage moderne et polyvalent majeur (C# 12/13), leader dans le cloud, le jeu vidéo et les applications d’entreprise.'
        ],
        'utilite': [
            'Langage multi-paradigme (objet, fonctionnel, asynchrone) typé statiquement et optimisé pour la productivité et la vitesse.',
            'S’appuie sur le runtime performant .NET (CLR) avec compilation JIT et Ahead-Of-Time (Native AOT).',
            'Moteur de prédilection pour le développement de jeux vidéo 2D/3D et de réalité virtuelle via le moteur Unity.',
            'Utilisé pour bâtir des API cloud scalables (ASP.NET Core), des microservices et des applications web fullstack (Blazor).',
            'Permet la création d’applications desktop et mobiles multiplateformes via .NET MAUI et Avalonia UI.'
        ],
        'url': 'https://dotnet.microsoft.com/languages/csharp',
        'badge': ('C#', 'https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=csharp&logoColor=white', 'Langages Applicatifs & Entreprise')
    },
    'kotlin': {
        'name': 'Kotlin',
        'histoire': [
            '2011 : dévoilé par JetBrains pour combler les lourdeurs de Java tout en garantissant une interopérabilité totale à 100 % sur la JVM.',
            '2016 : publication de la version stable Kotlin 1.0.',
            '2017–2019 : Google annonce Kotlin comme langage de premier rang, puis langage officiellement recommandé pour Android.',
            '2021+ : émergence de Kotlin Multiplatform (KMP) pour partager la logique métier entre iOS, Android, Desktop et Web.',
            'Aujourd’hui : nouveau compilateur K2 ultra-rapide (Kotlin 2.0+), langage moderne plébiscité sur mobile et backend.'
        ],
        'utilite': [
            'Langage concis et expressif éliminant par conception les erreurs de pointeurs nuls grâce au système de types null-safe.',
            'Gère les opérations asynchrones complexes de manière élégante et légère via les coroutines.',
            'Interopérabilité transparente et bidirectionnelle sans friction avec tout le code et les bibliothèques Java existants.',
            'Standard officiel de l’industrie pour le développement d’applications mobiles Android modernes (Jetpack Compose).',
            'De plus en plus adopté côté backend avec Spring Boot, Ktor et pour le partage de code multiplateforme (KMP).'
        ],
        'url': 'https://kotlinlang.org',
        'badge': ('Kotlin', 'https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white', 'Langages Applicatifs & Entreprise')
    },
    'groovy': {
        'name': 'Groovy',
        'histoire': [
            '2003 : initié par James Strachan et Bob McWhirter comme langage dynamique pour la plateforme Java.',
            '2007 : adoption par la communauté Java et émergence du framework web Grails.',
            '2015 : transfert officiel du projet à la fondation Apache, devenant Apache Groovy.',
            '2020–2022 : versions 3 et 4 apportant le nouveau parseur Parrot et une intégration étroite des fonctionnalités modernes de la JVM.',
            'Aujourd’hui : langage de script et d’automatisation incontournable des pipelines d’intégration continue (CI/CD).'
        ],
        'utilite': [
            'Langage dynamique et optionnellement typé s’intégrant de façon native et transparente avec le code Java.',
            'Syntaxe concise et expressive simplifiant l’écriture de DSL (Domain-Specific Languages).',
            'Moteur d’écriture de référence pour les scripts d’automatisation de build Gradle.',
            'Langage des pipelines complexes d’intégration continue et de déploiement sous Jenkins (Jenkinsfile).',
            'Utilisé pour les tests unitaires et d’intégration expressifs avec le framework Spock.'
        ],
        'url': 'https://groovy-lang.org',
        'badge': ('Groovy', 'https://img.shields.io/badge/Groovy-4298B8?style=for-the-badge&logo=apachegroovy&logoColor=white', 'Langages Applicatifs & Entreprise')
    },
    'swift': {
        'name': 'Swift',
        'histoire': [
            '2010–2014 : initié par Chris Lattner chez Apple pour remplacer Objective-C par un langage moderne, sûr et rapide.',
            '2015 : ouverture du projet en open source et portage sur les systèmes Linux.',
            '2019 : introduction du framework d’interface déclaratif SwiftUI et stabilisation de l’ABI.',
            '2021 : ajout d’un modèle de concurrence moderne natif (async/await, acteurs, isolation des tâches).',
            'Aujourd’hui : Swift 6 apporte la garantie stricte de concurrence sûre par analyse statique (data race safety).'
        ],
        'utilite': [
            'Langage compilé puissant à typage statique fort, inférence de types et gestion automatique de mémoire par ARC.',
            'Langage officiel exclusif pour le développement d’applications sur l’ensemble des plateformes Apple (iOS, macOS, watchOS, visionOS).',
            'Élimine de larges classes de bugs grâce à la gestion obligatoire des optionnels et la sécurité des accès mémoire.',
            'Permet la création d’interfaces déclaratives réactives avec SwiftUI.',
            'S’étend aux serveurs web légers et microservices haute performance (Swift on Server via Vapor).'
        ],
        'url': 'https://www.swift.org',
        'badge': ('Swift', 'https://img.shields.io/badge/Swift-F05138?style=for-the-badge&logo=swift&logoColor=white', 'Langages Applicatifs & Entreprise')
    },
    'objective-c': {
        'name': 'Objective-C',
        'histoire': [
            '1983–1984 : créé par Brad Cox et Tom Love chez Stepstone en ajoutant la transmission de messages inspirée de Smalltalk au langage C.',
            '1988 : licencié par NeXT de Steve Jobs pour devenir le langage fondamental du système d’exploitation NeXTSTEP.',
            '1996 : NeXT est racheté par Apple, faisant d’Objective-C le socle de Mac OS X, Cocoa et de l’iPhone OS (iOS).',
            '2011 : introduction du comptage automatique de références (ARC) simplifiant la gestion mémoire.',
            'Aujourd’hui : langage patrimonial mature et stable, progressivement remplacé par Swift mais conservé dans les frameworks historiques d’Apple.'
        ],
        'utilite': [
            'Sur-ensemble strict du C ajoutant une orientation objet dynamique basée sur l’envoi de messages à l’exécution (runtime dynamic dispatch).',
            'Dispose d’une compatibilité binaire immédiate et absolue avec le code source C et C++ (via Objective-C++).',
            'Fondation sur laquelle ont été bâtis tous les frameworks historiques d’Apple (Foundation, AppKit, UIKit).',
            'Permet la modification dynamique des classes et méthodes au moment de l’exécution (method swizzling).',
            'Utilisé pour maintenir et interfacer des bases de code natives existantes sur macOS et iOS.'
        ],
        'url': 'https://developer.apple.com/documentation/objectivec',
        'badge': ('Objective-C', 'https://img.shields.io/badge/Objective--C-000000?style=for-the-badge&logo=apple&logoColor=white', 'Langages Applicatifs & Entreprise')
    },
    'perl': {
        'name': 'Perl',
        'histoire': [
            '1987 : créé par Larry Wall comme outil de manipulation de fichiers texte et de génération de rapports pour Unix.',
            '1994 : sortie de Perl 5, réécriture fondamentale introduisant l’orienté objet, les modules et le gestionnaire CPAN.',
            'Années 1990–2000 : surnommé "le ruban adhésif d’Internet", moteur incontournable des premiers scripts web dynamiques (CGI).',
            '2019 : séparation claire de la branche Perl 6 (devenue le langage distinct Raku) pour pérenniser l’évolution de Perl 5.',
            'Aujourd’hui : langage stable (Perl 5.40+), reconnu pour la puissance de ses expressions régulières et sa fiabilité système.'
        ],
        'utilite': [
            'Langage interprété puissant optimisé pour le traitement de texte complexe, le parsing et l’administration système.',
            'Intègre le moteur d’expressions régulières (regex) le plus complet et influent de l’histoire de l’informatique (PCRE).',
            'Dispose de l’archive CPAN, l’un des plus anciens et vastes répertoires de bibliothèques open source au monde.',
            'Utilisé pour l’automatisation de scripts d’infrastructure Unix, le nettoyage de données et les pipelines bioinformatiques.',
            'Permet le prototypage rapide grâce à sa philosophie emblématique : "There is more than one way to do it" (TMTOWTDI).'
        ],
        'url': 'https://www.perl.org',
        'badge': ('Perl', 'https://img.shields.io/badge/Perl-39457E?style=for-the-badge&logo=perl&logoColor=white', 'Langages Web & Scripting Dynamique')
    },
    'lua': {
        'name': 'Lua',
        'histoire': [
            '1993 : conçu par Roberto Ierusalimschy, Luiz Henrique de Figueiredo et Waldemar Celes à l’Université PUC-Rio au Brésil.',
            'Années 2000 : adoption massive comme langage de script d’extension dans les moteurs de jeux vidéo (World of Warcraft, CryEngine).',
            '2011 : création du compilateur JIT ultra-rapide LuaJIT par Mike Pall, atteignant des vitesses proches du code C natif.',
            '2015–2020 : Lua 5.3 et 5.4 introduisent le support des entiers 64 bits natifs et les variables à portée déterministe (<close>).',
            'Aujourd’hui : standard mondial incontournable pour l’embarquement dans les applications hôtes (Redis, Nginx, Neovim).'
        ],
        'utilite': [
            'Langage de script léger, rapide et compact conçu spécifiquement pour être intégré (embedded) dans des programmes C/C++.',
            'Empreinte mémoire minuscule (interpréteur complet de moins de 300 Ko) facilitant son intégration dans l’embarqué et l’IoT.',
            'S’appuie sur une structure de données unique et hautement polyvalente : les tables associatives.',
            'Moteur de scripting de référence pour les jeux vidéo (Roblox, LÖVE 2D), les serveurs web (OpenResty/Nginx) et bases NoSQL (Redis).',
            'Permet la configuration et l’extension de logiciels de pointe comme l’éditeur de code Neovim.'
        ],
        'url': 'https://www.lua.org',
        'badge': ('Lua', 'https://img.shields.io/badge/Lua-2C2D72?style=for-the-badge&logo=lua&logoColor=white', 'Langages Web & Scripting Dynamique')
    },
    'tcl': {
        'name': 'Tcl',
        'histoire': [
            '1988 : créé par John Ousterhout à l’Université de Berkeley pour unifier les langages de commande de logiciels de CAO électronique.',
            '1991 : ajout de Tk (Tcl/Tk), boîte à outils graphique permettant de créer des interfaces visuelles multiplateformes en quelques lignes.',
            'Années 1990 : adoption stratégique par l’industrie des semi-conducteurs et des réseaux de télécommunication (Cisco).',
            '2000–2020 : évolutions vers Tcl 8.6 apportant l’orientation objet native (TclOO) et les coroutines de flux.',
            'Aujourd’hui : Tcl/Tk 9.0 modernise le standard avec un support 64 bits complet et UTF-8 universel.'
        ],
        'utilite': [
            'Langage de script dynamique où tout élément (y compris le code et les structures de contrôle) est manipulable comme une chaîne de caractères.',
            'Permet l’intégration et l’extension immédiate d’applications C via une API C d’une grande simplicité.',
            'Standard universel de facto pour le pilotage et l’automatisation des suites de conception électronique (EDA, FPGA, Synopsys, Xilinx).',
            'Fournit l’infrastructure graphique Tk utilisée notamment pour les outils graphiques de base de Git (gitk, git-gui) et Python (IDLE).',
            'Utilisé pour les bancs de tests automatisés et le scripting d’équipements réseaux industriels.'
        ],
        'url': 'https://www.tcl-lang.org',
        'badge': ('Tcl', 'https://img.shields.io/badge/Tcl-145B94?style=for-the-badge&logo=tcl&logoColor=white', 'Langages Web & Scripting Dynamique')
    },
    'powershell': {
        'name': 'PowerShell',
        'histoire': [
            '2006 : créé par Jeffrey Snover et Microsoft sous le nom de code "Monad" pour révolutionner l’administration système sous Windows.',
            '2009–2012 : versions 2.0 et 3.0 intégrées nativement dans Windows et Windows Server avec le remoting WinRM.',
            '2016 : Microsoft publie le code source en open source sous le nom PowerShell Core, assurant son portage sur Linux et macOS.',
            '2020+ : fusion officielle dans la gamme moderne PowerShell 7+ basée sur le runtime .NET Core.',
            'Aujourd’hui : outil central d’automatisation, de configuration cloud et d’administration multiplateforme.'
        ],
        'utilite': [
            'Shell en ligne de commande et langage de script orienté objets manipulant des objets .NET structurés plutôt que du texte brut.',
            'Dispose d’un écosystème de commandes standardisées (cmdlets) suivant une convention stricte Verbe-Nom (Get-Process, Set-Item).',
            'Intègre un système puissant de pipeline passant directement des flux d’objets avec leurs propriétés et méthodes typées.',
            'Indispensable pour l’administration des infrastructures cloud Microsoft Azure, Active Directory et Microsoft 365.',
            'Permet la gestion de configuration déclarative de parcs de serveurs via PowerShell DSC (Desired State Configuration).'
        ],
        'url': 'https://learn.microsoft.com/powershell/',
        'badge': ('PowerShell', 'https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white', 'Langages Web & Scripting Dynamique')
    },
    'haskell': {
        'name': 'Haskell',
        'histoire': [
            '1990 : conçu par un comité international de chercheurs académiques pour créer un langage fonctionnel pur et ouvert.',
            '1998 : publication du rapport Haskell 98 stabilisant la définition formelle du langage.',
            'Années 2000 : le compilateur GHC (Glasgow Haskell Compiler) devient le moteur de référence et d’innovation continue.',
            '2010 : publication de la norme Haskell 2010 introduisant l’interface de fonctions étrangères (FFI) standardisée.',
            'Aujourd’hui : référence théorique et industrielle pour le typage avancé, la vérification formelle et l’analyse statique.'
        ],
        'utilite': [
            'Langage purement fonctionnel à évaluation paresseuse (lazy evaluation) et typage statique fort inféré (système Hindley-Milner).',
            'Isole strictement les effets de bord (I/O, état mutable) du code pur grâce au concept de monades.',
            'Permet d’exprimer des abstractions mathématiques complexes avec des garanties formelles de correction à la compilation.',
            'Utilisé dans le secteur financier pour la modélisation de risques, l’écriture de compilateurs et la recherche en théorie des types.',
            'Moteur de développement de logiciels renommés comme Pandoc et xmonad.'
        ],
        'url': 'https://www.haskell.org',
        'badge': ('Haskell', 'https://img.shields.io/badge/Haskell-5D4F85?style=for-the-badge&logo=haskell&logoColor=white', 'Langages Fonctionnels & Déclaratifs')
    },
    'ocaml': {
        'name': 'OCaml',
        'histoire': [
            '1996 : créé par Xavier Leroy, Damien Doligez et l’équipe Cristal de l’INRIA en France, unifiant Caml avec l’orienté objet.',
            'Années 2000 : adoption par l’industrie financière (Jane Street) et pour l’écriture d’outils d’analyse de code statique.',
            '2014 : création de projets d’envergure comme le système de paquets OPAM et le compilateur ReasonML chez Meta.',
            '2022 : sortie historique d’OCaml 5.0 introduisant le parallélisme multicœur natif et les gestionnaires d’effets algébriques (effect handlers).',
            'Aujourd’hui : pilier de l’ingénierie formelle, de l’analyse statique de programmes et des systèmes critiques.'
        ],
        'utilite': [
            'Langage fonctionnel et impératif typé statiquement produisant des binaires natifs ultra-rapides et compacts.',
            'Dispose d’un système de modules et de foncteurs paramétriques parmi les plus puissants de l’informatique.',
            'Fournit une inférence de type complète évitant d’avoir à annoter manuellement chaque variable.',
            'Utilisé pour construire des compilateurs (Rust a initialement été prototypé en OCaml), des assistants de preuve (Coq) et du trading quantitatif.',
            'Idéal pour l’analyse formelle et la vérification de logiciels industriels (Astrée, Frama-C).'
        ],
        'url': 'https://ocaml.org',
        'badge': ('OCaml', 'https://img.shields.io/badge/OCaml-EC6813?style=for-the-badge&logo=ocaml&logoColor=white', 'Langages Fonctionnels & Déclaratifs')
    },
    'elixir': {
        'name': 'Elixir',
        'histoire': [
            '2012 : créé par José Valim (ancien membre de l’équipe Ruby on Rails) chez Plataformatec pour moderniser l’accès à la machine virtuelle BEAM.',
            '2014 : sortie de la version 1.0 et essor du framework web Phoenix.',
            '2018–2020 : intégration de Phoenix LiveView, révolutionnant le développement d’interfaces web temps réel sans JavaScript complexe.',
            '2022+ : expansion vers le calcul numérique, l’intelligence artificielle et le machine learning avec les projets Nx et Livebook.',
            'Aujourd’hui : technologie de référence pour les systèmes temps réel massivement distribués et tolérants aux pannes.'
        ],
        'utilite': [
            'Langage fonctionnel dynamique s’exécutant sur la machine virtuelle Erlang (BEAM) et bénéficiant de son modèle d’acteurs (OTP).',
            'Offre une syntaxe élégante et productive inspirée de Ruby tout en conservant l’immutabilité et le pattern matching.',
            'Prend en charge la métaprogrammation avancée par macros grâce à la représentation du code en structures de données natives.',
            'Conçu pour gérer des millions de connexions concurrentes simultanées (chats, plateformes de streaming, IoT, télécoms).',
            'Permet de concevoir des systèmes auto-cicatrisants capables de redémarrer automatiquement les processus en échec sans interruption.'
        ],
        'url': 'https://elixir-lang.org',
        'badge': ('Elixir', 'https://img.shields.io/badge/Elixir-4B275F?style=for-the-badge&logo=elixir&logoColor=white', 'Langages Fonctionnels & Déclaratifs')
    },
    'erlang': {
        'name': 'Erlang',
        'histoire': [
            '1986 : développé par Joe Armstrong, Robert Virding et Mike Williams au laboratoire informatique d’Ericsson.',
            '1998 : publié en open source par Ericsson, marquant le début de son adoption industrielle internationale.',
            'Années 2000 : déploiement comme infrastructure dorsale de commutation téléphonique et de messageries massives (WhatsApp, RabbitMQ).',
            '2016–2020 : intégration d’un compilateur JIT natif ultra-performant dans le runtime OTP (Erlang/OTP 24+).',
            'Aujourd’hui : norme industrielle d’excellence pour la haute disponibilité ("neuf 9" de fiabilité : 99.9999999%).'
        ],
        'utilite': [
            'Langage fonctionnel concurrent basé sur le modèle d’acteurs et des processus légers isolés sans mémoire partagée.',
            'Intègre la philosophie "Let it crash" via des arbres de supervision hiérarchiques redémarrant les composants défaillants.',
            'Permet la mise à jour de code à chaud en production (hot code reloading) sans interruption de service.',
            'Moteur de systèmes de courtage de messages distribués (RabbitMQ, EMQX) et de serveurs de messagerie instantanée.',
            'Offre une distribution transparente permettant à des nœuds sur des machines distinctes de communiquer nativement.'
        ],
        'url': 'https://www.erlang.org',
        'badge': ('Erlang', 'https://img.shields.io/badge/Erlang-A90533?style=for-the-badge&logo=erlang&logoColor=white', 'Langages Fonctionnels & Déclaratifs')
    },
    'clojure': {
        'name': 'Clojure',
        'histoire': [
            '2007 : conçu par Rich Hickey comme un dialecte moderne et dynamique de Lisp conçu pour la machine virtuelle Java (JVM).',
            '2011 : lancement de ClojureScript, permettant de compiler Clojure vers JavaScript pour le développement web front-end.',
            '2015–2020 : adoption dans l’industrie de la fintech et du traitement d’événements en temps réel.',
            '2022+ : stabilisation des outils de développement interactif avec REPL (Read-Eval-Print Loop) et de la bibliothèque spec.',
            'Aujourd’hui : langage fonctionnel majeur prônant la simplicité, les structures de données persistantes et le développement interactif.'
        ],
        'utilite': [
            'Dialecte Lisp fonctionnel doté d’une syntaxe homoiconique (le code est représenté sous forme de données Lisp).',
            'Propose par défaut des structures de données immuables et persistantes à partage structurel efficace.',
            'Gère la concurrence de manière déterministe grâce à la mémoire transactionnelle logicielle (Software Transactional Memory - STM).',
            'Bénéficie d’un accès complet et immédiat à l’ensemble de l’écosystème Java et de ses bibliothèques.',
            'Idéal pour le développement exploratoire ultra-rapide grâce à un flux de travail centré sur le REPL connecté à l’application en cours.'
        ],
        'url': 'https://clojure.org',
        'badge': ('Clojure', 'https://img.shields.io/badge/Clojure-5881D8?style=for-the-badge&logo=clojure&logoColor=white', 'Langages Fonctionnels & Déclaratifs')
    },
    'common-lisp': {
        'name': 'Common Lisp',
        'histoire': [
            '1958–1984 : standardisé dans les années 1980 pour fédérer les multiples dialectes Lisp dérivés des travaux initiaux de John McCarthy (1958).',
            '1994 : publication de la norme officielle ANSI X3.226-1994, devenant le premier standard officiel Lisp.',
            'Années 1990 : pionnier absolu des systèmes de macros hygiéniques, du typage dynamique et de la compilation incrémentale.',
            '2000+ : développement d’implémentations compilées natives open source ultra-performantes (SBCL, CCL).',
            'Aujourd’hui : standard industriel historique et vivant, référence indémodable de la métaprogrammation et de l’intelligence artificielle symbolique.'
        ],
        'utilite': [
            'Langage multi-paradigme homoiconique offrant le système de macros le plus puissant et expressif de l’informatique.',
            'Intègre le Common Lisp Object System (CLOS), système orienté objet avancé avec multi-dispatch et modificateurs de méthodes.',
            'Permet la modification interactive du programme en cours d’exécution sans redémarrage via un système de conditions et redémarrages (condition system).',
            'Compilateurs modernes (comme SBCL) produisant du code machine natif hautement optimisé comparable au C.',
            'Utilisé dans l’ingénierie aérospatiale (NASA), la CAO, le routage algorithmique et la synthèse audio.'
        ],
        'url': 'https://common-lisp.net',
        'badge': ('Common Lisp', 'https://img.shields.io/badge/Common_Lisp-000000?style=for-the-badge&logo=lisp&logoColor=white', 'Langages Fonctionnels & Déclaratifs')
    },
    'scheme': {
        'name': 'Scheme',
        'histoire': [
            '1975 : créé par Guy L. Steele et Gerald Jay Sussman au MIT AI Lab pour explorer les modèles d’acteurs et la sémantique de programmation.',
            '1978–1998 : publication des célèbres rapports révisés sur le langage algorithmique Scheme (de R1RS à R5RS).',
            '1985 : publication du manuel d’informatique légendaire "SICP" (Structure and Interpretation of Computer Programs) basé sur Scheme.',
            '2007–2013 : scission constructive entre R6RS (orienté applications industrielles) et R7RS (fidèle à la simplicité minimaliste du noyau).',
            'Aujourd’hui : modèle de pureté pédagogique et conceptuelle, intégré dans des systèmes de configuration et d’extension (GNU Guile, Guix).'
        ],
        'utilite': [
            'Dialecte Lisp minimaliste appliquant rigoureusement la portée lexicale statique et l’optimisation obligatoire des appels terminaux (tail-call optimization).',
            'Traite les procédures comme des citoyens de première classe (first-class citizens) avec fermetures lexicales complètes.',
            'Intègre le mécanisme des continuations de première classe via call-with-current-continuation (call/cc).',
            'Utilisé comme moteur d’extension de logiciels libres majeurs (GNU GIMP via Script-Fu, distribution GNU Guix).',
            'Langage de référence dans la recherche académique sur les langages de programmation et la sémantique formelle.'
        ],
        'url': 'https://www.scheme.org',
        'badge': ('Scheme', 'https://img.shields.io/badge/Scheme-7D7D7D?style=for-the-badge&logo=scheme&logoColor=white', 'Langages Fonctionnels & Déclaratifs')
    },
    'racket': {
        'name': 'Racket',
        'histoire': [
            '1995 : initié par Matthias Felleisen et son équipe sous le nom initial de PLT Scheme à l’Université Rice.',
            '2010 : émancipation de Scheme et adoption du nom Racket pour refléter sa nature de méta-langage pour concevoir des langages.',
            '2018 : projet Racket on Chez Scheme (CS) remplaçant la machine virtuelle historique en C par Chez Scheme pour un gain de performances massif.',
            '2021+ : adoption officielle de Racket CS comme moteur par défaut de la distribution.',
            'Aujourd’hui : plateforme de référence mondiale pour l’ingénierie des langages dédiés (Language-Oriented Programming).'
        ],
        'utilite': [
            'Langage multi-paradigme et plateforme permettant de créer de nouveaux langages de programmation complets via la directive #lang.',
            'Dispose du système de macros syntaxiques le plus avancé du monde Lisp (système de syntax-parse et d’hygiène lexicale).',
            'Fournit un environnement de développement intégré prêt à l’emploi (DrRacket) et une riche bibliothèque standard (GUI, graphisme, réseau).',
            'Permet la cohabitation transparente de sous-langages typés statiquement (Typed Racket) et paresseux (Lazy Racket).',
            'Utilisé pour l’éducation en informatique, la recherche formelle, l’écriture de DSLs métier et la production de scripts.'
        ],
        'url': 'https://racket-lang.org',
        'badge': ('Racket', 'https://img.shields.io/badge/Racket-3C5CAA?style=for-the-badge&logo=racket&logoColor=white', 'Langages Fonctionnels & Déclaratifs')
    },
    'fsharp': {
        'name': 'F#',
        'histoire': [
            '2005 : conçu par Don Syme chez Microsoft Research Cambridge comme adaptation moderne d’OCaml pour l’écosystème .NET.',
            '2010 : intégré comme langage de premier ordre dans Microsoft Visual Studio 2010.',
            '2014 : ouverture en open source sous la gouvernance de la F# Software Foundation.',
            '2020+ : intégration étroite avec les versions modernes de .NET (F# 6, 7, 8) et le développement web fullstack (Fable).',
            'Aujourd’hui : langage fonctionnel de référence sur la plateforme .NET, alliant rigueur mathématique et accès à l’écosystème C#.'
        ],
        'utilite': [
            'Langage fonctionnel typé statiquement avec inférence de type complète, immutabilité par défaut et pattern matching expressif.',
            'Intègre les fournisseurs de types (Type Providers), permettant d’extraire automatiquement des types vérifiés à partir de sources externes (JSON, SQL, CSV).',
            'Bénéficie d’une interopérabilité sans friction avec l’ensemble des bibliothèques et frameworks .NET.',
            'Permet la compilation vers JavaScript pour le front-end via le transpilateur Fable.',
            'Très utilisé dans la finance quantitative, la modélisation mathématique, l’analyse de données et les architectures backend robustes.'
        ],
        'url': 'https://fsharp.org',
        'badge': ('F#', 'https://img.shields.io/badge/F%23-378BBA?style=for-the-badge&logo=fsharp&logoColor=white', 'Langages Fonctionnels & Déclaratifs')
    },
    'elm': {
        'name': 'Elm',
        'histoire': [
            '2012 : conçu par Evan Czaplicki dans le cadre de sa thèse universitaire pour éliminer les erreurs à l’exécution sur le web.',
            '2016 : formalisation de "The Elm Architecture" (TEA), modèle architectural ayant directement inspiré Redux et l’état réactif moderne.',
            '2018 : version 0.19 optimisant drastiquement la taille des fichiers JS générés et la vitesse de compilation.',
            '2020+ : modèle de référence pour les messages d’erreur de compilateur clairs, pédagogiques et orientés développeur.',
            'Aujourd’hui : langage de niche reconnu pour sa promesse tenue : zéro exception d’exécution (zero runtime exceptions).'
        ],
        'utilite': [
            'Langage purement fonctionnel typé se compilant en JavaScript optimisé pour les interfaces utilisateur web.',
            'Garantit l’absence totale d’erreurs du type "undefined is not a function" à l’exécution grâce à son système de types stricts.',
            'Fournit l’architecture TEA native (Model-Update-View) gérant les événements de manière unidirectionnelle et déterministe.',
            'Propose le compilateur aux messages d’erreur les plus conviviaux et explicatifs de l’industrie logicielle.',
            'Utilisé pour créer des applications web front-end où la fiabilité et la maintenabilité sont des priorités absolues.'
        ],
        'url': 'https://elm-lang.org',
        'badge': ('Elm', 'https://img.shields.io/badge/Elm-1293D8?style=for-the-badge&logo=elm&logoColor=white', 'Langages Fonctionnels & Déclaratifs')
    },
    'purescript': {
        'name': 'PureScript',
        'histoire': [
            '2013 : créé par Phil Freeman comme un langage fortement inspiré de Haskell se compilant vers du code JavaScript lisible.',
            '2016–2019 : adoption par des équipes cherchant la rigueur de Haskell pour le développement front-end et back-end Node.js.',
            '2020 : création de backends alternatifs compilant vers C, C++, Go et Erlang.',
            '2022+ : version 0.15 stabilisant le système de modules et l’optimiseur de code intermédiaire.',
            'Aujourd’hui : alternative fonctionnelle pure à TypeScript pour les projets exigeant un typage statique absolu.'
        ],
        'utilite': [
            'Langage purement fonctionnel à évaluation stricte (eager evaluation) doté d’un système de types expressif dérivé de Haskell.',
            'Prend en charge les classes de types (type classes), les types d’ordres supérieurs (higher-kinded types) et les types de rangs multiples.',
            'Produit du code JavaScript propre sans runtime lourd, facilitant l’interopérabilité avec les bibliothèques JS existantes.',
            'Permet la gestion explicite des effets de bord via la monade Effect.',
            'Utilisé pour des applications web monopages complexes, des systèmes de traitement financier et des architectures serveur Node.js.'
        ],
        'url': 'https://www.purescript.org',
        'badge': ('PureScript', 'https://img.shields.io/badge/PureScript-1D222D?style=for-the-badge&logo=purescript&logoColor=white', 'Langages Fonctionnels & Déclaratifs')
    },
    'gleam': {
        'name': 'Gleam',
        'histoire': [
            '2016–2019 : créé par Louis Pilfold pour apporter la sûreté du typage statique à la machine virtuelle Erlang (BEAM).',
            '2022 : ajout d’un backend officiel compilant directement vers JavaScript et intégration avec l’écosystème Node.js et Deno.',
            '2024 : publication officielle de la version stable Gleam 1.0.',
            '2024+ : adoption enthousiaste par les communautés fonctionnelles à la recherche d’une alternative typée et moderne sur BEAM.',
            'Aujourd’hui : langage fonctionnel émergent en plein essor, combinant la robustesse d’Erlang et la clarté de Rust/Elm.'
        ],
        'utilite': [
            'Langage fonctionnel typé statiquement et sans valeurs nulles s’exécutant sur la VM Erlang ou dans un moteur JavaScript.',
            'Offre une inférence de types complète et des messages d’erreur de compilateur clairs et bienveillants.',
            'S’intègre sans friction avec les paquets et modules existants d’Erlang et d’Elixir.',
            'Bénéficie de la tolérance aux pannes, de la distribution et de la concurrence massive des processus légers BEAM.',
            'Idéal pour construire des API backend résilientes et des applications web fullstack typées de bout en bout.'
        ],
        'url': 'https://gleam.run',
        'badge': ('Gleam', 'https://img.shields.io/badge/Gleam-FFAFF3?style=for-the-badge&logo=gleam&logoColor=black', 'Langages Fonctionnels & Déclaratifs')
    },
    'crystal': {
        'name': 'Crystal',
        'histoire': [
            '2011–2014 : initié par Ary Borenszweig chez Manas.Tech pour créer un langage ayant l’élégance de Ruby et la vitesse du C.',
            '2017 : adoption du modèle de concurrence par fibres et canaux inspiré de CSP (Communication Sequential Processes).',
            '2021 : publication de la version stable Crystal 1.0 garantissant la stabilité du langage.',
            '2023+ : support natif officiel pour Windows, Linux et macOS et optimisation du ramasse-miettes BDWGC.',
            'Aujourd’hui : langage compilé mature apprécié pour son rapport imbattable entre expressivité syntaxique et performances brutes.'
        ],
        'utilite': [
            'Langage orienté objet compilé statiquement vers du code machine natif via l’infrastructure LLVM.',
            'Syntaxe quasiment identique à celle de Ruby avec inférence de types automatique globale.',
            'Contrôle strict des types nil à la compilation pour prévenir les plantages d’exécution.',
            'Intègre un système de macros puissant et une gestion de concurrence légère basée sur des fibres (fibers).',
            'Utilisé pour les microservices backend à haute vélocité, les outils CLI rapides et le web avec Lucky ou Kemal.'
        ],
        'url': 'https://crystal-lang.org',
        'badge': ('Crystal', 'https://img.shields.io/badge/Crystal-000000?style=for-the-badge&logo=crystal&logoColor=white', 'Langages Fonctionnels & Déclaratifs')
    },
    'r': {
        'name': 'R',
        'histoire': [
            '1993 : créé par Ross Ihaka et Robert Gentleman à l’Université d’Auckland en Nouvelle-Zélande comme implémentation open source du langage S.',
            '2000 : publication de la version stable R 1.0.0 par le R Core Team.',
            'Années 2010 : révolution de l’analyse de données avec l’émergence du Tidyverse (ggplot2, dplyr) créé par Hadley Wickham.',
            '2015+ : standardisation dans la recherche pharmaceutique, les biostatistiques et la science des données académique.',
            'Aujourd’hui : standard mondial incontesté de l’analyse statistique, de l’économétrie et de la visualisation de données.'
        ],
        'utilite': [
            'Langage et environnement interprété spécialement conçu pour le calcul statistique, la fouille de données et le graphisme.',
            'Fournit des structures de données natives pour les vecteurs, matrices, listes et tableaux de données (data frames).',
            'Dispose de l’immense répertoire de paquets scientifiques CRAN (Comprehensive R Archive Network).',
            'Outil de référence pour les études cliniques, l’épidémiologie, la bioinformatique et l’évaluation des politiques publiques.',
            'Permet la génération de rapports reproductibles et tableaux de bord interactifs (R Markdown, Quarto, Shiny).'
        ],
        'url': 'https://www.r-project.org',
        'badge': ('R', 'https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white', 'Langages Scientifiques & Données')
    },
    'julia': {
        'name': 'Julia',
        'histoire': [
            '2009–2012 : conçu au MIT par Jeff Bezanson, Stefan Karpinski, Viral B. Shah et Alan Edelman pour résoudre le "problème des deux langages" (coder en Python/R, optimiser en C/C++).',
            '2018 : publication de la version stable 1.0 lors de la conférence JuliaCon.',
            '2020 : entrée dans le club fermé des langages capables d’atteindre le petaflop de calcul sur supercalculateur.',
            '2023+ : Julia 1.10+ apporte des temps de compilation (Time To First Plot) drastiquement réduits et une gestion avancée des GPU.',
            'Aujourd’hui : langage de choix pour l’informatique scientifique de pointe, la modélisation climatique et l’apprentissage automatique différentiable.'
        ],
        'utilite': [
            'Langage dynamique de haut niveau conçu pour atteindre les performances du C grâce à la compilation JIT basée sur LLVM.',
            'S’appuie sur le multi-dispatch (multiple dispatch) comme paradigme central, permettant d’étendre le comportement des fonctions selon le type de tous leurs arguments.',
            'Prend en charge la programmation parallèle, le calcul distribué et l’accélération native sur GPU (CUDA, AMD, Apple Silicon).',
            'Utilisé pour la simulation aérospatiale (NASA), l’optimisation de réseaux électriques, l’astrophysique et la pharmacométrie.',
            'Intègre la différentiation automatique native pour le Scientific Machine Learning (SciML).'
        ],
        'url': 'https://julialang.org',
        'badge': ('Julia', 'https://img.shields.io/badge/Julia-9558B2?style=for-the-badge&logo=julia&logoColor=white', 'Langages Scientifiques & Données')
    },
    'matlab': {
        'name': 'MATLAB',
        'histoire': [
            '1984 : créé par Cleve Moler pour donner à ses étudiants un accès simple aux bibliothèques LINPACK et EISPACK sans programmer en Fortran.',
            '1984 : fondation de la société MathWorks par Jack Little et Cleve Moler pour commercialiser la plateforme.',
            '1990 : introduction de Simulink, environnement de simulation dynamique par schéma-blocs.',
            '2000–2020 : intégration massive de boîtes à outils (toolboxes) dédiées au traitement du signal, à l’automobile et à l’aérospatiale.',
            'Aujourd’hui : plateforme de référence dans l’ingénierie industrielle, le contrôle-commande et l’enseignement universitaire.'
        ],
        'utilite': [
            'Langage et environnement de calcul matriciel orienté ingénierie, simulation physique et traitement algorithmique.',
            'Fournit des milliers de fonctions mathématiques, d’optimisation, de traitement d’images et de télécommunications prêtes à l’emploi.',
            'Permet la modélisation de systèmes dynamiques et la génération automatique de code C/C++ embarqué certifiable (via Simulink).',
            'Standard omniprésent dans l’industrie automobile (ADAS, moteurs), l’aéronautique, la défense et les technologies médicales.',
            'Facilite le prototypage d’algorithmes grâce à des interfaces visuelles riches et des outils de tracé de données avancés.'
        ],
        'url': 'https://www.mathworks.com/products/matlab.html',
        'badge': ('MATLAB', 'https://img.shields.io/badge/MATLAB-0076A8?style=for-the-badge&logo=mathworks&logoColor=white', 'Langages Scientifiques & Données')
    },
    'sas': {
        'name': 'SAS',
        'histoire': [
            '1966–1976 : développé par Anthony Barr et James Goodnight à l’Université d’État de Caroline du Nord pour analyser des données agricoles.',
            '1976 : fondation de SAS Institute pour commercialiser le logiciel auprès des entreprises et gouvernements.',
            'Années 1980–2000 : standardisation mondiale dans les essais cliniques pharmaceutiques (normes FDA) et les institutions financières.',
            '2015+ : lancement de SAS Viya, plateforme cloud native d’analytique et d’intelligence artificielle.',
            'Aujourd’hui : environnement analytique propriétaire prédominant pour la conformité réglementaire et la gestion de risques bancaires.'
        ],
        'utilite': [
            'Langage procédural et système intégré pour la gestion, la manipulation de gros volumes de données et l’analyse statistique avancée.',
            'Structuré autour d’étapes de données (DATA steps) pour la transformation et d’étapes de procédures (PROC steps) pour l’analyse.',
            'Reconnu et exigé par les organismes de réglementation sanitaire (FDA, EMA) pour la validation des essais cliniques de médicaments.',
            'Utilisé pour le scoring de crédit bancaire, la détection de fraudes d’assurance et le marketing prédictif.',
            'Offre une stabilité et une traçabilité rigoureuse des calculs indispensables aux audits de conformité.'
        ],
        'url': 'https://www.sas.com',
        'badge': ('SAS', 'https://img.shields.io/badge/SAS-0077C8?style=for-the-badge&logo=sas&logoColor=white', 'Langages Scientifiques & Données')
    },
    'wolfram': {
        'name': 'Wolfram Language',
        'histoire': [
            '1988 : créé par le physicien Stephen Wolfram comme moteur symbolique de Mathematica.',
            '2009 : lancement du moteur de connaissances computationnelles Wolfram|Alpha reposant sur le langage.',
            '2014 : officialisation du nom "Wolfram Language" comme langage de programmation à part entière fondé sur la connaissance intégrée.',
            '2020+ : intégration avec les modèles d’IA générative comme moteur de calcul exact et de requêtage structuré.',
            'Aujourd’hui : langage computationnel unique intégrant des algorithmes avancés et des pétaoctets de données encyclopédiques curées.'
        ],
        'utilite': [
            'Langage multi-paradigme fondé sur la réécriture d’expressions symboliques et le calcul formel exact.',
            'Intègre nativement dans le langage des millions de données mondiales vérifiées (géographie, physique, histoire, finance, chimie).',
            'Permet la résolution exacte d’équations différentielles, l’algèbre symbolique et le traitement de tenseurs.',
            'Utilisé dans la recherche fondamentale en physique théorique, les mathématiques pures et la finance quantitative.',
            'Fournit l’infrastructure des carnets interactifs (Wolfram Notebooks), précurseurs directs de Jupyter.'
        ],
        'url': 'https://www.wolfram.com/language/',
        'badge': ('Wolfram', 'https://img.shields.io/badge/Wolfram-DD1100?style=for-the-badge&logo=wolfram&logoColor=white', 'Langages Scientifiques & Données')
    },
    'apl': {
        'name': 'APL',
        'histoire': [
            '1966 : créé par Kenneth E. Iverson chez IBM comme notation mathématique concise pour décrire les architectures matérielles et algorithmes.',
            '1970–1980 : adoption par les banques et sociétés d’investissement sur mainframes IBM.',
            '1990 : création de dialectes modernes par Morten Kromberg et Dyalog Ltd.',
            '2000+ : inspiration directe pour des langages matriciels dérivés (J, K, Q, BQN).',
            'Aujourd’hui : utilisé dans les systèmes financiers temps réel et le traitement de données volumineuses par des experts dédiés.'
        ],
        'utilite': [
            'Langage de programmation matriciel (array programming) utilisant un jeu de symboles typographiques et glyphes non-ASCII uniques.',
            'Permet d’exprimer des transformations complexes sur des tableaux multidimensionnels entiers sans boucle explicite.',
            'Favorise une densité de code exceptionnelle où des algorithmes entiers s’écrivent sur une seule ligne (one-liners).',
            'Utilisé dans le trading algorithmique, l’actuariat d’assurance, le calcul de risques et l’optimisation logistique.',
            'Offre une vitesse de calcul très élevée grâce à la vectorisation matérielle automatique de ses primitives.'
        ],
        'url': 'https://www.dyalog.com',
        'badge': ('APL', 'https://img.shields.io/badge/APL-00609C?style=for-the-badge&logo=dyalog&logoColor=white', 'Langages Scientifiques & Données')
    },
    'prolog': {
        'name': 'Prolog',
        'histoire': [
            '1972 : créé par Alain Colmerauer et Philippe Roussel à l’Université d’Aix-Marseille II en collaboration avec Robert Kowalski.',
            'Années 1980 : choisi par le gouvernement japonais comme langage central du projet national des ordinateurs de 5ᵉ génération.',
            '1995 : publication de la norme internationale ISO/IEC 13211-1.',
            '2000+ : développement d’implémentations open source puissantes comme SWI-Prolog et Scryer Prolog.',
            'Aujourd’hui : référence mondiale de la programmation par contraintes, du raisonnement automatique et du web sémantique.'
        ],
        'utilite': [
            'Langage de programmation logique déclaratif où les programmes sont constitués de faits et de règles logiques (clauses de Horn).',
            'Trouve automatiquement les solutions à un problème via un moteur d’unification et de retour sur trace (backtracking).',
            'Permet la programmation par contraintes (CLP) pour résoudre des problèmes combinatoires complexes.',
            'Utilisé pour les systèmes experts, l’analyse syntaxique de langues naturelles (Grammaires à Clauses Définies), la vérification de règles de sécurité et les ontologies.',
            'Appliqué à la résolution d’emplois du temps, à la planification logistique et au droit computationnel.'
        ],
        'url': 'https://www.swi-prolog.org',
        'badge': ('Prolog', 'https://img.shields.io/badge/Prolog-E44D26?style=for-the-badge&logo=prolog&logoColor=white', 'Langages Logiques & Formels')
    },
    'lean': {
        'name': 'Lean',
        'histoire': [
            '2013 : initié par Leonardo de Moura chez Microsoft Research pour créer un assistant de preuve interactif et un langage de programmation.',
            '2017 : essor de la bibliothèque mathématique communautaire Mathlib, formalisant des pans entiers des mathématiques modernes.',
            '2021 : réécriture complète avec Lean 4, devenant un langage compilé autonome et performant capable de s’auto-compiler.',
            '2023+ : utilisé par des médaillés Fields (Terence Tao) et des laboratoires de recherche en IA pour la formalisation et la vérification automatisée de théorèmes.',
            'Aujourd’hui : pointe de la recherche mondiale en mathématiques formelles et génération de code prouvé par IA.'
        ],
        'utilite': [
            'Assistant de preuve interactif et langage de programmation fonctionnel pur basé sur le calcul des constructions inductives (théorie des types dépendants).',
            'Permet d’écrire des théorèmes mathématiques et de vérifier leur démonstration avec une certitude absolue infaillible.',
            'Sert de langage de programmation généraliste rapide compilé vers le C.',
            'Utilisé pour la formalisation des mathématiques pures et la vérification de la correction de logiciels critiques.',
            'Sert de terrain d’entraînement privilégié pour les modèles d’intelligence artificielle résolvant des problèmes de raisonnement complexe (Olympiades de maths).'
        ],
        'url': 'https://lean-lang.org',
        'badge': ('Lean', 'https://img.shields.io/badge/Lean-2B2B2B?style=for-the-badge&logo=lean&logoColor=white', 'Langages Logiques & Formels')
    },
    'coq': {
        'name': 'Coq (Rocq)',
        'histoire': [
            '1984 : initié par Thierry Coquand et Gérard Huet à l’INRIA sous le nom de Coq (renommé officiellement "The Rocq Prover" en 2024).',
            '2005 : formalisation et démonstration intégrale du célèbre théorème des quatre couleurs par Georges Gonthier.',
            '2008 : création de CompCert, le premier compilateur C industriel mathématiquement prouvé exempt de bugs de compilation.',
            '2013 : formalisation du théorème de Feit-Thompson (théorème de l’ordre impair en théorie des groupes).',
            'Aujourd’hui : référence mondiale pour la certification logicielle critique et la recherche en sémantique formelle.'
        ],
        'utilite': [
            'Système formel de gestion de preuves basé sur le Calcul des Constructions Inductives et la correspondance de Curry-Howard (une preuve est un programme).',
            'Permet de certifier mathématiquement des algorithmes, protocoles de sécurité et compilateurs.',
            'Dispose de la commande d’extraction automatique générant du code OCaml, Haskell ou Scheme certifié conforme à la spécification.',
            'Utilisé pour la vérification de circuits cryptographiques, de cartes à puce bancaires et de micro-noyaux sécurisés.',
            'Fondement d’avancées majeures en sécurité des systèmes d’exploitation et langages de programmation formels.'
        ],
        'url': 'https://coq.inria.fr',
        'badge': ('Coq', 'https://img.shields.io/badge/Coq-C73B28?style=for-the-badge&logo=inria&logoColor=white', 'Langages Logiques & Formels')
    },
    'agda': {
        'name': 'Agda',
        'histoire': [
            '1999 : créé initialement par Catarina Coquand à l’Université de technologie Chalmers en Suède.',
            '2007 : réécriture complète en tant qu’Agda 2 par Ulf Norell, introduisant un assistant de preuve interactif orienté programmation.',
            '2015+ : exploration active de la théorie homotopique des types (Cubical Agda) et des types d’égalités supérieures.',
            '2020+ : utilisé comme langage d’enseignement universitaire de premier plan pour les types dépendants.',
            'Aujourd’hui : plateforme de recherche majeure pour la programmation avec types dépendants et la théorie des catégories computationnelles.'
        ],
        'utilite': [
            'Langage purement fonctionnel doté de types dépendants totaux (garantissant la terminaison des calculs).',
            'Permet d’encoder des invariants logiques complexes directement au sein des signatures de types.',
            'Offre un mode interactif puissant sous Emacs/VS Code pour construire du code et des preuves par complétion de trous (holes).',
            'Utilisé pour formaliser la sémantique de nouveaux langages de programmation et des structures algébriques avancées.',
            'Compilable vers Haskell ou JavaScript pour l’exécution de programmes prouvés.'
        ],
        'url': 'https://wiki.portal.chalmers.se/agda/pmwiki.php',
        'badge': ('Agda', 'https://img.shields.io/badge/Agda-293241?style=for-the-badge&logo=haskell&logoColor=white', 'Langages Logiques & Formels')
    },
    'idris': {
        'name': 'Idris',
        'histoire': [
            '2011 : créé par Edwin Brady à l’Université de St Andrews pour rendre la programmation avec types dépendants accessible pour le développement généraliste.',
            '2017 : publication du livre de référence "Type-Driven Development with Idris".',
            '2020 : sortie d’Idris 2, réécrit entièrement en Idris et s’appuyant sur la théorie des types quantitatifs (Quantitative Type Theory - QTT).',
            '2023+ : intégration avec des backends Chez Scheme, C, JavaScript et Node.js.',
            'Aujourd’hui : langage pionnier démontrant comment les types dépendants et les types linéaires transforment l’ingénierie logicielle au quotidien.'
        ],
        'utilite': [
            'Langage fonctionnel généraliste avec types dépendants complets et gestion des ressources à la compilation via types quantitatifs (QTT).',
            'Permet d’indiquer au compilateur combien de fois une variable peut être utilisée (0 fois pour les preuves pures, 1 fois pour les ressources linéaires, ou sans limite).',
            'Garantit à la compilation le respect absolu de protocoles d’états (machines à états finis, sockets, fichiers).',
            'Génère du code exécutable performant en effaçant totalement les preuves logiques lors de la phase d’émission.',
            'Idéal pour concevoir des logiciels réseau ultra-sécurisés, des parseurs certifiés et de la cryptographie.'
        ],
        'url': 'https://www.idris-lang.org',
        'badge': ('Idris', 'https://img.shields.io/badge/Idris-9400D3?style=for-the-badge&logo=idris&logoColor=white', 'Langages Logiques & Formels')
    },
    'vyper': {
        'name': 'Vyper',
        'histoire': [
            '2017 : initié par Vitalik Buterin et les contributeurs de la communauté Ethereum comme alternative sécurisée à Solidity.',
            '2019 : adoption de la syntaxe Pythonique et élimination délibérée des fonctionnalités jugées propices aux vulnérabilités (pas d’héritage, pas de récursion).',
            '2021 : publication de versions stables auditées et intégration dans les protocoles DeFi majeurs (Curve Finance).',
            '2023+ : optimisations de compilation pour réduire drastiquement la consommation de gaz des smart contracts sur l’EVM.',
            'Aujourd’hui : langage de smart contracts majeur sur Ethereum, réputé pour sa simplicité d’audit et son minimalisme de sécurité.'
        ],
        'utilite': [
            'Langage de contrats intelligents ciblant la machine virtuelle Ethereum (EVM) avec une syntaxe fortement inspirée de Python 3.',
            'Conçu pour maximiser la lisibilité du code et rendre l’écriture de smart contracts trompeurs ou vulnérables quasi impossible.',
            'Interdit délibérément les fonctionnalités dangereuses (modificateurs, récursion infinie, surcharge d’opérateurs, assembleur inline).',
            'Fournit une vérification stricte des débordements arithmétiques et des vérifications de limites de tableaux par défaut.',
            'Utilisé pour sécuriser des milliards de dollars dans la finance décentralisée (DeFi).'
        ],
        'url': 'https://docs.vyperlang.org',
        'badge': ('Vyper', 'https://img.shields.io/badge/Vyper-333333?style=for-the-badge&logo=ethereum&logoColor=white', 'Langages Smart Contracts & Web3')
    },
    'move': {
        'name': 'Move',
        'histoire': [
            '2019 : conçu par l’équipe de recherche de Diem/Libra chez Meta (Facebook) sous la direction de Sam Blackshear.',
            '2022 : émancipation après l’arrêt de Diem et adoption comme langage central des blockchains Aptos et Sui.',
            '2023 : formalisation de Move 2024 apportant des fonctionnalités modernes (énumérations, macros, méthodes sur types).',
            '2024+ : expansion vers de multiples réseaux décentralisés de couche 1 et 2 (Movement, Rooch).',
            'Aujourd’hui : langage blockchain novateur centré sur la sécurité et la représentation native d’actifs numériques finis.'
        ],
        'utilite': [
            'Langage de smart contracts basé sur la logique linéaire où les actifs numériques sont traités comme des ressources de première classe.',
            'Garantit qu’une ressource (token, NFT) ne peut jamais être dupliquée, perdue ou dépensée deux fois par analyse statique du bytecode.',
            'Sépare strictement la logique des modules de l’état de stockage des comptes pour une sécurité maximale.',
            'Fournit un vérificateur formel intégré (Move Prover) pour prouver mathématiquement les propriétés des contrats.',
            'Moteur d’exécution ultra-rapide permettant le traitement parallèle des transactions sur Aptos et Sui.'
        ],
        'url': 'https://move-language.github.io/move/',
        'badge': ('Move', 'https://img.shields.io/badge/Move-0081FB?style=for-the-badge&logo=meta&logoColor=white', 'Langages Smart Contracts & Web3')
    },
    'cairo': {
        'name': 'Cairo',
        'histoire': [
            '2020 : créé par l’équipe de StarkWare pour écrire des programmes dont l’exécution peut être prouvée cryptographiquement via les preuves STARK.',
            '2022 : transition majeure avec Cairo 1.0, réécrivant le langage sous une syntaxe et un système de types inspirés de Rust.',
            '2023 : déploiement en production comme langage de contrats intelligents du réseau Starknet (Ethereum Layer 2).',
            '2024+ : intégration du compilateur Sierra garantissant la décidabilité et la non-réversibilité des transactions prouvables.',
            'Aujourd’hui : pionnier mondial de la programmation pour les systèmes de preuves à divulgation nulle de connaissance (Zero-Knowledge / ZK).'
        ],
        'utilite': [
            'Langage compilé à typage statique de type Rust conçu pour générer des traces d’exécution prouvables par des arguments cryptographiques STARK.',
            'Permet la scalabilité massive de la blockchain en compressant des milliers de transactions en une seule preuve mathématique succincte.',
            'Garantit la sécurité d’exécution via la couche intermédiaire Sierra empêchant les transactions invalides d’échouer sans preuve.',
            'Utilisé pour les applications décentralisées (dApps), les jeux on-chain et les protocoles de mise à l’échelle sur Starknet.',
            'Permet la vérification hors-chaîne ultra-rapide de calculs computationnels très lourds.'
        ],
        'url': 'https://www.cairo-lang.org',
        'badge': ('Cairo', 'https://img.shields.io/badge/Cairo-EB5E28?style=for-the-badge&logo=ethereum&logoColor=white', 'Langages Smart Contracts & Web3')
    },
    'clarity': {
        'name': 'Clarity',
        'histoire': [
            '2020 : développé par la Stacks Foundation et Algorand pour apporter des smart contracts sécurisés à l’écosystème Bitcoin.',
            '2021 : lancement sur le réseau principal Stacks, rattachant les contrats à la sécurité du réseau Bitcoin.',
            '2023 : déploiement de Clarity 2 apportant de nouvelles primitives cryptographiques et des fonctions de manipulation de chaînes.',
            '2024 : activation de la mise à niveau Stacks Nakamoto décuplant la vitesse des blocs tout en conservant la finalité 100% Bitcoin.',
            'Aujourd’hui : langage de référence pour les applications décentralisées et la DeFi ancrées directement sur Bitcoin.'
        ],
        'utilite': [
            'Langage de smart contracts interprété et non-Turing complet garantissant la prévisibilité totale des coûts d’exécution et du comportement.',
            'Code source déployé directement sur la blockchain sous forme textuelle lisible (sans compilation en bytecode opaque).',
            'Permet l’analyse statique mathématique complète du code avant toute transaction pour éliminer les boucles infinies et les dépassements de gaz.',
            'Interagit nativement avec l’état et les transactions de la blockchain Bitcoin.',
            'Utilisé pour créer des tokens, DAO et protocoles de finance décentralisée sur le réseau Bitcoin.'
        ],
        'url': 'https://clarity-lang.org',
        'badge': ('Clarity', 'https://img.shields.io/badge/Clarity-5546FF?style=for-the-badge&logo=bitcoin&logoColor=white', 'Langages Smart Contracts & Web3')
    },
    'sway': {
        'name': 'Sway',
        'histoire': [
            '2022 : initié par Fuel Labs pour concevoir un langage de smart contracts pour la machine virtuelle haute performance FuelVM.',
            '2023 : adoption d’une syntaxe et d’un outillage inspirés de Rust (Sway toolchain / Forc).',
            '2024 : lancement du mainnet Fuel, première couche d’exécution rollup parallèle pour Ethereum.',
            '2024+ : expansion de l’écosystème de finance décentralisée et de DEX haute fréquence sur Fuel.',
            'Aujourd’hui : langage Web3 émergent optimisé pour l’exécution hautement parallèle et la consommation minimale de ressources.'
        ],
        'utilite': [
            'Langage de contrats intelligents compilé combinant la syntaxe de Rust avec des fonctionnalités spécifiques à la blockchain.',
            'Conçu pour exploiter le modèle UTXO étendu et l’architecture parallèle de la FuelVM.',
            'Fournit la sécurité des types, le pattern matching et un système de traits expressif.',
            'Élimine les goulots d’étranglement de l’EVM en permettant l’exécution simultanée de transactions indépendantes.',
            'Utilisé pour les plateformes d’échange décentralisées (DEX), les carnets d’ordres on-chain et les bridges Layer-2.'
        ],
        'url': 'https://www.fuel.network',
        'badge': ('Sway', 'https://img.shields.io/badge/Sway-00F58C?style=for-the-badge&logo=fuel&logoColor=black', 'Langages Smart Contracts & Web3')
    },
    'algol': {
        'name': 'ALGOL',
        'histoire': [
            '1958 : conçu par un comité international d’informaticiens européens et américains (ACM/GAMM) sous le nom d’ALGOL 58.',
            '1960 : publication d’ALGOL 60 par Peter Naur, introduisant la notation BNF (Backus-Naur Form) et la structure en blocs lexicale.',
            '1968 : publication d’ALGOL 68, introduisant un système de types riches et la définition formelle rigoureuse.',
            'Années 1970 : ancêtre direct et matrice conceptuelle de Pascal, C, Simula, Ada et de tous les langages impératifs modernes.',
            'Aujourd’hui : monument historique de l’informatique théorique, ayant fixé le standard de description des algorithmes.'
        ],
        'utilite': [
            'Langage impératif ayant introduit la notion universelle de portée de variables en blocs délimités (begin ... end).',
            'Premier langage à avoir formalisé le passage de paramètres par valeur et par nom.',
            'A servi de format universel standard de publication d’algorithmes dans la littérature scientifique pendant plus de 30 ans.',
            'A établi les bases de la syntaxe des langages à accolades modernes (C, Java, JavaScript).',
            'Pilier fondamental de l’enseignement et de l’histoire de l’architecture des compilateurs.'
        ],
        'url': 'https://www.computerhistory.org',
        'badge': ('ALGOL', 'https://img.shields.io/badge/ALGOL-1A1A1A?style=for-the-badge&logo=computerhistory&logoColor=white', 'Langages Historiques & Pionniers')
    },
    'basic': {
        'name': 'BASIC',
        'histoire': [
            '1964 : créé par John G. Kemeny et Thomas E. Kurtz au Dartmouth College pour démocratiser l’accès à l’informatique aux étudiants non scientifiques.',
            '1975 : Bill Gates et Paul Allen écrivent Altair BASIC, fondant ainsi la société Microsoft.',
            'Années 1980 : langage universellement intégré en ROM dans la quasi-totalité des micro-ordinateurs familiaux (Apple II, Commodore 64, ZX Spectrum).',
            '1991 : sortie de Visual Basic 1.0 chez Microsoft, inventant le développement visuel par glisser-déposer sur Windows.',
            'Aujourd’hui : langage historique ayant initié des générations entières de développeurs, survivant sous forme de Visual Basic .NET et VBA.'
        ],
        'utilite': [
            'Langage impératif à la syntaxe accessible inspirée de l’anglais naturel pour un apprentissage immédiat de la programmation.',
            'A popularisé le mode interactif direct et la numérotation des lignes d’instructions sur micro-ordinateurs.',
            'Visual Basic a standardisé la création d’interfaces graphiques événementielles pour les applications de gestion.',
            'VBA (Visual Basic for Applications) reste un moteur d’automatisation majeur au sein de la suite Microsoft Office (Excel).',
            'A ouvert l’ère de l’informatique personnelle grand public dans le monde entier.'
        ],
        'url': 'https://www.dartmouth.edu',
        'badge': ('BASIC', 'https://img.shields.io/badge/BASIC-1976D2?style=for-the-badge&logo=visualstudio&logoColor=white', 'Langages Historiques & Pionniers')
    },
    'smalltalk': {
        'name': 'Smalltalk',
        'histoire': [
            '1972 : conçu au Xerox PARC par Alan Kay, Dan Ingalls, Adele Goldberg et le Learning Research Group.',
            '1980 : publication de Smalltalk-80, version de référence diffusée dans le monde académique et industriel.',
            'Années 1980 : inspire directement Steve Jobs pour l’interface du Macintosh et pose les fondations de l’architecture MVC.',
            'Années 1990 : influence déterminante sur la conception d’Objective-C, Ruby, Python, Java et du refactoring moderne.',
            'Aujourd’hui : environnement vivant maintenu par des projets modernes open source comme Pharo et Squeak.'
        ],
        'utilite': [
            'Langage purement orienté objet où absolument tout élément (nombres, classes, méthodes, blocs d’exécution) est un objet.',
            'Fondé sur le principe de la communication d’objets par envoi dynamique de messages.',
            'Environnement graphique réflexif intégrant l’éditeur, le débogueur et la machine virtuelle dans une image persistante modifiable à chaud.',
            'A inventé le patron d’architecture Modèle-Vue-Contrôleur (MVC) et les environnements graphiques à fenêtres modernes.',
            'Utilisé pour la simulation logicielle complexe, l’enseignement du génie logiciel et la recherche en interfaces utilisateur.'
        ],
        'url': 'https://www.smalltalk.org',
        'badge': ('Smalltalk', 'https://img.shields.io/badge/Smalltalk-57889C?style=for-the-badge&logo=smalltalk&logoColor=white', 'Langages Historiques & Pionniers')
    },
    'simula': {
        'name': 'Simula',
        'histoire': [
            '1962–1967 : développé par Ole-Johan Dahl et Kristen Nygaard au Centre de calcul norvégien (NCC) à Oslo.',
            '1967 : publication de Simula 67, introduisant pour la toute première fois dans l’histoire les classes, objets et l’héritage.',
            '2001 : Dahl et Nygaard reçoivent conjointement le prestigieux prix Turing pour la création de la programmation orientée objet.',
            'Années 1970–1980 : influence directe sur Bjarne Stroustrup pour la conception de C++ et Alan Kay pour Smalltalk.',
            'Aujourd’hui : reconnu comme l’ancêtre originel fondamental de la programmation orientée objet moderne.'
        ],
        'utilite': [
            'Langage pionnier conçu initialement pour la simulation d’événements discrets (systèmes d’attente, réseaux, trafic).',
            'A inventé les concepts universels de classes, d’instances d’objets, de sous-classes et d’héritage.',
            'A introduit le masquage d’informations et les méthodes virtuelles.',
            'Permettait la quasi-concurrence de processus via des coroutines pour simuler des entités réelles autonomes.',
            'A posé les bases conceptuelles de l’ensemble des langages orientés objet industriels modernes (C++, Java, C#).'
        ],
        'url': 'https://www.mn.uio.no/ifi/english/',
        'badge': ('Simula', 'https://img.shields.io/badge/Simula-002D62?style=for-the-badge&logo=openaccess&logoColor=white', 'Langages Historiques & Pionniers')
    },
    'logo': {
        'name': 'Logo',
        'histoire': [
            '1967 : créé par Wally Feurzeig, Seymour Papert et Cynthia Solomon chez BBN Technologies et au MIT.',
            '1970–1980 : développement de la théorie du constructivisme éducatif par Papert et diffusion de la célèbre "Tortue Logo".',
            'Années 1980 : déploiement mondial dans les écoles primaires et secondaires sur micro-ordinateurs Apple II et Thomson.',
            'Années 2000 : inspiration directe pour la création de Scratch par le MIT Media Lab.',
            'Aujourd’hui : jalon pédagogique historique majeur pour l’apprentissage de la pensée algorithmique et computationnelle.'
        ],
        'utilite': [
            'Langage d’apprentissage interactif dérivé de Lisp, doté d’une syntaxe simple sans parenthèses obligatoires.',
            'Permet de piloter une "tortue" graphique virtuelle ou robotique sur un plan cartésien par des commandes géométriques simples (AVANCE, TOURNE).',
            'Enseigne de manière visuelle et kinesthésique les concepts de boucles, de récursivité et de décomposition procédurale.',
            'Traite les listes et les mots comme des données de première classe pour la manipulation textuelle.',
            'A démontré l’impact de l’informatique comme outil d’éveil cognitif pour les enfants.'
        ],
        'url': 'https://el.media.mit.edu/logo-foundation/',
        'badge': ('Logo', 'https://img.shields.io/badge/Logo-2B2B2B?style=for-the-badge&logo=mit&logoColor=white', 'Langages Historiques & Pionniers')
    },
    'forth': {
        'name': 'Forth',
        'histoire': [
            '1968–1970 : développé par Charles H. Moore pour piloter en temps réel le radiotélescope de l’Observatoire national de Kitt Peak.',
            '1977 : standardisation par le Forth Standards Team (Forth-77, Forth-79, Forth-83).',
            '1994 : adoption de la norme officielle ANSI X3.215-1994.',
            'Années 1980–2000 : utilisé pour les micro-firmwares d’ordinateurs (Open Firmware sur Apple PowerPC, Sun SPARC) et missions spatiales (NASA).',
            'Aujourd’hui : langage de niche reconnu pour son minimalisme extrême et son adéquation avec les microcontrôleurs embarqués.'
        ],
        'utilite': [
            'Langage impératif et extensible basé sur une pile (stack-based) utilisant la notation polonaise inverse (RPN).',
            'Compilateur et interpréteur ultra-compact tenant dans quelques kilo-octets de mémoire sans système d’exploitation hôte.',
            'Permet de définir de nouveaux mots (words) qui étendent dynamiquement le dictionnaire du langage au fur et à mesure du développement.',
            'Accès direct aux adresses mémoire physiques et aux registres des processeurs.',
            'Utilisé dans le contrôle de télescopes, l’instrumentation spatiale, les chargeurs d’amorçage et les systèmes industriels temps réel.'
        ],
        'url': 'https://www.forth.org',
        'badge': ('Forth', 'https://img.shields.io/badge/Forth-000000?style=for-the-badge&logo=forth&logoColor=white', 'Langages Historiques & Pionniers')
    },
    'pli': {
        'name': 'PL/I',
        'histoire': [
            '1964 : conçu par IBM pour unifier le calcul scientifique (Fortran) et la gestion d’entreprise (COBOL) sur l’ordinateur central IBM System/360.',
            '1976 : standardisation ANSI (ANSI X3.53-1976), suivie par l’ISO en 1979.',
            'Années 1970–1990 : langage d’infrastructure principal du système d’exploitation Multics (qui inspira directement Unix).',
            'Années 2000+ : modernisation continue par IBM pour les environnements z/OS et les architectures cloud hybrides.',
            'Aujourd’hui : langage patrimonial majeur exécuté dans les infrastructures transactionnelles bancaires et aéroportuaires critiques.'
        ],
        'utilite': [
            'Langage procédural puissant et exhaustif combinant le calcul scientifique avancé, le traitement de fichiers commerciaux et la manipulation de texte.',
            'A introduit la gestion structurée des exceptions et des interruptions matérielles (ON conditions).',
            'Permet l’allocation dynamique de mémoire, les pointeurs typés et les tableaux multidimensionnels à bornes variables.',
            'Utilisé pour exécuter des millions de transactions bancaires quotidiennes sur mainframes IBM zSystems.',
            'Intègre des mécanismes de préprocesseur sophistiqués et une compatibilité étroite avec CICS et DB2.'
        ],
        'url': 'https://www.ibm.com/products/pli-compiler-zos',
        'badge': ('PL/I', 'https://img.shields.io/badge/PL/I-052FAD?style=for-the-badge&logo=ibm&logoColor=white', 'Langages Historiques & Pionniers')
    },
    'vhdl': {
        'name': 'VHDL',
        'histoire': [
            '1983 : développé à l’initiative du Département de la Défense américain (DoD) dans le cadre du programme VHSIC pour documenter le comportement des puces électroniques.',
            '1987 : standardisation officielle par l’IEEE (IEEE 1076-1987).',
            '1993–2008 : révisions majeures IEEE 1076-1993 et 1076-2008 ajoutant la synthèse logique avancée et les types protégés.',
            'Années 2000+ : adoption prédominante en Europe et dans les secteurs aérospatial, militaire et des télécoms.',
            'Aujourd’hui : norme mondiale pour la conception et la vérification de circuits intégrés numériques (ASIC et FPGA).'
        ],
        'utilite': [
            'Langage de description matérielle (HDL) fortement typé décrivant la structure, les connexions et le comportement temporel de circuits électroniques.',
            'Modélise le parallélisme matériel intrinsèque où les processus s’exécutent simultanément en réponse aux fronts d’horloge et signaux.',
            'Permet la simulation précise au niveau des portes logiques et des délais de propagation temporels.',
            'Sert de code source pour la synthèse logique automatique sur puces FPGA (Xilinx, Altera) et circuits ASIC sur mesure.',
            'Utilisé dans les systèmes radar, l’avionique spatiale, le traitement de signal radiofréquence et l’automobile.'
        ],
        'url': 'https://standards.ieee.org',
        'badge': ('VHDL', 'https://img.shields.io/badge/VHDL-00629B?style=for-the-badge&logo=ieee&logoColor=white', 'Langages Description Matérielle & Domaines Spécifiques')
    },
    'verilog': {
        'name': 'Verilog',
        'histoire': [
            '1984 : créé par Prabhu Goel et Phil Moorby chez Gateway Design Automation comme langage de simulation de circuits matériels.',
            '1990 : racheté par Cadence Design Systems et ouvert au domaine public pour contrer la montée de VHDL.',
            '1995 : première standardisation internationale par l’IEEE (IEEE 1364-1995 / Verilog-95).',
            '2001–2005 : Verilog-2001 apporte la syntaxe signée et des améliorations majeures avant son extension dans SystemVerilog.',
            'Aujourd’hui : langage de conception de puces le plus répandu aux États-Unis et en Asie pour les microprocesseurs et GPU.'
        ],
        'utilite': [
            'Langage de description matérielle à syntaxe concise inspirée du langage C pour concevoir et simuler des circuits numériques.',
            'Permet la modélisation à différents niveaux d’abstraction : niveau transfert de registres (RTL), niveau portes logiques et niveau interrupteurs.',
            'Modélise le comportement événementiel piloté par les changements de signaux d’horloge (always @(posedge clk)).',
            'Langage central utilisé pour concevoir les architectures de microprocesseurs modernes (x86, ARM, RISC-V) et de processeurs graphiques.',
            'Intègre des primitives de simulation pour valider le fonctionnement logique avant la fabrication sur silicium.'
        ],
        'url': 'https://standards.ieee.org',
        'badge': ('Verilog', 'https://img.shields.io/badge/Verilog-00629B?style=for-the-badge&logo=ieee&logoColor=white', 'Langages Description Matérielle & Domaines Spécifiques')
    },
    'systemverilog': {
        'name': 'SystemVerilog',
        'histoire': [
            '2002 : initié par le consortium Accellera pour étendre Verilog avec des capacités avancées de vérification de circuits.',
            '2005 : publication de la première norme unifiée IEEE 1800-2005.',
            '2009 : fusion officielle de la norme Verilog de base dans la norme IEEE 1800-2009 SystemVerilog.',
            '2017–2023 : évolutions vers IEEE 1800-2023 renforçant la méthodologie de vérification universelle (UVM).',
            'Aujourd’hui : standard absolu de l’industrie des semi-conducteurs pour la conception et la vérification formelle de puces complexes.'
        ],
        'utilite': [
            'Langage unifié de description matérielle (HDVL) combinant conception RTL, programmation orientée objet et assertions logiques.',
            'Fournit la méthodologie standard UVM (Universal Verification Methodology) pour tester automatiquement des architectures de processeurs.',
            'Intègre la génération de stimuli aléatoires sous contraintes et la mesure de couverture fonctionnelle.',
            'Prend en charge les assertions temporelles (SystemVerilog Assertions - SVA) pour surveiller en continu les protocoles de bus de données.',
            'Indispensable pour concevoir et valider les SoC modernes contenant des milliards de transistors (Apple Silicon, NVIDIA, AMD, Qualcomm).'
        ],
        'url': 'https://standards.ieee.org',
        'badge': ('SystemVerilog', 'https://img.shields.io/badge/SystemVerilog-00629B?style=for-the-badge&logo=ieee&logoColor=white', 'Langages Description Matérielle & Domaines Spécifiques')
    },
    'mojo': {
        'name': 'Mojo',
        'histoire': [
            '2022–2023 : créé par Chris Lattner (créateur de LLVM, Clang et Swift) et la startup Modular.',
            '2023 : dévoilé publiquement comme sur-ensemble de Python conçu pour la programmation d’IA et de matériel hétérogène.',
            '2024 : ouverture en open source de la bibliothèque standard et du compilateur.',
            '2024+ : intégration avec le moteur d’exécution d’intelligence artificielle Modular MAX.',
            'Aujourd’hui : langage pionnier combinant l’ergonomie syntaxique de Python avec la puissance matérielle de C/C++ et Rust.'
        ],
        'utilite': [
            'Langage conçu pour l’accélération de modèles d’intelligence artificielle, de machine learning et de calcul matriciel sur GPU/TPU/CPU.',
            'Sur-ensemble de Python apportant un typage statique strict optionnel (fn vs def) et la gestion de mémoire par ownership.',
            'S’appuie sur l’infrastructure de compilation moderne MLIR (Multi-Level Intermediate Representation).',
            'Permet la vectorisation matérielle automatique (SIMD) et le tuilage de boucles pour saturer la bande passante mémoire.',
            'Offre des gains de performances jusqu’à plusieurs milliers de fois supérieurs à CPython sur les algorithmes d’IA.'
        ],
        'url': 'https://www.modular.com/mojo',
        'badge': ('Mojo', 'https://img.shields.io/badge/Mojo-FF4B00?style=for-the-badge&logo=mojo&logoColor=white', 'Langages Émergents & Recherche')
    },
    'carbon': {
        'name': 'Carbon',
        'histoire': [
            '2022 : dévoilé par Chandler Carruth et des ingénieurs de Google lors de la conférence CppNorth.',
            'Conçu explicitement comme un successeur expérimental pour C++, à l’instar de Kotlin pour Java ou Swift pour Objective-C.',
            '2023–2024 : développement communautaire ouvert de la sémantique formelle, de l’outil de build et de l’interpréteur de référence.',
            '2024+ : priorisation de l’interopérabilité bidirectionnelle totale avec les bases de code C++ existantes.',
            'Aujourd’hui : projet de recherche en open source explorant la modernisation sans friction du code C++ à grande échelle.'
        ],
        'utilite': [
            'Langage système conçu pour offrir des performances équivalentes à C++ avec une ergonomie et une sécurité modernes.',
            'Permet d’importer et d’appeler du code C++ directement dans Carbon (et inversement) sans adaptateurs manuels.',
            'Propose une syntaxe épurée avec inférence de types, déclarations introduites par des mots-clés clairs (fn, var, let) et génériques vérifiés.',
            'Vise à éliminer les comportements indéfinis historiques et à renforcer la sécurité mémoire progressive des bases de code massives.',
            'Destiné aux écosystèmes industriels disposant de millions de lignes de code C++ impossibles à réécrire en Rust.'
        ],
        'url': 'https://github.com/carbon-language/carbon-lang',
        'badge': ('Carbon', 'https://img.shields.io/badge/Carbon-4285F4?style=for-the-badge&logo=google&logoColor=white', 'Langages Émergents & Recherche')
    },
    'koka': {
        'name': 'Koka',
        'histoire': [
            '2012 : conçu par Daan Leijen chez Microsoft Research pour explorer la programmation fonctionnelle avec typage des effets.',
            '2019 : introduction du compilateur vers C s’appuyant sur l’allocation mémoire par comptage de références avec réutilisation de mémoire (Perceus).',
            '2021 : formalisation des gestionnaires d’effets algébriques (algebraic effect handlers) de premier ordre.',
            '2023+ : référence internationale dans la recherche sur la gestion de mémoire sans ramasse-miettes conventionnel.',
            'Aujourd’hui : langage expérimental d’avant-garde ayant influencé OCaml 5, WebAssembly et les standards d’effets modernes.'
        ],
        'utilite': [
            'Langage fortement typé doté d’un système d’inférence d’effets indiquant précisément dans la signature de chaque fonction les effets de bord produits.',
            'Intègre la technologie novatrice Perceus : libération automatique et déterministe de la mémoire sans pause de ramasse-miettes.',
            'Permet la réutilisation sur place (in-place mutation) automatique des structures de données fonctionnelles lorsque leur référence est unique.',
            'Fournit des gestionnaires d’effets algébriques permettant d’implémenter des coroutines, des exceptions et de l’asynchronisme de manière composable.',
            'Compilable vers du code C propre et hautement optimisé rivalisant en vitesse avec C++.'
        ],
        'url': 'https://koka-lang.github.io/koka/doc/index.html',
        'badge': ('Koka', 'https://img.shields.io/badge/Koka-00A4EF?style=for-the-badge&logo=microsoft&logoColor=white', 'Langages Émergents & Recherche')
    },
    'hare': {
        'name': 'Hare',
        'histoire': [
            '2019–2022 : créé par Drew DeVault et une équipe d’ingénieurs système indépendants pour fournir un langage système minimaliste.',
            '2022 : publication de la première version bêta publique et gel des fonctionnalités fondamentales.',
            '2023 : enrichissement de la bibliothèque standard autonome et développement de logiciels système natifs (navigateur Mercury, client mail).',
            '2024+ : portage sur les systèmes FreeBSD, OpenBSD et Linux sans dépendance à libc obligatoire.',
            'Aujourd’hui : langage système puriste fidèle à la philosophie Unix, conçu pour durer des décennies sans changements cassants.'
        ],
        'utilite': [
            'Langage système statiquement typé sans runtime lourd, sans garbage collector et sans allocation mémoire implicite.',
            'Fournit une bibliothèque standard autonome écrite entièrement en Hare et en assembleur sans dépendre de la bibliothèque C standard (libc).',
            'Vitesse de compilation quasi-instantanée s’appuyant sur le backend de compilateur modulaire QBE.',
            'Conçu pour écrire des systèmes d’exploitation, des utilitaires de ligne de commande, des démons réseau et des pilotes matériels.',
            'Garantit une stabilité absolue avec une spécification figée protégeant le code écrit contre toute obsolescence future.'
        ],
        'url': 'https://harelang.org',
        'badge': ('Hare', 'https://img.shields.io/badge/Hare-3B4252?style=for-the-badge&logo=hare&logoColor=white', 'Langages Émergents & Recherche')
    },
    'roc': {
        'name': 'Roc',
        'histoire': [
            '2020 : initié par Richard Feldman (figure majeure de la communauté Elm) pour étendre les bénéfices d’Elm aux serveurs, CLI et applications natives.',
            '2022 : développement de l’architecture par plateformes isolant la logique applicative des dépendances hôtes.',
            '2023 : mise au point du compilateur vers LLVM et webAssembly avec optimisations de mémoire par comptage de références automatique.',
            '2024+ : adoption enthousiaste pour des applications temps réel, des serveurs web et de la synthèse audio native.',
            'Aujourd’hui : langage fonctionnel émergent prometteur centré sur la convivialité, les performances et l’absence d’exceptions à l’exécution.'
        ],
        'utilite': [
            'Langage purement fonctionnel typé statiquement avec inférence de types complète, se compilant vers du code machine natif ultra-rapide.',
            'Sépare strictement le code applicatif pur de la "Plateforme" (gestionnaire d’I/O, réseau, graphisme écrit en Rust/C/Zig).',
            'Élimine les exceptions à l’exécution (pas de null, pas de plantages inattendus).',
            'Fournit des messages d’erreur de compilation parmi les plus clairs et conviviaux au monde.',
            'Idéal pour les services backend rapides, les outils en ligne de commande, les scripts système et les applications temps réel.'
        ],
        'url': 'https://www.roc-lang.org',
        'badge': ('Roc', 'https://img.shields.io/badge/Roc-7C3AED?style=for-the-badge&logo=roc&logoColor=white', 'Langages Émergents & Recherche')
    }
}

def run():
    target_dir = os.path.join(os.path.dirname(__file__), '..', 'languages')
    os.makedirs(target_dir, exist_ok=True)
    
    count = 0
    for slug, data in LANG_DB.items():
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
    print(f'Génération terminée : {count} fiches écrites.')

if __name__ == '__main__':
    run()
