import os

WAVE3_DB = {
    # Game Development & Engine Scripting
    'gdscript': {
        'name': 'GDScript (Godot)',
        'histoire': [
            '2014 : créé par Juan Linietsky et Ariel Manzur pour motoriser le moteur de jeu open source Godot Engine.',
            '2018 : Godot 3.0 introduit le typage statique optionnel améliorant les performances et l’autocomplétion.',
            '2023 : Godot 4.0 refond le moteur de GDScript (annotations, lambdas de premier ordre, typage strict, compilation bytecode accélérée).',
            '2023–2024 : vague massive de migration de développeurs Unity vers Godot et GDScript.',
            'Aujourd’hui : langage de prédilection du développement de jeux vidéo 2D et 3D indépendants open source.'
        ],
        'utilite': [
            'Langage de haut niveau à syntaxe indentée inspirée de Python conçu pour s’intégrer sans friction avec le moteur Godot.',
            'Optimisé pour l’architecture par arbre de nœuds et scènes de Godot via des mots-clés dédiés (@onready, @export, signals).',
            'Exécuté avec une latence quasi-nulle grâce à une liaison directe en mémoire C++ sans couche de glue FFI lourde.',
            'Offre un typage statique optionnel permettant des vérifications à la frappe dans l’éditeur intégré.',
            'Idéal pour prototyper et produire des jeux vidéo commerciaux complets multiplateformes (PC, Mobile, Web, Consoles).'
        ],
        'url': 'https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/',
        'badge': ('GDScript', 'https://img.shields.io/badge/GDScript-478CBF?style=for-the-badge&logo=godotengine&logoColor=white', 'Jeux Vidéo & Moteurs 3D')
    },
    'unrealscript': {
        'name': 'UnrealScript',
        'histoire': [
            '1998 : conçu par Tim Sweeney chez Epic Games pour alimenter le tout premier jeu Unreal.',
            '2004–2006 : pilier incontournable de l’ère Unreal Engine 3, motorisant des centaines de superproductions (Gears of War, Mass Effect, Batman Arkham).',
            '2014 : Epic Games remplace UnrealScript par C++ natif et le système de scripting visuel Blueprints dans Unreal Engine 4.',
            '2023 : annonce du nouveau langage Verse par Tim Sweeney pour l’écosystème Unreal Engine et l’UEFN.',
            'Aujourd’hui : monument historique du développement de jeux vidéo ayant défini le gameplay scripting moderne.'
        ],
        'utilite': [
            'Langage orienté objet fortement typé conçu sur mesure pour la logique de gameplay, l’IA et la réplication réseau temps réel.',
            'Introduisait les états d’acteurs (states) directement dans la syntaxe pour modéliser le comportement des entités.',
            'Gérait nativement le passage du temps et l’attente non bloquante via des fonctions latentes (latent functions).',
            'Permettait la modification du code de jeu sans recompilation complète du moteur C++ sous-jacent.',
            'A inspiré directement l’architecture des moteurs de jeux contemporains et la modélisation réseau multijoueur.'
        ],
        'url': 'https://docs.unrealengine.com',
        'badge': ('UnrealScript', 'https://img.shields.io/badge/UnrealScript-313131?style=for-the-badge&logo=unrealengine&logoColor=white', 'Jeux Vidéo & Moteurs 3D')
    },
    'gml': {
        'name': 'GML (GameMaker)',
        'histoire': [
            '1999 : créé par Mark Overmars à l’Université d’Utrecht pour accompagner la sortie de GameMaker.',
            '2012 : YoYo Games introduit GameMaker: Studio avec export multiplateforme natif.',
            '2020 : refonte majeure de GML (GameMaker Language) avec l’ajout des structures de données anonymes, fonctions et méthodes de première classe.',
            '2023+ : moteur sous-jacent de méga-succès indépendants acclamés (Undertale, Hotline Miami, Katana Zero, Risk of Rain).',
            'Aujourd’hui : technologie reine pour la création de jeux 2D indépendants ultra-véloces.'
        ],
        'utilite': [
            'Langage impératif et dynamique spécialement conçu pour manipuler des objets graphiques, des événements et des collisions 2D.',
            'Permet l’alternance instantanée entre le scripting textuel GML et le système visuel par blocs (Visual GML).',
            'Intègre nativement la gestion de la physique 2D (Box2D), des sons, des surfaces de rendu et des particules.',
            'Compilable en code natif C++ ultra-performant via la technologie YoYo Compiler (YYC).',
            'Idéal pour concevoir et publier des jeux indépendants sur Steam, Nintendo Switch, PlayStation, Xbox et Mobile.'
        ],
        'url': 'https://gamemaker.io',
        'badge': ('GML', 'https://img.shields.io/badge/GML-000000?style=for-the-badge&logo=gamemaker&logoColor=white', 'Jeux Vidéo & Moteurs 3D')
    },
    'squirrel': {
        'name': 'Squirrel',
        'histoire': [
            '2003 : créé par Alberto Demichelis pour offrir une alternative à Lua dotée d’une syntaxe de style C et d’une véritable orientation objet.',
            'Années 2000–2010 : adopté par Valve pour scripter le gameplay et les modes de jeu de Left 4 Dead 2, Portal 2 et Counter-Strike: Global Offensive.',
            '2016 : utilisé pour motoriser les serveurs multijoueurs de GTA et Mafia II (modding multijoueur).',
            '2020+ : maintien actif comme moteur de script embarqué rapide dans les microcontrôleurs (Electric Imp IoT).',
            'Aujourd’hui : moteur de scripting de jeu vidéo reconnu pour sa gestion déterministe de la mémoire par comptage de références.'
        ],
        'utilite': [
            'Langage de script léger orienté objet conçu pour être embarqué simplement dans des moteurs C/C++.',
            'Syntaxe familière proche de C, C++ et JavaScript avec classes, héritage, générateurs et gestion des exceptions.',
            'Libération mémoire déterministe et immédiate grâce au comptage de références sans gel imprévisible de ramasse-miettes.',
            'Utilisé pour les scripts d’intelligence artificielle, l’orchestration de dialogues et le modding de jeux vidéo AAA.',
            'Empreinte mémoire très faible et intégration aisée avec les structures de données natives du C++.'
        ],
        'url': 'http://www.squirrel-lang.org',
        'badge': ('Squirrel', 'https://img.shields.io/badge/Squirrel-8E44AD?style=for-the-badge&logo=cplusplus&logoColor=white', 'Jeux Vidéo & Moteurs 3D')
    },

    # Audio, Music & DSP
    'faust': {
        'name': 'FAUST',
        'histoire': [
            '2002 : conçu par Yann Orlarey et l’équipe du laboratoire GRAME-CNCM à Lyon (Functional AUdio STream).',
            '2010 : publication du compilateur FAUST 2 avec génération automatique de code C++, Rust, WebAssembly et LLVM IR.',
            '2015 : adoption mondiale par les fabricants de synthétiseurs, pédales d’effets et logiciels de MAO.',
            '2022+ : intégration avec le Web Audio API et les processeurs embarqués pour la lutherie électronique moderne.',
            'Aujourd’hui : standard mondial de la recherche et de l’industrie pour la synthèse sonore et le traitement du signal audio temps réel.'
        ],
        'utilite': [
            'Langage purement fonctionnel synchrone dédié au traitement numérique du signal sonore (DSP) et au calcul temps réel.',
            'Permet de concevoir des filtres audio, synthétiseurs, réverbérations et effets sonores sous forme d’équations mathématiques formelles.',
            'Compilateur ultra-optimisé générant du code C++, Rust ou WebAssembly à performances maximales avec vectorisation SIMD automatique.',
            'Permet d’exporter un même algorithme en plugin VST, AU, patch Max/MSP, Pure Data, application iOS/Android ou binaire pour microcontrôleur.',
            'Fournit une vérification formelle des délais et garantit l’absence d’allocation dynamique en cours de traitement audio.'
        ],
        'url': 'https://faust.grame.fr',
        'badge': ('FAUST', 'https://img.shields.io/badge/FAUST-009688?style=for-the-badge&logo=audacity&logoColor=white', 'Audio, Musique & DSP Temps Réel')
    },
    'supercollider': {
        'name': 'SuperCollider',
        'histoire': [
            '1996 : créé par James McCartney comme logiciel propriétaire de synthèse audio sur Macintosh.',
            '2002 : libération du code source en open source sous licence GNU GPL, déclenchant l’essor du live coding musical.',
            '2010 : architecture stabilisée autour du serveur de synthèse modulaire (scsynth / supernova) et du langage client (sclang).',
            '2020+ : adoption massive dans l’art sonore génératif, la spatialisation acoustique 3D (Ambisonics) et la recherche en psychoacoustique.',
            'Aujourd’hui : environnement de référence pour la composition algorithmique et les concerts de code en direct.'
        ],
        'utilite': [
            'Langage orienté objet dynamique (sclang) couplé à un serveur de synthèse sonore temps réel ultra-rapide (scsynth).',
            'Permet la création d’arbres de synthèse sonore complexes (synthdefs) générant du son échantillon par échantillon.',
            'Moteur de prédilection de la scène mondiale du live coding (TidalCycles repose sur le moteur SuperCollider).',
            'Gère la spatialisation sonore multicanale sur des centaines de haut-parleurs simultanés.',
            'Permet le contrôle d’installations d’art sonore interactif via les protocoles OSC (Open Sound Control) et MIDI.'
        ],
        'url': 'https://supercollider.github.io',
        'badge': ('SuperCollider', 'https://img.shields.io/badge/SuperCollider-121212?style=for-the-badge&logo=musicbrainz&logoColor=white', 'Audio, Musique & DSP Temps Réel')
    },
    'pure-data': {
        'name': 'Pure Data (Pd)',
        'histoire': [
            '1996 : créé par Miller Puckette à l’IRCAM comme logiciel libre successeur du système Max.',
            '2000 : émergence de distributions communautaires majeures (Pd-extended, Purr Data).',
            '2010+ : intégration dans des synthétiseurs matériels modulaires et des ordinateurs monocartes (Raspberry Pi, Bela).',
            '2020+ : projet libpd permettant d’embarquer des patchs Pure Data comme moteur audio au sein de jeux vidéo Unity et Unreal Engine.',
            'Aujourd’hui : environnement visuel open source mondialement enseigné dans les conservatoires et écoles d’art numérique.'
        ],
        'utilite': [
            'Langage de programmation graphique par flux de données (dataflow) où les algorithmes sont créés en reliant des boîtes d’objets audio et de contrôle.',
            'Permet la génération sonore en temps réel, le traitement vidéo interactif (GEM) et le contrôle de capteurs physiques.',
            'Fonctionne sur toutes les plateformes (Linux, macOS, Windows, microcontrôleurs embarqués Bela).',
            'Utilisé par des artistes, sound designers et compositeurs pour des installations d’art interactif et la performance scénique.',
            'Intégrable dans des applications mobiles et jeux vidéo grâce à la bibliothèque C autonome libpd.'
        ],
        'url': 'https://puredata.info',
        'badge': ('Pure Data', 'https://img.shields.io/badge/Pure_Data-00457C?style=for-the-badge&logo=soundcharts&logoColor=white', 'Audio, Musique & DSP Temps Réel')
    },
    'chuck': {
        'name': 'ChucK',
        'histoire': [
            '2003 : conçu par Ge Wang et Perry Cook à l’Université de Princeton pour explorer la programmation sonore fortement temporisée.',
            '2008 : moteur de création du Stanford Laptop Orchestra (SLOrk) et du Mobile Phone Orchestra (MoPhO).',
            '2018 : intégration avec WebAssembly (WebChucK) permettant la synthèse sonore directe dans les navigateurs web.',
            '2024+ : enrichissement du support multithread et des interfaces graphiques interactives (ChuGL).',
            'Aujourd’hui : langage d’enseignement universitaire de référence pour l’acoustique numérique et la programmation musicale concurrente.'
        ],
        'utilite': [
            'Langage de programmation musicale fortement temporisé (strongly-timed) permettant de contrôler explicitement l’avancée du temps.',
            'Utilise l’opérateur Chuck (=>) pour router de manière intuitive les flux audio et assigner les variables.',
            'Permet la concurrence précise à l’échantillon près (sample-accurate timing) de multiples processus musicaux indépendants.',
            'Modifie et injecte du code à la volée pendant l’exécution sans interruption audio (On-the-fly Programming).',
            'Utilisé pour les performances de musique électronique en direct, la recherche acoustique et l’apprentissage de la MAO générative.'
        ],
        'url': 'https://chuck.stanford.edu',
        'badge': ('ChucK', 'https://img.shields.io/badge/ChucK-2C3E50?style=for-the-badge&logo=stanford&logoColor=white', 'Audio, Musique & DSP Temps Réel')
    },
    'csound': {
        'name': 'Csound',
        'histoire': [
            '1985 : développé par Barry Vercoe au MIT Media Lab, descendant direct de la série historique MUSIC-N de Max Mathews.',
            'Années 1990 : standardisation mondiale pour l’électroacoustique et la composition musicale sur micro-ordinateurs.',
            '2005 : publication de Csound 5 avec réécriture sous forme de bibliothèque d’API réutilisable (libcsound).',
            '2015+ : Csound 6 apporte la recompilation de code à chaud et le calcul accéléré sur GPU.',
            'Aujourd’hui : le plus ancien, puissant et documenté des systèmes de synthèse sonore computationnelle.'
        ],
        'utilite': [
            'Langage et compilateur audio basé sur la distinction entre l’Orchestre (description des instruments DSP) et la Partition (suite d’événements temporels).',
            'Fournit plus de 2 000 générateurs, filtres, tables d’ondes et modèles physiques intégrés (opcodes).',
            'Offre une précision de calcul en double précision à virgule flottante d’une fidélité sonore irréprochable.',
            'Intégrable dans Python, C++, Java, Max/MSP, Pure Data et les navigateurs Web via WebAssembly.',
            'Utilisé pour la musique de film, la recherche en psychoacoustique et la synthèse de modèles physiques réalistes.'
        ],
        'url': 'https://csound.com',
        'badge': ('Csound', 'https://img.shields.io/badge/Csound-2D3748?style=for-the-badge&logo=itunes&logoColor=white', 'Audio, Musique & DSP Temps Réel')
    },

    # Query, Graph & Data Languages
    'graphql': {
        'name': 'GraphQL (SDL)',
        'histoire': [
            '2012 : créé en interne chez Meta (Facebook) pour résoudre les limites de bande passante et la lenteur des applications mobiles.',
            '2015 : publication publique des spécifications et ouverture de la première implémentation de référence open source.',
            '2018 : transfert du projet à la fondation indépendante GraphQL Foundation hébergée par la Linux Foundation.',
            '2021+ : standardisation universelle pour les API de grandes entreprises (GitHub, Shopify, Twitter, Netflix).',
            'Aujourd’hui : standard mondial incontesté pour les API web déclaratives et fortement typées.'
        ],
        'utilite': [
            'Langage de requêtage et de description de schémas (SDL) permettant aux clients de demander exactement les données dont ils ont besoin, et rien de plus.',
            'Élimine définitivement les problèmes de sous-récupération (under-fetching) et sur-récupération (over-fetching) de données.',
            'Fournit un typage statique strict et un graphe unique reliant l’ensemble des microservices d’une organisation.',
            'Intègre la documentation automatique et l’autocomplétion interactive des requêtes (GraphiQL, Apollo Studio).',
            'Prend en charge les mises à jour en temps réel via le mécanisme des abonnements (GraphQL Subscriptions).'
        ],
        'url': 'https://graphql.org',
        'badge': ('GraphQL', 'https://img.shields.io/badge/GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white', 'Requêtes de Données & Graphes')
    },
    'sparql': {
        'name': 'SPARQL',
        'histoire': [
            '2004–2008 : standardisé par le W3C comme langage de requête officiel du Web Sémantique et du modèle de données RDF.',
            '2013 : publication de la norme SPARQL 1.1 introduisant les sous-requêtes, agrégations et mises à jour (SPARQL Update).',
            '2015+ : moteur d’interrogation officiel de Wikidata (Wikidata Query Service) reliant les connaissances de l’humanité.',
            '2020+ : moteur de recherche pour les bases de connaissances d’entreprise et les données ouvertes liées (Linked Open Data).',
            'Aujourd’hui : norme mondiale pour l’interrogation des ontologies, des graphes de connaissances (Knowledge Graphs) et de l’Open Data.'
        ],
        'utilite': [
            'Langage de requête déclaratif basé sur la correspondance de motifs de triplets RDF (Sujet - Prédicat - Objet).',
            'Permet d’interroger simultanément de multiples bases de données de connaissances distribuées à travers le monde (Federated Queries).',
            'Moteur de requêtage de Wikidata permettant de poser des questions complexes sur des milliards de faits vérifiés.',
            'Utilisé dans le secteur biomédical, les bibliothèques nationales, la muséographie et l’intelligence économique.',
            'Prend en charge le raisonnement logique et l’inférence sémantique basée sur les standards OWL et RDFS.'
        ],
        'url': 'https://www.w3.org/TR/sparql11-query/',
        'badge': ('SPARQL', 'https://img.shields.io/badge/SPARQL-005A9C?style=for-the-badge&logo=w3c&logoColor=white', 'Requêtes de Données & Graphes')
    },
    'cypher': {
        'name': 'Cypher (OpenCypher)',
        'histoire': [
            '2011 : conçu par Neo4j pour offrir un langage déclaratif intuitif pour interroger les bases de données orientées graphes.',
            '2015 : ouverture en tant que standard ouvert avec le projet openCypher.',
            '2018–2023 : adoption par de multiples moteurs de graphes industriels (AWS Neptune, RedisGraph, SAP HANA, Memgraph).',
            '2024 : influence directe et intégration au sein de la nouvelle norme internationale ISO GQL (Graph Query Language).',
            'Aujourd’hui : langage d’interrogation de graphes le plus populaire et ergonomique au monde.'
        ],
        'utilite': [
            'Langage déclaratif utilisant une notation visuelle en art ASCII intuitive pour représenter les nœuds (n:Label) et relations -[:REL]-> (m).',
            'Optimisé pour traverser des graphes de relations complexes à très haute vitesse sans les jointures coûteuses du SQL.',
            'Utilisé pour la détection de fraudes bancaires, les réseaux sociaux, les moteurs de recommandation et la cybersécurité.',
            'Permet la recherche de chemins les plus courts (shortestPath) et l’analyse de communautés au sein de réseaux massifs.',
            'Standardisé au niveau mondial dans le cadre de la spécification openCypher.'
        ],
        'url': 'https://opencypher.org',
        'badge': ('Cypher', 'https://img.shields.io/badge/Cypher-008CC1?style=for-the-badge&logo=neo4j&logoColor=white', 'Requêtes de Données & Graphes')
    },
    'xquery': {
        'name': 'XQuery',
        'histoire': [
            '2007 : standardisé par le W3C comme langage d’interrogation et de transformation pour les données XML et documentaires.',
            '2014 : publication de la recommandation XQuery 3.0 apportant la programmation fonctionnelle de premier ordre.',
            '2017 : publication de XQuery 3.1 intégrant le support natif des formats JSON et des tableaux associatifs.',
            'Années 2010–2020 : moteur central des bases de données de documents d’entreprise (MarkLogic, eXist-db, BaseX).',
            'Aujourd’hui : norme mondiale pour l’extraction, l’analyse et la transformation de collections de documents structurés.'
        ],
        'utilite': [
            'Langage fonctionnel fortement typé conçu pour interroger, transformer et générer des documents XML, HTML et JSON.',
            'S’appuie sur les expressions FLWOR (For, Let, Where, Order by, Return) pour manipuler des ensembles de données complexes.',
            'Intègre le moteur d’adressage de nœuds XPath pour naviguer dans les arborescences documentaires.',
            'Utilisé par les maisons d’édition internationales, les institutions législatives (journaux officiels) et le renseignement.',
            'Permet le traitement transactionnel de très grands volumes de documents sans perte de fidélité sémantique.'
        ],
        'url': 'https://www.w3.org/TR/xquery-31/',
        'badge': ('XQuery', 'https://img.shields.io/badge/XQuery-E44D26?style=for-the-badge&logo=w3c&logoColor=white', 'Requêtes de Données & Graphes')
    },

    # Hardware Synthesis & Open Hardware
    'chisel': {
        'name': 'Chisel (RISC-V)',
        'histoire': [
            '2012 : conçu à l’Université de Berkeley par Jonathan Bachrach, Krste Asanović et l’équipe d’inventeurs de l’architecture RISC-V.',
            '2015 : création des générateurs de processeurs open source Rocket Chip et BOOM (Berkeley Out-of-Order Machine).',
            '2021 : transfert du projet sous la gouvernance de Chips Alliance (Linux Foundation).',
            '2023+ : adoption industrielle majeure par Google, SiFive et Intel pour accélérer la conception de puces RISC-V sur mesure.',
            'Aujourd’hui : technologie de pointe pour la conception de matériel numérique moderne par génération de circuits.'
        ],
        'utilite': [
            'Langage de description et de génération matérielle (HDL) implémenté comme DSL au sein de Scala.',
            'Apporte les concepts de programmation orientée objet, de polymorphisme et de programmation fonctionnelle à la conception de silicium.',
            'Génère automatiquement du code Verilog synthétisable et des modèles de simulation ultra-rapides en C++ (via FIRRTL).',
            'Permet de concevoir des architectures de processeurs hautement paramétrables et personnalisables en quelques lignes de code.',
            'Moteur de développement originel et de référence de l’écosystème international de processeurs ouverts RISC-V.'
        ],
        'url': 'https://www.chisel-lang.org',
        'badge': ('Chisel', 'https://img.shields.io/badge/Chisel_HDL-DC322F?style=for-the-badge&logo=scala&logoColor=white', 'Conception Matérielle & Open Hardware')
    },
    'bluespec': {
        'name': 'Bluespec (BSV)',
        'histoire': [
            '2000 : développé par Arvind et son équipe au MIT sur la base des règles de réécriture atomiques (Term Rewriting Systems).',
            '2003 : fondation de Bluespec Inc. pour commercialiser le compilateur et la méthodologie de conception.',
            '2020 : ouverture du compilateur Bluespec (BSC) en open source sous licence libre BSD.',
            '2023+ : utilisé pour la conception d’accélérateurs matériels cryptographiques et de cœurs RISC-V certifiés.',
            'Aujourd’hui : référence académique et industrielle pour la conception matérielle correcte par construction.'
        ],
        'utilite': [
            'Langage de synthèse matérielle de haut niveau basé sur des règles atomiques de transition d’états (Guarded Atomic Actions).',
            'Élimine automatiquement les conflits de synchronisation de bus et les conditions de course matérielles lors de la compilation.',
            'Génère du code Verilog/SystemVerilog RTL certifiable et garanti sans bugs de synchronisation inter-modules.',
            'Intègre un système de types statiques avancé et des fonctionnalités fonctionnelles inspirées de Haskell.',
            'Utilisé pour les interconnexions de processeurs à très faible latence, les routeurs réseau sur puce (NoC) et la cryptographie.'
        ],
        'url': 'https://bluespec.com',
        'badge': ('Bluespec', 'https://img.shields.io/badge/Bluespec-003366?style=for-the-badge&logo=mit&logoColor=white', 'Conception Matérielle & Open Hardware')
    },

    # Systems & Wirth Family (Modula / Oberon)
    'modula-2': {
        'name': 'Modula-2',
        'histoire': [
            '1978 : conçu par Niklaus Wirth à l’ETH Zurich comme successeur de Pascal pour le système de station de travail Lilith.',
            '1980 : publication du rapport de définition du langage introduisant le concept fondamental de modules séparés (Definition & Implementation).',
            '1996 : standardisation internationale officielle par l’ISO (ISO/IEC 10514-1).',
            '2022 : intégration officielle du compilateur GNU Modula-2 (gm2) dans la suite GCC 13.',
            'Aujourd’hui : modèle historique de clarté modulaire ayant inspiré Ada, Java, Modula-3 et les architectures logicielles modernes.'
        ],
        'utilite': [
            'Langage système impératif structuré introduisant la séparation stricte entre interface publique de module et code d’implémentation.',
            'Intègre la gestion native de la quasi-concurrence de processus via des coroutines sans surcoût système.',
            'Permet l’accès direct au matériel et aux adresses mémoire tout en maintenant une stricte vérification des types.',
            'Utilisé historiquement pour l’écriture de systèmes d’exploitation temps réel, la commande de métros et les micro-logiciels critiques.',
            'Excellente base pédagogique pour l’apprentissage du génie logiciel rigoureux et de la compilation.'
        ],
        'url': 'https://www.modula2.org',
        'badge': ('Modula-2', 'https://img.shields.io/badge/Modula--2-00549D?style=for-the-badge&logo=gnu&logoColor=white', 'Systèmes Modulaires & Wirth')
    },
    'oberon': {
        'name': 'Oberon',
        'histoire': [
            '1986–1988 : créé par Niklaus Wirth et Jürg Gutknecht à l’ETH Zurich dans une quête de minimalisme logiciel absolu.',
            '1992 : publication de l’environnement et système d’exploitation Oberon System tenant intégralement sur une seule disquette.',
            '2013 : révision "Oberon-07", épurant encore le langage pour en faire le système complet le plus compact et transparent au monde.',
            'Années 2020 : utilisé pour enseigner la conception de processeurs matériels (RISC5 sur FPGA) et de compilateurs en moins de 50 pages de code.',
            'Aujourd’hui : chef-d’œuvre d’élégance minimaliste et référence ultime du principe de simplicité en informatique.'
        ],
        'utilite': [
            'Langage de programmation système et orienté objet minimaliste doté d’un ramasse-miettes automatique et d’un typage strict.',
            'Introduit l’extension de types (type extension) comme mécanisme unifié pour la programmation orientée objet sans complexité inutile.',
            'Compilateur complet capable de s’auto-compiler en moins de 4 000 lignes de code source lisibles par un humain.',
            'Permet de piloter un système d’exploitation graphique interactif entier sans aucune couche logicielle superflue.',
            'Utilisé dans l’embarqué critique et la recherche sur les architectures informatiques autonomes et vérifiables.'
        ],
        'url': 'http://www.projectoberon.com',
        'badge': ('Oberon', 'https://img.shields.io/badge/Oberon-003366?style=for-the-badge&logo=openaccess&logoColor=white', 'Systèmes Modulaires & Wirth')
    },

    # Esoteric & CS Theoretical Milestones
    'brainfuck': {
        'name': 'Brainfuck',
        'histoire': [
            '1993 : créé par Urban Müller pour concevoir le compilateur de langage Turing-complet le plus minuscule possible (moins de 240 octets sur Amiga).',
            'Années 2000 : adoption culte par les théoriciens de la calculabilité et les passionnés de défis de programmation extrême.',
            '2010+ : implémenté dans des milliers de compilateurs, synthétisé sur FPGA matériels et prouvé équivalent aux machines de Turing universelles.',
            'Aujourd’hui : le plus célèbre et influent de tous les langages ésotériques de l’histoire de l’informatique.'
        ],
        'utilite': [
            'Langage ésotérique minimaliste constitué d’un ruban infini d’octets de mémoire et d’un pointeur manipulé par exactement 8 symboles : > < + - . , [ ].',
            'Fournit une démonstration vivante et concrète du modèle théorique de la Machine de Turing universelle.',
            'Utilisé pour tester la capacité d’optimisation des compilateurs et la formalisation mathématique de la décidabilité.',
            'Sert de défi de programmation pour la création d’émulateurs, d’interpréteurs et de transpilateurs dans de nouveaux langages.',
            'Prouve qu’un ensemble minimaliste de 8 instructions suffit mathématiquement à exécuter n’importe quel algorithme calculable.'
        ],
        'url': 'https://esolangs.org/wiki/Brainfuck',
        'badge': ('Brainfuck', 'https://img.shields.io/badge/Brainfuck-2B2B2B?style=for-the-badge&logo=codewars&logoColor=white', 'Ésotériques & Théorie Informatique')
    },
    'befunge': {
        'name': 'Befunge',
        'histoire': [
            '1993 : inventé par Chris Pressey pour créer un langage dont le flux de contrôle d’exécution est bidimensionnel (2D).',
            '1998 : formalisation de la spécification Befunge-98 au sein de la famille générique Funge.',
            'Années 2000 : sujet d’études universitaires en informatique théorique sur les automates cellulaires et la non-linéarité du code.',
            'Aujourd’hui : archétype des langages à espace de code planaire bidirectionnel (Funge-space).'
        ],
        'utilite': [
            'Langage ésotérique basé sur une pile où le pointeur d’instruction (IP) se déplace dans les quatre directions spatiales (haut, bas, gauche, droite).',
            'Le code source est disposé sur une grille bidimensionnelle de 80x25 caractères modifiable dynamiquement par le programme lui-même à l’exécution.',
            'Permet l’auto-modification de code en temps réel via les instructions de lecture (g) et d’écriture (p) sur la grille.',
            'Démontre les propriétés de calculabilité sur des surfaces géométriques non séquentielles.',
            'Utilisé comme exercice d’ingéniosité algorithmique et d’architecture de machines virtuelles insolites.'
        ],
        'url': 'https://esolangs.org/wiki/Befunge',
        'badge': ('Befunge', 'https://img.shields.io/badge/Befunge-4B0082?style=for-the-badge&logo=gameandwatch&logoColor=white', 'Ésotériques & Théorie Informatique')
    },
    'whitespace': {
        'name': 'Whitespace',
        'histoire': [
            '2003 : créé le 1er avril par Edwin Brady et Chris Morris à l’Université de Durham pour renverser les conventions syntaxiques.',
            '2004 : publication de la version stable 0.3 définissant les règles formelles de la machine virtuelle sous-jacente.',
            'Années 2010 : utilisé dans les défis de stéganographie (dissimuler du code exécutable invisible au sein de fichiers texte ordinaires).',
            'Aujourd’hui : classique absolu de la culture hacker et de la recherche sur la représentation des grammaires.'
        ],
        'utilite': [
            'Langage impératif basé sur une pile dont la syntaxe n’utilise exclusivement que des caractères d’espacement invisibles (Espace, Tabulation, Saut de ligne).',
            'Ignore totalement tous les caractères visibles non-espaces, considérés comme de simples commentaires transparents.',
            'Permet de dissimuler des programmes complets et fonctionnels à l’intérieur du code source d’autres langages sans altérer leur comportement.',
            'Dispose d’un jeu d’instructions complet avec manipulation de pile, arithmétique, mémoire tas (heap) et flux conditionnels.',
            'Utilisé pour des démonstrations de sécurité informatique, d’obfuscation et de cryptostéganographie logicielle.'
        ],
        'url': 'https://esolangs.org/wiki/Whitespace',
        'badge': ('Whitespace', 'https://img.shields.io/badge/Whitespace-FFFFFF?style=for-the-badge&logo=ghost&logoColor=black', 'Ésotériques & Théorie Informatique')
    },
    'malbolge': {
        'name': 'Malbolge',
        'histoire': [
            '1998 : créé par Ben Olmstead et nommé d’après le huitième cercle de l’Enfer de Dante, conçu pour être le langage le plus difficile à programmer au monde.',
            '2000 : le tout premier programme Malbolge fonctionnel ("Hello World") est produit non pas par un humain mais par un algorithme de recherche en faisceau après deux ans de calcul.',
            '2004 : Lou Scheffer publie une analyse cryptanalytique du chiffrement d’instructions de Malbolge.',
            'Aujourd’hui : référence théorique absolue de la complexité extrême et de l’obfuscation computationnelle quasi-chiffrée.'
        ],
        'utilite': [
            'Langage ésotérique basé sur une machine virtuelle ternaire (trits) et une mémoire circulaire auto-modifiante et cryptée après chaque instruction exécutée.',
            'Chaque instruction est déchiffrée selon une table de substitution modulaire puis modifiée immédiatement après son exécution.',
            'Rend l’écriture de boucles et de branchements déterministes presque indiscernable d’un processus de déchiffrement cryptographique.',
            'Utilisé dans la recherche sur la résistance des logiciels contre la rétro-ingénierie et l’analyse statique.',
            'Démontre les limites extrêmes de la compréhension humaine de flux de calculs mathématiquement déterministes.'
        ],
        'url': 'https://esolangs.org/wiki/Malbolge',
        'badge': ('Malbolge', 'https://img.shields.io/badge/Malbolge-8B0000?style=for-the-badge&logo=hackthebox&logoColor=white', 'Ésotériques & Théorie Informatique')
    },

    # Modern Specific & Hybrid
    'ballerina': {
        'name': 'Ballerina',
        'histoire': [
            '2015–2017 : initié par Sanjiva Weerawarana et WSO2 pour créer un langage centré dès sa conception sur l’intégration cloud et les API réseau.',
            '2019 : publication de Ballerina Swan Lake avec système de types structurels et représentation graphique bidirectionnelle automatique.',
            '2022 : standardisation de l’écosystème avec connecteurs de services cloud prêts à l’emploi (AWS, Azure, Kafka, gRPC).',
            '2024+ : adoption par les entreprises pour orchestrer des architectures microservices et des intégrations d’API complexes.',
            'Aujourd’hui : langage novateur transformant le code texte en diagrammes de séquence architecturaux exécutables.'
        ],
        'utilite': [
            'Langage compilé cloud-native statiquement typé où les appels réseau distants sont des constructions syntaxiques de premier ordre (->).',
            'Génère automatiquement un diagramme de séquence UML parfait et synchronisé en temps réel avec le code source.',
            'Intègre nativement les types JSON, XML et tableaux tabulaires avec validation de schémas intégrée.',
            'Fournit la concurrence sécurisée et l’observabilité distribuée automatique (OpenTelemetry, Prometheus).',
            'Conçu pour simplifier l’écriture d’API REST, de passerelles GraphQL et de pipelines d’intégration de données d’entreprise.'
        ],
        'url': 'https://ballerina.io',
        'badge': ('Ballerina', 'https://img.shields.io/badge/Ballerina-20B6B0?style=for-the-badge&logo=ballerina&logoColor=white', 'Langages Hybrides & Intégration Cloud')
    },
    'vala': {
        'name': 'Vala',
        'histoire': [
            '2006 : créé par Jürg Billeter et Raffaele Sandrini pour offrir une syntaxe moderne de style C# au sein du projet de bureau GNOME.',
            '2010 : adoption comme langage officiel pour le développement de nombreuses applications fondamentales de GNOME et d’elementary OS.',
            '2018–2022 : modernisation continue du compilateur valac pour cibler les normes C99/C11.',
            'Aujourd’hui : langage de référence pour développer des applications graphiques natives rapides et légères sous Linux/GTK.'
        ],
        'utilite': [
            'Langage orienté objet avec syntaxe moderne se compilant directement en code source C utilisant le framework objet GObject.',
            'Fournit la gestion automatique de la mémoire par comptage de références sans la surcharge d’une machine virtuelle ou d’un GC lourd.',
            'Permet d’écrire des applications GTK 4 riches avec des performances et une réactivité natives pures.',
            'Langage cœur de l’environnement elementary OS et de logiciels populaires comme Geary et Déjà Dup.',
            'Garantit une interopérabilité immédiate et totale avec toutes les bibliothèques C basées sur GObject Introspection.'
        ],
        'url': 'https://vala.dev',
        'badge': ('Vala', 'https://img.shields.io/badge/Vala-A56DE2?style=for-the-badge&logo=gnome&logoColor=white', 'Langages Hybrides & Intégration Cloud')
    },
    'red': {
        'name': 'Red',
        'histoire': [
            '2011 : créé par Nenad Rakocevic pour offrir un successeur moderne, compilé et complet au langage homoiconique Rebol.',
            '2015 : ajout de Red/System, sous-couche de bas niveau équivalente au C permettant d’écrire des pilotes et allocations directes.',
            '2018 : intégration d’un système d’interface graphique multiplateforme complet tenant dans un binaire autonome de moins de 1 Mo.',
            '2023+ : avancées sur le compilateur 64 bits natif et l’écosystème modulaire.',
            'Aujourd’hui : technologie unique combinant programmation système de bas niveau et DSLs de très haut niveau dans un exécutable minuscule.'
        ],
        'utilite': [
            'Langage homoiconique et compilé permettant la création illimitée de langages dédiés (DSLs) avec une syntaxe sans parenthèses obligatoires.',
            'Intègre sa propre chaîne de compilation complète (compilateur, lieur, outillage GUI) dans un seul binaire de 1 Mo sans dépendances.',
            'Permet la programmation système de bas niveau (Red/System) et la création d’interfaces graphiques réactives en quelques lignes.',
            'Dispose de types de données sémantiques riches natifs (emails, URLs, devises, pourcentages, coordonnées).',
            'Idéal pour créer des utilitaires autonomes multiplateformes ultra-légers (Windows, Linux, macOS, ARM).'
        ],
        'url': 'https://www.red-lang.org',
        'badge': ('Red', 'https://img.shields.io/badge/Red-DE2B26?style=for-the-badge&logo=red&logoColor=white', 'Langages Hybrides & Intégration Cloud')
    },
    'rebol': {
        'name': 'Rebol',
        'histoire': [
            '1997 : conçu par Carl Sassenrath (l’architecte du système d’exploitation multitâche de l’Amiga) pour révolutionner l’échange de données sur Internet.',
            '1999 : sortie de Rebol 2, intégrant nativement des dizaines de protocoles réseau (HTTP, FTP, SMTP, POP3) et un moteur GUI vectoriel (VID).',
            '2012 : libération officielle de Rebol 3 en open source sous licence Apache 2.0.',
            'Années 2000–2010 : source d’inspiration directe pour la création du format JSON par Douglas Crockford et du langage Red.',
            'Aujourd’hui : monument d’ingénierie logicielle ayant démontré la puissance de la communication par dialectes contextuels.'
        ],
        'utilite': [
            'Langage d’échange de données et de programmation homoiconique où les données et le code partagent exactement la même structure.',
            'Fournit plus de 40 types de données natifs comprenant la sémantique de date, heure, couleur, devise, URL et adresse IP.',
            'Permet d’écrire des clients et serveurs réseau complets avec interface graphique en moins de 10 lignes de code lisibles.',
            'Pionnier historique des formats de sérialisation légers ayant inspiré JSON et YAML.',
            'Utilisé pour l’automatisation réseau rapide, la création de DSLs métier et les outils distribués ultra-compacts.'
        ],
        'url': 'http://www.rebol.com',
        'badge': ('Rebol', 'https://img.shields.io/badge/Rebol-577788?style=for-the-badge&logo=amigaos&logoColor=white', 'Langages Hybrides & Intégration Cloud')
    },
    'mercury': {
        'name': 'Mercury',
        'histoire': [
            '1995 : conçu par Fergus Henderson, Thomas Conway et Zoltan Somogyi à l’Université de Melbourne pour moderniser la programmation logique.',
            '2000 : publication de versions stables intégrant la pureté déclarative et des performances comparables au C.',
            '2010+ : enrichissement du système de types, modes et déterminisme pour la vérification formelle.',
            '2023+ : maintien actif avec backends C, Java et C# pour le développement de logiciels critiques.',
            'Aujourd’hui : référence mondiale pour la programmation logique purement déclarative et fortement typée à hautes performances.'
        ],
        'utilite': [
            'Langage de programmation logique et fonctionnel purement déclaratif doté d’un système de types statiques, de modes et de déterminisme strict.',
            'Élimine totalement les effets de bord cachés et garantit la correction du flux de données à la compilation.',
            'Compilateur ultra-optimisé générant du code C natif extrêmement rapide rivalisant avec les meilleurs langages impératifs.',
            'Permet de prouver à la compilation si un prédicat a 0, 1 ou plusieurs solutions (analyse de déterminisme).',
            'Utilisé pour les systèmes experts complexes, l’analyse formelle de sécurité et les moteurs de planification logistique avancée.'
        ],
        'url': 'https://mercurylang.org',
        'badge': ('Mercury', 'https://img.shields.io/badge/Mercury-E44D26?style=for-the-badge&logo=prolog&logoColor=white', 'Langages Logiques & Formels')
    },
    'dylan': {
        'name': 'Dylan',
        'histoire': [
            '1992 : conçu par Apple Computer pour alimenter l’ordinateur de poche Apple Newton.',
            '1995 : publication du livre de référence "Dylan Reference Manual" et passage à une syntaxe à accolades plus accessible dérivée d’Algol/Pascal.',
            '1998 : Harlequin publie l’environnement de développement professionnel OpenDylan.',
            '2012+ : reprise en open source par la fondation Dylan Hackers avec compilateur natif basé sur LLVM.',
            'Aujourd’hui : technologie d’avant-garde ayant influencé le système de multi-dispatch de Julia et le modèle objet de Python.'
        ],
        'utilite': [
            'Langage multi-paradigme orienté objet dynamique et typé basé sur le multi-dispatch (multimethods) et la compilation native optimisée.',
            'Sépare les classes de leurs méthodes pour permettre l’extension ouverte du comportement des types sans héritage rigide.',
            'Intègre un système de macros hygiéniques puissant basé sur les arbres syntaxiques.',
            'Compilable vers du code machine natif via LLVM avec élimination du dispatch dynamique lorsque les types sont connus.',
            'Utilisé pour la recherche en génie logiciel, le traitement symbolique et la modélisation objet avancée.'
        ],
        'url': 'https://opendylan.org',
        'badge': ('Dylan', 'https://img.shields.io/badge/Dylan-000000?style=for-the-badge&logo=apple&logoColor=white', 'Langages Hybrides & Intégration Cloud')
    },
    'icon': {
        'name': 'Icon',
        'histoire': [
            '1977 : conçu par Ralph Griswold à l’Université d’Arizona comme successeur de SNOBOL pour la manipulation de texte de haut niveau.',
            'Années 1980–1990 : pionnier du concept d’évaluation dirigée par le but (Goal-Directed Evaluation) et des générateurs.',
            '2000+ : évolution vers le langage Unicon (Unified Extended Icon) avec support objet et réseau natif.',
            'Aujourd’hui : monument d’informatique théorique pour la concision du traitement de motifs textuels et la recherche heuristique.'
        ],
        'utilite': [
            'Langage impératif doté du modèle novateur d’évaluation dirigée par le but où chaque expression produit une séquence de valeurs.',
            'Intègre le retour sur trace automatique (backtracking) au sein des expressions sans nécessiter de structures de boucles explicites.',
            'Fournit des facilités natives de balayage de chaînes (string scanning) d’une concision inégalée pour le parsing de texte.',
            'Permet d’exprimer des algorithmes combinatoires et de résolution de problèmes avec un volume de code minime.',
            'A directement inspiré le mécanisme des générateurs (yield) dans Python, JavaScript et C#.'
        ],
        'url': 'https://www.cs.arizona.edu/icon/',
        'badge': ('Icon', 'https://img.shields.io/badge/Icon-1B365D?style=for-the-badge&logo=gnu&logoColor=white', 'Langages Hybrides & Intégration Cloud')
    },
    'snobol': {
        'name': 'SNOBOL',
        'histoire': [
            '1962 : créé par David J. Farber, Ralph Griswold et Ivan P. Polonsky aux laboratoires Bell d’AT&T.',
            '1967 : sortie de SNOBOL4, version emblématique introduisant le pattern matching comme type de données de première classe.',
            'Années 1970–1980 : utilisé mondialement dans les sciences humaines et la linguistique computationnelle pour l’analyse de textes littéraires.',
            'Aujourd’hui : ancêtre historique vénéré ayant donné naissance aux moteurs d’expressions régulières et au traitement de texte moderne.'
        ],
        'utilite': [
            'Langage pionnier entièrement centré sur la manipulation de chaînes de caractères et la reconnaissance de formes textuelles.',
            'Traite les motifs (patterns) comme des objets de première classe pouvant être combinés, imbriqués et concaténés dynamiquement.',
            'Moteur historique d’analyse morphologique, d’indexation de corpus textuels et de traduction automatique des langues.',
            'Intégrait le typage dynamique et la conversion automatique de types bien avant l’avènement des langages de script modernes.',
            'A établi les fondements conceptuels sur lesquels reposent AWK, Perl, Python et les parseurs modernes.'
        ],
        'url': 'http://www.snobol4.org',
        'badge': ('SNOBOL', 'https://img.shields.io/badge/SNOBOL-333333?style=for-the-badge&logo=bell&logoColor=white', 'Langages Historiques & Pionniers')
    },
    'postscript': {
        'name': 'PostScript',
        'histoire': [
            '1982–1984 : créé par John Warnock et Charles Geschke, fondateurs d’Adobe Systems, pour révolutionner l’impression graphique.',
            '1985 : intégré dans l’imprimante Apple LaserWriter, déclenchant la révolution mondiale de la publication assistée par ordinateur (PAO).',
            '1993 : sert de fondation architecturale directe pour la création du format universel PDF (Portable Document Format).',
            'Aujourd’hui : standard mondial omniprésent interprété directement par les microprocesseurs des imprimantes et traceurs professionnels.'
        ],
        'utilite': [
            'Langage de programmation impératif et vectoriel Turing-complet basé sur une pile (stack-based) décrivant l’apparence visuelle d’une page imprimée.',
            'Permet le tracé de courbes de Bézier, la manipulation de polices vectorielles scalables et la composition typographique haute résolution.',
            'Exécuté directement par le processeur RIP (Raster Image Processor) intégré à l’intérieur des imprimantes laser professionnelles.',
            'Matrice technique dont sont issus les formats graphiques vectoriels modernes (PDF, EPS, SVG).',
            'Permet la programmation d’effets visuels et de fractales directement dans le fichier d’impression sans logiciel externe.'
        ],
        'url': 'https://www.adobe.com/products/postscript.html',
        'badge': ('PostScript', 'https://img.shields.io/badge/PostScript-FF0000?style=for-the-badge&logo=adobe&logoColor=white', 'Langages Historiques & Pionniers')
    },
    'tex': {
        'name': 'TeX / LaTeX',
        'histoire': [
            '1978 : créé par Donald Knuth (auteur de The Art of Computer Programming) à l’Université Stanford pour fixer la perfection typographique mathématique.',
            '1984 : Leslie Lamport conçoit LaTeX comme surcouche de macros structurées de haut niveau au-dessus du moteur TeX.',
            '1989 : Knuth gèle officiellement les fonctionnalités de TeX, les versions convergeant asymptotiquement vers le nombre π (version actuelle 3.141592653...).',
            'Aujourd’hui : standard planétaire absolu et incontesté de l’édition scientifique, des thèses académiques et des publications en mathématiques et physique.'
        ],
        'utilite': [
            'Système de composition typographique et langage de programmation par macros dédié à la mise en page scientifique de haute précision.',
            'Offre le moteur de rendu de formules mathématiques le plus parfait, esthétique et rigoureux de l’histoire de l’édition.',
            'Gère automatiquement la numérotation des sections, les références croisées, les index et la bibliographie savante (BibTeX/Biber).',
            'Standard exigé par les plus grandes revues scientifiques mondiales (Nature, IEEE, ACM, arXiv) pour la soumission d’articles.',
            'Garantit une pérennité et une reproductibilité exacte au pixel près des documents sur plusieurs décennies.'
        ],
        'url': 'https://www.latex-project.org',
        'badge': ('TeX LaTeX', 'https://img.shields.io/badge/TeX_LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white', 'Langages Historiques & Pionniers')
    }
}

def run():
    target_dir = os.path.join(os.path.dirname(__file__), '..', 'languages')
    os.makedirs(target_dir, exist_ok=True)
    
    count = 0
    for slug, data in WAVE3_DB.items():
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
    print(f'Vague 3 terminée : {count} nouvelles fiches écrites !')

if __name__ == '__main__':
    run()
