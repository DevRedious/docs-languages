import os

# Comprehensive metadata mapping for all 203 badges
BADGE_META = {
    # Systems & Low-level
    'c.md': ('C', 'https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black', 'Langages Systèmes & Bas Niveau'),
    'cpp.md': ('C++', 'https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white', 'Langages Systèmes & Bas Niveau'),
    'rust.md': ('Rust', 'https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white', 'Langages Systèmes & Bas Niveau'),
    'zig.md': ('Zig', 'https://img.shields.io/badge/Zig-F7A41D?style=for-the-badge&logo=zig&logoColor=black', 'Langages Systèmes & Bas Niveau'),
    'nim.md': ('Nim', 'https://img.shields.io/badge/Nim-FFE953?style=for-the-badge&logo=nim&logoColor=black', 'Langages Systèmes & Bas Niveau'),
    'd.md': ('D', 'https://img.shields.io/badge/D-B03931?style=for-the-badge&logo=d&logoColor=white', 'Langages Systèmes & Bas Niveau'),
    'assembly.md': ('Assembly', 'https://img.shields.io/badge/Assembly-6E4C13?style=for-the-badge&logo=assemblyscript&logoColor=white', 'Langages Systèmes & Bas Niveau'),
    'fortran.md': ('Fortran', 'https://img.shields.io/badge/Fortran-734F96?style=for-the-badge&logo=fortran&logoColor=white', 'Langages Systèmes & Bas Niveau'),
    'ada.md': ('Ada', 'https://img.shields.io/badge/Ada-02F0C2?style=for-the-badge&logo=ada&logoColor=black', 'Langages Systèmes & Bas Niveau'),
    'pascal.md': ('Pascal', 'https://img.shields.io/badge/Pascal-00549D?style=for-the-badge&logo=delphi&logoColor=white', 'Langages Systèmes & Bas Niveau'),
    'odin.md': ('Odin', 'https://img.shields.io/badge/Odin-1A2B3C?style=for-the-badge&logo=odin&logoColor=white', 'Langages Systèmes & Bas Niveau'),
    'v.md': ('V', 'https://img.shields.io/badge/V-4F80AA?style=for-the-badge&logo=v&logoColor=white', 'Langages Systèmes & Bas Niveau'),

    # Enterprise & OOP
    'java.md': ('Java', 'https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=java&logoColor=white', 'Langages Applicatifs & Entreprise'),
    'csharp.md': ('C#', 'https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=csharp&logoColor=white', 'Langages Applicatifs & Entreprise'),
    'kotlin.md': ('Kotlin', 'https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white', 'Langages Applicatifs & Entreprise'),
    'scala.md': ('Scala', 'https://img.shields.io/badge/Scala-DC322F?style=for-the-badge&logo=scala&logoColor=white', 'Langages Applicatifs & Entreprise'),
    'groovy.md': ('Groovy', 'https://img.shields.io/badge/Groovy-4298B8?style=for-the-badge&logo=apachegroovy&logoColor=white', 'Langages Applicatifs & Entreprise'),
    'swift.md': ('Swift', 'https://img.shields.io/badge/Swift-F05138?style=for-the-badge&logo=swift&logoColor=white', 'Langages Applicatifs & Entreprise'),
    'objective-c.md': ('Objective-C', 'https://img.shields.io/badge/Objective--C-000000?style=for-the-badge&logo=apple&logoColor=white', 'Langages Applicatifs & Entreprise'),
    'dart.md': ('Dart', 'https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white', 'Langages Applicatifs & Entreprise'),
    'go.md': ('Go', 'https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white', 'Langages Applicatifs & Entreprise'),

    # Enterprise & 4GL
    'abap.md': ('ABAP', 'https://img.shields.io/badge/ABAP-008FD3?style=for-the-badge&logo=sap&logoColor=white', 'Entreprise, ERP & 4GL Métier'),
    'rpg.md': ('RPG IBM i', 'https://img.shields.io/badge/RPG_IBM_i-052FAD?style=for-the-badge&logo=ibm&logoColor=white', 'Entreprise, ERP & 4GL Métier'),
    'mumps.md': ('MUMPS', 'https://img.shields.io/badge/MUMPS-002D62?style=for-the-badge&logo=medicare&logoColor=white', 'Entreprise, ERP & 4GL Métier'),
    'progress-abl.md': ('Progress ABL', 'https://img.shields.io/badge/Progress_ABL-5BC500?style=for-the-badge&logo=progress&logoColor=white', 'Entreprise, ERP & 4GL Métier'),
    'visual-foxpro.md': ('Visual FoxPro', 'https://img.shields.io/badge/Visual_FoxPro-C41F14?style=for-the-badge&logo=visualstudio&logoColor=white', 'Entreprise, ERP & 4GL Métier'),
    'clipper.md': ('Clipper', 'https://img.shields.io/badge/Clipper_xBase-1B365D?style=for-the-badge&logo=dosbox&logoColor=white', 'Entreprise, ERP & 4GL Métier'),
    'rexx.md': ('Rexx', 'https://img.shields.io/badge/Rexx-052FAD?style=for-the-badge&logo=ibm&logoColor=white', 'Entreprise, ERP & 4GL Métier'),

    # Web & Dynamic Scripting
    'html.md': ('HTML5', 'https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white', 'Langages Web & Scripting Dynamique'),
    'css.md': ('CSS3', 'https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white', 'Langages Web & Scripting Dynamique'),
    'javascript.md': ('JavaScript', 'https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black', 'Langages Web & Scripting Dynamique'),
    'typescript.md': ('TypeScript', 'https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white', 'Langages Web & Scripting Dynamique'),
    'python.md': ('Python', 'https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white', 'Langages Web & Scripting Dynamique'),
    'ruby.md': ('Ruby', 'https://img.shields.io/badge/Ruby-CC342D?style=for-the-badge&logo=ruby&logoColor=white', 'Langages Web & Scripting Dynamique'),
    'php.md': ('PHP', 'https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white', 'Langages Web & Scripting Dynamique'),
    'perl.md': ('Perl', 'https://img.shields.io/badge/Perl-39457E?style=for-the-badge&logo=perl&logoColor=white', 'Langages Web & Scripting Dynamique'),
    'lua.md': ('Lua', 'https://img.shields.io/badge/Lua-2C2D72?style=for-the-badge&logo=lua&logoColor=white', 'Langages Web & Scripting Dynamique'),
    'tcl.md': ('Tcl', 'https://img.shields.io/badge/Tcl-145B94?style=for-the-badge&logo=tcl&logoColor=white', 'Langages Web & Scripting Dynamique'),
    'sql.md': ('SQL', 'https://img.shields.io/badge/SQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white', 'Langages Web & Scripting Dynamique'),
    'webassembly.md': ('WebAssembly', 'https://img.shields.io/badge/WebAssembly-654FF0?style=for-the-badge&logo=webassembly&logoColor=white', 'Langages Web & Scripting Dynamique'),
    'xojo.md': ('Xojo', 'https://img.shields.io/badge/Xojo-8CC63F?style=for-the-badge&logo=visualstudio&logoColor=black', 'Langages Web & Scripting Dynamique'),

    # GPU & Shaders
    'cuda.md': ('CUDA', 'https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white', 'GPU, Shaders & Graphisme'),
    'opencl.md': ('OpenCL', 'https://img.shields.io/badge/OpenCL-005C8A?style=for-the-badge&logo=khronos&logoColor=white', 'GPU, Shaders & Graphisme'),
    'glsl.md': ('GLSL', 'https://img.shields.io/badge/GLSL-5586A4?style=for-the-badge&logo=opengl&logoColor=white', 'GPU, Shaders & Graphisme'),
    'hlsl.md': ('HLSL', 'https://img.shields.io/badge/HLSL-0078D7?style=for-the-badge&logo=windows&logoColor=white', 'GPU, Shaders & Graphisme'),
    'wgsl.md': ('WGSL', 'https://img.shields.io/badge/WGSL-005A9C?style=for-the-badge&logo=w3c&logoColor=white', 'GPU, Shaders & Graphisme'),
    'metal.md': ('Metal MSL', 'https://img.shields.io/badge/Metal_MSL-000000?style=for-the-badge&logo=apple&logoColor=white', 'GPU, Shaders & Graphisme'),

    # Game Development & Engine Scripting
    'gdscript.md': ('GDScript', 'https://img.shields.io/badge/GDScript-478CBF?style=for-the-badge&logo=godotengine&logoColor=white', 'Jeux Vidéo & Moteurs 3D'),
    'unrealscript.md': ('UnrealScript', 'https://img.shields.io/badge/UnrealScript-313131?style=for-the-badge&logo=unrealengine&logoColor=white', 'Jeux Vidéo & Moteurs 3D'),
    'gml.md': ('GML', 'https://img.shields.io/badge/GML-000000?style=for-the-badge&logo=gamemaker&logoColor=white', 'Jeux Vidéo & Moteurs 3D'),
    'squirrel.md': ('Squirrel', 'https://img.shields.io/badge/Squirrel-8E44AD?style=for-the-badge&logo=cplusplus&logoColor=white', 'Jeux Vidéo & Moteurs 3D'),

    # Audio, Music & DSP
    'faust.md': ('FAUST', 'https://img.shields.io/badge/FAUST-009688?style=for-the-badge&logo=audacity&logoColor=white', 'Audio, Musique & DSP Temps Réel'),
    'supercollider.md': ('SuperCollider', 'https://img.shields.io/badge/SuperCollider-121212?style=for-the-badge&logo=musicbrainz&logoColor=white', 'Audio, Musique & DSP Temps Réel'),
    'pure-data.md': ('Pure Data', 'https://img.shields.io/badge/Pure_Data-00457C?style=for-the-badge&logo=soundcharts&logoColor=white', 'Audio, Musique & DSP Temps Réel'),
    'chuck.md': ('ChucK', 'https://img.shields.io/badge/ChucK-2C3E50?style=for-the-badge&logo=stanford&logoColor=white', 'Audio, Musique & DSP Temps Réel'),
    'csound.md': ('Csound', 'https://img.shields.io/badge/Csound-2D3748?style=for-the-badge&logo=itunes&logoColor=white', 'Audio, Musique & DSP Temps Réel'),

    # Query & Graph
    'graphql.md': ('GraphQL', 'https://img.shields.io/badge/GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white', 'Requêtes de Données, Graphes & Schémas'),
    'sparql.md': ('SPARQL', 'https://img.shields.io/badge/SPARQL-005A9C?style=for-the-badge&logo=w3c&logoColor=white', 'Requêtes de Données, Graphes & Schémas'),
    'cypher.md': ('Cypher', 'https://img.shields.io/badge/Cypher-008CC1?style=for-the-badge&logo=neo4j&logoColor=white', 'Requêtes de Données, Graphes & Schémas'),
    'xquery.md': ('XQuery', 'https://img.shields.io/badge/XQuery-E44D26?style=for-the-badge&logo=w3c&logoColor=white', 'Requêtes de Données, Graphes & Schémas'),
    'xpath.md': ('XPath', 'https://img.shields.io/badge/XPath-005A9C?style=for-the-badge&logo=w3c&logoColor=white', 'Requêtes de Données, Graphes & Schémas'),
    'kql.md': ('KQL', 'https://img.shields.io/badge/KQL_Kusto-0089D6?style=for-the-badge&logo=microsoftazure&logoColor=white', 'Requêtes de Données, Graphes & Schémas'),
    'prql.md': ('PRQL', 'https://img.shields.io/badge/PRQL-F15A24?style=for-the-badge&logo=postgresql&logoColor=white', 'Requêtes de Données, Graphes & Schémas'),

    # Shells & Unix Stream
    'bash.md': ('Bash', 'https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white', 'Shells & Outils de Flux Unix'),
    'zsh.md': ('Zsh', 'https://img.shields.io/badge/Zsh-F1502F?style=for-the-badge&logo=zsh&logoColor=white', 'Shells & Outils de Flux Unix'),
    'fish.md': ('Fish', 'https://img.shields.io/badge/Fish_Shell-38BDF8?style=for-the-badge&logo=fishshell&logoColor=white', 'Shells & Outils de Flux Unix'),
    'powershell.md': ('PowerShell', 'https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white', 'Shells & Outils de Flux Unix'),
    'ksh.md': ('Ksh', 'https://img.shields.io/badge/KornShell-000000?style=for-the-badge&logo=gnubash&logoColor=white', 'Shells & Outils de Flux Unix'),
    'tcsh.md': ('Tcsh', 'https://img.shields.io/badge/Tcsh-2B2B2B?style=for-the-badge&logo=freebsd&logoColor=white', 'Shells & Outils de Flux Unix'),
    'awk.md': ('AWK', 'https://img.shields.io/badge/AWK-1A1A1A?style=for-the-badge&logo=gnubash&logoColor=white', 'Shells & Outils de Flux Unix'),
    'sed.md': ('Sed', 'https://img.shields.io/badge/Sed-2C3E50?style=for-the-badge&logo=gnubash&logoColor=white', 'Shells & Outils de Flux Unix'),

    # Formal Specification
    'tla-plus.md': ('TLA+', 'https://img.shields.io/badge/TLA+-FF9900?style=for-the-badge&logo=amazonwebservices&logoColor=white', 'Spécification Formelle & Modélisation'),
    'alloy.md': ('Alloy', 'https://img.shields.io/badge/Alloy-1F2937?style=for-the-badge&logo=mit&logoColor=white', 'Spécification Formelle & Modélisation'),
    'datalog.md': ('Datalog', 'https://img.shields.io/badge/Datalog-181717?style=for-the-badge&logo=github&logoColor=white', 'Spécification Formelle & Modélisation'),
    'promela.md': ('Promela', 'https://img.shields.io/badge/Promela_SPIN-0B3D91?style=for-the-badge&logo=nasa&logoColor=white', 'Spécification Formelle & Modélisation'),

    # Functional & Declarative
    'haskell.md': ('Haskell', 'https://img.shields.io/badge/Haskell-5D4F85?style=for-the-badge&logo=haskell&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'ocaml.md': ('OCaml', 'https://img.shields.io/badge/OCaml-EC6813?style=for-the-badge&logo=ocaml&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'standard-ml.md': ('Standard ML', 'https://img.shields.io/badge/Standard_ML-4B32C3?style=for-the-badge&logo=edx&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'alice-ml.md': ('Alice ML', 'https://img.shields.io/badge/Alice_ML-4B32C3?style=for-the-badge&logo=edx&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'elixir.md': ('Elixir', 'https://img.shields.io/badge/Elixir-4B275F?style=for-the-badge&logo=elixir&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'erlang.md': ('Erlang', 'https://img.shields.io/badge/Erlang-A90533?style=for-the-badge&logo=erlang&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'clojure.md': ('Clojure', 'https://img.shields.io/badge/Clojure-5881D8?style=for-the-badge&logo=clojure&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'common-lisp.md': ('Common Lisp', 'https://img.shields.io/badge/Common_Lisp-000000?style=for-the-badge&logo=lisp&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'scheme.md': ('Scheme', 'https://img.shields.io/badge/Scheme-7D7D7D?style=for-the-badge&logo=scheme&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'racket.md': ('Racket', 'https://img.shields.io/badge/Racket-3C5CAA?style=for-the-badge&logo=racket&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'janet.md': ('Janet', 'https://img.shields.io/badge/Janet-AA2233?style=for-the-badge&logo=lisp&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'fennel.md': ('Fennel', 'https://img.shields.io/badge/Fennel-2C2D72?style=for-the-badge&logo=lua&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'hy.md': ('Hy', 'https://img.shields.io/badge/Hy-3776AB?style=for-the-badge&logo=python&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'shen.md': ('Shen', 'https://img.shields.io/badge/Shen-2C3E50?style=for-the-badge&logo=lisp&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'carp.md': ('Carp', 'https://img.shields.io/badge/Carp-663399?style=for-the-badge&logo=rust&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'fsharp.md': ('F#', 'https://img.shields.io/badge/F%23-378BBA?style=for-the-badge&logo=fsharp&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'elm.md': ('Elm', 'https://img.shields.io/badge/Elm-1293D8?style=for-the-badge&logo=elm&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'purescript.md': ('PureScript', 'https://img.shields.io/badge/PureScript-1D222D?style=for-the-badge&logo=purescript&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'gleam.md': ('Gleam', 'https://img.shields.io/badge/Gleam-FFAFF3?style=for-the-badge&logo=gleam&logoColor=black', 'Langages Fonctionnels & Déclaratifs'),
    'crystal.md': ('Crystal', 'https://img.shields.io/badge/Crystal-000000?style=for-the-badge&logo=crystal&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'unison.md': ('Unison', 'https://img.shields.io/badge/Unison-5C4EE5?style=for-the-badge&logo=unison&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'flix.md': ('Flix', 'https://img.shields.io/badge/Flix-E53935?style=for-the-badge&logo=java&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'chapel.md': ('Chapel', 'https://img.shields.io/badge/Chapel-009999?style=for-the-badge&logo=hpe&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),
    'pony.md': ('Pony', 'https://img.shields.io/badge/Pony-1B1F23?style=for-the-badge&logo=pony&logoColor=white', 'Langages Fonctionnels & Déclaratifs'),

    # Scientific & Data
    'r.md': ('R', 'https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white', 'Langages Scientifiques & Données'),
    'julia.md': ('Julia', 'https://img.shields.io/badge/Julia-9558B2?style=for-the-badge&logo=julia&logoColor=white', 'Langages Scientifiques & Données'),
    'matlab.md': ('MATLAB', 'https://img.shields.io/badge/MATLAB-0076A8?style=for-the-badge&logo=mathworks&logoColor=white', 'Langages Scientifiques & Données'),
    'scilab.md': ('Scilab', 'https://img.shields.io/badge/Scilab-005696?style=for-the-badge&logo=scilab&logoColor=white', 'Langages Scientifiques & Données'),
    'octave.md': ('GNU Octave', 'https://img.shields.io/badge/GNU_Octave-0790BA?style=for-the-badge&logo=gnubash&logoColor=white', 'Langages Scientifiques & Données'),
    'sas.md': ('SAS', 'https://img.shields.io/badge/SAS-0077C8?style=for-the-badge&logo=sas&logoColor=white', 'Langages Scientifiques & Données'),
    'wolfram.md': ('Wolfram', 'https://img.shields.io/badge/Wolfram-DD1100?style=for-the-badge&logo=wolfram&logoColor=white', 'Langages Scientifiques & Données'),
    'apl.md': ('APL', 'https://img.shields.io/badge/APL-00609C?style=for-the-badge&logo=dyalog&logoColor=white', 'Langages Scientifiques & Données'),
    'j.md': ('J', 'https://img.shields.io/badge/J-004B87?style=for-the-badge&logo=j&logoColor=white', 'Langages Scientifiques & Données'),
    'k.md': ('K', 'https://img.shields.io/badge/K_Kx-003366?style=for-the-badge&logo=kx&logoColor=white', 'Langages Scientifiques & Données'),
    'q.md': ('Q', 'https://img.shields.io/badge/Q_kdb+-00558F?style=for-the-badge&logo=kx&logoColor=white', 'Langages Scientifiques & Données'),
    'bqn.md': ('BQN', 'https://img.shields.io/badge/BQN-2E3440?style=for-the-badge&logo=matrix&logoColor=white', 'Langages Scientifiques & Données'),
    'labview.md': ('LabVIEW', 'https://img.shields.io/badge/LabVIEW-FFD100?style=for-the-badge&logo=nationalinstruments&logoColor=black', 'Langages Scientifiques & Données'),

    # Logic & Formal
    'prolog.md': ('Prolog', 'https://img.shields.io/badge/Prolog-E44D26?style=for-the-badge&logo=prolog&logoColor=white', 'Langages Logiques & Formels'),
    'mercury.md': ('Mercury', 'https://img.shields.io/badge/Mercury-E44D26?style=for-the-badge&logo=prolog&logoColor=white', 'Langages Logiques & Formels'),
    'curry.md': ('Curry', 'https://img.shields.io/badge/Curry-5D4F85?style=for-the-badge&logo=haskell&logoColor=white', 'Langages Logiques & Formels'),
    'lean.md': ('Lean', 'https://img.shields.io/badge/Lean-2B2B2B?style=for-the-badge&logo=lean&logoColor=white', 'Langages Logiques & Formels'),
    'coq.md': ('Coq', 'https://img.shields.io/badge/Coq-C73B28?style=for-the-badge&logo=inria&logoColor=white', 'Langages Logiques & Formels'),
    'agda.md': ('Agda', 'https://img.shields.io/badge/Agda-293241?style=for-the-badge&logo=haskell&logoColor=white', 'Langages Logiques & Formels'),
    'idris.md': ('Idris', 'https://img.shields.io/badge/Idris-9400D3?style=for-the-badge&logo=idris&logoColor=white', 'Langages Logiques & Formels'),

    # Smart Contracts & Web3
    'solidity.md': ('Solidity', 'https://img.shields.io/badge/Solidity-363636?style=for-the-badge&logo=solidity&logoColor=white', 'Smart Contracts & Web3'),
    'vyper.md': ('Vyper', 'https://img.shields.io/badge/Vyper-333333?style=for-the-badge&logo=ethereum&logoColor=white', 'Smart Contracts & Web3'),
    'move.md': ('Move', 'https://img.shields.io/badge/Move-0081FB?style=for-the-badge&logo=meta&logoColor=white', 'Smart Contracts & Web3'),
    'cairo.md': ('Cairo', 'https://img.shields.io/badge/Cairo-EB5E28?style=for-the-badge&logo=ethereum&logoColor=white', 'Smart Contracts & Web3'),
    'clarity.md': ('Clarity', 'https://img.shields.io/badge/Clarity-5546FF?style=for-the-badge&logo=bitcoin&logoColor=white', 'Smart Contracts & Web3'),
    'sway.md': ('Sway', 'https://img.shields.io/badge/Sway-00F58C?style=for-the-badge&logo=fuel&logoColor=black', 'Smart Contracts & Web3'),
    'cadence.md': ('Cadence', 'https://img.shields.io/badge/Cadence-00EF8B?style=for-the-badge&logo=flow&logoColor=black', 'Smart Contracts & Web3'),
    'plutus.md': ('Plutus', 'https://img.shields.io/badge/Plutus-0033AD?style=for-the-badge&logo=cardano&logoColor=white', 'Smart Contracts & Web3'),
    'michelson.md': ('Michelson', 'https://img.shields.io/badge/Michelson-2C7DF7?style=for-the-badge&logo=tezos&logoColor=white', 'Smart Contracts & Web3'),
    'scilla.md': ('Scilla', 'https://img.shields.io/badge/Scilla-29CCC4?style=for-the-badge&logo=zilliqa&logoColor=black', 'Smart Contracts & Web3'),
    'foundry.md': ('Foundry', 'https://img.shields.io/badge/Foundry-1C1E24?style=for-the-badge&logo=ethereum&logoColor=white', 'Smart Contracts & Web3'),
    'viem.md': ('Viem', 'https://img.shields.io/badge/Viem-1E1E1E?style=for-the-badge&logo=ethereum&logoColor=white', 'Smart Contracts & Web3'),

    # Hardware & Open Hardware
    'vhdl.md': ('VHDL', 'https://img.shields.io/badge/VHDL-00629B?style=for-the-badge&logo=ieee&logoColor=white', 'Description Matérielle & Open Hardware'),
    'verilog.md': ('Verilog', 'https://img.shields.io/badge/Verilog-00629B?style=for-the-badge&logo=ieee&logoColor=white', 'Description Matérielle & Open Hardware'),
    'systemverilog.md': ('SystemVerilog', 'https://img.shields.io/badge/SystemVerilog-00629B?style=for-the-badge&logo=ieee&logoColor=white', 'Description Matérielle & Open Hardware'),
    'chisel.md': ('Chisel', 'https://img.shields.io/badge/Chisel_HDL-DC322F?style=for-the-badge&logo=scala&logoColor=white', 'Description Matérielle & Open Hardware'),
    'bluespec.md': ('Bluespec', 'https://img.shields.io/badge/Bluespec-003366?style=for-the-badge&logo=mit&logoColor=white', 'Description Matérielle & Open Hardware'),

    # Modular & Wirth Family
    'modula-2.md': ('Modula-2', 'https://img.shields.io/badge/Modula--2-00549D?style=for-the-badge&logo=gnu&logoColor=white', 'Systèmes Modulaires & Wirth'),
    'oberon.md': ('Oberon', 'https://img.shields.io/badge/Oberon-003366?style=for-the-badge&logo=openaccess&logoColor=white', 'Systèmes Modulaires & Wirth'),

    # Esoteric & CS Theory
    'brainfuck.md': ('Brainfuck', 'https://img.shields.io/badge/Brainfuck-2B2B2B?style=for-the-badge&logo=codewars&logoColor=white', 'Ésotériques & Théorie Informatique'),
    'befunge.md': ('Befunge', 'https://img.shields.io/badge/Befunge-4B0082?style=for-the-badge&logo=gameandwatch&logoColor=white', 'Ésotériques & Théorie Informatique'),
    'whitespace.md': ('Whitespace', 'https://img.shields.io/badge/Whitespace-FFFFFF?style=for-the-badge&logo=ghost&logoColor=black', 'Ésotériques & Théorie Informatique'),
    'malbolge.md': ('Malbolge', 'https://img.shields.io/badge/Malbolge-8B0000?style=for-the-badge&logo=hackthebox&logoColor=white', 'Ésotériques & Théorie Informatique'),

    # Hybrid & Specialized
    'ballerina.md': ('Ballerina', 'https://img.shields.io/badge/Ballerina-20B6B0?style=for-the-badge&logo=ballerina&logoColor=white', 'Langages Hybrides & Spécifiques'),
    'vala.md': ('Vala', 'https://img.shields.io/badge/Vala-A56DE2?style=for-the-badge&logo=gnome&logoColor=white', 'Langages Hybrides & Spécifiques'),
    'red.md': ('Red', 'https://img.shields.io/badge/Red-DE2B26?style=for-the-badge&logo=red&logoColor=white', 'Langages Hybrides & Spécifiques'),
    'rebol.md': ('Rebol', 'https://img.shields.io/badge/Rebol-577788?style=for-the-badge&logo=amigaos&logoColor=white', 'Langages Hybrides & Spécifiques'),
    'dylan.md': ('Dylan', 'https://img.shields.io/badge/Dylan-000000?style=for-the-badge&logo=apple&logoColor=white', 'Langages Hybrides & Spécifiques'),
    'icon.md': ('Icon', 'https://img.shields.io/badge/Icon-1B365D?style=for-the-badge&logo=gnu&logoColor=white', 'Langages Hybrides & Spécifiques'),
    'ceylon.md': ('Ceylon', 'https://img.shields.io/badge/Ceylon-D9531E?style=for-the-badge&logo=eclipseide&logoColor=white', 'Langages Hybrides & Spécifiques'),
    'fantom.md': ('Fantom', 'https://img.shields.io/badge/Fantom-2B579A?style=for-the-badge&logo=java&logoColor=white', 'Langages Hybrides & Spécifiques'),
    'nemerle.md': ('Nemerle', 'https://img.shields.io/badge/Nemerle-007ACC?style=for-the-badge&logo=dotnet&logoColor=white', 'Langages Hybrides & Spécifiques'),
    'boo.md': ('Boo', 'https://img.shields.io/badge/Boo-000000?style=for-the-badge&logo=unity&logoColor=white', 'Langages Hybrides & Spécifiques'),
    'pike.md': ('Pike', 'https://img.shields.io/badge/Pike-2C3E50?style=for-the-badge&logo=cplusplus&logoColor=white', 'Langages Hybrides & Spécifiques'),
    'io.md': ('Io', 'https://img.shields.io/badge/Io-1E1E1E?style=for-the-badge&logo=ghost&logoColor=white', 'Langages Hybrides & Spécifiques'),
    'ring.md': ('Ring', 'https://img.shields.io/badge/Ring-18BC9C?style=for-the-badge&logo=c&logoColor=white', 'Langages Hybrides & Spécifiques'),
    'ur-web.md': ('Ur/Web', 'https://img.shields.io/badge/Ur_Web-1A365D?style=for-the-badge&logo=mit&logoColor=white', 'Langages Hybrides & Spécifiques'),

    # Historical & Pioneers
    'algol.md': ('ALGOL', 'https://img.shields.io/badge/ALGOL-1A1A1A?style=for-the-badge&logo=computerhistory&logoColor=white', 'Langages Historiques & Pionniers'),
    'basic.md': ('BASIC', 'https://img.shields.io/badge/BASIC-1976D2?style=for-the-badge&logo=visualstudio&logoColor=white', 'Langages Historiques & Pionniers'),
    'cobol.md': ('COBOL', 'https://img.shields.io/badge/COBOL-003C71?style=for-the-badge&logo=ibm&logoColor=white', 'Langages Historiques & Pionniers'),
    'forth.md': ('Forth', 'https://img.shields.io/badge/Forth-000000?style=for-the-badge&logo=forth&logoColor=white', 'Langages Historiques & Pionniers'),
    'logo.md': ('Logo', 'https://img.shields.io/badge/Logo-2B2B2B?style=for-the-badge&logo=mit&logoColor=white', 'Langages Historiques & Pionniers'),
    'pli.md': ('PL/I', 'https://img.shields.io/badge/PL/I-052FAD?style=for-the-badge&logo=ibm&logoColor=white', 'Langages Historiques & Pionniers'),
    'simula.md': ('Simula', 'https://img.shields.io/badge/Simula-002D62?style=for-the-badge&logo=openaccess&logoColor=white', 'Langages Historiques & Pionniers'),
    'smalltalk.md': ('Smalltalk', 'https://img.shields.io/badge/Smalltalk-57889C?style=for-the-badge&logo=smalltalk&logoColor=white', 'Langages Historiques & Pionniers'),
    'snobol.md': ('SNOBOL', 'https://img.shields.io/badge/SNOBOL-333333?style=for-the-badge&logo=bell&logoColor=white', 'Langages Historiques & Pionniers'),
    'postscript.md': ('PostScript', 'https://img.shields.io/badge/PostScript-FF0000?style=for-the-badge&logo=adobe&logoColor=white', 'Langages Historiques & Pionniers'),
    'tex.md': ('TeX LaTeX', 'https://img.shields.io/badge/TeX_LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white', 'Langages Historiques & Pionniers'),

    # Desktop Automation & Scripting
    'applescript.md': ('AppleScript', 'https://img.shields.io/badge/AppleScript-999999?style=for-the-badge&logo=apple&logoColor=white', 'Automatisation Desktop & Web Scripting'),
    'autohotkey.md': ('AutoHotkey', 'https://img.shields.io/badge/AutoHotkey-334455?style=for-the-badge&logo=autohotkey&logoColor=white', 'Automatisation Desktop & Web Scripting'),
    'vbscript.md': ('VBScript', 'https://img.shields.io/badge/VBScript-1976D2?style=for-the-badge&logo=windows&logoColor=white', 'Automatisation Desktop & Web Scripting'),
    'actionscript.md': ('ActionScript', 'https://img.shields.io/badge/ActionScript-FF0000?style=for-the-badge&logo=adobe&logoColor=white', 'Automatisation Desktop & Web Scripting'),
    'coffeescript.md': ('CoffeeScript', 'https://img.shields.io/badge/CoffeeScript-2F2625?style=for-the-badge&logo=coffeescript&logoColor=white', 'Automatisation Desktop & Web Scripting'),
    'hack.md': ('Hack', 'https://img.shields.io/badge/Hack-0081FB?style=for-the-badge&logo=meta&logoColor=white', 'Automatisation Desktop & Web Scripting'),

    # Emerging & Research
    'mojo.md': ('Mojo', 'https://img.shields.io/badge/Mojo-FF4B00?style=for-the-badge&logo=mojo&logoColor=white', 'Langages Émergents & Recherche'),
    'carbon.md': ('Carbon', 'https://img.shields.io/badge/Carbon-4285F4?style=for-the-badge&logo=google&logoColor=white', 'Langages Émergents & Recherche'),
    'koka.md': ('Koka', 'https://img.shields.io/badge/Koka-00A4EF?style=for-the-badge&logo=microsoft&logoColor=white', 'Langages Émergents & Recherche'),
    'hare.md': ('Hare', 'https://img.shields.io/badge/Hare-3B4252?style=for-the-badge&logo=hare&logoColor=white', 'Langages Émergents & Recherche'),
    'roc.md': ('Roc', 'https://img.shields.io/badge/Roc-7C3AED?style=for-the-badge&logo=roc&logoColor=white', 'Langages Émergents & Recherche'),

    # Frameworks & UI & Runtimes
    'react.md': ('React', 'https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black', 'Frameworks, Runtimes & Écosystèmes'),
    'vue.md': ('Vue.js', 'https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'svelte.md': ('Svelte', 'https://img.shields.io/badge/Svelte-FF3E00?style=for-the-badge&logo=svelte&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'flutter.md': ('Flutter', 'https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'tailwind-css.md': ('Tailwind CSS', 'https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'bootstrap.md': ('Bootstrap', 'https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'tanstack.md': ('TanStack', 'https://img.shields.io/badge/TanStack-FF4154?style=for-the-badge&logo=reactquery&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'swr.md': ('SWR', 'https://img.shields.io/badge/SWR-000000?style=for-the-badge&logo=vercel&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'tauri.md': ('Tauri', 'https://img.shields.io/badge/Tauri-24C8DB?style=for-the-badge&logo=tauri&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'actix.md': ('Actix', 'https://img.shields.io/badge/Actix-000000?style=for-the-badge&logo=actix&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'yew.md': ('Yew', 'https://img.shields.io/badge/Yew-CE412B?style=for-the-badge&logo=rust&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'dioxus.md': ('Dioxus', 'https://img.shields.io/badge/Dioxus-000000?style=for-the-badge&logo=rust&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'leptos.md': ('Leptos', 'https://img.shields.io/badge/Leptos-EF3939?style=for-the-badge&logo=rust&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'laravel.md': ('Laravel', 'https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'ruby-on-rails.md': ('Ruby on Rails', 'https://img.shields.io/badge/Ruby_on_Rails-D30001?style=for-the-badge&logo=rubyonrails&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'jinja.md': ('Jinja', 'https://img.shields.io/badge/Jinja-B41717?style=for-the-badge&logo=jinja&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'trpc.md': ('tRPC', 'https://img.shields.io/badge/tRPC-2596BE?style=for-the-badge&logo=trpc&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'vite.md': ('Vite', 'https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'babel.md': ('Babel', 'https://img.shields.io/badge/Babel-F9DC3E?style=for-the-badge&logo=babel&logoColor=black', 'Frameworks, Runtimes & Écosystèmes'),
    'node-js.md': ('Node.js', 'https://img.shields.io/badge/Node.js-5FA04E?style=for-the-badge&logo=nodedotjs&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'prisma.md': ('Prisma', 'https://img.shields.io/badge/Prisma-2D3748?style=for-the-badge&logo=prisma&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'prisma-client.md': ('Prisma Client', 'https://img.shields.io/badge/Prisma_Client-2D3748?style=for-the-badge&logo=prisma&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'prisma-migrate.md': ('Prisma Migrate', 'https://img.shields.io/badge/Prisma_Migrate-0284C7?style=for-the-badge&logo=prisma&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'prisma-studio.md': ('Prisma Studio', 'https://img.shields.io/badge/Prisma_Studio-9333EA?style=for-the-badge&logo=prisma&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
    'prisma-accelerate.md': ('Prisma Accelerate', 'https://img.shields.io/badge/Prisma_Accelerate-16A34A?style=for-the-badge&logo=prisma&logoColor=white', 'Frameworks, Runtimes & Écosystèmes'),
}

CATEGORIES_ORDER = [
    'Langages Systèmes & Bas Niveau',
    'Langages Applicatifs & Entreprise',
    'Entreprise, ERP & 4GL Métier',
    'Langages Web & Scripting Dynamique',
    'GPU, Shaders & Graphisme',
    'Jeux Vidéo & Moteurs 3D',
    'Audio, Musique & DSP Temps Réel',
    'Requêtes de Données, Graphes & Schémas',
    'Shells & Outils de Flux Unix',
    'Spécification Formelle & Modélisation',
    'Langages Fonctionnels & Déclaratifs',
    'Langages Scientifiques & Données',
    'Langages Logiques & Formels',
    'Smart Contracts & Web3',
    'Description Matérielle & Open Hardware',
    'Systèmes Modulaires & Wirth',
    'Langages Hybrides & Spécifiques',
    'Langages Historiques & Pionniers',
    'Automatisation Desktop & Web Scripting',
    'Ésotériques & Théorie Informatique',
    'Langages Émergents & Recherche',
    'Frameworks, Runtimes & Écosystèmes',
    'Autres Fiches'
]

def run():
    base_dir = '/home/dev_redious/Documents/Dev/docs-languages'
    lang_dir = os.path.join(base_dir, 'languages')
    all_files = sorted(os.listdir(lang_dir))

    cats = {cat: [] for cat in CATEGORIES_ORDER}

    total_count = 0
    for f in all_files:
        if not f.endswith('.md'):
            continue
        total_count += 1
        meta = BADGE_META.get(f)
        if meta:
            name, badge_url, cat = meta
            if cat in cats:
                cats[cat].append((name, badge_url, f))
            else:
                cats['Autres Fiches'].append((name, badge_url, f))
        else:
            clean_name = f.replace('.md', '').replace('-', ' ').title()
            badge_url = f'https://img.shields.io/badge/{clean_name.replace(" ", "_")}-000000?style=for-the-badge'
            cats['Autres Fiches'].append((clean_name, badge_url, f))

    sections = []
    for cat_name in CATEGORIES_ORDER:
        items = cats[cat_name]
        if not items:
            continue
        items.sort(key=lambda x: x[0].lower())
        badges_str = ' '.join([f'[![{name}]({badge})](languages/{fname})' for name, badge, fname in items])
        sections.append(f'### {cat_name} ({len(items)})\n\n{badges_str}\n')

    readme_content = f'''<div align="center">
  <img src="assets/logo.png" alt="docs-languages logo" width="200">

  <p align="center">
    <img src="https://img.shields.io/badge/Format-Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white" alt="Markdown" />
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="MIT" /></a>
    <img src="https://img.shields.io/badge/Fiches-{total_count}-38BDF8?style=for-the-badge" alt="{total_count} fiches" />
  </p>
  <p align="center">
    <i>Bibliothèque universelle de documentations synthétiques et standardisées sur l'histoire et l'utilité des langages de programmation.</i><br>
    Dépôt <a href="https://github.com/DevRedious/docs-languages">DevRedious/docs-languages</a>
  </p>
</div>

---

## Structure du projet

Chaque documentation de langage respecte un format strict et concis, découpé en trois sections :

1. **Histoire** : 5 repères chronologiques clés (création, évolutions, standardisation, maturité, état actuel).
2. **Utilité** : 5 points synthétiques sur la nature, le rôle, les forces techniques, les cas d'usage et l'écosystème.
3. **Ressources** : Lien officiel de référence.

## Bibliothèque des langages ({total_count} fiches)

Cliquez sur le logo d'un langage pour ouvrir directement sa fiche documentaire :

''' + '\n'.join(sections) + '''
## Modèle

Pour ajouter ou proposer une nouvelle fiche, suivez le format défini dans [TEMPLATE.md](TEMPLATE.md).
'''

    with open(os.path.join(base_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f'README.md mis à jour avec {total_count} badges classés par catégorie.')

if __name__ == '__main__':
    run()
