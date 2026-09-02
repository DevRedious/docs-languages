import os

EXPANSION_DB = {
    # Enterprise & 4GL
    'abap': {
        'name': 'ABAP',
        'histoire': [
            '1983 : créé par SAP comme langage de génération de rapports (Allgemeiner Berichts-Aufbereitungs-Prozessor) pour SAP R/2.',
            '1992 : refonte majeure pour SAP R/3, devenant le langage exclusif de programmation des applications de gestion métier du système.',
            '1999 : introduction d’ABAP Objects avec la version 4.6, apportant l’orientation objet complète.',
            '2015 : modernisation pour SAP S/4HANA et intégration étroite avec la base en mémoire SAP HANA (ABAP Core Data Services).',
            'Aujourd’hui : standard mondial incontesté des ERP d’entreprise avec l’environnement ABAP Cloud.'
        ],
        'utilite': [
            'Langage de haut niveau conçu sur mesure pour le traitement transactionnel des processus d’affaires et financiers des entreprises.',
            'Intègre nativement le SQL (Open SQL) directement dans la syntaxe du langage sans couche ORM intermédiaire.',
            'Bénéficie d’un environnement de développement complet intégré au serveur d’applications SAP (ABAP Workbench / Eclipse ADT).',
            'Utilisé par la majorité des entreprises du Fortune 500 pour personnaliser leurs processus industriels, logistiques et comptables.',
            'Gère les verrouillages transactionnels logiques (LUW - Logical Units of Work) indispensables à l’intégrité bancaire et comptable.'
        ],
        'url': 'https://community.sap.com/topics/abap',
        'badge': ('ABAP', 'https://img.shields.io/badge/ABAP-008FD3?style=for-the-badge&logo=sap&logoColor=white', 'Entreprise & 4GL Métier')
    },
    'rpg': {
        'name': 'RPG (IBM i)',
        'histoire': [
            '1959 : créé par IBM comme émulateur de cartes perforées (Report Program Generator) sur les ordinateurs IBM 1401.',
            '1969 : lancement de RPG II pour le système IBM System/3, établissant le modèle cyclique de traitement par lots.',
            '1988 : RPG/400 accompagne le lancement historique de la gamme des serveurs IBM AS/400.',
            '1995–2001 : RPG IV et ILE RPG révolutionnent le langage avec l’intégration modulaire et le format libre (Free-Format).',
            'Aujourd’hui : RPG moderne en format totalement libre (Fully Free-Form RPG) intégré avec REST, JSON et les conteneurs sur IBM i.'
        ],
        'utilite': [
            'Langage déclaratif et procédural de très haut niveau optimisé pour le traitement rapide de flux de données commerciaux et bancaires.',
            'Conçu pour exécuter des millions de transactions par seconde avec une stabilité de plateforme légendaire sans redémarrage.',
            'Intègre l’accès natif direct aux tables et vues de la base de données relationnelle DB2 pour IBM i.',
            'Pilier fondamental de l’informatique bancaire, de l’assurance, de la grande distribution et des chaînes logistiques mondiales.',
            'Permet l’interopérabilité totale avec Java, Node.js, Python et les services web modernes sur architecture Power.'
        ],
        'url': 'https://www.ibm.com/products/ibm-i',
        'badge': ('RPG', 'https://img.shields.io/badge/RPG_IBM_i-052FAD?style=for-the-badge&logo=ibm&logoColor=white', 'Entreprise & 4GL Métier')
    },
    'mumps': {
        'name': 'MUMPS (M)',
        'histoire': [
            '1966 : développé par Neil Pappalardo et Octo Barnett au Massachusetts General Hospital pour informatiser les dossiers médicaux.',
            '1977 : standardisation officielle ANSI (ANSI X11.1-1977), suivie par l’ISO en 1990.',
            '1997 : InterSystems lance Caché (devenu InterSystems IRIS), modernisant MUMPS avec l’accès SQL et orienté objet.',
            '2010+ : moteur sous-jacent du système VistA du Département des Anciens Combattants américain et du leader médical Epic Systems.',
            'Aujourd’hui : technologie sous-tendant les dossiers médicaux de plus de 300 millions de patients dans le monde et le système boursier mondial.'
        ],
        'utilite': [
            'Langage dynamique associant de manière indissociable un langage de programmation et une base de données transactionnelle hiérarchique.',
            'Stocke les données directement sur disque via des tableaux globaux hiérarchiques persistants (globals) sans étape de mapping relationnel.',
            'Offre une vitesse de lecture et d’écriture en mémoire partagée parmi les plus fulgurantes de l’industrie logicielle.',
            'Standard universel des systèmes d’information hospitaliers (Dossier Patient Informatisé), de la santé et des transactions de cartes bancaires.',
            'Garantit une persistance des données et une tolérance aux pannes exceptionnelles éprouvées depuis plus de 50 ans.'
        ],
        'url': 'https://www.intersystems.com',
        'badge': ('MUMPS', 'https://img.shields.io/badge/MUMPS-002D62?style=for-the-badge&logo=medicare&logoColor=white', 'Entreprise & 4GL Métier')
    },
    'progress-abl': {
        'name': 'Progress ABL (OpenEdge)',
        'histoire': [
            '1984 : créé par Progress Software sous le nom de Progress 4GL pour simplifier la création d’applications de gestion d’entreprise.',
            '1993 : introduction du serveur de bases de données relationnelles OpenEdge et de l’environnement graphique GUI.',
            '2006 : renommage officiel en OpenEdge Advanced Business Language (ABL) avec ajout de l’orientation objet.',
            '2018+ : intégration avec les microservices, les API REST/JSON et les architectures cloud hybrides.',
            'Aujourd’hui : langage d’entreprise mature motorisant des milliers d’applications ERP, financières et industrielles.'
        ],
        'utilite': [
            'Langage de quatrième génération (4GL) combinant règles métier, logique transactionnelle et persistance de données en un seul bloc.',
            'Permet d’écrire des opérations de base de données directement dans la syntaxe sans recourir à des requêtes SQL verbeuses.',
            'Gère automatiquement les transactions, le verrouillage des enregistrements et l’intégrité référentielle.',
            'Moteur de progiciels de gestion intégrés (ERP), de solutions bancaires et d’outils de gestion de chaînes d’approvisionnement.',
            'Réputé pour son coût total de possession (TCO) très faible et l’extrême productivité de développement métier.'
        ],
        'url': 'https://www.progress.com/openedge',
        'badge': ('Progress ABL', 'https://img.shields.io/badge/Progress_ABL-5BC500?style=for-the-badge&logo=progress&logoColor=white', 'Entreprise & 4GL Métier')
    },
    'visual-foxpro': {
        'name': 'Visual FoxPro',
        'histoire': [
            '1984 : Fox Software crée FoxBASE pour offrir un clone de dBase II ultra-rapide sur PC.',
            '1992 : Microsoft rachète Fox Software pour intégrer la technologie de base de données ultra-rapide Rushmore.',
            '1995 : lancement de Visual FoxPro 3.0, introduisant la programmation orientée objet complète et le RAD sous Windows 95.',
            '2007 : Microsoft publie la version finale Visual FoxPro 9.0 Service Pack 2.',
            'Aujourd’hui : environnement historique vénéré pour la vitesse de son moteur de données local, toujours maintenu par des communautés actives.'
        ],
        'utilite': [
            'Langage de programmation procédural et orienté objet intégrant son propre moteur de base de données relationnelle locale sur disque.',
            'Pionnier de la technologie d’optimisation de requêtes Rushmore offrant des temps de réponse instantanés sur gros volumes.',
            'Permet la création rapide d’applications de bureau Windows complètes avec formulaires, grilles de données et rapports.',
            'Utilisé historiquement pour gérer la comptabilité, les stocks et la facturation des PME/ETI mondiales.',
            'Offre une syntaxe de requêtage SQL intégrée fusionnée avec les commandes natives de manipulation de tables (.dbf).'
        ],
        'url': 'https://learn.microsoft.com/previous-versions/visualstudio/foxpro/',
        'badge': ('Visual FoxPro', 'https://img.shields.io/badge/Visual_FoxPro-C41F14?style=for-the-badge&logo=visualstudio&logoColor=white', 'Entreprise & 4GL Métier')
    },
    'clipper': {
        'name': 'Clipper',
        'histoire': [
            '1985 : créé par Nantucket Corporation (Nantucket Inc.) pour compiler les scripts dBase III en fichiers exécutables natifs .EXE autonomes.',
            '1990 : sortie de Clipper 5.0, révolutionnant le langage avec les blocs de code (closures), les tableaux multidimensionnels et les objets.',
            '1992 : rachat de Nantucket par Computer Associates (CA), devenant CA-Clipper.',
            '2000+ : renaissance open source sous la forme des compilateurs Harbour et xHarbour (multiplateformes, 32/64 bits).',
            'Aujourd’hui : langage patrimonial majeur continuant de vivre au travers du projet Harbour pour la modernisation d’applications de gestion.'
        ],
        'utilite': [
            'Compilateur et langage de programmation impératif conçu pour bâtir des applications de gestion d’entreprise complètes.',
            'Produit des binaires natifs rapides sans interpréteur externe lourd.',
            'Fournit une gestion native des fichiers de données relationnels xBase (.dbf, .ntx, .cdx).',
            'A popularisé l’utilisation des blocs de code anonymes permettant une approche fonctionnelle avant l’heure.',
            'Utilisé pour maintenir des parcs applicatifs industriels, médicaux et douaniers.'
        ],
        'url': 'https://harbour.github.io',
        'badge': ('Clipper', 'https://img.shields.io/badge/Clipper_xBase-1B365D?style=for-the-badge&logo=dosbox&logoColor=white', 'Entreprise & 4GL Métier')
    },
    'rexx': {
        'name': 'Rexx',
        'histoire': [
            '1979 : créé par Mike Cowlishaw au centre de recherche IBM de Hursley comme langage de script structuré et lisible pour l’humain.',
            '1988 : standardisé par IBM comme langage de procédures unifié pour son architecture logicielle SAA (Systems Application Architecture).',
            '1990 : adoption par Commodore comme langage de script système par excellence de l’Amiga (ARexx).',
            '1996 : publication de la norme officielle ANSI X3.274-1996 et émergence de versions orientées objet (Object REXX).',
            'Aujourd’hui : langage d’automatisation incontournable des systèmes d’exploitation IBM z/OS (Mainframe) et Linux via Regina REXX.'
        ],
        'utilite': [
            'Langage de script interprété à typage dynamique conçu pour maximiser la lisibilité et la simplicité syntaxique.',
            'Gère les opérations arithmétiques décimales à précision arbitraire exacte sans erreurs d’arrondi en virgule flottante.',
            'Intègre le puissant mécanisme des tableaux associatifs à clés multiples (stem variables).',
            'Sert de langage de contrôle et d’orchestration de scripts pour les environnements de production mainframes (TSO, ISPF).',
            'Permet l’automatisation de flux applicatifs inter-processus et la création de macros système.'
        ],
        'url': 'https://www.rexxla.org',
        'badge': ('Rexx', 'https://img.shields.io/badge/Rexx-052FAD?style=for-the-badge&logo=ibm&logoColor=white', 'Entreprise & 4GL Métier')
    },

    # GPU & Shaders
    'cuda': {
        'name': 'CUDA C/C++',
        'histoire': [
            '2006–2007 : dévoilé par NVIDIA sous la direction d’Ian Buck pour transformer les GPU de simples accélérateurs graphiques en processeurs de calcul massif (GPGPU).',
            '2012 : AlexNet remporte le concours ImageNet grâce à un entraînement accéléré par CUDA, déclenchant l’explosion de l’IA moderne.',
            '2017–2020 : intégration des cœurs Tensor Core pour le calcul matriciel en demi-précision et précision mixte (architectures Volta et Ampere).',
            '2022–2024 : déploiement des architectures Hopper et Blackwell, optimisées pour les grands modèles de langage (LLMs).',
            'Aujourd’hui : plateforme et langage hétérogène incontestés à la base de toute la révolution mondiale de l’intelligence artificielle.'
        ],
        'utilite': [
            'Extension de C/C++ permettant de programmer directement les milliers de cœurs de calcul parallèle des GPU NVIDIA.',
            'Utilise le modèle de programmation SIMT (Single Instruction, Multiple Threads) organisé en grilles, blocs et warps de threads.',
            'Permet la gestion manuelle ultra-fine de la mémoire partagée locale (shared memory) et des registres.',
            'Socle technologique absolu de tous les frameworks d’apprentissage profond (PyTorch, TensorFlow, vLLM, TensorRT).',
            'Utilisé dans le rendu 3D temps réel, la dynamique moléculaire, la simulation sismique et l’astrophysique.'
        ],
        'url': 'https://developer.nvidia.com/cuda-zone',
        'badge': ('CUDA', 'https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white', 'GPU, Shaders & Graphisme')
    },
    'opencl': {
        'name': 'OpenCL',
        'histoire': [
            '2008 : initié par Apple en collaboration avec AMD, IBM, Intel et NVIDIA, puis confié au consortium Khronos Group.',
            '2009 : publication de la norme OpenCL 1.0 comme standard ouvert et libre de droits pour le calcul hétérogène.',
            '2015 : OpenCL 2.1 introduit l’arbre de représentation intermédiaire standard SPIR-V.',
            '2020 : publication d’OpenCL 3.0, modularisant la spécification pour s’adapter aux architectures matérielles de pointe et à l’embarqué.',
            'Aujourd’hui : standard industriel ouvert pour exécuter du calcul parallèle sur CPU, GPU, DSP et FPGA multi-constructeurs.'
        ],
        'utilite': [
            'Langage dérivé du C99 (OpenCL C) et API permettant d’écrire des kernels de calcul exécutés de façon transparente sur du matériel hétérogène.',
            'Garantit la portabilité du code source de calcul sans verrouillage propriétaire envers un constructeur unique.',
            'Permet l’exploitation combinée des processeurs multi-cœurs (CPU), puces graphiques (GPU) et accélérateurs matériels (FPGA/NPU).',
            'Utilisé dans le traitement d’images médicales, la vision par ordinateur (OpenCV), le montage vidéo professionnel et la finance.',
            'Prend en charge la compilation à la volée (JIT) des kernels ou la distribution sous format intermédiaire binaire SPIR-V.'
        ],
        'url': 'https://www.khronos.org/opencl/',
        'badge': ('OpenCL', 'https://img.shields.io/badge/OpenCL-005C8A?style=for-the-badge&logo=khronos&logoColor=white', 'GPU, Shaders & Graphisme')
    },
    'glsl': {
        'name': 'GLSL',
        'histoire': [
            '2004 : standardisé par le Khronos Group avec la publication d’OpenGL 2.0 pour remplacer le pipeline fixe par des shaders programmables.',
            '2009 : standardisation de GLSL ES pour la spécification OpenGL ES 2.0, révolutionnant les graphismes 3D sur smartphones et tablettes.',
            '2011 : adoption comme langage de shaders natif du web avec la standardisation de WebGL 1.0 par le W3C et Khronos.',
            '2016+ : compilation de GLSL vers le format binaire intermédiaire SPIR-V pour l’API Vulkan.',
            'Aujourd’hui : langage de shaders universel pour les applications graphiques OpenGL, Vulkan et WebGL.'
        ],
        'utilite': [
            'Langage de haut niveau à syntaxe de type C conçu spécifiquement pour s’exécuter massivement en parallèle sur les processeurs graphiques.',
            'Permet de programmer toutes les étapes du pipeline graphique : vertex shaders, fragment/pixel shaders, geometry et compute shaders.',
            'Intègre nativement les types de vecteurs mathématiques (vec2, vec3, vec4), matrices (mat4) et fonctions trigonométriques matérielles.',
            'Moteur du rendu 3D pour le web interactif (Three.js, Babylon.js via WebGL) et de milliers d’applications multiplateformes.',
            'Utilisé pour les effets visuels de post-traitement, l’éclairage physique réaliste (PBR) et l’art génératif (Shadertoy).'
        ],
        'url': 'https://www.khronos.org/opengl/wiki/OpenGL_Shading_Language',
        'badge': ('GLSL', 'https://img.shields.io/badge/GLSL-5586A4?style=for-the-badge&logo=opengl&logoColor=white', 'GPU, Shaders & Graphisme')
    },
    'hlsl': {
        'name': 'HLSL',
        'histoire': [
            '2002 : conçu par Microsoft en collaboration avec NVIDIA et ATI pour l’API DirectX 9.0 (Shader Model 1.0 & 2.0).',
            '2006 : refonte pour DirectX 10 unifiant l’architecture des shaders (Shader Model 4.0).',
            '2015 : DirectX 12 et Shader Model 6.0 introduisent le compilateur open source DXC (DirectX Shader Compiler) basé sur LLVM.',
            '2018 : Shader Model 6.3 apporte le support matériel du ray tracing temps réel (DirectX Raytracing - DXR).',
            'Aujourd’hui : standard absolu du jeu vidéo AAA sur consoles Xbox et PC Windows, compilable vers DirectX et Vulkan.'
        ],
        'utilite': [
            'Langage de programmation de shaders de haut niveau conçu pour le pipeline graphique matériel DirectX.',
            'Permet la programmation des shaders géométriques, de pixels, de calcul, de maillage (Mesh Shaders) et de lancer de rayons (Ray Tracing).',
            'Langage de shaders par défaut des plus grands moteurs de jeux vidéo de l’industrie (Unreal Engine, Unity).',
            'Compilable vers le format intermédiaire DXIL (DirectX Intermediate Language) ou SPIR-V pour un ciblage multiplateforme.',
            'Optimisé pour tirer le potentiel maximal des architectures de GPU modernes de dernière génération.'
        ],
        'url': 'https://learn.microsoft.com/windows/win32/direct3dhlsl/dx-graphics-hlsl',
        'badge': ('HLSL', 'https://img.shields.io/badge/HLSL-0078D7?style=for-the-badge&logo=windows&logoColor=white', 'GPU, Shaders & Graphisme')
    },
    'wgsl': {
        'name': 'WGSL',
        'histoire': [
            '2020 : conçu par le W3C GPU for the Web Community Group comme langage de shaders standard de la nouvelle API WebGPU.',
            '2023 : déploiement initial de WebGPU et WGSL dans les navigateurs Google Chrome 113+ et Firefox.',
            '2024 : intégration dans Safari et adoption par les moteurs de rendu WebAssembly et Rust (wgpu).',
            '2024+ : adoption par les frameworks de machine learning pour exécuter des modèles d’IA directement dans le navigateur (WebLLM, Transformers.js).',
            'Aujourd’hui : standard de nouvelle génération pour le graphisme 3D et le calcul GPU sécurisé sur le Web.'
        ],
        'utilite': [
            'Langage de shaders spécialement conçu pour WebGPU, garantissant la sûreté mémoire et la conformité stricte pour les navigateurs.',
            'Se traduit de manière déterministe et efficace vers les langages de shaders natifs sous-jacents (HLSL, MSL, SPIR-V).',
            'Permet d’exécuter à la fois des shaders graphiques haute fidélité et des shaders de calcul généraliste (Compute Shaders).',
            'Moteur de l’intelligence artificielle locale dans le navigateur Web sans dépendance logicielle côté serveur.',
            'Adopté par l’écosystème Rust natif via la bibliothèque wgpu pour le développement d’applications desktop et web unifiées.'
        ],
        'url': 'https://www.w3.org/TR/WGSL/',
        'badge': ('WGSL', 'https://img.shields.io/badge/WGSL-005A9C?style=for-the-badge&logo=w3c&logoColor=white', 'GPU, Shaders & Graphisme')
    },
    'metal': {
        'name': 'Metal Shading Language (MSL)',
        'histoire': [
            '2014 : dévoilé par Apple lors de la WWDC 2014 pour remplacer OpenGL par une API graphique à très faible surcharge matérielle.',
            '2017 : lancement de Metal 2, optimisant le calcul GPU généraliste et l’apprentissage automatique.',
            '2020 : transition vers les puces Apple Silicon (M1/M2/M3/M4) avec mémoire unifiée partagée CPU/GPU ultra-rapide.',
            '2022–2023 : Metal 3 introduit le ray tracing matériel accéléré, le mesh shading et l’upscaling spatial MetalFX.',
            'Aujourd’hui : langage exclusif et optimisé pour l’accélération graphique et IA sur tous les appareils Apple (Mac, iPad, iPhone, Vision Pro).'
        ],
        'utilite': [
            'Langage de shaders basé sur C++14 avec des extensions spécifiques au matériel graphique Apple.',
            'Exploite l’architecture de mémoire unifiée (UMA) des puces Apple Silicon, éliminant les transferts de mémoire coûteux entre CPU et GPU.',
            'Permet la programmation de shaders de rendu 3D, de lancer de rayons matériel et de calculs tensoriels d’IA.',
            'Moteur de rendu de référence pour les logiciels de création professionnelle sur Mac (Final Cut Pro, Blender Metal, DaVinci Resolve).',
            'Moteur sous-jacent du framework Apple MLX et de CoreML pour l’exécution locale de modèles d’IA générative.'
        ],
        'url': 'https://developer.apple.com/metal/',
        'badge': ('Metal MSL', 'https://img.shields.io/badge/Metal_MSL-000000?style=for-the-badge&logo=apple&logoColor=white', 'GPU, Shaders & Graphisme')
    },

    # Shells & Stream
    'awk': {
        'name': 'AWK',
        'histoire': [
            '1977 : créé aux laboratoires Bell par Alfred Aho, Peter Weinberger et Brian Kernighan (dont les initiales forment le nom AWK).',
            '1985 : sortie de New AWK (nawk), introduisant les fonctions définies par l’utilisateur et la manipulation de flux avancée.',
            '1988 : création de GNU Awk (gawk) par le projet GNU, devenu l’implémentation de référence sous Linux.',
            '1992 : standardisation officielle au sein de la norme internationale POSIX.',
            'Aujourd’hui : outil universel préinstallé par défaut sur la quasi-totalité des systèmes d’exploitation Unix, Linux et macOS.'
        ],
        'utilite': [
            'Langage de programmation orienté données conçu pour le traitement ligne par ligne et l’extraction de données textuelles.',
            'Structuré autour du modèle Motif-Action (pattern-action) exécutant des blocs d’instructions lorsque des conditions sont remplies.',
            'Découpe automatiquement chaque ligne en champs indexés ($1, $2, $NF), facilitant l’analyse de fichiers structurés (CSV, logs).',
            'Indispensable dans les pipelines d’administration système, l’agrégation de métriques et le traitement de données volumineuses en streaming.',
            'Prend en charge les tableaux associatifs, les expressions régulières et le formatage de rapports avancés.'
        ],
        'url': 'https://www.gnu.org/software/gawk/',
        'badge': ('AWK', 'https://img.shields.io/badge/AWK-1A1A1A?style=for-the-badge&logo=gnubash&logoColor=white', 'Shells & Outils de Flux Unix')
    },
    'sed': {
        'name': 'Sed',
        'histoire': [
            '1974 : développé par Lee E. McMahon aux laboratoires Bell comme éditeur de texte non interactif orienté flux (Stream Editor).',
            'Années 1970–1980 : intégration standardisée dans toutes les versions d’Unix d’AT&T et de BSD.',
            '1989 : création de GNU sed par le projet GNU, apportant des extensions majeures aux expressions régulières.',
            '1992 : standardisation officielle au sein de la norme POSIX.',
            'Aujourd’hui : utilitaire fondamental préinstallé sur tous les serveurs et conteneurs Linux du monde.'
        ],
        'utilite': [
            'Langage de commande compact et éditeur de flux conçu pour transformer, filtrer et substituer du texte à la volée.',
            'Permet la substitution textuelle massive par expressions régulières (s/recherche/remplacement/g) sans charger le fichier en RAM.',
            'Traite les flux de données continus (pipes) ligne par ligne avec une vitesse d’exécution maximale.',
            'Indispensable dans les scripts d’installation, les Dockerfiles et l’automatisation de la configuration système.',
            'Intègre un espace de travail temporaire (hold space) permettant des manipulations conditionnelles multilignes complexes.'
        ],
        'url': 'https://www.gnu.org/software/sed/',
        'badge': ('Sed', 'https://img.shields.io/badge/Sed-2C3E50?style=for-the-badge&logo=gnubash&logoColor=white', 'Shells & Outils de Flux Unix')
    },
    'zsh': {
        'name': 'Zsh (Z Shell)',
        'histoire': [
            '1990 : créé par Paul Falstad à l’Université de Princeton comme shell interactif combinant le meilleur de ksh, tcsh et bash.',
            '2009 : création du framework communautaire Oh My Zsh par Robby Russell, provoquant une explosion de popularité mondiale.',
            '2019 : Apple choisit officiellement Zsh comme shell par défaut sur tous les ordinateurs macOS à partir de macOS Catalina.',
            '2020+ : écosystème riche de plugins ultra-rapides (zsh-autosuggestions, zsh-syntax-highlighting, Powerlevel10k).',
            'Aujourd’hui : shell interactif de prédilection de millions de développeurs et ingénieurs DevOps.'
        ],
        'utilite': [
            'Shell en ligne de commande hautement programmable et personnalisable compatible avec la syntaxe POSIX et Bash.',
            'Dispose du système d’autocomplétion contextuelle programmable le plus puissant et complet de l’écosystème Unix.',
            'Intègre le globbing étendu récursif puissant (ex: **/*.ts) et la correction orthographique automatique des commandes.',
            'Prend en charge la thématisation visuelle avancée du prompt (statut Git, temps d’exécution, environnement virtuel).',
            'Offre un partage d’historique de commandes en temps réel entre toutes les sessions de terminal ouvertes.'
        ],
        'url': 'https://www.zsh.org',
        'badge': ('Zsh', 'https://img.shields.io/badge/Zsh-F1502F?style=for-the-badge&logo=zsh&logoColor=white', 'Shells & Outils de Flux Unix')
    },
    'fish': {
        'name': 'Fish Shell',
        'histoire': [
            '2005 : créé par Axel Liljencrantz sous la devise "friendly interactive shell" pour réinventer l’expérience du terminal.',
            '2011 : refonte communautaire du projet avec passage au développement open source sur GitHub.',
            '2021 : sortie de Fish 3.x, stabilisant les performances et les fonctionnalités interactives clé en main.',
            '2024 : réécriture complète du cœur de Fish en Rust (Fish 4.0) pour des gains massifs de réactivité et de sûreté mémoire.',
            'Aujourd’hui : référence mondiale des shells interactifs modernes out-of-the-box ne nécessitant aucune configuration manuelle.'
        ],
        'utilite': [
            'Shell interactif moderne proposant coloration syntaxique, autosuggestions et autocomplétion par onglets prêtes à l’emploi.',
            'Génère automatiquement les complétions de commandes en analysant dynamiquement les pages de manuel (man pages) du système.',
            'Adopte une syntaxe de script épurée et cohérente rejetant délibérément les pièges historiques des shells POSIX.',
            'Fournit un outil de configuration graphique complet accessible directement depuis le navigateur web (fish_config).',
            'Conçu pour maximiser l’efficacité quotidienne des développeurs en réduisant drastiquement le nombre de frappes clavier.'
        ],
        'url': 'https://fishshell.com',
        'badge': ('Fish', 'https://img.shields.io/badge/Fish_Shell-38BDF8?style=for-the-badge&logo=fishshell&logoColor=white', 'Shells & Outils de Flux Unix')
    },
    'ksh': {
        'name': 'KornShell (ksh)',
        'histoire': [
            '1983 : créé par David Korn aux laboratoires Bell d’AT&T pour combiner la compatibilité du Bourne shell avec les fonctionnalités interactives du C shell.',
            '1988 : publication de ksh88, devenu la base de référence de la standardisation officielle POSIX Shell.',
            '1993 : version majeure ksh93 introduisant les types de données associatifs, les nombres flottants et les fonctions mathématiques.',
            '2000 : publication du code source en open source sous licence CPL.',
            'Aujourd’hui : shell historique de référence pour les environnements de production d’entreprise Unix (AIX, Solaris, Linux).'
        ],
        'utilite': [
            'Shell de commande et langage de script puissant réputé pour sa rapidité d’exécution supérieure à la plupart des shells concurrents.',
            'Norme historique dont sont directement issus les mécanismes modernes d’évaluation arithmétique $(( ... )) et de substitution $( ... ).',
            'Prend en charge la manipulation native des nombres à virgule flottante et les structures de données associatives.',
            'Standard privilégié pour les scripts d’administration et batchs transactionnels dans les banques et télécoms sur serveurs AIX.',
            'Garantit une compatibilité ascendante rigoureuse assurant l’exécution sans faille de scripts conçus il y a plusieurs décennies.'
        ],
        'url': 'http://www.kornshell.com',
        'badge': ('Ksh', 'https://img.shields.io/badge/KornShell-000000?style=for-the-badge&logo=gnubash&logoColor=white', 'Shells & Outils de Flux Unix')
    },
    'tcsh': {
        'name': 'C Shell (csh / tcsh)',
        'histoire': [
            '1978 : créé par Bill Joy à l’Université de Berkeley pour le système d’exploitation BSD Unix, adoptant une syntaxe inspirée du langage C.',
            '1983 : Ken Greer développe tcsh à l’Université Carnegie Mellon en ajoutant l’autocomplétion des commandes et l’édition de ligne de commande.',
            'Années 1980–1990 : shell interactif par défaut des stations de travail Silicon Graphics (IRIX) et des environnements universitaires.',
            '2000+ : maintien continu de la compatibilité sur les systèmes FreeBSD et les distributions Linux.',
            'Aujourd’hui : utilisé dans les environnements académiques scientifiques et les chaînes de conception de semi-conducteurs (EDA).'
        ],
        'utilite': [
            'Shell interactif dont la syntaxe de contrôle (if, while, foreach) est directement calquée sur la syntaxe du langage C.',
            'Pionnier historique de l’autocomplétion de noms de fichiers et de l’historique des commandes (!n, !$).',
            'Dispose d’un éditeur de ligne de commande complet avec raccourcis de style Emacs ou Vi intégrés.',
            'Utilisé traditionnellement pour piloter des suites de simulation électronique et des stations de calcul scientifique.',
            'Offre une gestion native des alias de commandes avec passage d’arguments positionnels.'
        ],
        'url': 'https://www.tcsh.org',
        'badge': ('Tcsh', 'https://img.shields.io/badge/Tcsh-2B2B2B?style=for-the-badge&logo=freebsd&logoColor=white', 'Shells & Outils de Flux Unix')
    },

    # Formal Specification & Logic
    'tla-plus': {
        'name': 'TLA+ (Leslie Lamport)',
        'histoire': [
            '1999 : conçu par Leslie Lamport (prix Turing 2013) comme langage formel pour modéliser et spécifier les systèmes concurrents et distribués.',
            '2002 : publication du livre fondamental "Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers".',
            '2014 : publication d’un article marquant d’Amazon Web Services (AWS) révélant l’utilisation de TLA+ pour concevoir des services critiques comme S3 et DynamoDB.',
            '2019 : adoption par Microsoft pour vérifier la cohérence des protocoles distribués Azure et Cosmos DB.',
            'Aujourd’hui : standard mondial de la spécification formelle de protocoles de consensus et d’architectures distribuées.'
        ],
        'utilite': [
            'Langage de modélisation formelle basé sur la logique temporelle des actions (Temporal Logic of Actions) et la théorie des ensembles.',
            'Permet de décrire rigoureusement le comportement d’un système distribué avant d’écrire la moindre ligne de code applicatif.',
            'Fournit le vérificateur de modèles TLC (Model Checker) explorant exhaustivement tous les états possibles pour trouver les bugs de concurrence rares.',
            'Détecte infailliblement les interblocages (deadlocks), les corruptions de données distribuées et les violations de vivacité (liveness).',
            'Utilisé pour concevoir des bases de données distribuées, des algorithmes de consensus (Raft, Paxos) et des puces électroniques.'
        ],
        'url': 'https://lamport.azurewebsites.net/tla/tla.html',
        'badge': ('TLA+', 'https://img.shields.io/badge/TLA+-FF9900?style=for-the-badge&logo=amazonwebservices&logoColor=white', 'Spécification Formelle & Modélisation')
    },
    'alloy': {
        'name': 'Alloy',
        'histoire': [
            '1997 : conçu par Daniel Jackson au laboratoire de recherche en informatique du MIT (CSAIL).',
            '2006 : publication de l’ouvrage de référence "Software Abstractions: Logic, Language, and Analysis".',
            '2012–2018 : versions 4 et 5 intégrant des solveurs SAT modernes pour une analyse structurelle ultra-rapide.',
            '2021 : sortie d’Alloy 6 intégrant nativement des opérateurs de logique temporelle linéaire (LTL).',
            'Aujourd’hui : outil pédagogique et industriel majeur pour explorer et valider la cohérence des architectures logicielles.'
        ],
        'utilite': [
            'Langage déclaratif de spécification structurelle basé sur la logique des relations au premier ordre.',
            'Permet de modéliser des ontologies complexes, des politiques de sécurité et des structures de données abstraites.',
            'Utilise le solveur Alloy Analyzer pour générer automatiquement des contre-exemples visuels lorsqu’une propriété est violée.',
            'Permet de valider la conception d’API, de systèmes de contrôle d’accès (RBAC/ABAC) et de protocoles réseau.',
            'Fournit une visualisation graphique interactive immédiate des instances de modèles valides.'
        ],
        'url': 'https://alloytools.org',
        'badge': ('Alloy', 'https://img.shields.io/badge/Alloy-1F2937?style=for-the-badge&logo=mit&logoColor=white', 'Spécification Formelle & Modélisation')
    },
    'datalog': {
        'name': 'Datalog',
        'histoire': [
            '1977–1980 : formalisé par des chercheurs en bases de données déductives comme sous-ensemble déclaratif de Prolog sans fonctions complexes.',
            'Années 1990 : standardisation théorique pour l’analyse statique de programmes et l’optimisation de requêtes récursives.',
            '2010+ : résurgence industrielle majeure avec le moteur de base de données Datomic (Rich Hickey) et l’outil d’analyse de sécurité GitHub CodeQL.',
            '2020+ : moteur sous-jacent des bases de données de graphes modernes et des moteurs d’autorisation cloud (Open Policy Agent, Oso).',
            'Aujourd’hui : technologie de pointe pour l’analyse de vulnérabilités logicielles et l’audit de code automatisé.'
        ],
        'utilite': [
            'Langage de requête logique déclaratif et totalement décidable (terminaison toujours garantie sur données finies).',
            'Prend en charge nativement les requêtes récursives complexes (fermetures transitives, graphes de dépendances).',
            'Moteur de requêtage de sécurité officiel de GitHub CodeQL pour détecter automatiquement des failles de sécurité dans le code source.',
            'Utilisé pour les bases de données immuables orientées faits (Datomic) et les moteurs de déduction de règles métier.',
            'Permet d’exprimer des règles d’inférence logique avec des performances d’exécution massivement parallélisables.'
        ],
        'url': 'https://codeql.github.com',
        'badge': ('Datalog', 'https://img.shields.io/badge/Datalog-181717?style=for-the-badge&logo=github&logoColor=white', 'Spécification Formelle & Modélisation')
    },
    'promela': {
        'name': 'Promela (SPIN)',
        'histoire': [
            '1980 : conçu par Gerard Holzmann aux laboratoires Bell pour modéliser les protocoles de communication concurrents.',
            '1989 : sortie du vérificateur de modèles SPIN (Simple Promela Interpreter).',
            '2001 : Gerard Holzmann et le projet SPIN reçoivent le prix ACM System Software Award pour l’impact de l’outil.',
            'Années 2000–2020 : utilisé pour vérifier formellement le logiciel de commande des missions spatiales de la NASA (rovers martiens).',
            'Aujourd’hui : référence académique et industrielle pour la vérification formelle des systèmes asynchrones distribués.'
        ],
        'utilite': [
            'Langage de modélisation de processus communicants (Process Meta Language) asynchrones via canaux de messages.',
            'Permet de spécifier des propriétés de sûreté et de vivacité exprimées en logique temporelle linéaire (LTL).',
            'Utilise le vérificateur de modèles SPIN pour vérifier automatiquement des millions d’états en quelques secondes.',
            'Détecte infailliblement les conditions de course, les interblocages et les états inaccessibles dans les protocoles réseau.',
            'Utilisé dans le contrôle de réacteurs nucléaires, les systèmes de freinage ferroviaires et les télécommunications.'
        ],
        'url': 'https://spinroot.com',
        'badge': ('Promela', 'https://img.shields.io/badge/Promela_SPIN-0B3D91?style=for-the-badge&logo=nasa&logoColor=white', 'Spécification Formelle & Modélisation')
    },

    # Functional / Modern Dialects
    'standard-ml': {
        'name': 'Standard ML (SML)',
        'histoire': [
            '1983–1984 : conçu par Robin Milner et son équipe à l’Université d’Édimbourg comme langage de métaprogrammation pour le prouveur LCF.',
            '1990 : publication de la définition formelle rigoureuse "The Definition of Standard ML".',
            '1997 : publication de la révision formelle SML ’97 établissant la norme de référence.',
            'Années 1990–2000 : ancêtre direct d’OCaml, F#, Elm et source d’inspiration fondamentale du système de types de Rust.',
            'Aujourd’hui : modèle théorique d’élégance pour la théorie des types et l’écriture de compilateurs vérifiés (MLton, CakeML).'
        ],
        'utilite': [
            'Langage fonctionnel statiquement typé doté d’une inférence de types complète (Hindley-Milner) et d’un typage algébrique rigoureux.',
            'Possède l’un des systèmes de modules paramétriques (structures, signatures, foncteurs) les plus puissants de l’informatique.',
            'Dispose de compilateurs à optimisation globale produisant du code natif ultra-rapide (compilateur MLton sans runtime lourd).',
            'CakeML fournit une chaîne de compilation complète mathématiquement prouvée conforme depuis le code source jusqu’au binaire machine.',
            'Langage de choix pour l’enseignement de la sémantique des langages de programmation et la recherche formelle.'
        ],
        'url': 'https://smlfamily.github.io',
        'badge': ('Standard ML', 'https://img.shields.io/badge/Standard_ML-4B32C3?style=for-the-badge&logo=edx&logoColor=white', 'Familles Fonctionnelles & ML')
    },
    'janet': {
        'name': 'Janet',
        'histoire': [
            '2017–2019 : créé par Calvin Rose comme un langage moderne inspiré de Lisp, dynamique et facilement intégrable en C.',
            '2020 : enrichissement de la bibliothèque standard et du gestionnaire de paquets jpm.',
            '2022 : adoption dans le développement d’outils CLI rapides, de jeux vidéo 2D et de serveurs web légers.',
            '2024+ : stabilisation des fonctionnalités d’asynchronisme basées sur les fibres (fibers).',
            'Aujourd’hui : alternative moderne à Lua pour ceux qui préfèrent l’expressivité des macros Lisp et des structures de données riches.'
        ],
        'utilite': [
            'Dialecte Lisp impératif et fonctionnel compact conçu pour être embarqué simplement dans des applications C.',
            'Fournit des structures de données mutables et immuables riches (tableaux, tables associatives, tuples, structs).',
            'Intègre un moteur de grammaires à motifs d’analyse syntaxique natif (PEG - Parsing Expression Grammars).',
            'Gère la concurrence coopérative légère grâce à des fibres (fibers) de première classe avec coroutines.',
            'Permet la compilation de programmes complets en exécutables natifs autonomes sans dépendances externes.'
        ],
        'url': 'https://janet-lang.org',
        'badge': ('Janet', 'https://img.shields.io/badge/Janet-AA2233?style=for-the-badge&logo=lisp&logoColor=white', 'Familles Fonctionnelles & ML')
    },
    'fennel': {
        'name': 'Fennel',
        'histoire': [
            '2016 : créé par Andrey Listopadov et Phil Hagelberg (Technomancy) pour apporter la puissance de Lisp à l’écosystème Lua.',
            '2018 : adoption par les communautés de jeux vidéo (moteur LÖVE 2D) et de personnalisation d’éditeurs de code.',
            '2021 : publication de la version stable Fennel 1.0 garantissant la stabilité rétrocompatible.',
            '2023+ : utilisation croissante pour configurer Neovim et les gestionnaires de fenêtres sous Linux.',
            'Aujourd’hui : pont parfait combinant l’expressivité de Lisp et l’extrême légèreté du runtime Lua.'
        ],
        'utilite': [
            'Langage Lisp se compilant directement vers du code Lua propre sans aucun surcoût d’exécution à la vitesse de Lua/LuaJIT.',
            'Garantit une interopérabilité bidirectionnelle totale à 100 % avec toutes les bibliothèques et modules Lua existants.',
            'Fournit un système complet de macros hygiéniques exécutées lors de la phase de compilation.',
            'Utilisé pour créer des jeux vidéo indépendants (LÖVE), des scripts système et des plugins pour Neovim.',
            'Permet le rechargement de code à chaud et le débogage interactif direct via un REPL connecté.'
        ],
        'url': 'https://fennel-lang.org',
        'badge': ('Fennel', 'https://img.shields.io/badge/Fennel-2C2D72?style=for-the-badge&logo=lua&logoColor=white', 'Familles Fonctionnelles & ML')
    },
    'hy': {
        'name': 'Hy',
        'histoire': [
            '2012 : initié par Paul Tagliamonte lors de la conférence PyCon pour transformer Python en un dialecte Lisp complet.',
            '2015–2020 : refonte continue pour convertir le code Hy directement en arbre syntaxique abstrait (AST) Python natif.',
            '2022 : publication de Hy 1.0a, apportant une compatibilité étroite avec les versions modernes de Python 3.10+.',
            '2024+ : adoption par les développeurs Python souhaitant tirer parti des macros pour la métaprogrammation.',
            'Aujourd’hui : symbiose unique permettant d’utiliser toute la richesse de Lisp avec l’intégralité de l’écosystème Python.'
        ],
        'utilite': [
            'Dialecte Lisp qui se traduit directement en AST Python, s’exécutant de manière transparente sur l’interpréteur CPython standard.',
            'Permet d’importer et d’utiliser n’importe quelle bibliothèque Python (NumPy, PyTorch, Django, FastAPI) avec une syntaxe Lisp.',
            'Offre un système de macros complet pour étendre et transformer le langage à la compilation.',
            'Permet d’écrire du code de science des données et de machine learning avec l’expressivité d’un Lisp moderne.',
            'Offre un REPL interactif avec auto-complétion et introspection immédiate des objets Python.'
        ],
        'url': 'https://hylang.org',
        'badge': ('Hy', 'https://img.shields.io/badge/Hy-3776AB?style=for-the-badge&logo=python&logoColor=white', 'Familles Fonctionnelles & ML')
    },
    'unison': {
        'name': 'Unison',
        'histoire': [
            '2015–2019 : conçu par Paul Chiusano et Rúnar Bjarnason pour repenser les fondements de la programmation distribuée moderne.',
            '2021 : introduction du concept de code adressé par le contenu (Content-Addressed Code) où chaque fonction est identifiée par son hachage cryptographique.',
            '2023 : lancement d’Unison Cloud, permettant de déployer et d’orchestrer des calculs distribués comme de simples appels de fonctions.',
            '2024+ : enrichissement du système de gestion d’effets algébriques (Abilities).',
            'Aujourd’hui : langage pionnier réinventant la gestion des dépendances et le déploiement cloud sans builds ni conteneurs.'
        ],
        'utilite': [
            'Langage purement fonctionnel typé où le code n’est pas stocké sous forme de fichiers texte mais dans une base de données de nœuds hachés (SHA-256).',
            'Élimine définitivement les conflits de dépendances ("dependency hell") et rend les builds instantanés sans recompilation.',
            'Permet le déploiement distribué de fonctions sur des clusters distants de manière transparente via le système de types.',
            'Intègre un système puissant de gestion d’effets algébriques (Abilities) pour isoler les entrées/sorties et l’état.',
            'Idéal pour les microservices hautement distribués, le calcul cloud sans serveur et les pipelines de données.'
        ],
        'url': 'https://www.unison-lang.org',
        'badge': ('Unison', 'https://img.shields.io/badge/Unison-5C4EE5?style=for-the-badge&logo=unison&logoColor=white', 'Familles Fonctionnelles & ML')
    },
    'flix': {
        'name': 'Flix',
        'histoire': [
            '2015 : initié par Magnus Madsen à l’Université d’Aarhus et à l’Université de Waterloo pour marier programmation fonctionnelle et logique.',
            '2020 : intégration d’un système de polymorphisme d’effets algébriques unique au monde.',
            '2023 : développement d’un compilateur vers bytecode JVM autonome sans dépendance externe.',
            '2024+ : enrichissement de la bibliothèque standard et outillage IDE complet pour Visual Studio Code.',
            'Aujourd’hui : langage de recherche de pointe combinant le meilleur de Scala, Haskell et Datalog.'
        ],
        'utilite': [
            'Langage fonctionnel, impératif et logique typé statiquement s’exécutant sur la machine virtuelle Java (JVM).',
            'Intègre nativement Datalog au sein du langage sous forme de contraintes logiques de première classe.',
            'Propose un système de types avec inférence de pureté et vérification des effets algébriques à la compilation.',
            'Produit du bytecode JVM hautement optimisé rivalisant en vitesse avec Java et Scala.',
            'Idéal pour l’analyse statique de programmes, la vérification de règles de sécurité et les systèmes d’aide à la décision.'
        ],
        'url': 'https://flix.dev',
        'badge': ('Flix', 'https://img.shields.io/badge/Flix-E53935?style=for-the-badge&logo=java&logoColor=white', 'Familles Fonctionnelles & ML')
    },
    'chapel': {
        'name': 'Chapel',
        'histoire': [
            '2003–2009 : développé par Cray Inc. (aujourd’hui Hewlett Packard Enterprise) dans le cadre du projet HPCS de la DARPA.',
            '2015 : ouverture en open source et adoption sur les supercalculateurs du Top 500 mondial.',
            '2024 : publication de la version stable Chapel 2.0 garantissant la stabilité du langage et de l’API.',
            '2024+ : intégration native du calcul accéléré sur GPU multi-vendeurs (NVIDIA et AMD).',
            'Aujourd’hui : langage parallèle productif leader pour le calcul haute performance (HPC) à l’échelle exaflopique.'
        ],
        'utilite': [
            'Langage compilé conçu pour le calcul scientifique parallèle massif sur architectures distribuées à mémoire partagée ou répartie (PGAS).',
            'Sépare la description des algorithmes parallèles de la distribution géographique des données sur le cluster (domaines et distributions).',
            'Offre une syntaxe moderne et expressive inspirée de Python avec les performances du code C/Fortran avec MPI.',
            'Permet d’écrire des programmes s’exécutant à la fois sur un ordinateur portable et sur des supercalculateurs de 100 000 cœurs.',
            'Utilisé pour la simulation climatique, l’astrophysique numérique et le traitement de données à très grande échelle.'
        ],
        'url': 'https://chapel-lang.org',
        'badge': ('Chapel', 'https://img.shields.io/badge/Chapel-009999?style=for-the-badge&logo=hpe&logoColor=white', 'Familles Fonctionnelles & ML')
    },
    'pony': {
        'name': 'Pony',
        'histoire': [
            '2014–2015 : créé par Sylvan Clebsch pour résoudre les problèmes de concurrence sans surcoût de verrous (locks).',
            '2017 : formalisation mathématique de son système de capacités de références (Reference Capabilities).',
            '2020+ : adoption dans le secteur de la finance haute fréquence pour des systèmes nécessitant zéro blocage et faible latence.',
            '2023+ : optimisations du compilateur LLVM et de son ramasse-miettes distribué sans pause globale (ORCA).',
            'Aujourd’hui : référence théorique et pratique pour la concurrence ultra-rapide sans interblocages par conception.'
        ],
        'utilite': [
            'Langage système compilé basé sur le modèle d’acteurs avec typage statique strict et mémoire sûre sans verrous.',
            'Garantit mathématiquement l’absence totale de courses de données (data races) grâce aux capacités de références (iso, val, ref).',
            'Ramasse-miettes par acteur sans aucune pause globale d’application (pas de stop-the-world GC).',
            'Produit des binaires natifs ultra-performants via le compilateur LLVM.',
            'Idéal pour les passerelles financières de trading haute fréquence, les serveurs de jeux vidéo multijoueurs et l’IoT.'
        ],
        'url': 'https://www.ponylang.io',
        'badge': ('Pony', 'https://img.shields.io/badge/Pony-1B1F23?style=for-the-badge&logo=pony&logoColor=white', 'Familles Fonctionnelles & ML')
    },

    # Scientific & Financial Array
    'j': {
        'name': 'J',
        'histoire': [
            '1990 : créé par Kenneth E. Iverson (le créateur d’APL) et Roger Hui pour offrir les bénéfices d’APL avec des caractères ASCII standards.',
            'Années 1990–2000 : adoption dans l’analyse financière, l’actuariat et les laboratoires de recherche mathématique.',
            '2011 : passage officiel en logiciel libre open source sous licence GPLv3.',
            '2020+ : versions modernes J9.4+ apportant des optimisations vectorielles SIMD (AVX-512) et le support GPU.',
            'Aujourd’hui : langage matriciel d’une puissance d’abstraction mathématique inégalée dans l’écosystème ASCII.'
        ],
        'utilite': [
            'Langage de programmation matriciel (array programming) et fonctionnel tacite (point-free) utilisant le jeu de caractères ASCII standard.',
            'Permet d’écrire des calculs matriciels et tenseurs multidimensionnels complexes sans jamais déclarer de boucles explicites.',
            'Prend en charge la programmation fonctionnelle tacite où les fonctions sont composées par des verbes, adverbes et conjonctions.',
            'Utilisé pour les modèles de tarification financière, la cryptographie, les statistiques et le traitement du signal.',
            'Exécute les opérations vectorielles à des vitesses proches du silicium pur grâce à des primitives matérielles optimisées.'
        ],
        'url': 'https://www.jsoftware.com',
        'badge': ('J', 'https://img.shields.io/badge/J-004B87?style=for-the-badge&logo=j&logoColor=white', 'Scientifiques, Mathématiques & Finance')
    },
    'k': {
        'name': 'K (Kx Systems)',
        'histoire': [
            '1993 : créé par Arthur Whitney comme successeur ultra-compact et optimisé d’APL et J.',
            '1998 : intégration de K comme moteur d’exécution de la célèbre base de données chronologique kdb+.',
            'Années 2000–2020 : standard mondial incontesté des systèmes d’analyse de données de marché en temps réel à Wall Street.',
            '2020+ : développement de variantes ouvertes modernes comme Shakti par Arthur Whitney.',
            'Aujourd’hui : technologie sous-jacente des plus grandes banques d’investissement et fonds spéculatifs mondiaux.'
        ],
        'utilite': [
            'Langage matriciel et relationnel ultra-dense conçu pour traiter des milliards d’événements financiers par seconde.',
            'Fusionne intimement le langage de programmation matriciel avec un moteur de base de données orienté colonnes (kdb+).',
            'Permet d’analyser des flux de cotations boursières (tick data) en mémoire avec une latence quasi-nulle.',
            'Utilisé pour le trading algorithmique haute fréquence, la surveillance de risques de marché et la détection d’anomalies financières.',
            'Empreinte mémoire et taille de binaire minuscules garantissant une efficacité maximale du cache processeur.'
        ],
        'url': 'https://kx.com',
        'badge': ('K', 'https://img.shields.io/badge/K_Kx-003366?style=for-the-badge&logo=kx&logoColor=white', 'Scientifiques, Mathématiques & Finance')
    },
    'q': {
        'name': 'Q (kdb+)',
        'histoire': [
            '2003 : conçu par Arthur Whitney chez Kx Systems comme surcouche lisible au langage K pour faciliter l’écriture de requêtes sur kdb+.',
            'Années 2000–2010 : adoption généralisée par les banques d’investissement (Goldman Sachs, Morgan Stanley, JP Morgan).',
            '2018 : intégration avec Python (PyQ) et les outils modernes de science des données.',
            '2023 : lancement de kdb+ sur les places de marché cloud AWS et Azure.',
            'Aujourd’hui : standard de l’industrie financière pour l’interrogation et l’analyse de données de séries temporelles massives.'
        ],
        'utilite': [
            'Langage expressif de requêtage et de calcul vectoriel pour les séries temporelles et données de flux continus.',
            'Intègre le langage qSQL permettant des requêtes temporelles avancées (asof joins, window joins) impossibles en SQL classique.',
            'Traite des pétaoctets de données financières chronologiques avec des performances de lecture instantanées.',
            'Langage de référence pour les quant traders, analystes de risques et ingénieurs de données de marché.',
            'Gère nativement les tables en mémoire vive et les partitions historiques sur disque de manière unifiée.'
        ],
        'url': 'https://code.kx.com/q/',
        'badge': ('Q', 'https://img.shields.io/badge/Q_kdb+-00558F?style=for-the-badge&logo=kx&logoColor=white', 'Scientifiques, Mathématiques & Finance')
    },
    'bqn': {
        'name': 'BQN',
        'histoire': [
            '2020–2021 : créé par Marshall Lochbaum pour concevoir un langage matriciel moderne corrigeant les incohérences historiques d’APL.',
            '2022 : adoption d’une syntaxe épurée et d’un modèle de première classe pour toutes les entités (fonctions, modificateurs).',
            '2023 : implémentations natives ultra-rapides (CBQN) utilisant les instructions vectorielles matérielles AVX-512.',
            '2024+ : engouement au sein des chercheurs en programmation matricielle et en optimisation de calcul.',
            'Aujourd’hui : le plus moderne et rigoureux des langages de programmation matricielle contemporains.'
        ],
        'utilite': [
            'Langage de programmation matriciel complet fondé sur des glyphes dédiés et une grammaire régulière sans cas particuliers.',
            'Traite les fonctions et les modificateurs comme des citoyens de première classe manipulables dans des tableaux.',
            'Permet d’exprimer des transformations de données multidimensionnelles complexes avec une concision et une clarté remarquables.',
            'Compilateur CBQN compilant vers du code vectoriel tirant pleinement parti des registres SIMD modernes.',
            'Utilisé pour le traitement d’images, le calcul scientifique, l’analyse de données et la recherche algorithmique.'
        ],
        'url': 'https://mlochbaum.github.io/BQN/',
        'badge': ('BQN', 'https://img.shields.io/badge/BQN-2E3440?style=for-the-badge&logo=matrix&logoColor=white', 'Scientifiques, Mathématiques & Finance')
    },
    'scilab': {
        'name': 'Scilab',
        'histoire': [
            '1984–1990 : initié à l’INRIA et à l’École Nationale des Ponts et Chaussées sous le nom initial de Blaise, puis PsiLab.',
            '1994 : diffusion officielle sous le nom Scilab comme alternative open source et libre à MATLAB.',
            '2003 : création du Consortium Scilab pour coordonner le développement industriel.',
            '2017 : intégration de l’environnement Xcos pour la simulation de systèmes dynamiques par schémas-blocs.',
            'Aujourd’hui : logiciel libre de référence utilisé mondialement dans l’enseignement supérieur et l’ingénierie publique.'
        ],
        'utilite': [
            'Logiciel et langage de calcul numérique dédié aux applications scientifiques et à l’ingénierie industrielle.',
            'Fournit des centaines de fonctions mathématiques pour l’algèbre linéaire, l’optimisation, les statistiques et le traitement du signal.',
            'Intègre l’outil visuel Xcos pour modéliser et simuler graphiquement des systèmes hybrides et asservissements continus/discrets.',
            'Utilisé dans le secteur aérospatial (CNES, ESA), l’automobile et la recherche académique en automatique.',
            'Permet l’interfaçage aisé avec des bibliothèques externes écrites en C, C++, Fortran et Java.'
        ],
        'url': 'https://www.scilab.org',
        'badge': ('Scilab', 'https://img.shields.io/badge/Scilab-005696?style=for-the-badge&logo=scilab&logoColor=white', 'Scientifiques, Mathématiques & Finance')
    },
    'octave': {
        'name': 'GNU Octave',
        'histoire': [
            '1988–1992 : initié par John W. Eaton à l’Université du Texas à Austin comme outil compagnon pour un cours de génie chimique.',
            '1997 : publication de la première édition du manuel de référence GNU Octave.',
            'Années 2000–2015 : perfectionnement de la compatibilité syntaxique presque totale avec MATLAB.',
            '2019–2024 : versions 5 à 9 apportant une interface graphique (GUI) moderne et une exécution accélérée des scripts.',
            'Aujourd’hui : principale alternative libre et gratuite à MATLAB au sein du projet GNU.'
        ],
        'utilite': [
            'Langage de haut niveau destiné au calcul numérique linéaire et non linéaire et aux expériences scientifiques numériques.',
            'Offre une compatibilité syntaxique directe quasi-parfaite permettant d’exécuter la grande majorité des scripts MATLAB sans modification.',
            'Dispose d’outils graphiques intégrés pour la visualisation de données 2D et 3D (via gnuplot et OpenGL).',
            'Permet l’automatisation de calculs scientifiques sous Linux sans frais de licences propriétaires.',
            'Extensible par des modules et paquets spécialisés via l’écosystème Octave Forge.'
        ],
        'url': 'https://octave.org',
        'badge': ('GNU Octave', 'https://img.shields.io/badge/GNU_Octave-0790BA?style=for-the-badge&logo=gnubash&logoColor=white', 'Scientifiques, Mathématiques & Finance')
    },
    'labview': {
        'name': 'LabVIEW (G)',
        'histoire': [
            '1986 : créé par Jeff Kodosky chez National Instruments (NI) pour automatiser les bancs de mesure sur Macintosh.',
            '1992 : portage sous Windows et Sun Solaris, standardisant la programmation graphique d’instrumentation.',
            'Années 2000 : intégration de cibles FPGA programmables directement en langage graphique G sans coder en VHDL.',
            '2020+ : intégration étroite avec Python, les protocoles industriels IoT et les systèmes de test automobile autonomes.',
            'Aujourd’hui : standard mondial incontesté de l’acquisition de données, du contrôle d’instruments et des bancs de test industriels.'
        ],
        'utilite': [
            'Langage de programmation graphique par flux de données (Dataflow) où les programmes sont construits par câblage de nœuds (diagrammes).',
            'Crée simultanément la logique de traitement et l’interface utilisateur physique virtuelle (Face Avant avec boutons, jauges, oscilloscopes).',
            'Pilote directement des milliers d’instruments de mesure physiques (oscilloscopes, capteurs, cartes d’acquisition DAQ, bus GPIB/CAN).',
            'Permet de compiler du code graphique directement vers des puces matérielles FPGA pour des temps de réponse à la microseconde.',
            'Utilisé sur les bancs de tests des lanceurs spatiaux (SpaceX, Ariane), les chaînes de fabrication automobile et les accélérateurs de particules (CERN).'
        ],
        'url': 'https://www.ni.com/labview',
        'badge': ('LabVIEW', 'https://img.shields.io/badge/LabVIEW-FFD100?style=for-the-badge&logo=nationalinstruments&logoColor=black', 'Scientifiques, Mathématiques & Finance')
    },

    # Specialized Web3
    'cadence': {
        'name': 'Cadence (Flow)',
        'histoire': [
            '2019–2020 : développé par Dapper Labs (créateurs de CryptoKitties et NBA Top Shot) pour la blockchain Flow.',
            '2021 : pionnier de la programmation orientée ressources (Resource-Oriented Programming) sur smart contracts.',
            '2024 : mise à niveau majeure Cadence 1.0 sécurisant définitivement la sémantique du langage.',
            '2024+ : adoption par des marques mondiales pour l’émission d’actifs numériques et d’expériences de jeu grand public.',
            'Aujourd’hui : langage de référence pour les smart contracts sécurisés d’applications grand public et de jeux décentralisés.'
        ],
        'utilite': [
            'Langage de smart contracts fortement typé fondé sur la programmation orientée ressources et les types linéaires.',
            'Traite les NFT et tokens comme des objets de ressource uniques stockés directement dans le compte de l’utilisateur.',
            'Empêche par conception la duplication ou la destruction accidentelle d’actifs de valeur.',
            'Utilisé pour des applications blockchain à fort volume d’utilisateurs (NBA Top Shot, Disney Pinnacle).',
            'Fournit une vérification formelle des pré et post-conditions sur chaque fonction de contrat.'
        ],
        'url': 'https://cadence-lang.org',
        'badge': ('Cadence', 'https://img.shields.io/badge/Cadence-00EF8B?style=for-the-badge&logo=flow&logoColor=black', 'Smart Contracts & Web3 Spécialisés')
    },
    'plutus': {
        'name': 'Plutus (Cardano)',
        'histoire': [
            '2018–2021 : conçu par IOHK (Input Output Global) sous la direction de Philip Wadler pour la blockchain Cardano.',
            '2021 : déploiement sur le réseau principal Cardano lors de la mise à niveau Alonzo, activant les smart contracts.',
            '2022 : lancement de Plutus Core v2 (mise à niveau Vasil) réduisant la taille des scripts et le coût en ressources.',
            '2024+ : essor d’outils dérivés modernes comme Aiken pour simplifier l’écriture de validateurs Plutus.',
            'Aujourd’hui : socle formellement vérifié de la finance décentralisée et des applications décentralisées sur Cardano.'
        ],
        'utilite': [
            'Langage de smart contracts basé sur Haskell s’appuyant sur le modèle EUTXO (Extended Unspent Transaction Output).',
            'Permet d’écrire la logique on-chain (compilée vers Plutus Core) et off-chain dans un langage fonctionnel unifié.',
            'Garantit le déterminisme absolu : le coût en frais et l’effet exact d’une transaction sont connus avec certitude avant soumission.',
            'Bénéficie de la rigueur mathématique et de l’absence d’effets de bord incontrôlés propres à Haskell.',
            'Utilisé pour sécuriser des protocoles DeFi, des systèmes de vote de gouvernance et des échanges décentralisés.'
        ],
        'url': 'https://plutus.readthedocs.io',
        'badge': ('Plutus', 'https://img.shields.io/badge/Plutus-0033AD?style=for-the-badge&logo=cardano&logoColor=white', 'Smart Contracts & Web3 Spécialisés')
    },
    'michelson': {
        'name': 'Michelson (Tezos)',
        'histoire': [
            '2014–2018 : conçu par Arthur Breitman et l’équipe Tezos comme langage de bas niveau formellement vérifiable pour la blockchain Tezos.',
            '2018 : lancement du mainnet Tezos avec Michelson comme langage de smart contracts natif de la machine virtuelle.',
            'Années 2020 : enrichissement régulier via les amendements on-chain démocratiques de Tezos (Babylon, Edo, Nairobi).',
            '2023+ : support de langages de haut niveau compilant vers Michelson (SmartPy, Ligo, Archetype).',
            'Aujourd’hui : langage de smart contracts de référence pour la vérification formelle de code financier et institutionnel.'
        ],
        'utilite': [
            'Langage de contrats intelligents basé sur une pile (stack-based), fortement typé et sans effets de bord non contrôlés.',
            'Conçu pour permettre la preuve mathématique formelle de l’absence de bugs critiques via des assistants de preuve (Coq).',
            'Exécuté directement par le nœud Tezos sans étape de compilation vers un bytecode opaque.',
            'Utilisé pour les actifs numériques artistiques (objkt.com), la tokenisation d’actifs institutionnels et la gouvernance décentralisée.',
            'Garantit la sûreté de typage statique de l’état et des messages échangés entre contrats.'
        ],
        'url': 'https://tezos.gitlab.io/active/michelson.html',
        'badge': ('Michelson', 'https://img.shields.io/badge/Michelson-2C7DF7?style=for-the-badge&logo=tezos&logoColor=white', 'Smart Contracts & Web3 Spécialisés')
    },
    'scilla': {
        'name': 'Scilla (Zilliqa)',
        'histoire': [
            '2018 : conçu par des chercheurs de l’Université nationale de Singapour (NUS) et l’équipe Zilliqa.',
            '2019 : lancement sur le mainnet Zilliqa, devenant le premier langage de contrats intelligents sur blockchain partitionnée (sharding).',
            '2021 : intégration d’un framework de vérification formelle basé sur l’assistant de preuve Coq.',
            '2023+ : optimisations de la machine virtuelle Scilla pour le traitement de micro-paiements à très haut débit.',
            'Aujourd’hui : pionnier de la sécurité des smart contracts par séparation stricte entre calcul et communication.'
        ],
        'utilite': [
            'Langage de smart contracts basé sur le modèle des automates finis communicants (Communicating Automata).',
            'Interdit délibérément la complétude de Turing non maîtrisée pour rendre le code entièrement vérifiable et traçable.',
            'Élimine structurellement les attaques de réentrance qui ont historiquement coûté des centaines de millions de dollars sur d’autres réseaux.',
            'Sépare strictement les transitions d’état pur des opérations d’envoi de messages.',
            'Utilisé pour la finance décentralisée, les passerelles de paiement rapide et la gestion d’actifs numériques sur Zilliqa.'
        ],
        'url': 'https://scilla-lang.org',
        'badge': ('Scilla', 'https://img.shields.io/badge/Scilla-29CCC4?style=for-the-badge&logo=zilliqa&logoColor=black', 'Smart Contracts & Web3 Spécialisés')
    },

    # Desktop Automation & Scripting
    'applescript': {
        'name': 'AppleScript',
        'histoire': [
            '1993 : créé par Apple et introduit dans System 7.1.1 pour automatiser les applications sous l’environnement Mac OS.',
            '2001 : transition vers Mac OS X avec intégration étroite de Cocoa et des architectures de script UNIX.',
            '2014 : Apple ajoute JavaScript for Automation (JXA) comme alternative syntaxique partageant le même pont d’automatisation.',
            '2021+ : cohabitation avec l’application Raccourcis (Shortcuts) sur macOS Monterey et ultérieurs.',
            'Aujourd’hui : moteur d’automatisation de bureau historique et puissant pilotant les flux de travail professionnels sur Mac.'
        ],
        'utilite': [
            'Langage de script basé sur une syntaxe en langage pseudo-naturel anglais (Natural Language Syntax) pour piloter le système d’exploitation macOS.',
            'Envoie des événements Apple Events aux applications pour automatiser des tâches complexes entre logiciels distincts.',
            'Standard d’automatisation pour les suites créatives (Adobe InDesign, Photoshop, Illustrator) et la publication assistée par ordinateur.',
            'Permet de manipuler directement le Finder, les applications de productivité (Numbers, Pages, Mail) et les fenêtres système.',
            'Utilisé par les imprimeurs, photographes, éditeurs de presse et développeurs pour automatiser leurs chaînes de production.'
        ],
        'url': 'https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/',
        'badge': ('AppleScript', 'https://img.shields.io/badge/AppleScript-999999?style=for-the-badge&logo=apple&logoColor=white', 'Automatisation Desktop & Web Scripting')
    },
    'autohotkey': {
        'name': 'AutoHotkey',
        'histoire': [
            '2003 : créé par Chris Mallett comme fork d’AutoIt pour offrir une gestion avancée des raccourcis clavier sous Windows.',
            '2014 : développement communautaire majeur de la branche moderne AutoHotkey v2 par Steve Gray (Lexikos).',
            '2023 : publication officielle d’AutoHotkey v2.0, rationalisant la syntaxe avec un langage totalement structuré et orienté objet.',
            '2024+ : standard mondial incontesté de l’automatisation de l’interface utilisateur et des macros sous Windows.',
            'Aujourd’hui : outil d’une flexibilité incomparable pour transformer la productivité bureautique et le contrôle matériel.'
        ],
        'utilite': [
            'Langage de script et moteur d’automatisation léger sous Windows pour intercepter et remapper le clavier, la souris et les manettes.',
            'Permet la création de raccourcis clavier globaux (hotkeys), de remplacements de texte instantanés (hotstrings) et de fenêtres graphiques personnalisées.',
            'Pilote directement l’API Win32 pour manipuler les fenêtres, menus, contrôles et processus d’arrière-plan.',
            'Permet la compilation de scripts en exécutables autonomes .exe distribuables sans installation préalable.',
            'Utilisé pour l’ergonomie au travail, le gaming, l’assistance à l’accessibilité et la saisie automatisée de données.'
        ],
        'url': 'https://www.autohotkey.com',
        'badge': ('AutoHotkey', 'https://img.shields.io/badge/AutoHotkey-334455?style=for-the-badge&logo=autohotkey&logoColor=white', 'Automatisation Desktop & Web Scripting')
    },
    'vbscript': {
        'name': 'VBScript',
        'histoire': [
            '1996 : lancé par Microsoft avec Internet Explorer 3.0 comme alternative à JavaScript pour le web et l’administration système Windows.',
            '1998 : intégré au Windows Script Host (WSH) et au moteur de serveur web Active Server Pages (ASP classique).',
            'Années 2000 : outil standard des administrateurs système pour l’automatisation des parcs de PC d’entreprise Windows.',
            '2023 : Microsoft annonce la dépréciation programmée de VBScript au profit de PowerShell.',
            'Aujourd’hui : technologie patrimoniale encore présente dans des millions de scripts d’administration et macros d’anciennes applications.'
        ],
        'utilite': [
            'Langage de script allégé dérivé de Visual Basic s’exécutant nativement dans l’environnement Windows Script Host.',
            'Permet l’interaction avec les composants COM (Component Object Model) et les interfaces WMI (Windows Management Instrumentation).',
            'Moteur historique de la première génération de sites web dynamiques Microsoft (Classic ASP).',
            'Utilisé pour les scripts de connexion réseau (logon scripts), la gestion de parc Active Directory et le test logiciel (UFT/QTP).',
            'Fournit une syntaxe simple et tolérante pour exécuter des commandes système automatisées.'
        ],
        'url': 'https://learn.microsoft.com/previous-versions/windows/internet-explorer/ie-developer/scripting-articles/t0aew7h6(v=vs.84)',
        'badge': ('VBScript', 'https://img.shields.io/badge/VBScript-1976D2?style=for-the-badge&logo=windows&logoColor=white', 'Automatisation Desktop & Web Scripting')
    },
    'actionscript': {
        'name': 'ActionScript',
        'histoire': [
            '1998–2000 : créé par Gary Grossman chez Macromedia pour apporter de l’interactivité aux animations vectorielles Flash.',
            '2006 : sortie majeure d’ActionScript 3.0 (AS3) réécrit sur la machine virtuelle AVM2 avec typage statique et orienté objet conforme à ECMAScript 4.',
            'Années 2000–2010 : technologie dominante du web multimédia interactif, des vidéos en ligne (YouTube à ses débuts) et des jeux web.',
            '2020 : arrêt officiel d’Adobe Flash Player marquant la fin d’une ère pour le web riche interactif.',
            'Aujourd’hui : technologie historique majeure ayant formé toute une génération de développeurs de jeux et d’interfaces animées.'
        ],
        'utilite': [
            'Langage orienté objet dérivé d’ECMAScript conçu pour créer des animations interactives, jeux vidéo et applications Internet riches (RIA).',
            'Pilotait l’arbre d’affichage graphique vectoriel hiérarchique de Flash (DisplayObject, MovieClip).',
            'Permettait la diffusion de flux vidéo/audio en streaming (RTMP) et le chargement dynamique d’éléments multimédias.',
            'Moteur d’applications de bureau et mobiles multiplateformes via le runtime Adobe AIR.',
            'A posé les bases conceptuelles de l’animation d’interface moderne réutilisées aujourd’hui en HTML5 Canvas et WebGL.'
        ],
        'url': 'https://www.adobe.com/products/air.html',
        'badge': ('ActionScript', 'https://img.shields.io/badge/ActionScript-FF0000?style=for-the-badge&logo=adobe&logoColor=white', 'Automatisation Desktop & Web Scripting')
    },
    'coffeescript': {
        'name': 'CoffeeScript',
        'histoire': [
            '2009 : créé par Jeremy Ashkenas pour offrir une syntaxe élégante et concise inspirée de Ruby et Python se compilant en JavaScript.',
            '2011 : intégré par défaut dans Ruby on Rails 3.1, propulsant son adoption massive par des milliers de startups web.',
            'Années 2010 : influence déterminante et directe sur le comité TC39 pour la spécification du standard JavaScript moderne ES6 (ES2015).',
            '2017 : sortie de CoffeeScript 2 pour produire du code JavaScript ES6 natif.',
            'Aujourd’hui : jalon historique fondamental dont quasiment toutes les innovations (fonctions fléchées, classes, destructuring, interpolation) ont été intégrées dans JavaScript standard.'
        ],
        'utilite': [
            'Langage transpilé vers JavaScript éliminant les accolades et points-virgules au profit d’une indentation significative propre.',
            'A inventé la syntaxe des fonctions fléchées (-> et =>) préservant le contexte lexical du mot-clé this.',
            'A popularisé l’assignation par décomposition (destructuring), les paramètres par défaut et l’opérateur d’enchaînement optionnel (?.).',
            'Permettait d’écrire du code front-end et back-end Node.js avec une concision et une clarté divisant le volume de code par deux.',
            'A servi de tremplin intellectuel vers l’ère des transpilateurs web modernes (Babel, TypeScript).'
        ],
        'url': 'https://coffeescript.org',
        'badge': ('CoffeeScript', 'https://img.shields.io/badge/CoffeeScript-2F2625?style=for-the-badge&logo=coffeescript&logoColor=white', 'Automatisation Desktop & Web Scripting')
    },
    'hack': {
        'name': 'Hack (HHVM)',
        'histoire': [
            '2014 : développé par Meta (Facebook) sous la direction de Julien Verlaguet pour apporter un typage statique strict et des performances massives à PHP.',
            '2016 : conversion intégrale du code source monolithique de Facebook vers Hack.',
            '2019 : rupture définitive avec la compatibilité descendante PHP pour faire de Hack un langage totalement autonome et indépendant sur HHVM.',
            '2021+ : ajout de fonctionnalités d’avant-garde (génériques réifiés, types d’union stricts, modules hermétiques).',
            'Aujourd’hui : langage d’infrastructure principal motorisant les milliards de requêtes quotidiennes des plateformes de Meta.'
        ],
        'utilite': [
            'Langage de programmation pour le web combinant la rapidité de développement dynamique avec la rigueur d’un vérificateur de types statiques instantané.',
            'S’exécute exclusivement sur la machine virtuelle HipHop Virtual Machine (HHVM) avec compilation JIT native ultra-performante.',
            'Vérifie le typage de millions de lignes de code en quelques millisecondes grâce à un serveur d’analyse statique résident en mémoire.',
            'Intègre nativement les opérations asynchrones de première classe (async/await) et les collections immuables typées (Vec, Dict, Keysets).',
            'Conçu spécifiquement pour soutenir des bases de code web hyperscale maintenues par des milliers d’ingénieurs en simultané.'
        ],
        'url': 'https://hacklang.org',
        'badge': ('Hack', 'https://img.shields.io/badge/Hack-0081FB?style=for-the-badge&logo=meta&logoColor=white', 'Automatisation Desktop & Web Scripting')
    }
}

def run():
    target_dir = os.path.join(os.path.dirname(__file__), '..', 'languages')
    os.makedirs(target_dir, exist_ok=True)
    
    count = 0
    for slug, data in EXPANSION_DB.items():
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
    print(f'Expansion terminée : {count} nouvelles fiches générées dans {target_dir} !')

if __name__ == '__main__':
    run()
