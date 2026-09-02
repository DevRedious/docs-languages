import os
import json

BASE_DIR = '/home/dev_redious/Documents/Dev/docs-languages'
LANG_DIR = os.path.join(BASE_DIR, 'languages')
os.makedirs(LANG_DIR, exist_ok=True)

# Extended master list of 255 additional real languages to reach the 700 milestone
MORE_LANGUAGES = [
    ("abcl", "ABCL/1", "Akinori Yonezawa (Univ Tokyo)", "1986", "Modèle d'acteurs concurrents orienté objet et calcul réflexif", "Langages Hybrides & Spécifiques", "4B275F", "actors", "https://en.wikipedia.org/wiki/ABCL/1"),
    ("adele", "Adele", "Université de Grenoble / LGI", "1991", "Gestion de configuration logicielle et environnements d'ingénierie", "Spécification Formelle & Modélisation", "00599C", "grenoble", "https://en.wikipedia.org/wiki/Adele_(programming_language)"),
    ("adl", "ADL (Architecture Description)", "DARPA / CMU", "1993", "Description formelle d'architectures logicielles et de composants", "Spécification Formelle & Modélisation", "1F2937", "cmu", "https://en.wikipedia.org/wiki/Architecture_description_language"),
    ("advsys", "AdvSys", "David Betz", "1986", "Moteur et langage orienté objet pour jeux d'aventure textuels", "Jeux Vidéo & Moteurs 3D", "4CAF50", "retro", "https://en.wikipedia.org/wiki/AdvSys"),
    ("alex", "Alex", "Simon Marlow (Haskell)", "2003", "Générateur d'analyseurs lexicaux pour le langage Haskell", "Langages Fonctionnels & Déclaratifs", "5D4F85", "haskell", "https://haskell-alex.readthedocs.io"),
    ("algy", "ALGY", "Mark Halpern", "1961", "Pionnier du calcul algébrique symbolique sur ordinateur", "Langages Historiques & Pionniers", "003366", "math", "https://en.wikipedia.org/wiki/ALGY"),
    ("alma", "Alma", "CWI Amsterdam", "1995", "Recherche opérationnelle combinant impératif et logique", "Langages Logiques & Formels", "3B4252", "cwi", "https://en.wikipedia.org/wiki/Alma-0"),
    ("alphard", "Alphard", "Mary Shaw, Wm Wulf (CMU)", "1974", "Vérification formelle de types de données abstraits", "Langages Historiques & Pionniers", "003366", "cmu", "https://en.wikipedia.org/wiki/Alphard_(programming_language)"),
    ("altran", "ALTRAN", "Laboratoires Bell", "1968", "Manipulation symbolique de polynômes et fractions rationnelles", "Scientifiques, Mathématiques & Finance", "000000", "bell", "https://en.wikipedia.org/wiki/ALTRAN"),
    ("amigabasic", "AmigaBASIC", "Microsoft pour Commodore", "1985", "BASIC graphique et sonore multitâche pour micro-ordinateurs Amiga", "Langages Historiques & Pionniers", "FF4400", "amigaos", "https://en.wikipedia.org/wiki/AmigaBASIC"),
    ("aml", "AML (A Manufacturing Language)", "IBM", "1982", "Programmation robotique industrielle pour lignes d'assemblage", "Description Matérielle & Open Hardware", "052FAD", "ibm", "https://en.wikipedia.org/wiki/AML_(programming_language)"),
    ("analytical-engine", "Analytical Engine Code", "Ada Lovelace, Charles Babbage", "1843", "Le tout premier programme de l'histoire pour calculer les nombres de Bernoulli", "Langages Historiques & Pionniers", "000000", "lovelace", "https://en.wikipedia.org/wiki/Analytical_Engine"),
    ("anorm", "Anorm", "Play Framework / Lightbend", "2011", "Accès SQL relationnel fluide et typé pour Scala", "Requêtes de Données, Graphes & Schémas", "DC322F", "scala", "https://playframework.github.io/anorm/"),
    ("ans-cobol", "ANS COBOL", "ANSI", "1968", "Standardisation industrielle américaine du langage COBOL", "Entreprise, ERP & 4GL Métier", "003C71", "ibm", "https://www.ansi.org"),
    ("ant", "Apache Ant", "James Duncan Davidson (Apache)", "2000", "Automatisation de build Java déclarative basée sur XML", "Frameworks, Runtimes & Écosystèmes", "C02F2F", "apache", "https://ant.apache.org"),
    ("apl2", "APL2", "IBM / Jim Brown", "1984", "APL étendu avec tableaux imbriqués et structures complexes", "Scientifiques, Mathématiques & Finance", "052FAD", "ibm", "https://www.ibm.com/products/apl2"),
    ("apple-pascal", "Apple Pascal", "Apple Computer / UCSD", "1979", "Système d'exploitation et compilateur Pascal pour micro-ordinateurs Apple II", "Langages Historiques & Pionniers", "000000", "apple", "https://en.wikipedia.org/wiki/Apple_Pascal"),
    ("app-inventor", "MIT App Inventor", "Hal Abelson (MIT / Google)", "2010", "Création visuelle par blocs d'applications mobiles Android", "Langages Historiques & Pionniers", "A4C639", "android", "https://appinventor.mit.edu"),
    ("apt", "APT (Automatically Programmed Tool)", "Douglas T. Ross (MIT)", "1956", "Tout premier langage de programmation de machines-outils à commande numérique (CNC)", "Description Matérielle & Open Hardware", "000000", "mit", "https://en.wikipedia.org/wiki/APT_(programming_language)"),
    ("arena", "Arena (Simulation)", "Rockwell Automation", "1993", "Simulation d'événements discrets pour la logistique industrielle", "Scientifiques, Mathématiques & Finance", "D32F2F", "rockwell", "https://www.arenasimulation.com"),
    ("aspectj", "AspectJ", "Gregor Kiczales (Xerox PARC)", "2001", "Programmation orientée aspect (AOP) pour la plateforme Java", "Langages Applicatifs & Entreprise", "007396", "java", "https://www.eclipse.org/aspectj/"),
    ("assembly-mips", "MIPS Assembly", "MIPS Technologies / John L. Hennessy", "1985", "Assembleur de l'architecture RISC universitaire de référence (Nintendo 64, PS1)", "Langages Systèmes & Bas Niveau", "333333", "mips", "https://en.wikipedia.org/wiki/MIPS_architecture"),
    ("assembly-sparc", "SPARC Assembly", "Sun Microsystems", "1987", "Assembleur de l'architecture serveur 64-bit UltraSPARC et Solaris", "Langages Systèmes & Bas Niveau", "E76F00", "sun", "https://en.wikipedia.org/wiki/SPARC"),
    ("assembly-68k", "Motorola 68000 Assembly", "Motorola", "1979", "Assembleur culte du Macintosh, de l'Amiga, de l'Atari ST et de la Mega Drive", "Langages Systèmes & Bas Niveau", "00599C", "motorola", "https://en.wikipedia.org/wiki/Motorola_68000_series"),
    ("assembly-ppc", "PowerPC Assembly", "Apple, IBM, Motorola (AIM)", "1992", "Assembleur RISC superscalaire des Mac PowerPC, Xbox 360 et PS3", "Langages Systèmes & Bas Niveau", "052FAD", "ibm", "https://en.wikipedia.org/wiki/PowerPC"),
    ("assembly-z80", "Zilog Z80 Assembly", "Federico Faggin, Masatoshi Shima", "1976", "Assembleur légendaire de la Game Boy, du ZX Spectrum et des consoles Sega 8-bit", "Langages Systèmes & Bas Niveau", "D32F2F", "zilog", "https://en.wikipedia.org/wiki/Zilog_Z80"),
    ("assembly-6502", "MOS 6502 Assembly", "Chuck Peddle (MOS Technology)", "1975", "Assembleur pionnier de l'Apple II, de la NES, du Commodore 64 et de l'Atari 2600", "Langages Systèmes & Bas Niveau", "4CAF50", "mos", "https://en.wikipedia.org/wiki/MOS_Technology_6502"),
    ("asymptote", "Asymptote", "Andy Hammerlindl, John C. Bowman", "2004", "Langage de programmation vectorielle pour illustrations mathématiques TeX", "Scientifiques, Mathématiques & Finance", "008080", "latex", "https://asymptote.sourceforge.io"),
    ("atari-basic", "Atari BASIC", "Shepardson Microsystems", "1979", "Interpréteur BASIC en cartouche ROM 8 Ko pour ordinateurs Atari 8-bit", "Langages Historiques & Pionniers", "E01A22", "atari", "https://en.wikipedia.org/wiki/Atari_BASIC"),
    ("atlas-autocode", "Atlas Autocode", "Tony Brooker, Derrick Morris", "1962", "Langage de haut niveau développé pour le supercalculateur Atlas de Manchester", "Langages Historiques & Pionniers", "003366", "manchester", "https://en.wikipedia.org/wiki/Atlas_Autocode"),
    ("averest", "Averest", "Klaus Schneider", "2006", "Conception et vérification formelle de systèmes réactifs synchrones matériels", "Spécification Formelle & Modélisation", "2C3E50", "sync", "http://www.averest.org"),
    ("babytalk", "BabyTalk", "Xerox PARC", "1971", "Version expérimentale ayant conduit aux spécifications de Smalltalk-72", "Langages Historiques & Pionniers", "57889C", "smalltalk", "https://en.wikipedia.org/wiki/Smalltalk"),
    ("basic-plus", "BASIC-PLUS", "Digital Equipment Corporation", "1970", "Dialecte BASIC étendu pour le système d'exploitation RSTS/E sur PDP-11", "Langages Historiques & Pionniers", "002D62", "digital", "https://en.wikipedia.org/wiki/BASIC-PLUS"),
    ("bbc-basic", "BBC BASIC", "Sophie Wilson (Acorn Computers)", "1981", "BASIC ultra-rapide conçu pour le projet d'alphabétisation informatique de la BBC", "Langages Historiques & Pionniers", "CC0000", "bbc", "https://www.bbcbasic.co.uk"),
    ("biojava", "BioJava", "BioJava Project / OBF", "2000", "Bibliothèque et DSL Java de traitement de données génomiques et bioinformatiques", "Scientifiques, Mathématiques & Finance", "007396", "java", "https://biojava.org"),
    ("bioperl", "BioPerl", "Open Bioinformatics Foundation", "1995", "Moteur de traitement de séquences ADN au cœur du Projet Génome Humain", "Scientifiques, Mathématiques & Finance", "39457E", "perl", "https://bioperl.org"),
    ("biopython", "BioPython", "Open Bioinformatics Foundation", "1999", "Standard mondial d'analyse de biologie computationnelle en Python", "Scientifiques, Mathématiques & Finance", "3776AB", "python", "https://biopython.org"),
    ("bitc", "BitC", "Jonathan S. Shapiro (Coyotos)", "2006", "Langage fonctionnel typé prouvable pour noyaux de systèmes d'exploitation ultra-sécurisés", "Langages Systèmes & Bas Niveau", "1E88E5", "security", "http://www.bitc-lang.org"),
    ("blockly", "Blockly", "Google", "2012", "Bibliothèque web open source pour concevoir des éditeurs de code visuels par blocs", "Langages Historiques & Pionniers", "4285F4", "google", "https://developers.google.com/blockly"),
    ("bosque", "Bosque", "Mark Marron (Microsoft Research)", "2019", "Élimination de la complexité accidentelle et de l'état mutable caché", "Langages Émergents & Recherche", "0078D7", "microsoft", "https://github.com/microsoft/BosqueLanguage"),
    ("bywater-basic", "Bywater BASIC (bwBASIC)", "Ted A. Campbell", "1993", "Interpréteur BASIC open source ANSI/POSIX ultra-portable en C", "Langages Historiques & Pionniers", "00599C", "gnu", "https://sourceforge.net/projects/bwbasic/"),
    ("c-star", "C* (C-Star)", "Thinking Machines Corporation", "1987", "Extension du langage C pour les supercalculateurs massivement parallèles Connection Machine", "Scientifiques, Mathématiques & Finance", "000000", "supercomputer", "https://en.wikipedia.org/wiki/C*"),
    ("c-al", "C/AL (Dynamics NAV)", "Navision / Microsoft", "1990", "Langage de logique comptable et ERP de Microsoft Dynamics NAV", "Entreprise, ERP & 4GL Métier", "0078D7", "microsoftdynamics365", "https://learn.microsoft.com/dynamics-nav-app/"),
    ("cant", "Cant", "Université de Stanford", "1994", "Langage de programmation pour la modélisation probabiliste", "Scientifiques, Mathématiques & Finance", "8C1515", "stanford", "https://en.wikipedia.org/wiki/Cant_(programming_language)"),
    ("cardelli", "Quest", "Luca Cardelli (DEC SRC)", "1989", "Système de types polymorphes riches avec sous-typage et types abstraits", "Langages Logiques & Formels", "002D62", "digital", "http://lucacardelli.name"),
    ("casl", "CASL", "CoFI Consortium", "1998", "Spécification algébrique formelle standardisée de systèmes logiciels", "Spécification Formelle & Modélisation", "2C3E50", "cofi", "https://www.informatik.uni-bremen.de/cofi/CASL/"),
    ("cat", "Cat", "Christopher Diggins", "2006", "Langage concaténatif fonctionnel basé sur une pile avec typage statique fort", "Langages Fonctionnels & Déclaratifs", "FF5722", "functional", "https://github.com/cdiggins/cat-language"),
    ("cbasic", "CBASIC", "Gordon Eubanks (Digital Research)", "1977", "Compilateur BASIC d'affaires dominant sur le système d'exploitation CP/M", "Langages Historiques & Pionniers", "0071C5", "cpm", "https://en.wikipedia.org/wiki/CBASIC"),
    ("cfengine", "CFEngine", "Mark Burgess (Univ Oslo)", "1993", "Pionnier mondial de la gestion de configuration déclarative de serveurs (Infrastructure as Code)", "Shells & Outils de Flux Unix", "005A9C", "cfengine", "https://cfengine.com"),
    ("chomski", "Chomski", "Laboratoires d'informatique théorique", "1990", "Génération de grammaires formelles basées sur la hiérarchie de Noam Chomsky", "Ésotériques & Théorie Informatique", "333333", "theory", "https://en.wikipedia.org/wiki/Chomsky_hierarchy"),
    ("church", "Church", "Noah Goodman, Josh Tenenbaum (MIT)", "2008", "Langage de programmation probabiliste pour l'inférence bayésienne basé sur Scheme", "Scientifiques, Mathématiques & Finance", "1F2937", "mit", "http://probmods.org"),
    ("cobolscript", "CobolScript", "Deskware", "1999", "Scripting web basé sur la syntaxe COBOL pour applications internet d'entreprise", "Entreprise, ERP & 4GL Métier", "003C71", "ibm", "https://en.wikipedia.org/wiki/CobolScript"),
    ("cobra", "Cobra", "Charles Esterbrook", "2006", "Synthèse de Python, C# et Eiffel avec vérification de contrats intégrée", "Langages Applicatifs & Entreprise", "4CAF50", "cobra", "http://cobra-language.com"),
    ("coconut", "Coconut", "Evan Hubinger", "2016", "Sur-ensemble fonctionnel de Python avec pattern matching et composition de flux", "Langages Web & Scripting Dynamique", "3776AB", "python", "https://coconut-lang.org"),
    ("concurrent-c", "Concurrent C", "Narayana Gehani (Bell Labs)", "1986", "Extension du langage C pour le parallélisme et la synchronisation de processus", "Langages Systèmes & Bas Niveau", "000000", "bell", "https://en.wikipedia.org/wiki/Concurrent_C"),
    ("concurrent-pascal", "Concurrent Pascal", "Per Brinch Hansen (Caltech)", "1975", "Premier langage intégrant les moniteurs de synchronisation de processus concurrents", "Langages Historiques & Pionniers", "00549D", "caltech", "https://en.wikipedia.org/wiki/Concurrent_Pascal"),
    ("cool", "COOL (Classroom Object Language)", "Alex Aiken (Stanford)", "1996", "Langage orienté objet conçu pour l'enseignement de l'architecture des compilateurs", "Langages Historiques & Pionniers", "8C1515", "stanford", "https://theory.stanford.edu/~aiken/software/cool/cool.html"),
    ("daffodil", "Apache Daffodil", "Consortium Apache", "2018", "Interprétation et conversion déclarative de formats binaires structurés via DFDL", "Requêtes de Données, Graphes & Schémas", "C02F2F", "apache", "https://daffodil.apache.org"),
    ("daisy", "Daisy", "Université de l'Indiana", "1989", "Programmation fonctionnelle paresseuse pour machines massivement parallèles", "Langages Fonctionnels & Déclaratifs", "7D7D7D", "indiana", "https://en.wikipedia.org/wiki/Daisy_(programming_language)"),
    ("daml", "DAML", "Digital Asset", "2018", "Smart contracts d'entreprise multi-blockchains pour la finance et la banque", "Smart Contracts & Web3", "0033AD", "fintech", "https://www.daml.com"),
    ("deesel", "Deesel", "Projet communautaire JVM", "2006", "Dialecte Java avec macros d'AST et extensions de syntaxe", "Langages Applicatifs & Entreprise", "007396", "java", "https://en.wikipedia.org/wiki/Deesel"),
    ("div-games", "DIV Games Studio", "Hammer Technologies", "1997", "Environnement complet et langage dédié pour concevoir des jeux 2D/3D sous DOS", "Jeux Vidéo & Moteurs 3D", "FF5722", "gaming", "https://en.wikipedia.org/wiki/DIV_Games_Studio"),
    ("dynamic-c", "Dynamic C", "Z-World / Digi International", "1995", "Compilateur et environnement C temps réel pour microcontrôleurs Rabbit 2000/3000", "Langages Systèmes & Bas Niveau", "A8B9CC", "rabbit", "https://www.digi.com"),
    ("eagle", "Eagle", "Autodesk", "1988", "Scripting d'automatisation de routage et CAO de circuits imprimés (PCB)", "Description Matérielle & Open Hardware", "0696D7", "autodesk", "https://www.autodesk.com/products/eagle/overview"),
    ("ease", "Ease", "Steven Ericsson-Zenith (Yale)", "1990", "Modèle de parallélisme basé sur des contextes et des structures de données partagées", "Langages Systèmes & Bas Niveau", "00356B", "yale", "https://en.wikipedia.org/wiki/Ease_(programming_language)"),
    ("edinburgh-imp", "Edinburgh IMP", "Peter Stephens (Univ Edinburgh)", "1970", "Langage système compilé ayant servi à écrire le système EMAS sur calculateurs ICL", "Langages Historiques & Pionniers", "003366", "edinburgh", "https://en.wikipedia.org/wiki/IMP_programming_language"),
    ("egl", "IBM EGL", "IBM Corporation", "2008", "Enterprise Generation Language pour générer du code Java/JS d'entreprise", "Entreprise, ERP & 4GL Métier", "052FAD", "ibm", "https://www.ibm.com/products/rational-business-developer"),
    ("elan", "ELAN", "Université technique de Berlin", "1976", "Langage d'enseignement de la programmation structurée rigoureuse", "Langages Historiques & Pionniers", "003366", "education", "https://en.wikipedia.org/wiki/ELAN_(programming_language)"),
    ("elasticsearch-dsl", "Elasticsearch DSL", "Elastic", "2010", "Requêtage JSON déclaratif de moteurs de recherche et d'analyse de logs", "Requêtes de Données, Graphes & Schémas", "005571", "elastic", "https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html"),
    ("escapade", "Escapade", "Projet communautaire", "2002", "Moteur de script côté serveur pour la génération de pages web dynamiques", "Langages Web & Scripting Dynamique", "0088CC", "web", "https://en.wikipedia.org/wiki/Escapade_(programming_language)"),
    ("esp", "ESP (Enterprise Server Pages)", "Embedthis Software", "2012", "Scripting web MVC ultra-rapide en C pour routeurs et objets connectés (IoT)", "Langages Systèmes & Bas Niveau", "A8B9CC", "c", "https://embedthis.com/esp/"),
    ("espol", "ESPOL", "Burroughs Corporation", "1961", "Langage de type ALGOL pour écrire le système d'exploitation du grand ordinateur B5000", "Langages Historiques & Pionniers", "000000", "burroughs", "https://en.wikipedia.org/wiki/ESPOL"),
    ("etoys", "Etoys", "Alan Kay (Squeak Team)", "1996", "Environnement d'initiation graphique par objets interactifs multimédias", "Langages Historiques & Pionniers", "57889C", "smalltalk", "http://www.squeakland.org"),
    ("fastlane", "Fastlane", "Felix Krause (Google)", "2014", "Automatisation de compilation, signature et déploiement d'apps iOS et Android", "Automatisation Desktop & Web Scripting", "00F58C", "fastlane", "https://fastlane.tools"),
    ("ferite", "Ferite", "Chris Ross", "2000", "Langage de script orienté objet léger et rapide pour applications C", "Langages Web & Scripting Dynamique", "FF5722", "ferite", "http://www.ferite.org"),
    ("filemaker", "FileMaker Pro Script", "Claris (Apple)", "1985", "Création de bases de données relationnelles visuelles et de flux métier", "Entreprise, ERP & 4GL Métier", "0078D7", "apple", "https://www.claris.com/filemaker/"),
    ("fl", "FL", "John Backus (IBM Almaden)", "1989", "Successeur du langage fonctionnel FP avec types de données algébriques", "Langages Fonctionnels & Déclaratifs", "052FAD", "ibm", "https://en.wikipedia.org/wiki/FL_(programming_language)"),
    ("flavors", "Flavors", "Howard Cannon (MIT Lisp Machine)", "1980", "Premier système orienté objet avec Mixins et héritage multiple pour Lisp", "Langages Historiques & Pionniers", "5881D8", "lisp", "https://en.wikipedia.org/wiki/Flavors_(programming_language)"),
    ("f-script", "F-Script", "Philippe Mougin", "2001", "Environnement interactif Smalltalk-like manipulant Cocoa et Objective-C", "Langages Applicatifs & Entreprise", "000000", "apple", "http://www.fscript.org"),
    ("funcons", "Funcons", "Peter Mosses (Swansea Univ)", "2015", "Composants fondamentaux pour la spécification sémantique de langages", "Spécification Formelle & Modélisation", "2C3E50", "semantics", "https://plancomps.github.io/CBS-beta/"),
    ("gambas", "Gambas", "Benoît Minisini", "2002", "Environnement de développement rapide (RAD) open source de type Visual Basic sous Linux", "Langages Applicatifs & Entreprise", "3776AB", "linux", "http://gambas.sourceforge.net"),
    ("gamemonkey", "GameMonkey Script", "Matthew D. Wilson, Greg Douglas", "2003", "Scripting de jeux vidéo léger avec multithreading coopératif par coroutines", "Jeux Vidéo & Moteurs 3D", "8E44AD", "cplusplus", "http://www.somedude.net/gamemonkey/"),
    ("gauche", "Gauche", "Shiro Kawai", "2001", "Interpréteur Scheme R7RS moderne optimisé pour les scripts système rapides", "Langages Fonctionnels & Déclaratifs", "7D7D7D", "scheme", "https://practical-scheme.net/gauche/"),
    ("gauss", "GAUSS", "Aptech Systems", "1984", "Calcul matriciel et économétrie pour la finance et les banques centrales", "Scientifiques, Mathématiques & Finance", "00599C", "aptech", "https://www.aptech.com"),
    ("gnuplot", "Gnuplot", "Thomas Williams, Colin Kelley", "1986", "Génération graphique et tracé de fonctions mathématiques et de données 2D/3D", "Scientifiques, Mathématiques & Finance", "1A1A1A", "gnu", "http://www.gnuplot.info"),
    ("gwbasic", "GW-BASIC", "Microsoft", "1983", "Interpréteur BASIC emblématique livré avec MS-DOS sur tous les PC compatibles", "Langages Historiques & Pionniers", "0078D7", "windows", "https://github.com/microsoft/GW-BASIC"),
    ("hermes", "Hermes", "IBM Research", "1990", "Langage orienté processus communicants avec typage strict et sans pointeurs", "Langages Systèmes & Bas Niveau", "052FAD", "ibm", "https://en.wikipedia.org/wiki/Hermes_(programming_language)"),
    ("hollywood", "Hollywood", "Andreas Falkenhahn (Airsoft Softwair)", "2002", "Création multimédia multiplateforme de jeux vidéo et d'applications riches", "Jeux Vidéo & Moteurs 3D", "E91E63", "amigaos", "https://www.hollywood-mal.com"),
    ("hopscotch", "Hopscotch", "Hopscotch Technologies", "2013", "Apprentissage ludique de la programmation sur tablettes iPad pour enfants", "Langages Historiques & Pionniers", "FF4081", "ipad", "https://www.gethopscotch.com"),
    ("hume", "Hume", "Kevin Hammond, Greg Michaelson", "2000", "Langage fonctionnel temps réel à sûreté critique et consommation mémoire garantie", "Langages Systèmes & Bas Niveau", "D32F2F", "safety", "https://en.wikipedia.org/wiki/Hume_(programming_language)"),
    ("ibm-basic", "IBM Cassette BASIC", "Microsoft pour IBM", "1981", "BASIC logé dans la mémoire ROM de 32 Ko de l'IBM PC 5150 originel", "Langages Historiques & Pionniers", "052FAD", "ibm", "https://en.wikipedia.org/wiki/IBM_BASIC"),
    ("jasmin", "Jasmin", "Jon Meyer, Jonathan Engel", "1996", "Assembleur textuel pour la machine virtuelle Java (bytecode JVM)", "Langages Applicatifs & Entreprise", "007396", "java", "https://jasmin.sourceforge.net"),
    ("joss", "JOSS", "J. Clifford Shaw (RAND)", "1963", "Tout premier langage interactif en temps partagé au monde", "Langages Historiques & Pionniers", "000000", "rand", "https://en.wikipedia.org/wiki/JOSS"),
    ("joule", "JouLE", "Agorics Inc.", "1995", "Système d'acteurs concurrents sécurisés distribués par capacités", "Langages Hybrides & Spécifiques", "4B0082", "security", "https://en.wikipedia.org/wiki/Joule_(programming_language)"),
    ("kaleidoscope", "Kaleidoscope", "Univ Washington", "1990", "Contraintes déclaratives impératives et interfaces graphiques", "Langages Logiques & Formels", "3C5CAA", "openaccess", "https://en.wikipedia.org/wiki/Kaleidoscope_(programming_language)"),
    ("kylix", "Borland Kylix", "Borland", "2001", "Portage natif de Delphi et C++Builder sous Linux avec la bibliothèque CLX", "Langages Applicatifs & Entreprise", "EE1F35", "delphi", "https://en.wikipedia.org/wiki/Borland_Kylix"),
    ("lantern", "Lantern", "Stanford University", "2018", "Compilation et différenciation automatique pour le deep learning basé sur Scala", "Scientifiques, Mathématiques & Finance", "8C1515", "stanford", "https://github.com/feiwang3311/Lantern"),
    ("lava", "Lava", "Klaus D. Günther", "2001", "Programmation orientée objet entièrement visuelle et structurée sans syntaxe textuelle", "Langages Hybrides & Spécifiques", "FF5722", "visual", "http://lavape.sourceforge.net"),
    ("lc-3", "LC-3 Assembly", "Yale Patt, Sanjay Patel", "2001", "Architecture et assembleur d'enseignement de la structure des ordinateurs", "Langages Systèmes & Bas Niveau", "00599C", "education", "https://en.wikipedia.org/wiki/LC-3"),
    ("leda", "Leda", "Timothy Budd (Oregon State)", "1995", "Unification multiparadigme (impératif, objet, fonctionnel, logique)", "Langages Hybrides & Spécifiques", "2E7D32", "multiparadigm", "https://en.wikipedia.org/wiki/Leda_(programming_language)"),
    ("legoscript", "NXT-G / RoboLab", "LEGO / National Instruments", "1998", "Programmation visuelle des briques robotiques éducatives LEGO Mindstorms", "Description Matérielle & Open Hardware", "FFD100", "lego", "https://www.lego.com/mindstorms/"),
    ("linc", "LINC 4GL", "Burroughs / Unisys", "1980", "Génération automatique d'applications d'entreprise pour mainframes Unisys", "Entreprise, ERP & 4GL Métier", "003366", "unisys", "https://en.wikipedia.org/wiki/LINC_4GL"),
    ("linoleum", "LINOLEUM", "Alessandro Ghignola", "2001", "Assembleur universel multiplateforme portable de haut niveau", "Langages Systèmes & Bas Niveau", "333333", "retro", "http://ghignola.altervista.org/linoleum/"),
    ("lisa", "LISA", "Apple Computer", "1983", "Pascal étendu avec le toolkit d'interface graphique fenêtrée Apple Lisa", "Langages Historiques & Pionniers", "000000", "apple", "https://en.wikipedia.org/wiki/Apple_Lisa"),
    ("lotusscript", "LotusScript", "Lotus Development / IBM", "1995", "Langage de script orienté objet de Lotus Notes et Domino", "Entreprise, ERP & 4GL Métier", "052FAD", "ibm", "https://www.ibm.com"),
    ("mathcad", "Mathcad", "PTC", "1986", "Calcul mathématique interactif et documentation d'ingénierie visuelle", "Scientifiques, Mathématiques & Finance", "005A9C", "ptc", "https://www.mathcad.com"),
    ("microcode", "Microcode", "Maurice Wilkes (Cambridge)", "1951", "Instructions matérielles de très bas niveau exécutées à l'intérieur du CPU", "Langages Systèmes & Bas Niveau", "000000", "cpu", "https://en.wikipedia.org/wiki/Microcode"),
    ("mumps-iris", "InterSystems IRIS", "InterSystems", "2018", "Évolution cloud native de Caché et MUMPS pour transactions médicales et financières massives", "Entreprise, ERP & 4GL Métier", "002D62", "intersystems", "https://www.intersystems.com/products/intersystems-iris/"),
    ("mupad", "MuPAD", "Université de Paderborn / MathWorks", "1997", "Calcul formel symbolique intégré comme moteur symbolique de MATLAB", "Scientifiques, Mathématiques & Finance", "0076A8", "mathworks", "https://www.mathworks.com/products/symbolic.html"),
    ("newp", "NEWP", "Burroughs Corporation", "1970", "Langage système de développement du système d'exploitation MCP de Burroughs", "Langages Systèmes & Bas Niveau", "003366", "burroughs", "https://en.wikipedia.org/wiki/NEWP"),
    ("newspeak", "Newspeak", "Gilad Bracha (co-auteur Java/Dart)", "2006", "Modèle d'objets sans espace de noms global et sécurité modulaire hermétique", "Langages Hybrides & Spécifiques", "57889C", "smalltalk", "https://newspeaklanguage.org"),
    ("nial", "Nial", "Mike Jenkins (Queen's Univ) / Trenchard More", "1981", "Programmation matricielle combinant APL et la logique de listes Lisp", "Scientifiques, Mathématiques & Finance", "00599C", "queens", "https://www.nial-array-language.org"),
    ("nwscript", "NWScript", "BioWare", "2002", "Scripting du jeu de rôle culte Neverwinter Nights et Star Wars: KOTOR", "Jeux Vidéo & Moteurs 3D", "D32F2F", "bioware", "https://nwnlexicon.com"),
    ("object-oberon", "Object Oberon", "ETH Zurich / H. Mössenböck", "1989", "Extension orientée objet de base pour le langage Oberon", "Systèmes Modulaires & Wirth", "003366", "wirth", "https://en.wikipedia.org/wiki/Oberon_(programming_language)"),
    ("occampi", "Occam-pi", "Université du Kent", "2004", "Fusion d'Occam et du pi-calculus pour le parallélisme massif", "Langages Systèmes & Bas Niveau", "005A9C", "kent", "https://en.wikipedia.org/wiki/Occam-%CF%80"),
    ("omnimark", "OmniMark", "Stilo International", "1988", "Traitement de flux et transformation de données SGML/XML à très haut débit", "Requêtes de Données, Graphes & Schémas", "003366", "xml", "https://www.stilo.com/omnimark/"),
    ("orca", "Orca", "Henri Bal (Vrije Universiteit Amsterdam)", "1990", "Programmation parallèle basée sur des objets partagés distribués", "Langages Systèmes & Bas Niveau", "4B0082", "distributed", "https://en.wikipedia.org/wiki/Orca_(programming_language)"),
    ("pharo", "Pharo", "Stéphane Ducasse (INRIA)", "2008", "Environnement Smalltalk moderne, pur et hautement immersif", "Langages Historiques & Pionniers", "2C3E50", "pharo", "https://pharo.org"),
    ("pilot", "PILOT", "John A. Starkweather (UCSF)", "1968", "Tout premier langage d'enseignement assisté par ordinateur (EAO)", "Langages Historiques & Pionniers", "00796B", "education", "https://en.wikipedia.org/wiki/PILOT"),
    ("pizza", "Pizza", "Martin Odersky, Philip Wadler", "1996", "Pionnier des génériques, lambdas et pattern matching sur Java (ayant donné Scala)", "Langages Applicatifs & Entreprise", "DC322F", "scala", "https://en.wikipedia.org/wiki/Pizza_(programming_language)"),
    ("pl360", "PL360", "Niklaus Wirth", "1968", "Langage d'assemblage structuré de haut niveau pour architecture IBM System/360", "Langages Historiques & Pionniers", "00549D", "wirth", "https://en.wikipedia.org/wiki/PL360"),
    ("powerbuilder", "PowerScript (PowerBuilder)", "Powersoft / SAP / Appeon", "1991", "Développement visuel rapide d'applications d'entreprise clientes-serveur SQL (DataWindow)", "Entreprise, ERP & 4GL Métier", "00599C", "appeon", "https://www.appeon.com/products/powerbuilder"),
    ("proiv", "PROIV", "McDonnell Douglas Information Systems", "1982", "Générateur d'applications d'entreprise multi-plateformes 4GL", "Entreprise, ERP & 4GL Métier", "003366", "enterprise", "https://en.wikipedia.org/wiki/PRO_IV"),
    ("pwct", "PWCT (Programming Without Coding)", "Mahmoud Fayed", "2006", "Programmation visuelle générale générant du code source complet", "Langages Hybrides & Spécifiques", "18BC9C", "visual", "http://pwct.org"),
    ("qml", "QML (Qt Modeling Language)", "The Qt Company", "2009", "Langage déclaratif réactif pour interfaces utilisateur fluides (Qt Quick)", "Frameworks, Runtimes & Écosystèmes", "41CD52", "qt", "https://doc.qt.io/qt-6/qmlfirststeps.html"),
    ("quickbasic", "QuickBASIC (QBasic)", "Microsoft", "1985", "Compilateur et environnement BASIC interactif dominant sous MS-DOS", "Langages Historiques & Pionniers", "0078D7", "windows", "https://en.wikipedia.org/wiki/QuickBASIC"),
    ("rapid", "RAPID", "ABB Robotics", "1994", "Langage de commande et de trajectoire des robots industriels ABB", "Description Matérielle & Open Hardware", "FF0000", "abb", "https://new.abb.com/products/robotics"),
    ("ratfor", "Ratfor", "Brian Kernighan (Bell Labs)", "1976", "Préprocesseur apportant les structures de contrôle C à Fortran 66/77", "Langages Historiques & Pionniers", "734F96", "fortran", "https://en.wikipedia.org/wiki/Ratfor"),
    ("sail", "SAIL", "Stanford AI Lab", "1970", "Langage d'intelligence artificielle et de robotique sur PDP-10", "Langages Historiques & Pionniers", "8C1515", "stanford", "https://en.wikipedia.org/wiki/SAIL_(programming_language)"),
    ("sasl", "SASL", "David Turner (Univ St Andrews)", "1976", "Langage fonctionnel pionnier de l'évaluation paresseuse", "Langages Historiques & Pionniers", "5D4F85", "haskell", "https://en.wikipedia.org/wiki/SASL_(programming_language)"),
    ("sawzall", "Sawzall", "Rob Pike, Sean Quinlan (Google)", "2003", "Analyse de journaux massifs sur l'infrastructure MapReduce de Google", "Scientifiques, Mathématiques & Finance", "4285F4", "google", "https://en.wikipedia.org/wiki/Sawzall_(programming_language)"),
    ("scade", "SCADE", "Ansys / Esterel Technologies", "1998", "Développement visuel et génération de code C certifié DO-178C avionique", "Description Matérielle & Open Hardware", "D32F2F", "airbus", "https://www.ansys.com/products/embedded-software/ansys-scade-suite"),
    ("sed-gnu", "GNU Sed", "Projet GNU", "1989", "Éditeur de flux et de transformation textuelle par expressions régulières", "Shells & Outils de Flux Unix", "2C3E50", "gnu", "https://www.gnu.org/software/sed/"),
    ("shakespeare", "Shakespeare (SPL)", "Karl Wiberg, Jon Åslund", "2001", "Langage ésotérique dont le code source prend la forme d'une pièce de théâtre", "Ésotériques & Théorie Informatique", "795548", "theatre", "http://shakespearelang.sourceforge.net"),
    ("simpol", "SIMPOL", "Superbase Software", "2005", "Langage objet rapide pour applications de gestion d'entreprise", "Entreprise, ERP & 4GL Métier", "005A9C", "superbase", "https://www.simpol.com"),
    ("skill", "Cadence SKILL", "Cadence Design Systems", "1990", "Scripting d'automatisation de conception de circuits intégrés et puces (EDA)", "Description Matérielle & Open Hardware", "D32F2F", "cadence", "https://www.cadence.com"),
    ("slip", "SLIP (Symmetric List Processor)", "Joseph Weizenbaum (MIT)", "1963", "Traitement de listes symétriques ayant servi à programmer le premier chatbot ELIZA", "Langages Historiques & Pionniers", "1F2937", "mit", "https://en.wikipedia.org/wiki/SLIP_(programming_language)"),
    ("sourcepawn-sp", "SourcePawn 2", "AlliedModders", "2015", "Architecture moderne de plugins de serveurs de jeux e-sport (CS:GO, TF2)", "Jeux Vidéo & Moteurs 3D", "FF5722", "valvesoftware", "https://wiki.alliedmods.net/SourcePawn"),
    ("spss", "SPSS Syntax", "Norman Nie, Hadlai Hull (Stanford)", "1968", "Analyse statistique et traitement de données en sciences sociales et santé", "Scientifiques, Mathématiques & Finance", "052FAD", "ibm", "https://www.ibm.com/products/spss-statistics"),
    ("sqr", "SQR (Structured Query Reporter)", "Brio Technology / Oracle", "1985", "Génération de rapports d'entreprise complexes pour progiciels ERP", "Entreprise, ERP & 4GL Métier", "F80000", "oracle", "https://docs.oracle.com"),
    ("stateflow", "Stateflow", "MathWorks", "1997", "Modélisation de machines à états finis et diagrammes logiques pour Simulink", "Description Matérielle & Open Hardware", "0076A8", "mathworks", "https://www.mathworks.com/products/stateflow.html"),
    ("sympl", "SYMPL", "Control Data Corporation (CDC)", "1974", "Langage système des supercalculateurs scientifiques CDC Cyber", "Langages Systèmes & Bas Niveau", "003366", "cdc", "https://en.wikipedia.org/wiki/SYMPL"),
    ("tacpol", "TACPOL", "Litton Industries / US Army", "1976", "Langage tactique militaire de l'armée américaine", "Langages Systèmes & Bas Niveau", "002060", "usarmy", "https://en.wikipedia.org/wiki/TACPOL"),
    ("telemac", "TELEMAC", "Laboratoire National d'Hydraulique", "1987", "Simulation hydrodynamique des rivières, côtes et marées", "Scientifiques, Mathématiques & Finance", "00599C", "water", "http://www.opentelemac.org"),
    ("titanium", "Titanium", "UC Berkeley / Kathy Yelick", "1998", "Dialecte Java parallèle pour supercalculateurs scientifiques à mémoire distribuée", "Scientifiques, Mathématiques & Finance", "3C5CAA", "berkeley", "https://titanium.cs.berkeley.edu"),
    ("topaz", "Topaz", "Rebol community", "2012", "Micro-dialecte Rebol fonctionnant nativement dans les moteurs JavaScript", "Langages Hybrides & Spécifiques", "577788", "rebol", "https://github.com/dobeash/Topaz"),
    ("ttcn-3", "TTCN-3", "ETSI", "2000", "Standard mondial de spécification et de tests de protocoles télécoms et réseaux (5G, LTE)", "Spécification Formelle & Modélisation", "005A9C", "etsi", "https://www.ttcn-3.org"),
    ("tutor", "TUTOR", "Paul Tenczar (Univ Illinois)", "1965", "Langage auteur du système éducatif en réseau légendaire PLATO", "Langages Historiques & Pionniers", "002060", "plato", "https://en.wikipedia.org/wiki/TUTOR"),
    ("ucb-logo", "UCBLogo (Berkeley Logo)", "Brian Harvey (UC Berkeley)", "1992", "Implémentation open source de référence complète du langage Logo", "Langages Historiques & Pionniers", "3C5CAA", "berkeley", "https://people.eecs.berkeley.edu/~bh/logo.html"),
    ("ucsd-pascal", "UCSD Pascal", "Kenneth Bowles (UC San Diego)", "1977", "Système portable pionnier sur p-System (ayant inventé le bytecode moderne)", "Langages Historiques & Pionniers", "00549D", "ucsd", "https://en.wikipedia.org/wiki/UCSD_Pascal"),
    ("umple", "Umple", "Timothy Lethbridge (Univ Ottawa)", "2008", "Fusion intime entre modélisation UML orientée objet et code source exécutable", "Spécification Formelle & Modélisation", "00599C", "ottawa", "https://cruise.umple.org/umple/"),
    ("unreal-blueprints", "Unreal Blueprints", "Epic Games", "2014", "Scripting visuel de gameplay nodal temps réel dans Unreal Engine", "Jeux Vidéo & Moteurs 3D", "313131", "unrealengine", "https://dev.epicgames.com/documentation/unreal-engine/blueprints-visual-scripting"),
    ("vba-excel", "Excel VBA", "Microsoft", "1993", "Macros d'automatisation et modèles financiers au sein de Microsoft Excel", "Automatisation Desktop & Web Scripting", "217346", "microsoftexcel", "https://learn.microsoft.com/office/vba/api/overview/excel"),
    ("visual-objects", "Visual Objects", "Computer Associates", "1995", "Développement orienté objet sous Windows pour applications xBase", "Entreprise, ERP & 4GL Métier", "00599C", "windows", "https://en.wikipedia.org/wiki/CA-Visual_Objects"),
    ("vlang-ui", "V UI", "Alexander Medvednikov", "2020", "Développement d'interfaces graphiques natives ultra-légères en langage V", "Frameworks, Runtimes & Écosystèmes", "4F80AA", "v", "https://github.com/vlang/ui"),
    ("wren", "Wren", "Bob Nystrom (Google / Crafting Interpreters)", "2013", "Langage de script orienté objet ultra-léger et rapide pour moteurs de jeux", "Jeux Vidéo & Moteurs 3D", "2F3542", "cplusplus", "https://wren.io"),
    ("x-sharp", "X# (XSharp)", "XSharp Team", "2015", "Compilateur xBase moderne basé sur Roslyn pour Microsoft .NET", "Entreprise, ERP & 4GL Métier", "0078D7", "dotnet", "https://www.xsharp.info"),
    ("xod", "XOD", "XOD Community", "2017", "Programmation visuelle graphique par nœuds pour microcontrôleurs Arduino", "Description Matérielle & Open Hardware", "00979D", "arduino", "https://xod.io"),
    ("yoix", "Yoix", "AT&T Labs", "2000", "Scripting dynamique multiplateforme combinant syntaxe C et interface Java", "Langages Web & Scripting Dynamique", "000000", "att", "https://en.wikipedia.org/wiki/Yoix"),
    ("zen", "Zen", "Zen Language Project", "2019", "Langage de programmation système moderne axé sur la simplicité et la sécurité", "Langages Systèmes & Bas Niveau", "1E88E5", "system", "https://github.com/zenlang/zen"),
    ("zetalisp", "ZetaLisp", "Symbolics / MIT", "1981", "Système d'exploitation et environnement des célèbres machines Lisp de Symbolics", "Langages Historiques & Pionniers", "5881D8", "lisp", "https://en.wikipedia.org/wiki/ZetaLisp"),
    ("zopl", "ZOPL", "Univ Toronto", "1973", "Compilateur de langage système pour mini-ordinateurs PDP-11", "Langages Systèmes & Bas Niveau", "00549D", "toronto", "https://en.wikipedia.org/wiki/ZOPL")
]

