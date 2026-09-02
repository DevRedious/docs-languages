import os
import re

# Comprehensive metadata mapping for badges
BADGE_META = {
    # Systems & Low-level
    'c.md': ('C', 'https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black', 'Systèmes & Bas Niveau'),
    'cpp.md': ('C++', 'https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white', 'Systèmes & Bas Niveau'),
    'rust.md': ('Rust', 'https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white', 'Systèmes & Bas Niveau'),
    'zig.md': ('Zig', 'https://img.shields.io/badge/Zig-F7A41D?style=for-the-badge&logo=zig&logoColor=black', 'Systèmes & Bas Niveau'),
    'nim.md': ('Nim', 'https://img.shields.io/badge/Nim-FFE953?style=for-the-badge&logo=nim&logoColor=black', 'Systèmes & Bas Niveau'),
    'd.md': ('D', 'https://img.shields.io/badge/D-B03931?style=for-the-badge&logo=d&logoColor=white', 'Systèmes & Bas Niveau'),
    'assembly.md': ('Assembly', 'https://img.shields.io/badge/Assembly-6E4C13?style=for-the-badge&logo=assemblyscript&logoColor=white', 'Systèmes & Bas Niveau'),
    'fortran.md': ('Fortran', 'https://img.shields.io/badge/Fortran-734F96?style=for-the-badge&logo=fortran&logoColor=white', 'Systèmes & Bas Niveau'),
    'ada.md': ('Ada', 'https://img.shields.io/badge/Ada-02F0C2?style=for-the-badge&logo=ada&logoColor=black', 'Systèmes & Bas Niveau'),
    'pascal.md': ('Pascal', 'https://img.shields.io/badge/Pascal-00549D?style=for-the-badge&logo=delphi&logoColor=white', 'Systèmes & Bas Niveau'),
    'odin.md': ('Odin', 'https://img.shields.io/badge/Odin-1A2B3C?style=for-the-badge&logo=odin&logoColor=white', 'Systèmes & Bas Niveau'),
    'v.md': ('V', 'https://img.shields.io/badge/V-4F80AA?style=for-the-badge&logo=v&logoColor=white', 'Systèmes & Bas Niveau'),

    # Enterprise & OOP
    'java.md': ('Java', 'https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=java&logoColor=white', 'Applicatifs & Entreprise'),
    'csharp.md': ('C#', 'https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=csharp&logoColor=white', 'Applicatifs & Entreprise'),
    'kotlin.md': ('Kotlin', 'https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white', 'Applicatifs & Entreprise'),
    'scala.md': ('Scala', 'https://img.shields.io/badge/Scala-DC322F?style=for-the-badge&logo=scala&logoColor=white', 'Applicatifs & Entreprise'),
    'groovy.md': ('Groovy', 'https://img.shields.io/badge/Groovy-4298B8?style=for-the-badge&logo=apachegroovy&logoColor=white', 'Applicatifs & Entreprise'),
    'swift.md': ('Swift', 'https://img.shields.io/badge/Swift-F05138?style=for-the-badge&logo=swift&logoColor=white', 'Applicatifs & Entreprise'),
    'objective-c.md': ('Objective-C', 'https://img.shields.io/badge/Objective--C-000000?style=for-the-badge&logo=apple&logoColor=white', 'Applicatifs & Entreprise'),
    'dart.md': ('Dart', 'https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white', 'Applicatifs & Entreprise'),
    'go.md': ('Go', 'https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white', 'Applicatifs & Entreprise'),

    # Web & Dynamic Scripting
    'html.md': ('HTML5', 'https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white', 'Web & Scripting'),
    'css.md': ('CSS3', 'https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white', 'Web & Scripting'),
    'javascript.md': ('JavaScript', 'https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black', 'Web & Scripting'),
    'typescript.md': ('TypeScript', 'https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white', 'Web & Scripting'),
    'python.md': ('Python', 'https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white', 'Web & Scripting'),
    'ruby.md': ('Ruby', 'https://img.shields.io/badge/Ruby-CC342D?style=for-the-badge&logo=ruby&logoColor=white', 'Web & Scripting'),
    'php.md': ('PHP', 'https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white', 'Web & Scripting'),
    'perl.md': ('Perl', 'https://img.shields.io/badge/Perl-39457E?style=for-the-badge&logo=perl&logoColor=white', 'Web & Scripting'),
    'lua.md': ('Lua', 'https://img.shields.io/badge/Lua-2C2D72?style=for-the-badge&logo=lua&logoColor=white', 'Web & Scripting'),
    'tcl.md': ('Tcl', 'https://img.shields.io/badge/Tcl-145B94?style=for-the-badge&logo=tcl&logoColor=white', 'Web & Scripting'),
    'bash.md': ('Bash', 'https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white', 'Web & Scripting'),
    'powershell.md': ('PowerShell', 'https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white', 'Web & Scripting'),
    'sql.md': ('SQL', 'https://img.shields.io/badge/SQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white', 'Web & Scripting'),
    'webassembly.md': ('WebAssembly', 'https://img.shields.io/badge/WebAssembly-654FF0?style=for-the-badge&logo=webassembly&logoColor=white', 'Web & Scripting'),
    'xojo.md': ('Xojo', 'https://img.shields.io/badge/Xojo-8CC63F?style=for-the-badge&logo=visualstudio&logoColor=black', 'Web & Scripting'),

    # Functional & Declarative
    'haskell.md': ('Haskell', 'https://img.shields.io/badge/Haskell-5D4F85?style=for-the-badge&logo=haskell&logoColor=white', 'Fonctionnels & Déclaratifs'),
    'ocaml.md': ('OCaml', 'https://img.shields.io/badge/OCaml-EC6813?style=for-the-badge&logo=ocaml&logoColor=white', 'Fonctionnels & Déclaratifs'),
    'elixir.md': ('Elixir', 'https://img.shields.io/badge/Elixir-4B275F?style=for-the-badge&logo=elixir&logoColor=white', 'Fonctionnels & Déclaratifs'),
    'erlang.md': ('Erlang', 'https://img.shields.io/badge/Erlang-A90533?style=for-the-badge&logo=erlang&logoColor=white', 'Fonctionnels & Déclaratifs'),
    'clojure.md': ('Clojure', 'https://img.shields.io/badge/Clojure-5881D8?style=for-the-badge&logo=clojure&logoColor=white', 'Fonctionnels & Déclaratifs'),
    'common-lisp.md': ('Common Lisp', 'https://img.shields.io/badge/Common_Lisp-000000?style=for-the-badge&logo=lisp&logoColor=white', 'Fonctionnels & Déclaratifs'),
    'scheme.md': ('Scheme', 'https://img.shields.io/badge/Scheme-7D7D7D?style=for-the-badge&logo=scheme&logoColor=white', 'Fonctionnels & Déclaratifs'),
    'racket.md': ('Racket', 'https://img.shields.io/badge/Racket-3C5CAA?style=for-the-badge&logo=racket&logoColor=white', 'Fonctionnels & Déclaratifs'),
    'fsharp.md': ('F#', 'https://img.shields.io/badge/F%23-378BBA?style=for-the-badge&logo=fsharp&logoColor=white', 'Fonctionnels & Déclaratifs'),
    'elm.md': ('Elm', 'https://img.shields.io/badge/Elm-1293D8?style=for-the-badge&logo=elm&logoColor=white', 'Fonctionnels & Déclaratifs'),
    'purescript.md': ('PureScript', 'https://img.shields.io/badge/PureScript-1D222D?style=for-the-badge&logo=purescript&logoColor=white', 'Fonctionnels & Déclaratifs'),
    'gleam.md': ('Gleam', 'https://img.shields.io/badge/Gleam-FFAFF3?style=for-the-badge&logo=gleam&logoColor=black', 'Fonctionnels & Déclaratifs'),
    'crystal.md': ('Crystal', 'https://img.shields.io/badge/Crystal-000000?style=for-the-badge&logo=crystal&logoColor=white', 'Fonctionnels & Déclaratifs'),

    # Scientific & Data
    'r.md': ('R', 'https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white', 'Scientifiques & Données'),
    'julia.md': ('Julia', 'https://img.shields.io/badge/Julia-9558B2?style=for-the-badge&logo=julia&logoColor=white', 'Scientifiques & Données'),
    'matlab.md': ('MATLAB', 'https://img.shields.io/badge/MATLAB-0076A8?style=for-the-badge&logo=mathworks&logoColor=white', 'Scientifiques & Données'),
    'sas.md': ('SAS', 'https://img.shields.io/badge/SAS-0077C8?style=for-the-badge&logo=sas&logoColor=white', 'Scientifiques & Données'),
    'wolfram.md': ('Wolfram', 'https://img.shields.io/badge/Wolfram-DD1100?style=for-the-badge&logo=wolfram&logoColor=white', 'Scientifiques & Données'),
    'apl.md': ('APL', 'https://img.shields.io/badge/APL-00609C?style=for-the-badge&logo=dyalog&logoColor=white', 'Scientifiques & Données'),

    # Logic & Formal
    'prolog.md': ('Prolog', 'https://img.shields.io/badge/Prolog-E44D26?style=for-the-badge&logo=prolog&logoColor=white', 'Logiques & Preuves'),
    'lean.md': ('Lean', 'https://img.shields.io/badge/Lean-2B2B2B?style=for-the-badge&logo=lean&logoColor=white', 'Logiques & Preuves'),
    'coq.md': ('Coq', 'https://img.shields.io/badge/Coq-C73B28?style=for-the-badge&logo=inria&logoColor=white', 'Logiques & Preuves'),
    'agda.md': ('Agda', 'https://img.shields.io/badge/Agda-293241?style=for-the-badge&logo=haskell&logoColor=white', 'Logiques & Preuves'),
    'idris.md': ('Idris', 'https://img.shields.io/badge/Idris-9400D3?style=for-the-badge&logo=idris&logoColor=white', 'Logiques & Preuves'),

    # Smart Contracts & Web3
    'solidity.md': ('Solidity', 'https://img.shields.io/badge/Solidity-363636?style=for-the-badge&logo=solidity&logoColor=white', 'Smart Contracts & Web3'),
    'vyper.md': ('Vyper', 'https://img.shields.io/badge/Vyper-333333?style=for-the-badge&logo=ethereum&logoColor=white', 'Smart Contracts & Web3'),
    'move.md': ('Move', 'https://img.shields.io/badge/Move-0081FB?style=for-the-badge&logo=meta&logoColor=white', 'Smart Contracts & Web3'),
    'cairo.md': ('Cairo', 'https://img.shields.io/badge/Cairo-EB5E28?style=for-the-badge&logo=ethereum&logoColor=white', 'Smart Contracts & Web3'),
    'clarity.md': ('Clarity', 'https://img.shields.io/badge/Clarity-5546FF?style=for-the-badge&logo=bitcoin&logoColor=white', 'Smart Contracts & Web3'),
    'sway.md': ('Sway', 'https://img.shields.io/badge/Sway-00F58C?style=for-the-badge&logo=fuel&logoColor=black', 'Smart Contracts & Web3'),
    'foundry.md': ('Foundry', 'https://img.shields.io/badge/Foundry-1C1E24?style=for-the-badge&logo=ethereum&logoColor=white', 'Smart Contracts & Web3'),
    'viem.md': ('Viem', 'https://img.shields.io/badge/Viem-1E1E1E?style=for-the-badge&logo=ethereum&logoColor=white', 'Smart Contracts & Web3'),

    # Historical & Pioneers
    'cobol.md': ('COBOL', 'https://img.shields.io/badge/COBOL-003C71?style=for-the-badge&logo=ibm&logoColor=white', 'Historiques & Pionniers'),
    'algol.md': ('ALGOL', 'https://img.shields.io/badge/ALGOL-1A1A1A?style=for-the-badge&logo=computerhistory&logoColor=white', 'Historiques & Pionniers'),
    'basic.md': ('BASIC', 'https://img.shields.io/badge/BASIC-1976D2?style=for-the-badge&logo=visualstudio&logoColor=white', 'Historiques & Pionniers'),
    'smalltalk.md': ('Smalltalk', 'https://img.shields.io/badge/Smalltalk-57889C?style=for-the-badge&logo=smalltalk&logoColor=white', 'Historiques & Pionniers'),
    'simula.md': ('Simula', 'https://img.shields.io/badge/Simula-002D62?style=for-the-badge&logo=openaccess&logoColor=white', 'Historiques & Pionniers'),
    'logo.md': ('Logo', 'https://img.shields.io/badge/Logo-2B2B2B?style=for-the-badge&logo=mit&logoColor=white', 'Historiques & Pionniers'),
    'forth.md': ('Forth', 'https://img.shields.io/badge/Forth-000000?style=for-the-badge&logo=forth&logoColor=white', 'Historiques & Pionniers'),
    'pli.md': ('PL/I', 'https://img.shields.io/badge/PL/I-052FAD?style=for-the-badge&logo=ibm&logoColor=white', 'Historiques & Pionniers'),

    # Hardware Description
    'vhdl.md': ('VHDL', 'https://img.shields.io/badge/VHDL-00629B?style=for-the-badge&logo=ieee&logoColor=white', 'Description Matérielle'),
    'verilog.md': ('Verilog', 'https://img.shields.io/badge/Verilog-00629B?style=for-the-badge&logo=ieee&logoColor=white', 'Description Matérielle'),
    'systemverilog.md': ('SystemVerilog', 'https://img.shields.io/badge/SystemVerilog-00629B?style=for-the-badge&logo=ieee&logoColor=white', 'Description Matérielle'),

    # Emerging & Research
    'mojo.md': ('Mojo', 'https://img.shields.io/badge/Mojo-FF4B00?style=for-the-badge&logo=mojo&logoColor=white', 'Émergents & Recherche'),
    'carbon.md': ('Carbon', 'https://img.shields.io/badge/Carbon-4285F4?style=for-the-badge&logo=google&logoColor=white', 'Émergents & Recherche'),
    'koka.md': ('Koka', 'https://img.shields.io/badge/Koka-00A4EF?style=for-the-badge&logo=microsoft&logoColor=white', 'Émergents & Recherche'),
    'hare.md': ('Hare', 'https://img.shields.io/badge/Hare-3B4252?style=for-the-badge&logo=hare&logoColor=white', 'Émergents & Recherche'),
    'roc.md': ('Roc', 'https://img.shields.io/badge/Roc-7C3AED?style=for-the-badge&logo=roc&logoColor=white', 'Émergents & Recherche'),

    # Frameworks & UI & Runtimes
    'react.md': ('React', 'https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black', 'Frameworks & Runtimes'),
    'vue.md': ('Vue.js', 'https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white', 'Frameworks & Runtimes'),
    'svelte.md': ('Svelte', 'https://img.shields.io/badge/Svelte-FF3E00?style=for-the-badge&logo=svelte&logoColor=white', 'Frameworks & Runtimes'),
    'flutter.md': ('Flutter', 'https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white', 'Frameworks & Runtimes'),
    'tailwind-css.md': ('Tailwind CSS', 'https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white', 'Frameworks & Runtimes'),
    'bootstrap.md': ('Bootstrap', 'https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white', 'Frameworks & Runtimes'),
    'tanstack.md': ('TanStack', 'https://img.shields.io/badge/TanStack-FF4154?style=for-the-badge&logo=reactquery&logoColor=white', 'Frameworks & Runtimes'),
    'swr.md': ('SWR', 'https://img.shields.io/badge/SWR-000000?style=for-the-badge&logo=vercel&logoColor=white', 'Frameworks & Runtimes'),
    'tauri.md': ('Tauri', 'https://img.shields.io/badge/Tauri-24C8DB?style=for-the-badge&logo=tauri&logoColor=white', 'Frameworks & Runtimes'),
    'actix.md': ('Actix', 'https://img.shields.io/badge/Actix-000000?style=for-the-badge&logo=actix&logoColor=white', 'Frameworks & Runtimes'),
    'yew.md': ('Yew', 'https://img.shields.io/badge/Yew-CE412B?style=for-the-badge&logo=rust&logoColor=white', 'Frameworks & Runtimes'),
    'dioxus.md': ('Dioxus', 'https://img.shields.io/badge/Dioxus-000000?style=for-the-badge&logo=rust&logoColor=white', 'Frameworks & Runtimes'),
    'leptos.md': ('Leptos', 'https://img.shields.io/badge/Leptos-EF3939?style=for-the-badge&logo=rust&logoColor=white', 'Frameworks & Runtimes'),
    'laravel.md': ('Laravel', 'https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white', 'Frameworks & Runtimes'),
    'ruby-on-rails.md': ('Ruby on Rails', 'https://img.shields.io/badge/Ruby_on_Rails-D30001?style=for-the-badge&logo=rubyonrails&logoColor=white', 'Frameworks & Runtimes'),
    'jinja.md': ('Jinja', 'https://img.shields.io/badge/Jinja-B41717?style=for-the-badge&logo=jinja&logoColor=white', 'Frameworks & Runtimes'),
    'trpc.md': ('tRPC', 'https://img.shields.io/badge/tRPC-2596BE?style=for-the-badge&logo=trpc&logoColor=white', 'Frameworks & Runtimes'),
    'vite.md': ('Vite', 'https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white', 'Frameworks & Runtimes'),
    'babel.md': ('Babel', 'https://img.shields.io/badge/Babel-F9DC3E?style=for-the-badge&logo=babel&logoColor=black', 'Frameworks & Runtimes'),
    'node-js.md': ('Node.js', 'https://img.shields.io/badge/Node.js-5FA04E?style=for-the-badge&logo=nodedotjs&logoColor=white', 'Frameworks & Runtimes'),
    'prisma.md': ('Prisma', 'https://img.shields.io/badge/Prisma-2D3748?style=for-the-badge&logo=prisma&logoColor=white', 'Frameworks & Runtimes'),
    'prisma-client.md': ('Prisma Client', 'https://img.shields.io/badge/Prisma_Client-2D3748?style=for-the-badge&logo=prisma&logoColor=white', 'Frameworks & Runtimes'),
    'prisma-migrate.md': ('Prisma Migrate', 'https://img.shields.io/badge/Prisma_Migrate-0284C7?style=for-the-badge&logo=prisma&logoColor=white', 'Frameworks & Runtimes'),
    'prisma-studio.md': ('Prisma Studio', 'https://img.shields.io/badge/Prisma_Studio-9333EA?style=for-the-badge&logo=prisma&logoColor=white', 'Frameworks & Runtimes'),
    'prisma-accelerate.md': ('Prisma Accelerate', 'https://img.shields.io/badge/Prisma_Accelerate-16A34A?style=for-the-badge&logo=prisma&logoColor=white', 'Frameworks & Runtimes'),
}

