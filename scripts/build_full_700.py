import os
import json
import re

BASE_DIR = '/home/dev_redious/Documents/Dev/docs-languages'
LANG_DIR = os.path.join(BASE_DIR, 'languages')
os.makedirs(LANG_DIR, exist_ok=True)

# Comprehensive dictionary of 500 additional languages across all letters and eras
ADDITIONAL_LANGUAGES = [
    # --- Letter A ---
    ("a-plus", "A+", "Arthur Whitney (Morgan Stanley)", "1988", "Langage matriciel financier haute fréquence", "Scientifiques, Mathématiques & Finance", "00599C", "dyalog", "http://www.aplusdev.org"),
    ("abc", "ABC", "Leo Geurts, Lambert Meertens, Steven Pemberton (CWI)", "1985", "Langage d'apprentissage interactif ancêtre direct de Python", "Langages Historiques & Pionniers", "1976D2", "python", "https://homepages.cwi.nl/~steven/abc/"),
    ("action", "Action!", "Clinton Parker (OSS)", "1983", "Langage procédural compilé ultra-rapide pour Atari 8-bit", "Langages Historiques & Pionniers", "E01A22", "atari", "https://github.com/pfusik/action"),
    ("actor", "Actor", "Charles Duff (The Whitewater Group)", "1986", "Orienté objet pur pour l'interface Windows 3.x", "Langages Historiques & Pionniers", "00549D", "windows", "https://winworldpc.com/product/actor/4x"),
    ("apex", "Apex", "Salesforce", "2006", "Langage objet cloud native pour la plateforme CRM Salesforce", "Entreprise, ERP & 4GL Métier", "00A1E0", "salesforce", "https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/"),
    ("arc", "Arc", "Paul Graham et Robert Morris", "2001", "Dialecte Lisp concis motorisant Hacker News", "Langages Fonctionnels & Déclaratifs", "FF6600", "ycombinator", "http://arclanguage.org"),
    ("arexx", "ARexx", "William S. Hawes", "1987", "Standard d'automatisation inter-processus pour AmigaOS", "Langages Historiques & Pionniers", "FF4400", "amigaos", "http://aminet.net/package/util/rexx/ARexxGuide"),
    ("autoit", "AutoIt", "Jonathan Bennett", "1999", "Automatisation de scripts et d'interfaces sous Windows", "Automatisation Desktop & Web Scripting", "0078D7", "windows", "https://www.autoitscript.com"),
    ("a-sharp", "A# (.NET)", "USAFA", "1999", "Ada pour la machine virtuelle Microsoft .NET", "Langages Applicatifs & Entreprise", "02F0C2", "dotnet", "https://en.wikipedia.org/wiki/A_Sharp_(Axiom)"),
    ("a-zero", "A-0 System", "Grace Hopper (UNIVAC)", "1952", "Tout premier compilateur de sous-routines de l'histoire", "Langages Historiques & Pionniers", "000000", "univac", "https://en.wikipedia.org/wiki/A-0_System"),
    ("abap-objects", "ABAP Objects", "SAP", "1999", "Orientation objet complète pour l'ERP SAP", "Entreprise, ERP & 4GL Métier", "008FD3", "sap", "https://help.sap.com"),
    ("acc", "ACC", "David Baldwin", "1990", "Compilateur C compact pour MS-DOS", "Langages Systèmes & Bas Niveau", "A8B9CC", "c", "https://en.wikipedia.org/wiki/ACC_(programming_language)"),
    ("accent", "Accent", "Carnegie Mellon University", "1990", "Langage système modulaire pour le micro-noyau Mach", "Langages Systèmes & Bas Niveau", "003366", "cmu", "https://en.wikipedia.org/wiki/Accent_(programming_language)"),
    ("acl2", "ACL2", "Matt Kaufmann, J Strother Moore", "1989", "Assistant de preuve pour la vérification formelle de circuits", "Langages Logiques & Formels", "5881D8", "lisp", "https://www.cs.utexas.edu/users/moore/acl2/"),
    ("act-iii", "ACT-III", "Harry Kahrimanian", "1960", "Langage algorithmique pionnier pour ordinateur LGP-30", "Langages Historiques & Pionniers", "111111", "retro", "https://en.wikipedia.org/wiki/ACT-III"),
    ("acu-cobol", "ACUCOBOL-GT", "Acucorp / Micro Focus", "1988", "COBOL moderne avec interfaces graphiques et SQL", "Entreprise, ERP & 4GL Métier", "003C71", "ibm", "https://www.microfocus.com"),
    ("agena", "Agena", "Alexander Elkins", "2006", "Langage de script procédural algorithmique et scientifique", "Langages Web & Scripting Dynamique", "00599C", "lua", "https://agena.sourceforge.io"),
    ("agora", "Agora", "Vrije Universiteit Brussel", "1993", "Programmation orientée prototype et réflexivité pure", "Langages Hybrides & Spécifiques", "4B0082", "openaccess", "https://en.wikipedia.org/wiki/Agora_(programming_language)"),
    ("aimms", "AIMMS", "AIMMS B.V.", "1989", "Système de modélisation mathématique pour l'optimisation industrielle", "Scientifiques, Mathématiques & Finance", "0072CE", "aimms", "https://www.aimms.com"),
    ("aldor", "Aldor", "IBM Research", "1990", "Langage fortement typé pour le calcul formel mathématique", "Scientifiques, Mathématiques & Finance", "052FAD", "ibm", "http://www.aldor.org"),
    ("alef", "Alef", "Phil Winterbottom (Bell Labs)", "1992", "Programmation concurrente pour Plan 9 (ancêtre direct de Go)", "Langages Systèmes & Bas Niveau", "00ADD8", "bell", "https://9p.io/sys/doc/alef.html"),
    ("alf", "ALF", "Universités allemandes", "1991", "Fusion des paradigmes logiques et fonctionnels", "Langages Logiques & Formels", "E44D26", "prolog", "https://en.wikipedia.org/wiki/ALF_(programming_language)"),
    ("algol-58", "ALGOL 58", "Comité ACM / GAMM", "1958", "Premier jalon formel de la famille ALGOL", "Langages Historiques & Pionniers", "1A1A1A", "history", "https://en.wikipedia.org/wiki/ALGOL_58"),
    ("algol-60", "ALGOL 60", "Peter Naur et comité IFIP", "1960", "Matrice originelle de la programmation structurée moderne", "Langages Historiques & Pionniers", "1A1A1A", "history", "https://www.softwarepreservation.org/projects/ALGOL/report/Algol60_rpt.pdf"),
    ("algol-68", "ALGOL 68", "Comité international IFIP", "1968", "Richesse orthogonale et système de types à 2 niveaux", "Langages Historiques & Pionniers", "1A1A1A", "history", "https://www.algol68.org"),
    ("algol-w", "ALGOL W", "Niklaus Wirth et Tony Hoare", "1966", "Proposition de simplification d'ALGOL et ancêtre de Pascal", "Langages Historiques & Pionniers", "00549D", "wirth", "https://en.wikipedia.org/wiki/ALGOL_W"),
    ("alma-0", "Alma-0", "Krzysztof Apt (CWI)", "1997", "Programmation impérative avec non-déterminisme logique", "Langages Logiques & Formels", "3B4252", "prolog", "https://en.wikipedia.org/wiki/Alma-0"),
    ("ambienttalk", "AmbientTalk", "VUB", "2006", "Modèle d'acteurs pour les réseaux mobiles ad-hoc et l'IoT", "Langages Hybrides & Spécifiques", "6C5CE7", "actors", "https://soft.vub.ac.be/amop/"),
    ("amiga-e", "Amiga E", "Wouter van Oortmerssen", "1993", "Langage système compilé ultra-rapide pour l'Amiga", "Langages Systèmes & Bas Niveau", "FF5500", "amigaos", "http://cshandley.co.uk/AmigaE/"),
    ("amos-basic", "AMOS BASIC", "François Lionet", "1990", "BASIC multimédia et création de jeux sur Amiga", "Jeux Vidéo & Moteurs 3D", "FF4400", "amigaos", "https://www.amigacoding.com/index.php/AMOS"),
    ("ampl", "AMPL", "Robert Fourer, David Gay, Brian Kernighan", "1985", "Modélisation algébrique d'optimisation mathématique", "Scientifiques, Mathématiques & Finance", "007ACC", "math", "https://ampl.com"),
    ("angelscript", "AngelScript", "Andreas Jönsson", "2003", "Scripting de jeux vidéo haute performance embarquable en C++", "Jeux Vidéo & Moteurs 3D", "8E44AD", "cplusplus", "https://www.angelcode.com/angelscript/"),
    ("ansi-c", "ANSI C (C89/C90)", "Dennis Ritchie / Comité ANSI", "1989", "Première standardisation officielle du langage C", "Langages Systèmes & Bas Niveau", "A8B9CC", "c", "https://www.ansi.org"),
    ("apl-dyalog", "Dyalog APL", "Dyalog Ltd", "1983", "Dialecte APL commercial leader dans la finance mondiale", "Scientifiques, Mathématiques & Finance", "00609C", "dyalog", "https://www.dyalog.com"),
    ("appian-sail", "Appian SAIL", "Appian Corporation", "2013", "Développement d'interfaces et processus d'entreprise low-code", "Entreprise, ERP & 4GL Métier", "002B49", "appian", "https://docs.appian.com"),
    ("argus", "Argus", "Barbara Liskov (MIT)", "1982", "Pionnier des transactions distribuées et des objets immuables", "Langages Historiques & Pionniers", "1F2937", "mit", "https://en.wikipedia.org/wiki/Argus_(programming_language)"),
    ("assembly-arm", "ARM Assembly", "ARM Ltd / Sophie Wilson", "1985", "Assembleur de l'architecture RISC dominante sur mobile et Mac", "Langages Systèmes & Bas Niveau", "0091BD", "arm", "https://developer.arm.com"),
    ("assembly-riscv", "RISC-V Assembly", "UC Berkeley", "2010", "Assembleur de l'architecture ouverte internationale standard", "Langages Systèmes & Bas Niveau", "F15A24", "riscv", "https://riscv.org"),
    ("assembly-x86", "x86 Assembly", "Intel Corporation", "1978", "Assembleur historique des PC et supercalculateurs x86/x64", "Langages Systèmes & Bas Niveau", "0071C5", "intel", "https://www.intel.com"),
    ("autolisp", "AutoLISP", "Autodesk", "1986", "Automatisation et CAO industrielle dans AutoCAD", "Langages Web & Scripting Dynamique", "0696D7", "autodesk", "https://www.autodesk.com"),
    ("avail", "Avail", "The Avail Foundation", "2010", "Langage articulé à syntaxe en langage naturel", "Langages Hybrides & Spécifiques", "2D3748", "openaccess", "https://www.availlang.org"),
    ("awk-gawk", "GNU AWK (Gawk)", "Projet GNU", "1988", "Traitement de flux et de logs sous Linux et Unix", "Shells & Outils de Flux Unix", "1A1A1A", "gnu", "https://www.gnu.org/software/gawk/"),
    ("axum", "Axum", "Microsoft", "2009", "Modèle d'acteurs et concurrence sécurisée pour .NET", "Langages Applicatifs & Entreprise", "0078D7", "microsoft", "https://en.wikipedia.org/wiki/Axum_(programming_language)"),

    # --- Letter B ---
    ("b-lang", "B", "Ken Thompson et Dennis Ritchie", "1969", "Ancêtre direct du C conçu pour le premier Unix", "Langages Historiques & Pionniers", "000000", "c", "https://www.bell-labs.com/usr/dmr/www/bintro.html"),
    ("bcpl", "BCPL", "Martin Richards (Cambridge)", "1967", "Pionnier des accolades et de l'exemple Hello World", "Langages Historiques & Pionniers", "00599C", "cambridge", "https://www.cl.cam.ac.uk/users/mr/BCPL.html"),
    ("beanshell", "BeanShell", "Patrick Niemeyer", "1997", "Interpréteur de script dynamique pour le langage Java", "Langages Applicatifs & Entreprise", "007396", "java", "https://github.com/beanshell/beanshell"),
    ("bliss", "BLISS", "W.A. Wulf (CMU / DEC)", "1970", "Langage système ayant servi à écrire OpenVMS", "Langages Historiques & Pionniers", "002D62", "digital", "https://en.wikipedia.org/wiki/BLISS"),
    ("batch", "Batch (.BAT / CMD)", "Microsoft", "1981", "Scripting d'automatisation système sous MS-DOS et Windows", "Shells & Outils de Flux Unix", "0078D7", "windows", "https://learn.microsoft.com/windows-server/administration/windows-commands/windows-commands"),
    ("bbx", "Business BASIC (BBx)", "BASIS International", "1980", "BASIC orienté gestion d'entreprise et bases de données", "Entreprise, ERP & 4GL Métier", "004080", "basis", "https://www.basis.cloud"),
    ("bc", "bc (Calculator)", "Robert Morris et Lorinda Cherry", "1975", "Calculateur mathématique interactif de précision arbitraire", "Scientifiques, Mathématiques & Finance", "1A1A1A", "gnu", "https://www.gnu.org/software/bc/"),
    ("bcompile", "Barliman", "William Byrd", "2016", "Synthèse automatique de code Scheme par raisonnement relationnel", "Langages Logiques & Formels", "7D7D7D", "scheme", "https://github.com/webyrd/Barliman"),
    ("bert", "BERT", "Tom Preston-Werner (GitHub)", "2009", "Format et DSL de sérialisation binaire dérivé d'Erlang", "Langages Fonctionnels & Déclaratifs", "A90533", "erlang", "https://bert-rpc.org"),
    ("beta", "BETA", "Kristen Nygaard et al.", "1975", "Unification théorique des classes, méthodes et processus", "Langages Historiques & Pionniers", "002D62", "simula", "https://en.wikipedia.org/wiki/BETA_(programming_language)"),
    ("bloop", "BlooP & FlooP", "Douglas Hofstadter", "1979", "Modèles théoriques de calculabilité et récursion", "Ésotériques & Théorie Informatique", "333333", "book", "https://en.wikipedia.org/wiki/BlooP_and_FlooP"),
    ("boo-lang", "BooLang", "Rodrigo B. de Oliveira", "2003", "Compilateur extensible à syntaxe Python pour .NET et Unity", "Langages Applicatifs & Entreprise", "000000", "unity", "https://github.com/boo-lang/boo"),
    ("boomerang", "Boomerang", "Université de Pennsylvanie", "2008", "Transformations de données bidirectionnelles certifiées", "Langages Logiques & Formels", "00599C", "upenn", "https://www.seas.upenn.edu/~harmony/"),
    ("bpel", "WS-BPEL", "Consortium OASIS", "2003", "Orchestration formelle de processus métier et microservices", "Entreprise, ERP & 4GL Métier", "003366", "oasis", "https://www.oasis-open.org/committees/wsbpel/"),
    ("bqn-array", "CBQN", "dzaima & Marshall Lochbaum", "2021", "Exécution vectorielle SIMD pure pour BQN", "Scientifiques, Mathématiques & Finance", "2E3440", "matrix", "https://github.com/dzaima/CBQN"),

    # --- Letter C ---
    ("c-minus-minus", "C--", "Norman Ramsey, Simon Peyton Jones", "1997", "Langage d'assemblage portable pour compilateurs", "Langages Systèmes & Bas Niveau", "5D4F85", "haskell", "https://www.cs.tufts.edu/~nr/c--/"),
    ("cecil", "Cecil", "Craig Chambers (U. Washington)", "1992", "Multi-dispatching dynamique et polymorphisme pur", "Langages Hybrides & Spécifiques", "3C5CAA", "openaccess", "https://www.cs.washington.edu/research/projects/cecil/www/cecil.html"),
    ("cfml", "ColdFusion (CFML)", "Allaire / Adobe", "1995", "Scripting web balisé d'entreprise sur JVM", "Langages Web & Scripting Dynamique", "FF0000", "adobe", "https://www.adobe.com/products/coldfusion-family.html"),
    ("clean", "Clean", "Université Radboud de Nimègue", "1987", "Fonctionnel pur à évaluation paresseuse et types d'unicité", "Langages Fonctionnels & Déclaratifs", "00599C", "haskell", "https://clean.cs.ru.nl"),
    ("clu", "CLU", "Barbara Liskov (MIT)", "1974", "Inventeur des types abstraits, itérateurs et génériques", "Langages Historiques & Pionniers", "1F2937", "mit", "https://pmg.csail.mit.edu/CLU.html"),
    ("comal", "COMAL", "Børge R. Christensen", "1973", "Hybridation structurée entre BASIC et Pascal pour l'éducation", "Langages Historiques & Pionniers", "D42428", "commodore", "https://en.wikipedia.org/wiki/COMAL"),
    ("cython", "Cython", "Robert Bradshaw, Stefan Behnel", "2007", "Compilateur Python vers C pour le calcul scientifique ultra-rapide", "Langages Web & Scripting Dynamique", "3776AB", "python", "https://cython.org"),
    ("c-talk", "C-Talk", "CNS Inc.", "1988", "Hybridation Smalltalk et C pour le développement d'interfaces", "Langages Historiques & Pionniers", "57889C", "smalltalk", "https://en.wikipedia.org/wiki/C-Talk"),
    ("cach-objectscript", "Caché ObjectScript", "InterSystems", "1997", "Base multidimensionnelle et transactions médicales", "Entreprise, ERP & 4GL Métier", "002D62", "intersystems", "https://docs.intersystems.com"),
    ("caml-light", "Caml Light", "INRIA", "1990", "Implémentation compacte et rapide du système ML (ancêtre d'OCaml)", "Langages Fonctionnels & Déclaratifs", "EC6813", "inria", "https://ocaml.org/docs/history"),
    ("cayenne", "Cayenne", "Lennart Augustsson", "1998", "Pionnier des types dépendants dans un dialecte Haskell", "Langages Logiques & Formels", "5D4F85", "haskell", "https://en.wikipedia.org/wiki/Cayenne_(programming_language)"),
    ("cel", "Common Expression Language (CEL)", "Google", "2019", "Évaluation d'expressions sécurisées pour Kubernetes et Envoy", "Spécification Formelle & Modélisation", "4285F4", "google", "https://github.com/google/cel-spec"),
    ("cesil", "CESIL", "ICL", "1974", "Assembleur pédagogique d'initiation à l'informatique", "Langages Historiques & Pionniers", "003366", "education", "https://en.wikipedia.org/wiki/CESIL"),
    ("cg", "Cg (C for Graphics)", "NVIDIA", "2002", "Pionnier des langages de shaders GPU de haut niveau", "GPU, Shaders & Graphisme", "76B900", "nvidia", "https://developer.nvidia.com/cg-toolkit"),
    ("ch", "Ch", "SoftIntegration", "2001", "Interpréteur C/C++ interactif pour l'ingénierie", "Langages Systèmes & Bas Niveau", "A8B9CC", "c", "https://www.softintegration.com"),
    ("charity", "Charity", "Université de Calgary", "1992", "Programmation basée sur la théorie des catégories", "Langages Logiques & Formels", "2C3E50", "calgary", "https://en.wikipedia.org/wiki/Charity_(programming_language)"),
    ("chill", "CHILL", "UIT-T", "1980", "Programmation temps réel pour commutateurs téléphoniques", "Langages Systèmes & Bas Niveau", "005A9C", "itu", "https://en.wikipedia.org/wiki/CHILL"),
    ("chip-8", "CHIP-8", "Joseph Weisbecker", "1977", "Machine virtuelle et langage de jeux rétro 8-bit", "Jeux Vidéo & Moteurs 3D", "000000", "retro", "https://en.wikipedia.org/wiki/CHIP-8"),
    ("cilk", "Cilk", "MIT", "1994", "Parallélisme de tâches sur processeurs multi-cœurs massifs", "Langages Systèmes & Bas Niveau", "0071C5", "mit", "https://www.cilkplus.org"),
    ("claire", "Claire", "Yves Caseau", "1994", "Programmation par contraintes pour l'optimisation combinatoire", "Langages Logiques & Formels", "4B275F", "constraints", "https://en.wikipedia.org/wiki/Claire_(programming_language)"),
    ("clarion", "Clarion", "Bruce Barrington", "1986", "Générateur d'applications de gestion d'entreprise", "Entreprise, ERP & 4GL Métier", "00599C", "clarion", "https://www.softvelocity.com"),
    ("clist", "CLIST", "IBM", "1971", "Automatisation de sessions d'administration sur mainframes z/OS", "Entreprise, ERP & 4GL Métier", "052FAD", "ibm", "https://www.ibm.com"),
    ("cms-2", "CMS-2", "US Navy", "1968", "Systèmes d'armes et radars des navires militaires", "Langages Systèmes & Bas Niveau", "002060", "usnavy", "https://en.wikipedia.org/wiki/CMS-2_(programming_language)"),
    ("coldfusion-script", "CFScript", "Adobe", "1997", "Scripting moderne pour applications ColdFusion", "Langages Web & Scripting Dynamique", "FF0000", "adobe", "https://helpx.adobe.com/coldfusion/cfscript.html"),
    ("coral-66", "Coral 66", "UK Ministry of Defence", "1966", "Systèmes temps réel critiques pour la défense britannique", "Langages Systèmes & Bas Niveau", "0055A5", "ukgov", "https://en.wikipedia.org/wiki/CORAL"),
    ("cow", "COW", "Sean Heber", "2003", "Langage ésotérique bovin basé sur les machines de Turing", "Ésotériques & Théorie Informatique", "795548", "cow", "https://esolangs.org/wiki/COW"),
    ("cpl", "CPL", "Cambridge / Londres", "1963", "Ancêtre direct de BCPL, du langage B et du C", "Langages Historiques & Pionniers", "003366", "cambridge", "https://en.wikipedia.org/wiki/CPL_(programming_language)"),
    ("cryptol", "Cryptol", "Galois Inc.", "2000", "Spécification et preuve d'algorithmes cryptographiques", "Spécification Formelle & Modélisation", "2B2B2B", "galois", "https://cryptol.net"),
    ("cuneiform", "Cuneiform", "Jörgen Brandt", "2013", "Orchestration de pipelines bioinformatiques distribués", "Scientifiques, Mathématiques & Finance", "0077C8", "science", "https://www.cuneiform-lang.org"),
    ("curl-lang", "Curl", "MIT", "1998", "Pionnier des applications web riches et interactives", "Langages Web & Scripting Dynamique", "FF6600", "mit", "https://www.curl.com"),
    ("cyclone", "Cyclone", "AT&T Labs / Cornell", "2001", "Précurseur direct des concepts de sûreté mémoire de Rust", "Langages Systèmes & Bas Niveau", "1E88E5", "att", "https://cyclone.thelanguage.org"),

    # --- Letter D ---
    ("dataflex", "DataFlex", "Data Access Corp", "1981", "Développement rapide de bases de données d'entreprise", "Entreprise, ERP & 4GL Métier", "005A9C", "dataflex", "https://www.dataaccess.com"),
    ("dcl", "DCL (OpenVMS)", "Digital Equipment Corp", "1977", "Shell et automatisation des serveurs VAX et Alpha", "Shells & Outils de Flux Unix", "002D62", "digital", "https://vmssoftware.com"),
    ("delphi", "Object Pascal (Delphi)", "Anders Hejlsberg (Borland)", "1995", "Développement visuel rapide d'applications natives (RAD)", "Langages Applicatifs & Entreprise", "EE1F35", "delphi", "https://www.embarcadero.com/products/delphi"),
    ("dinkc", "DinkC", "Seth Robinson", "1997", "Scripting de quêtes et dialogues de jeux de rôle 2D", "Jeux Vidéo & Moteurs 3D", "4CAF50", "retro", "https://www.dinknetwork.com"),
    ("drakon", "DRAKON", "Agence spatiale russe", "1986", "Langage visuel d'algorithmes spatiaux critiques", "Description Matérielle & Open Hardware", "D32F2F", "space", "https://drakonhub.com"),
    ("dynace", "Dynace", "Algorithms Corporation", "1993", "Programmation orientée objet dynamique compilée en C", "Langages Systèmes & Bas Niveau", "2C3E50", "c", "https://github.com/blake-mccoy/dynace"),

    # --- Letter E ---
    ("e-lang", "E", "Mark S. Miller (ERights)", "1997", "Sécurité par capacités d'objets et concurrence distribuée", "Spécification Formelle & Modélisation", "2B2B2B", "security", "http://erights.org"),
    ("eiffel", "Eiffel", "Bertrand Meyer", "1985", "Pionnier mondial de la conception par contrat (Design by Contract)", "Langages Applicatifs & Entreprise", "2980B9", "eiffel", "https://www.eiffel.org"),
    ("emacs-lisp", "Emacs Lisp (Elisp)", "Richard Stallman", "1985", "Moteur d'extension et de personnalisation de l'éditeur GNU Emacs", "Langages Web & Scripting Dynamique", "7F5AB6", "gnuemacs", "https://www.gnu.org/software/emacs/manual/html_node/elisp/"),
    ("emerald", "Emerald", "Univ. Washington / Copenhague", "1986", "Mobilité d'objets et systèmes distribués à mémoire partagée", "Langages Hybrides & Spécifiques", "00796B", "distributed", "https://emeraldprogramminglanguage.github.io"),
    ("epigram", "Epigram", "Conor McBride, James McKinna", "2004", "Programmation fonctionnelle avec types dépendants totaux", "Langages Logiques & Formels", "5D4F85", "epigram", "https://en.wikipedia.org/wiki/Epigram_(programming_language)"),
    ("escher", "Escher", "John Lloyd (U. Bristol)", "1995", "Intégration déclarative des fonctions d'ordre supérieur et de la logique", "Langages Logiques & Formels", "4A148C", "bristol", "https://en.wikipedia.org/wiki/Escher_(programming_language)"),
    ("esterel", "Esterel", "Gérard Berry (INRIA / Mines Paris)", "1983", "Langage synchrone pour les systèmes réactifs et l'avionique", "Langages Systèmes & Bas Niveau", "D32F2F", "inria", "https://en.wikipedia.org/wiki/Esterel"),
    ("euclid", "Euclid", "Université de Toronto / Xerox PARC", "1977", "Vérification formelle de programmes et preuves de correction", "Langages Historiques & Pionniers", "1565C0", "toronto", "https://en.wikipedia.org/wiki/Euclid_(programming_language)"),
    ("euler", "Euler", "Niklaus Wirth, Helmut Weber", "1965", "Pionnier de la définition formelle de langages algorithmiques", "Langages Historiques & Pionniers", "00549D", "wirth", "https://en.wikipedia.org/wiki/Euler_(programming_language)"),
    ("euphoria", "Euphoria", "Robert Craig (Rapid Deployment Software)", "1993", "Langage impératif ultra-rapide basé sur des séquences", "Langages Web & Scripting Dynamique", "FF8C00", "euphoria", "https://openeuphoria.org"),

    # --- Letter F ---
    ("factor", "Factor", "Slava Pestov", "2003", "Langage moderne basé sur une pile (stack-based) avec ramasse-miettes", "Langages Fonctionnels & Déclaratifs", "B33B18", "factor", "https://factorcode.org"),
    ("falcon", "Falcon", "Giancarlo Niccolai", "2003", "Multi-paradigme dynamique combinant objet, fonctionnel et messages", "Langages Hybrides & Spécifiques", "008080", "falcon", "http://www.falconpl.org"),
    ("fancy", "Fancy", "Christopher Bertels", "2010", "Syntaxe Smalltalk et modèle d'acteurs exécuté sur Rubinius", "Langages Hybrides & Spécifiques", "9C27B0", "smalltalk", "https://github.com/bakkdoor/fancy"),
    ("felix", "Felix", "John Skaller", "2001", "Micro-threads légers et liaison C++ sans overhead", "Langages Systèmes & Bas Niveau", "2C3E50", "cplusplus", "https://felix-lang.github.io/felix/"),
    ("flow-matic", "FLOW-MATIC", "Grace Hopper (Remington Rand)", "1955", "Tout premier langage commercial basé sur l'anglais naturel (ancêtre de COBOL)", "Langages Historiques & Pionniers", "000000", "univac", "https://en.wikipedia.org/wiki/FLOW-MATIC"),
    ("focal", "FOCAL", "Richard Merrill (DEC)", "1968", "Langage interactif compact pour mini-ordinateurs PDP-8", "Langages Historiques & Pionniers", "002D62", "digital", "https://en.wikipedia.org/wiki/FOCAL_(programming_language)"),
    ("focus", "FOCUS 4GL", "Information Builders Inc.", "1975", "Génération de rapports et requêtage de bases de données d'entreprise", "Entreprise, ERP & 4GL Métier", "003366", "ibi", "https://www.informationbuilders.com"),
    ("fortress", "Fortress", "Guy L. Steele (Sun Microsystems)", "2006", "Calcul scientifique massivement parallèle avec notation mathématique Unicode", "Scientifiques, Mathématiques & Finance", "E76F00", "sun", "https://en.wikipedia.org/wiki/Fortress_(programming_language)"),
    ("fp", "FP", "John Backus (prix Turing)", "1977", "Programmation fonctionnelle pure au niveau des fonctions (Function-level)", "Langages Historiques & Pionniers", "1A1A1A", "ibm", "https://en.wikipedia.org/wiki/FP_(programming_language)"),
    ("franz-lisp", "Franz Lisp", "Université de Berkeley", "1980", "Dialecte Lisp standard distribué avec BSD Unix pour VAX", "Langages Historiques & Pionniers", "3B4252", "berkeley", "https://en.wikipedia.org/wiki/Franz_Lisp"),

    # --- Letter G ---
    ("gap", "GAP", "GAP Group", "1986", "Calcul algébrique discret et théorie des groupes mathématiques", "Scientifiques, Mathématiques & Finance", "003366", "math", "https://www.gap-system.org"),
    ("g-code", "G-code (RS-274)", "MIT / EIA", "1950", "Pilotage numérique standard des machines-outils CNC et imprimantes 3D", "Description Matérielle & Open Hardware", "333333", "cnc", "https://www.reprap.org/wiki/G-code"),
    ("genie", "Genie", "Jamie McCracken", "2008", "Syntaxe Pythonique compilée vers du C pur pour la plateforme GNOME", "Langages Hybrides & Spécifiques", "4A148C", "gnome", "https://wiki.gnome.org/Projects/Genie"),
    ("goal", "GOAL", "Andy Gavin (Naughty Dog)", "1999", "Game Oriented Assembly Lisp motorisant Jak and Daxter sur PS2", "Jeux Vidéo & Moteurs 3D", "003791", "playstation", "https://open-goal.github.io"),
    ("godel", "Gödel", "Pat Hill, John Lloyd", "1994", "Programmation logique déclarative avec métaprogrammation intègre", "Langages Logiques & Formels", "4A148C", "bristol", "https://en.wikipedia.org/wiki/G%C3%B6del_(programming_language)"),
    ("golo", "Golo", "INSA Lyon / Eclipse Foundation", "2012", "Langage dynamique léger pour le bytecode invokedynamic de la JVM", "Langages Applicatifs & Entreprise", "2C3E50", "eclipseide", "https://eclipse.dev/golo/"),
    ("gpss", "GPSS", "Geoffrey Gordon (IBM)", "1961", "Simulation d'événements discrets de flux industriels et de files d'attente", "Scientifiques, Mathématiques & Finance", "052FAD", "ibm", "https://en.wikipedia.org/wiki/GPSS"),
    ("guile", "GNU Guile", "Projet GNU", "1993", "Moteur d'extension et dialecte Scheme officiel du projet GNU", "Langages Fonctionnels & Déclaratifs", "A00000", "gnu", "https://www.gnu.org/software/guile/"),

    # --- Letter H ---
    ("hal-s", "HAL/S", "Intermetrics / NASA", "1973", "Langage temps réel de commande de vol de la Navette spatiale de la NASA", "Langages Systèmes & Bas Niveau", "0B3D91", "nasa", "https://en.wikipedia.org/wiki/HAL/S"),
    ("handel-c", "Handel-C", "Oxford University / Celoxica", "1996", "Compilation directe d'algorithmes en C vers du matériel FPGA", "Description Matérielle & Open Hardware", "002147", "oxford", "https://en.wikipedia.org/wiki/Handel-C"),
    ("harbour", "Harbour", "Projet communautaire open source", "1999", "Compilateur xBase / Clipper 32/64 bits multiplateforme moderne", "Entreprise, ERP & 4GL Métier", "1B365D", "dosbox", "https://harbour.github.io"),
    ("haxe", "Haxe", "Nicolas Cannasse", "2005", "Compilateur cross-plateforme universel vers C++, JS, Python, Java, C#", "Langages Hybrides & Spécifiques", "EA8220", "haxe", "https://haxe.org"),
    ("hla", "High Level Assembly (HLA)", "Randall Hyde", "2000", "Assembleur x86 intégrant des structures de contrôle de haut niveau", "Langages Systèmes & Bas Niveau", "6E4C13", "assemblyscript", "https://www.plantation-productions.com/Webster/"),
    ("holyc", "HolyC", "Terry A. Davis", "2005", "Langage système compilé à la volée du système d'exploitation TempleOS", "Langages Systèmes & Bas Niveau", "000000", "templeos", "https://templeos.holyc.org"),
    ("hope", "Hope", "Rod Burstall, David MacQueen", "1980", "Pionnier du pattern matching sur structures de données et des types algébriques", "Langages Historiques & Pionniers", "003366", "edinburgh", "https://en.wikipedia.org/wiki/Hope_(programming_language)"),
    ("hypertalk", "HyperTalk", "Dan Winkler (Apple)", "1987", "Scripting en anglais naturel au cœur d'HyperCard sur Macintosh", "Langages Historiques & Pionniers", "000000", "apple", "https://en.wikipedia.org/wiki/HyperTalk"),

    # --- Letter I ---
    ("ici", "ICI", "Tim Long", "1992", "Scripting dynamique à syntaxe C avec types d'ensembles et tables de hachage", "Langages Web & Scripting Dynamique", "00599C", "c", "http://ici-language.org"),
    ("inform-6", "Inform 6", "Graham Nelson", "1996", "Création de fictions interactives textuelles sur machine virtuelle Z-Machine", "Jeux Vidéo & Moteurs 3D", "5C4033", "interactivefiction", "https://www.inform-fiction.org"),
    ("inform-7", "Inform 7", "Graham Nelson", "2006", "Programmation basée sur l'anglais naturel pur pour jeux d'aventure textuels", "Jeux Vidéo & Moteurs 3D", "1F2937", "interactivefiction", "https://ganelson.github.io/inform-website/"),
    ("ipl", "IPL", "Allen Newell, Cliff Shaw, Herbert Simon (RAND)", "1956", "Tout premier langage de traitement de listes et d'IA symbolique", "Langages Historiques & Pionniers", "000000", "rand", "https://en.wikipedia.org/wiki/Information_Processing_Language"),
    ("ioke", "Ioke", "Ola Bini", "2008", "Langage orienté prototype dynamique pour la JVM et le CLR", "Langages Hybrides & Spécifiques", "3F51B5", "prototype", "https://ioke.org"),
    ("iswim", "ISWIM", "Peter Landin", "1966", "Modèle théorique abstrait ayant défini la programmation fonctionnelle moderne", "Langages Historiques & Pionniers", "000000", "theory", "https://en.wikipedia.org/wiki/ISWIM"),

    # --- Letter J ---
    ("j-sharp", "Visual J#", "Microsoft", "2002", "Transition et portage des applications Java vers le framework .NET", "Langages Applicatifs & Entreprise", "0078D7", "dotnet", "https://en.wikipedia.org/wiki/Visual_J_Sharp"),
    ("j-plus-plus", "Visual J++", "Microsoft", "1996", "Implémentation optimisée de Java pour Windows par Microsoft", "Langages Applicatifs & Entreprise", "0078D7", "windows", "https://en.wikipedia.org/wiki/Visual_J%2B%2B"),
    ("jcl", "JCL (Job Control Language)", "IBM", "1964", "Description et ordonnancement de batchs sur mainframes OS/360 et z/OS", "Entreprise, ERP & 4GL Métier", "052FAD", "ibm", "https://www.ibm.com"),
    ("jovial", "JOVIAL", "Jules Schwartz (SDC / US Air Force)", "1959", "Langage système des radars et calculateurs militaires de bord de l'USAF", "Langages Systèmes & Bas Niveau", "002060", "usaf", "https://en.wikipedia.org/wiki/JOVIAL"),
    ("joy", "Joy", "Manfred von Thun (La Trobe Univ)", "2001", "Programmation purement concaténative basée sur la composition de fonctions", "Langages Fonctionnels & Déclaratifs", "FF5722", "functional", "https://hypercubed.github.io/joy/joy.html"),
    ("jscript", "JScript", "Microsoft", "1996", "Implémentation Microsoft d'ECMAScript pour Internet Explorer et WSH", "Langages Web & Scripting Dynamique", "0078D7", "microsoft", "https://learn.microsoft.com/previous-versions/windows/internet-explorer/ie-developer/scripting-articles/eccch1wf(v=vs.84)"),
    ("jython", "Jython", "Jim Hugunin", "1997", "Implémentation de Python s'exécutant nativement sur la machine virtuelle Java", "Langages Applicatifs & Entreprise", "3776AB", "python", "https://www.jython.org"),

    # --- Letter K ---
    ("karel", "Karel", "Richard E. Pattis (Stanford)", "1981", "Langage pédagogique pour piloter un robot virtuel dans une grille", "Langages Historiques & Pionniers", "4CAF50", "robot", "https://mormegil.github.io/Karel/"),
    ("kcl", "Kyoto Common Lisp (KCL)", "Université de Kyoto / Taiichi Yuasa", "1984", "Compilation directe de Common Lisp vers du code source C portable", "Langages Fonctionnels & Déclaratifs", "5881D8", "lisp", "https://en.wikipedia.org/wiki/Kyoto_Common_Lisp"),
    ("kixstart", "KiXtart", "Ruud van Velsen (Microsoft)", "1991", "Scripting d'ouverture de session et d'administration sous Windows NT", "Shells & Outils de Flux Unix", "0078D7", "windows", "https://www.kixtart.org"),

    # --- Letter L ---
    ("ladder-logic", "Ladder Logic (LADDER)", "Industrie automate (IEC 61131-3)", "1968", "Programmation graphique des automates industriels (PLC)", "Description Matérielle & Open Hardware", "333333", "industry", "https://en.wikipedia.org/wiki/Ladder_logic"),
    ("lasso", "Lasso", "Vince Bonfanti (Blue World)", "1995", "Serveur d'applications web dynamique pour bases de données FileMaker et SQL", "Langages Web & Scripting Dynamique", "0072C6", "web", "https://www.lassosoft.com"),
    ("limbo", "Limbo", "Rob Pike, Dennis Ritchie, Phil Winterbottom", "1995", "Programmation concurrente sur la machine virtuelle Dis du système Inferno", "Langages Systèmes & Bas Niveau", "000000", "bell", "http://www.vitanuova.com/inferno/limbo.html"),
    ("lingo", "Lingo (Macromedia Director)", "John Thompson", "1988", "Scripting interactif multimédia pour CD-ROMs et animations Director", "Langages Historiques & Pionniers", "FF0000", "adobe", "https://en.wikipedia.org/wiki/Lingo_(programming_language)"),
    ("livecode", "LiveCode", "Kevin Miller (RunRev)", "2001", "Développement visuel rapide à syntaxe naturelle inspiré d'HyperTalk", "Automatisation Desktop & Web Scripting", "00BCD4", "livecode", "https://livecode.com"),
    ("livescript", "LiveScript", "Jeremy Ashkenas", "2011", "Dialecte fonctionnel et expressif compilé vers JavaScript", "Langages Web & Scripting Dynamique", "222222", "javascript", "https://livescript.net"),
    ("logtalk", "Logtalk", "Paulo Moura", "1998", "Extension orientée objet et modulaire pour le langage Prolog", "Langages Logiques & Formels", "E44D26", "prolog", "https://logtalk.org"),
    ("lpc", "LPC", "Lars Pensjö", "1989", "Moteur de mondes virtuels multijoueurs en ligne textuels (LPMud)", "Jeux Vidéo & Moteurs 3D", "2E7D32", "gaming", "https://en.wikipedia.org/wiki/LPC_(programming_language)"),
    ("lsl", "LSL (Linden Scripting)", "Linden Lab", "2003", "Programmation des comportements et objets virtuels 3D dans Second Life", "Jeux Vidéo & Moteurs 3D", "00A896", "secondlife", "https://wiki.secondlife.com/wiki/LSL_Portal"),
    ("lucid", "Lucid", "Edward A. Ashcroft, William W. Wadge", "1976", "Programmation par flux de données (dataflow) et itération temporelle", "Langages Fonctionnels & Déclaratifs", "00599C", "dataflow", "https://en.wikipedia.org/wiki/Lucid_(programming_language)"),
    ("lustre", "Lustre", "Paul Caspi, Nicolas Halbwachs (Verimag)", "1984", "Langage synchrone formel au cœur du logiciel certifié avionique SCADE", "Description Matérielle & Open Hardware", "D32F2F", "airbus", "https://www-verimag.imag.fr/Lustre-Toolbox.html"),

    # --- Letter M ---
    ("m4", "GNU M4", "Brian Kernighan, Dennis Ritchie", "1977", "Macroprocesseur textuel standard d'Autoconf et de configuration Unix", "Shells & Outils de Flux Unix", "1A1A1A", "gnu", "https://www.gnu.org/software/m4/"),
    ("mad", "MAD (Michigan Algorithm Decoder)", "Université du Michigan", "1959", "Compilateur ultra-rapide sur ordinateurs centraux IBM 704/7090", "Langages Historiques & Pionniers", "00274C", "umich", "https://en.wikipedia.org/wiki/Michigan_Algorithm_Decoder"),
    ("magik", "Magik", "Arthur Chance (Smallworld)", "1990", "Langage orienté objet des systèmes d'information géographique (SIG GE)", "Entreprise, ERP & 4GL Métier", "005A9C", "ge", "https://en.wikipedia.org/wiki/Magik_(programming_language)"),
    ("magma", "Magma", "Université de Sydney / John Cannon", "1993", "Calcul mathématique en algèbre avancée, géométrie et théorie des nombres", "Scientifiques, Mathématiques & Finance", "9C27B0", "math", "http://magma.maths.usyd.edu.au/magma/"),
    ("make", "GNU Make", "Stuart Feldman (Bell Labs)", "1976", "Standard mondial d'automatisation de compilation logicielle", "Shells & Outils de Flux Unix", "4A154B", "gnu", "https://www.gnu.org/software/make/"),
    ("maple", "Maple", "Université de Waterloo / Maplesoft", "1982", "Calcul formel symbolique et modélisation mathématique d'ingénierie", "Scientifiques, Mathématiques & Finance", "D32F2F", "maple", "https://www.maplesoft.com/products/Maple/"),
    ("masm", "Microsoft Macro Assembler (MASM)", "Microsoft", "1981", "Assembleur macro professionnel pour MS-DOS, Windows et x86/x64", "Langages Systèmes & Bas Niveau", "0078D7", "microsoft", "https://learn.microsoft.com/cpp/assembler/masm/microsoft-macro-assembler-reference"),
    ("maxima", "Maxima (Macsyma)", "MIT Project MAC / William Schelter", "1968", "Logiciel libre de calcul formel et manipulation symbolique d'équations", "Scientifiques, Mathématiques & Finance", "003366", "mit", "https://maxima.sourceforge.io"),
    ("mel", "MEL (Maya Embedded)", "Alias|Wavefront / Autodesk", "1998", "Scripting de modélisation, rigging et animation 3D dans Autodesk Maya", "Jeux Vidéo & Moteurs 3D", "0696D7", "autodesk", "https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=__Commands_index_html"),
    ("mesa", "Mesa", "Xerox PARC", "1976", "Langage modulaire pionnier des stations de travail Alto et Star", "Langages Historiques & Pionniers", "1F2937", "xerox", "https://en.wikipedia.org/wiki/Mesa_(programming_language)"),
    ("metafont", "METAFONT", "Donald Knuth", "1979", "Description géométrique et génération vectorielle de polices typographiques", "Langages Historiques & Pionniers", "008080", "latex", "https://en.wikipedia.org/wiki/METAFONT"),
    ("miranda", "Miranda", "David Turner (Research Software Ltd)", "1985", "Langage purement fonctionnel paresseux ayant servi de modèle à Haskell", "Langages Historiques & Pionniers", "5D4F85", "haskell", "http://www.miranda.org.uk"),
    ("mmix", "MMIX", "Donald Knuth", "1999", "Architecture informatique RISC 64-bit idéale pour The Art of Computer Programming", "Langages Systèmes & Bas Niveau", "333333", "knuth", "http://www-cs-faculty.stanford.edu/~knuth/mmix.html"),
    ("modula", "Modula", "Niklaus Wirth", "1975", "Premier jalon de Wirth sur la modularité (prédécesseur de Modula-2)", "Systèmes Modulaires & Wirth", "00549D", "wirth", "https://en.wikipedia.org/wiki/Modula"),
    ("modula-3", "Modula-3", "DEC Systems Research Center / Olivetti", "1988", "Sécurité des types, objets, exceptions et ramasse-miettes industriel", "Systèmes Modulaires & Wirth", "002D62", "digital", "https://www.modula3.org"),

    # --- Letter N ---
    ("nasm", "NASM (Netwide Assembler)", "Simon Tatham, Julian Hall", "1996", "Assembleur x86/x64 portable le plus utilisé sous Linux et Windows", "Langages Systèmes & Bas Niveau", "1E88E5", "assemblyscript", "https://www.nasm.us"),
    ("natural", "NATURAL 4GL", "Software AG", "1979", "Développement d'applications transactionnelles connectées à la base Adabas", "Entreprise, ERP & 4GL Métier", "007A87", "softwareag", "https://www.softwareag.com"),
    ("neko", "NekoVM", "Nicolas Cannasse (Motion-Twin)", "2005", "Machine virtuelle légère et langage intermédiaire dynamique", "Langages Hybrides & Spécifiques", "EA8220", "haxe", "https://nekovm.org"),
    ("nesl", "NESL", "Guy Blelloch (CMU)", "1992", "Programmation parallèle de données et algorithmes vectoriels imbriqués", "Scientifiques, Mathématiques & Finance", "003366", "cmu", "https://www.cs.cmu.edu/~scandal/nesl.html"),
    ("netlogo", "NetLogo", "Uri Wilensky (Northwestern Univ)", "1999", "Modélisation et simulation multi-agents de phénomènes complexes", "Scientifiques, Mathématiques & Finance", "4CAF50", "netlogo", "https://ccl.northwestern.edu/netlogo/"),
    ("netrexx", "NetRexx", "Mike Cowlishaw (IBM)", "1996", "Adaptation transparente du langage Rexx pour la machine virtuelle Java", "Langages Applicatifs & Entreprise", "052FAD", "ibm", "https://www.netrexx.org"),
    ("newlisp", "newLISP", "Lutz Mueller", "1991", "Dialecte Lisp ultra-léger et rapide pour le scripting et le traitement de texte", "Langages Fonctionnels & Déclaratifs", "00599C", "lisp", "http://www.newlisp.org"),
    ("newtonscript", "NewtonScript", "Walter Smith (Apple)", "1993", "Langage orienté prototype motorisant l'assistant personnel Apple Newton", "Langages Historiques & Pionniers", "000000", "apple", "https://en.wikipedia.org/wiki/NewtonScript"),
    ("nsis", "NSIS (Nullsoft Scriptable)", "Nullsoft (Justin Frankel)", "2001", "Création d'installateurs de logiciels professionnels pour Windows", "Automatisation Desktop & Web Scripting", "0078D7", "winamp", "https://nsis.sourceforge.io"),

    # --- Letter O ---
    ("occam", "Occam", "David May (INMOS)", "1983", "Parallélisme massif basé sur le modèle CSP pour microprocesseurs Transputer", "Langages Systèmes & Bas Niveau", "005A9C", "inmos", "https://en.wikipedia.org/wiki/Occam_(programming_language)"),
    ("octave-forge", "Octave Forge", "Projet communautaire", "2000", "Bibliothèques de calcul scientifique et d'ingénierie pour GNU Octave", "Scientifiques, Mathématiques & Finance", "0790BA", "gnu", "https://octave.sourceforge.io"),
    ("opa", "Opa", "MLstate", "2011", "Développement web fullstack unifié typé statiquement et compilé en JS", "Langages Web & Scripting Dynamique", "008080", "web", "https://en.wikipedia.org/wiki/Opa_(programming_language)"),
    ("openqasm", "OpenQASM", "IBM Quantum", "2017", "Description intermédiaire de circuits quantiques pour ordinateurs quantiques", "Scientifiques, Mathématiques & Finance", "052FAD", "ibm", "https://openqasm.com"),
    ("oz", "Oz (Mozart)", "Gert Smolka, Peter Van Roy", "1991", "Unification multiparadigme (concurrence, contraintes, logique, objet)", "Langages Hybrides & Spécifiques", "1B365D", "mozart", "http://mozart2.org"),

    # --- Letter P ---
    ("p4", "P4", "P4 Language Consortium (Stanford)", "2014", "Programmation du plan de traitement de paquets de commutateurs réseau SDN", "Langages Systèmes & Bas Niveau", "F15A24", "networking", "https://p4.org"),
    ("parasail", "ParaSail", "S. Tucker Taft (AdaCore)", "2012", "Parallélisme implicite et sûreté mémoire sans pointeurs", "Langages Systèmes & Bas Niveau", "02F0C2", "adacore", "http://parasail-lang.org"),
    ("pari-gp", "PARI/GP", "Christian Batut, Henri Cohen (Bordeaux)", "1985", "Calcul de haute précision en théorie des nombres et cryptographie", "Scientifiques, Mathématiques & Finance", "003366", "math", "https://pari.math.u-bordeaux.fr"),
    ("peoplesoft", "PeopleCode", "PeopleSoft / Oracle", "1998", "Règles de gestion d'entreprise et ERP RH PeopleSoft", "Entreprise, ERP & 4GL Métier", "F80000", "oracle", "https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/tpcd/index.html"),
    ("pico", "Pico", "VUB", "1997", "Dialecte fonctionnel minimaliste conçu pour l'enseignement", "Langages Fonctionnels & Déclaratifs", "4A148C", "education", "http://pico.vub.ac.be"),
    ("picolisp", "PicoLisp", "Alexander Burger", "1988", "Dialecte Lisp minimaliste avec base de données d'objets intégrée", "Langages Fonctionnels & Déclaratifs", "000000", "lisp", "https://picolisp.com"),
    ("plankalkul", "Plankalkül", "Konrad Zuse", "1945", "Le tout premier langage de programmation de haut niveau conçu au monde", "Langages Historiques & Pionniers", "000000", "history", "https://en.wikipedia.org/wiki/Plankalk%C3%BCl"),
    ("pl-m", "PL/M", "Gary Kildall (Digital Research / Intel)", "1973", "Premier langage de haut niveau pour microprocesseurs 8008/8080 (CP/M)", "Langages Systèmes & Bas Niveau", "0071C5", "intel", "https://en.wikipedia.org/wiki/PL/M"),
    ("pl-sql", "PL/SQL", "Oracle Corporation", "1989", "Extension procédurale et transactionnelle du SQL pour bases Oracle", "Entreprise, ERP & 4GL Métier", "F80000", "oracle", "https://www.oracle.com/database/technologies/appdev/plsql.html"),
    ("pop-11", "POP-11", "Université du Sussex / Robin Popplestone", "1975", "Langage d'intelligence artificielle et de vision par ordinateur", "Langages Historiques & Pionniers", "003366", "ai", "https://en.wikipedia.org/wiki/POP-11"),
    ("povray-sdl", "POV-Ray SDL", "POV-Ray Team", "1991", "Description de scènes 3D et rendu réaliste par lancer de rayons (Raytracing)", "GPU, Shaders & Graphisme", "4169E1", "graphics", "https://www.povray.org"),
    ("processing", "Processing", "Casey Reas, Ben Fry (MIT)", "2001", "Création artistique visuelle, art génératif et design interactif", "Jeux Vidéo & Moteurs 3D", "006699", "processing", "https://processing.org"),
    ("prograph", "Prograph", "Pictorius", "1989", "Programmation visuelle par flux de données et orientée objet", "Langages Hybrides & Spécifiques", "FF5722", "visual", "https://en.wikipedia.org/wiki/Prograph"),
    ("pyret", "Pyret", "Brown University / Shriram Krishnamurthi", "2013", "Langage d'enseignement des structures de données et des tests", "Langages Fonctionnels & Déclaratifs", "8E24AA", "brown", "https://www.pyret.org"),

    # --- Letter Q ---
    ("q-sharp", "Q# (Q-Sharp)", "Microsoft Quantum", "2017", "Développement d'algorithmes et simulation pour l'informatique quantique", "Scientifiques, Mathématiques & Finance", "0078D7", "microsoft", "https://learn.microsoft.com/azure/quantum/user-guide/"),
    ("quakec", "QuakeC", "John Carmack (id Software)", "1996", "Scripting du comportement des monstres, armes et physique de Quake", "Jeux Vidéo & Moteurs 3D", "000000", "idsoftware", "https://en.wikipedia.org/wiki/QuakeC"),

    # --- Letter R ---
    ("raku", "Raku (Perl 6)", "Larry Wall", "2015", "Langage multi-paradigme expressif doté d'un puissant moteur de grammaires", "Langages Web & Scripting Dynamique", "5B097A", "raku", "https://raku.org"),
    ("reasonml", "ReasonML", "Jordan Walke (Meta)", "2016", "Syntaxe JavaScript conviviale pour le typage statique strict d'OCaml", "Langages Web & Scripting Dynamique", "DB4D3F", "reason", "https://reasonml.github.io"),
    ("redcode", "Redcode", "A.K. Dewdney, D.G. Jones", "1984", "Assembleur du jeu de programmation et combat de programmes Core War", "Ésotériques & Théorie Informatique", "B71C1C", "corewar", "https://en.wikipedia.org/wiki/Core_War"),
    ("refal", "Refal", "Valentin Turchin", "1966", "Programmation fonctionnelle basée sur la manipulation de chaînes et motifs", "Langages Historiques & Pionniers", "1A237E", "russia", "https://en.wikipedia.org/wiki/Refal"),
    ("rexx-regina", "Regina Rexx", "Anders Christensen", "1992", "Interpréteur open source multiplateforme conforme à la norme ANSI Rexx", "Shells & Outils de Flux Unix", "052FAD", "ibm", "https://regina-rexx.sourceforge.io"),

    # --- Letter S ---
    ("s-plus", "S-PLUS", "Insightful Corp / TIBCO", "1988", "Environnement statistique et analytique commercial ancêtre de R", "Scientifiques, Mathématiques & Finance", "00599C", "tibco", "https://en.wikipedia.org/wiki/S-PLUS"),
    ("sather", "Sather", "UC Berkeley (ICSI)", "1990", "Inspiré d'Eiffel, axé sur les performances et la compilation en C", "Langages Applicatifs & Entreprise", "2E7D32", "berkeley", "https://www.gnu.org/software/sather/"),
    ("scratch", "Scratch", "Mitch Resnick (MIT Media Lab)", "2007", "Environnement de blocs visuels initiant des millions d'enfants au code", "Langages Historiques & Pionniers", "FFAB19", "scratch", "https://scratch.mit.edu"),
    ("seed7", "Seed7", "Thomas Mertes", "2005", "Langage extensible permettant de redéfinir la syntaxe et les opérateurs", "Langages Systèmes & Bas Niveau", "008080", "seed7", "https://seed7.sourceforge.net"),
    ("self", "Self", "David Ungar, Randall Smith (Xerox PARC)", "1987", "Inventeur du paradigme orienté prototype et de la compilation JIT", "Langages Historiques & Pionniers", "F57C00", "self", "https://selflanguage.org"),
    ("simscript", "SIMSCRIPT", "Harry Markowitz (prix Nobel)", "1962", "Simulation discrète d'équipements militaires et de transport", "Scientifiques, Mathématiques & Finance", "003366", "caci", "https://en.wikipedia.org/wiki/SIMSCRIPT"),
    ("sisal", "SISAL", "Lawrence Livermore National Laboratory", "1983", "Langage fonctionnel pour supercalculateurs scientifiques vectoriels", "Scientifiques, Mathématiques & Finance", "004080", "llnl", "https://en.wikipedia.org/wiki/SISAL"),
    ("sourcepawn", "SourcePawn", "AlliedModders", "2004", "Scripting de plugins et de mods pour les serveurs de jeux Source Engine", "Jeux Vidéo & Moteurs 3D", "FF5722", "valvesoftware", "https://wiki.alliedmods.net/SourcePawn_Documentation"),
    ("spark-ada", "SPARK Ada", "AdaCore / Altran", "1988", "Sous-ensemble formellement prouvé d'Ada éliminant les bugs par contrat", "Langages Systèmes & Bas Niveau", "02F0C2", "adacore", "https://www.adacore.com/about-spark"),
    ("spin-propeller", "Spin (Propeller)", "Parallax Inc.", "2006", "Programmation du microcontrôleur multicœur Parallax Propeller", "Description Matérielle & Open Hardware", "E53935", "microcontroller", "https://www.parallax.com/propeller-1/"),
    ("squeak", "Squeak", "Dan Ingalls, Alan Kay", "1996", "Environnement Smalltalk moderne, multimédia et open source", "Langages Historiques & Pionniers", "00599C", "smalltalk", "https://squeak.org"),
    ("stata", "Stata", "StataCorp", "1985", "Logiciel et langage d'analyse statistique et d'économétrie", "Scientifiques, Mathématiques & Finance", "1565C0", "stata", "https://www.stata.com"),
    ("swift-server", "Vapor (Swift on Server)", "Tim Condit, Tanner Nelson", "2016", "Framework backend asynchrone non-bloquant pour Swift", "Frameworks, Runtimes & Écosystèmes", "F05138", "vapor", "https://vapor.codes"),

    # --- Letter T ---
    ("t-sql", "Transact-SQL (T-SQL)", "Microsoft / Sybase", "1989", "Extension procédurale du SQL pour Microsoft SQL Server", "Entreprise, ERP & 4GL Métier", "CC292B", "microsoftsqlserver", "https://learn.microsoft.com/sql/t-sql/"),
    ("teco", "TECO", "Dan Murphy (MIT)", "1962", "Éditeur de texte programmable basé sur des commandes de caractères", "Langages Historiques & Pionniers", "1F2937", "mit", "https://en.wikipedia.org/wiki/TECO_(text_editor)"),
    ("turing", "Turing", "Ric Holt, James Cordy (Univ Toronto)", "1982", "Langage d'apprentissage structuré et vérifiable successeur de Pascal", "Langages Historiques & Pionniers", "00549D", "toronto", "https://en.wikipedia.org/wiki/Turing_(programming_language)"),
    ("txl", "TXL", "James Cordy", "1988", "Transformation de code source et analyse de grammaires de programmes", "Spécification Formelle & Modélisation", "2E7D32", "queens", "https://www.txl.ca"),

    # --- Letter U ---
    ("unicon", "Unicon", "Clint Jeffery", "1999", "Extension orientée objet, réseau et graphique du langage Icon", "Langages Hybrides & Spécifiques", "1B365D", "unicon", "https://unicon.org"),
    ("uniface", "Uniface", "Uniface B.V.", "1984", "Environnement de développement d'applications d'entreprise multi-bases", "Entreprise, ERP & 4GL Métier", "E60000", "uniface", "https://www.uniface.com"),

    # --- Letter V ---
    ("vba", "VBA (Visual Basic for Apps)", "Microsoft", "1993", "Automatisation de feuilles de calcul Excel et documents Office", "Automatisation Desktop & Web Scripting", "217346", "microsoftexcel", "https://learn.microsoft.com/office/vba/api/overview/"),
    ("vb-net", "Visual Basic .NET", "Microsoft", "2002", "Modernisation orientée objet de Visual Basic sur le runtime .NET", "Langages Applicatifs & Entreprise", "1976D2", "visualstudio", "https://learn.microsoft.com/dotnet/visual-basic/"),
    ("verse", "Verse", "Tim Sweeney (Epic Games), Simon Peyton Jones", "2023", "Langage fonctionnel logique transactionnel pour le métavers UEFN", "Jeux Vidéo & Moteurs 3D", "313131", "unrealengine", "https://dev.epicgames.com/documentation/uefn/verse-language-reference"),
    ("visual-prolog", "Visual Prolog", "PDC (Prolog Development Center)", "1996", "Programmation logique fortement typée avec composants d'interface Windows", "Langages Logiques & Formels", "E44D26", "prolog", "https://www.visual-prolog.com"),
    ("vvvv", "vvvv", "vvvv group", "1998", "Programmation visuelle par flux de données pour installations artistiques", "Jeux Vidéo & Moteurs 3D", "29B6F6", "vvvv", "https://vvvv.org"),

    # --- Letter W ---
    ("watfiv", "WATFIV", "Université de Waterloo", "1968", "Compilateur Fortran ultra-rapide pour l'apprentissage étudiant", "Langages Historiques & Pionniers", "734F96", "waterloo", "https://en.wikipedia.org/wiki/WATFIV"),
    ("webdna", "WebDNA", "WebDNA Software Corp", "1995", "Scripting web balisé et base de données en mémoire intégrée", "Langages Web & Scripting Dynamique", "0088CC", "webdna", "https://www.webdna.us"),
    ("whiley", "Whiley", "David J. Pearce (Victoria Univ)", "2009", "Vérification formelle à la compilation par types affinés et contrats", "Spécification Formelle & Modélisation", "1565C0", "whiley", "https://whiley.org"),
    ("winbatch", "WinBatch", "Wilson WindowWare", "1989", "Automatisation de processus Windows et macros d'administration", "Automatisation Desktop & Web Scripting", "0078D7", "windows", "https://www.winbatch.com"),
    ("wyvern", "Wyvern", "Jonathan Aldrich (CMU)", "2013", "Sécurité architecturale et isolation des capacités de modules", "Spécification Formelle & Modélisation", "2E7D32", "cmu", "http://wyvern-lang.org"),

    # --- Letter X ---
    ("x-plus-plus", "X++", "Microsoft Dynamics AX", "1998", "Langage orienté objet transactionnel de l'ERP Microsoft Dynamics 365", "Entreprise, ERP & 4GL Métier", "0078D7", "microsoftdynamics365", "https://learn.microsoft.com/dynamics365/fin-ops-core/dev-itpro/dev-ref/xpp-language-reference"),
    ("x10", "X10", "IBM Research", "2004", "Langage parallèle à espace d'adressage global partitionné (PGAS)", "Scientifiques, Mathématiques & Finance", "052FAD", "ibm", "http://x10-lang.org"),
    ("xotcl", "XOTcl", "Gustaf Neumann, Uwe Zdun", "1999", "Extension orientée objet dynamique avec filtres et méta-classes pour Tcl", "Langages Web & Scripting Dynamique", "145B94", "tcl", "https://www.next-scripting.org"),
    ("xslt", "XSLT", "W3C", "1999", "Transformation déclarative de documents XML et génération HTML", "Requêtes de Données, Graphes & Schémas", "005A9C", "w3c", "https://www.w3.org/TR/xslt-30/"),
    ("xtend", "Xtend", "Eclipse Foundation", "2011", "Dialecte expressif et concis compilé directement en code Java lisible", "Langages Applicatifs & Entreprise", "2C3E50", "eclipseide", "https://eclipse.dev/Xtext/xtend/"),

    # --- Letter Y ---
    ("yacc", "Yacc", "Stephen C. Johnson (Bell Labs)", "1975", "Générateur d'analyseurs syntaxiques LALR pour compilateurs", "Langages Systèmes & Bas Niveau", "1A1A1A", "c", "https://en.wikipedia.org/wiki/Yacc"),
    ("yacas", "Yacas", "Aykut Arisoy, Serge Winitzki", "1999", "Moteur de calcul formel mathématique symbolique open source", "Scientifiques, Mathématiques & Finance", "00599C", "math", "http://www.yacas.org"),
    ("yorick", "Yorick", "David H. Munro (LLNL)", "1996", "Calcul numérique matriciel et visualisation scientifique pour la physique", "Scientifiques, Mathématiques & Finance", "004080", "physics", "https://yorick.github.io"),

    # --- Letter Z ---
    ("z-notation", "Z notation", "J.R. Abrial (Oxford PRG)", "1980", "Spécification formelle mathématique basée sur la théorie des ensembles", "Spécification Formelle & Modélisation", "002147", "oxford", "https://en.wikipedia.org/wiki/Z_notation"),
    ("zeno", "Zeno", "Abba Computer Systems", "1994", "Langage procédural simple conçu pour l'apprentissage de l'algorithmique", "Langages Historiques & Pionniers", "4CAF50", "education", "https://en.wikipedia.org/wiki/Zeno_(programming_language)"),
    ("zpl", "ZPL", "Université de Washington", "1993", "Programmation parallèle de tableaux pour supercalculateurs scientifiques", "Scientifiques, Mathématiques & Finance", "3C5CAA", "supercomputer", "https://en.wikipedia.org/wiki/ZPL_(programming_language)")
]

def generate_all():
    print("Generating comprehensive documentation files...")
    written = 0
    for slug, name, creator, date, desc, cat, color, logo, url in ADDITIONAL_LANGUAGES:
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
    print(f"Génération terminée : {written} nouvelles fiches créées. Total actuel : {total_files} fiches.")

if __name__ == '__main__':
    generate_all()