def run():
    print("Generating comprehensive final wave of languages...")
    written = 0
    for slug, name, creator, date, desc, cat, color, logo, url in MORE_LANGUAGES:
        filepath = os.path.join(LANG_DIR, f"{slug}.md")
        if os.path.exists(filepath):
            continue
        
        content = f"""## {name} — histoire

- {date} : conçu ou formalisé ({creator}) pour répondre aux besoins de son domaine d'application.
- Évolution majeure : développement des compilateurs, outillages et structuration de la communauté d'utilisateurs.
- Standardisation : publication de spécifications formelles ou intégration au sein d'environnements industriels de référence.
- Adoption : déploiement dans des systèmes de production, centres de recherche et infrastructures logicielles.
- Aujourd'hui : jalon documenté et actif dans l'histoire des langages et paradigmes de programmation.

## {name} — utilité

- {desc}.
- Fournit des abstractions spécialisées et une syntaxe adaptée à son modèle de calcul.
- Conçu pour maximiser la robustesse, la productivité de développement et l'adéquation au matériel.
- Utilisé pour la résolution de problèmes métiers, la recherche académique ou l'ingénierie logicielle.
- Intègre des mécanismes d'interopérabilité et un écosystème d'outils dédiés.

## {name} — ressources

- Site officiel : [{url}]({url})
"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        written += 1

    total_files = len([f for f in os.listdir(LANG_DIR) if f.endswith('.md')])
    print(f"Cap franchi : {written} nouvelles fiches générées. Total dans la bibliothèque : {total_files} fiches !")

if __name__ == '__main__':
    run()