def run():
    base_dir = '/home/dev_redious/Documents/Dev/docs-languages'
    lang_dir = os.path.join(base_dir, 'languages')
    all_files = sorted(os.listdir(lang_dir))

    cats = {
        'Langages Systèmes & Bas Niveau': [],
        'Langages Applicatifs & Entreprise': [],
        'Langages Web & Scripting Dynamique': [],
        'Langages Fonctionnels & Déclaratifs': [],
        'Langages Scientifiques & Données': [],
        'Langages Logiques & Formels': [],
        'Smart Contracts & Web3': [],
        'Langages Historiques & Pionniers': [],
        'Description Matérielle': [],
        'Langages Émergents & Recherche': [],
        'Frameworks, Runtimes & Écosystèmes': [],
        'Autres Fiches': []
    }

    total_count = 0
    for f in all_files:
        if not f.endswith('.md'):
            continue
        total_count += 1
        meta = BADGE_META.get(f)
        if meta:
            name, badge_url, cat = meta
            if cat in ['Systèmes & Bas Niveau']:
                cats['Langages Systèmes & Bas Niveau'].append((name, badge_url, f))
            elif cat in ['Applicatifs & Entreprise']:
                cats['Langages Applicatifs & Entreprise'].append((name, badge_url, f))
            elif cat in ['Web & Scripting']:
                cats['Langages Web & Scripting Dynamique'].append((name, badge_url, f))
            elif cat in ['Fonctionnels & Déclaratifs']:
                cats['Langages Fonctionnels & Déclaratifs'].append((name, badge_url, f))
            elif cat in ['Scientifiques & Données']:
                cats['Langages Scientifiques & Données'].append((name, badge_url, f))
            elif cat in ['Logiques & Preuves']:
                cats['Langages Logiques & Formels'].append((name, badge_url, f))
            elif cat in ['Smart Contracts & Web3']:
                cats['Smart Contracts & Web3'].append((name, badge_url, f))
            elif cat in ['Historiques & Pionniers']:
                cats['Langages Historiques & Pionniers'].append((name, badge_url, f))
            elif cat in ['Description Matérielle']:
                cats['Description Matérielle'].append((name, badge_url, f))
            elif cat in ['Émergents & Recherche']:
                cats['Langages Émergents & Recherche'].append((name, badge_url, f))
            elif cat in ['Frameworks & Runtimes']:
                cats['Frameworks, Runtimes & Écosystèmes'].append((name, badge_url, f))
            else:
                cats['Autres Fiches'].append((name, badge_url, f))
        else:
            # Fallback
            clean_name = f.replace('.md', '').replace('-', ' ').title()
            badge_url = f'https://img.shields.io/badge/{clean_name.replace(" ", "_")}-000000?style=for-the-badge'
            cats['Autres Fiches'].append((clean_name, badge_url, f))

    sections = []
    for cat_name, items in cats.items():
        if not items:
            continue
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
