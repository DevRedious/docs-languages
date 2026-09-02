import os
import re

BASE_DIR = '/home/dev_redious/Documents/Dev/docs-languages'
LANG_DIR = os.path.join(BASE_DIR, 'languages')

CATEGORIES = [
    ('Langages Systèmes & Bas Niveau', [
        'c', 'cpp', 'rust', 'zig', 'nim', 'd', 'assembly', 'fortran', 'ada', 'pascal',
        'odin', 'v', 'c-minus-minus', 'bliss', 'bliss-32', 'b-lang', 'bcpl', 'cilk', 'cilk-plus',
        'cms-2', 'coral-66', 'cyclone', 'dynace', 'felix', 'ficl', 'gnat-ada', 'hal-s',
        'hermes', 'hla', 'holyc', 'hume', 'jovial', 'lc-3', 'limbo', 'linoleum', 'masm',
        'microcode', 'mmix', 'nasm', 'newp', 'occam', 'occampi', 'orca', 'p4', 'parasail',
        'pl-m', 'pl360', 'seed7', 'spark-ada', 'sympl', 'tacpol', 'yacc', 'zen', 'zopl',
        'acc', 'accent', 'alef', 'amiga-e', 'ansi-c', 'assembly-arm', 'assembly-riscv',
        'assembly-x86', 'assembly-mips', 'assembly-sparc', 'assembly-68k', 'assembly-ppc',
        'assembly-z80', 'assembly-6502', 'bal-assembly', 'c-11', 'c-23', 'c-99', 'c-plus-plus-11',
        'c-plus-plus-20', 'c-plus-plus-23', 'chill', 'chill-96', 'ch', 'concurrent-c', 'bitc'
    ]),
    ('Langages Applicatifs & Entreprise', [
        'java', 'csharp', 'kotlin', 'scala', 'groovy', 'swift', 'objective-c', 'dart', 'go',
        'c-sharp-mono', 'beanshell', 'eiffel', 'eiffel-studio', 'golo', 'j-sharp', 'j-plus-plus',
        'jython', 'netrexx', 'pizza', 'sather', 'vb-net', 'xtend', 'a-sharp', 'axum',
        'clojure-clr', 'dart-flutter', 'jasmin'
    ]),
    ('Entreprise, ERP & 4GL Métier', [
        'abap', 'rpg', 'mumps', 'progress-abl', 'visual-foxpro', 'clipper', 'rexx',
        'abap-objects', 'acu-cobol', 'apex', 'appian-sail', 'bbx', 'bpel', 'cach-objectscript',
        'clarion', 'clarion-win', 'clist', 'dataflex', 'egl', 'filemaker', 'focus', 'harbour',
        'jcl', 'linc', 'lotusscript', 'magik', 'mumps-iris', 'natural', 'peoplesoft',
        'pl-sql', 'powerbuilder', 'proiv', 'rexx-regina', 'simpol', 'sqr', 't-sql',
        'uniface', 'visual-objects', 'x-plus-plus', 'x-sharp', 'ans-cobol', 'cal'
    ]),
    ('Langages Web & Scripting Dynamique', [
        'html', 'css', 'javascript', 'typescript', 'python', 'ruby', 'php', 'perl', 'lua',
        'tcl', 'sql', 'webassembly', 'xojo', 'cfml', 'coldfusion-script', 'curl-lang',
        'cython', 'emacs-lisp', 'euphoria', 'ferite', 'flow-js', 'ici', 'jscript',
        'lasso', 'livescript', 'metasploit-ruby', 'opa', 'raku', 'reasonml', 'webdna',
        'xotcl', 'yoix', 'agena', 'amber', 'autolisp', 'clojurescript-core', 'coconut'
    ]),
    ('GPU, Shaders & Graphisme', [
        'cuda', 'opencl', 'glsl', 'hlsl', 'wgsl', 'metal', 'cg', 'cuda-ptx', 'povray-sdl'
    ]),
    ('Jeux Vidéo & Moteurs 3D', [
        'gdscript', 'unrealscript', 'gml', 'squirrel', 'angelscript', 'amos-basic', 'chip-8',
        'dinkc', 'div-games', 'gamemonkey', 'goal', 'godot-csharp', 'hollywood', 'inform-6',
        'inform-7', 'lpc', 'lsl', 'mel', 'nwscript', 'processing', 'quakec', 'sourcepawn',
        'sourcepawn-sp', 'unreal-blueprints', 'verse', 'vvvv', 'wren', 'advsys', 'carmack-script',
        'cl-opengl', 'emberward-odin'
    ]),
    ('Audio, Musique & DSP Temps Réel', [
        'faust', 'supercollider', 'pure-data', 'chuck', 'csound'
    ]),
    ('Requêtes de Données, Graphes & Schémas', [
        'graphql', 'sparql', 'cypher', 'xquery', 'xpath', 'kql', 'prql', 'anorm',
        'clickhouse-sql', 'cypher-iso-gql', 'daffodil', 'elasticsearch-dsl', 'inkscape-svg',
        'omnimark', 'xslt'
    ]),
    ('Shells & Outils de Flux Unix', [
        'bash', 'zsh', 'fish', 'ksh', 'tcsh', 'powershell', 'awk', 'sed', 'awk-gawk',
        'awk-mawk', 'bash-posix', 'batch', 'csh', 'dcl', 'fish-shell-4', 'kixstart',
        'm4', 'make', 'sed-gnu'
    ]),
    ('Spécification Formelle & Modélisation', [
        'tla-plus', 'alloy', 'datalog', 'promela', 'act-one', 'adele', 'adl', 'alloy-4',
        'averest', 'b-method', 'boomerang', 'casl', 'casl-spec', 'cel', 'clymer',
        'cryptol', 'cryptol-verif', 'datalog-souffle', 'e-lang', 'event-b', 'frama-c',
        'ttcn-3', 'txl', 'umple', 'whiley', 'wyvern', 'z-notation'
    ]),
    ('Langages Fonctionnels & Déclaratifs', [
        'haskell', 'ocaml', 'standard-ml', 'alice-ml', 'elixir', 'erlang', 'clojure',
        'common-lisp', 'scheme', 'racket', 'janet', 'fennel', 'hy', 'shen', 'carp',
        'fsharp', 'elm', 'purescript', 'gleam', 'crystal', 'unison', 'flix', 'chapel',
        'pony', 'acl', 'alex', 'arc', 'arc-anarki', 'bert', 'caml-light', 'caml-special-light',
        'cat', 'caveman2', 'clasp', 'clean', 'daisy', 'erlang-otp', 'factor', 'factor-stack',
        'fl', 'gauche', 'gauche-scheme', 'gleam-otp', 'guile', 'haskell-ghc', 'joy',
        'lucid', 'newlisp', 'pico', 'picolisp', 'pyret'
    ]),
    ('Scientifiques, Mathématiques & Finance', [
        'r', 'julia', 'matlab', 'scilab', 'octave', 'sas', 'wolfram', 'apl', 'j', 'k',
        'q', 'bqn', 'labview', 'a-plus', 'aimms', 'aldor', 'algae', 'ampl', 'ampl-solver',
        'apl-dyalog', 'apl-ngn', 'apl2', 'arena', 'asymptote', 'asymptote-vec', 'bc',
        'biojava', 'bioperl', 'biopython', 'bqn-array', 'c-star', 'cant', 'church',
        'cuneiform', 'fortress', 'gap', 'gauss', 'gnuplot', 'gpss', 'julia-flux',
        'lantern', 'magma', 'maple', 'mathcad', 'maxima', 'mupad', 'nesl', 'netlogo',
        'nial', 'numpy-c', 'octave-forge', 'openqasm', 'pari-gp', 'q-sharp', 's-plus',
        'sasl', 'sawzall', 'simscript', 'sisal', 'spss', 'stata', 'telemac', 'titanium',
        'x10', 'yacas', 'yorick', 'zpl'
    ]),
    ('Logiques & Preuves (Formels)', [
        'prolog', 'mercury', 'curry', 'lean', 'coq', 'agda', 'idris', 'acl2', 'acronym',
        'alf', 'alma', 'alma-0', 'anubis', 'bcompile', 'cayenne', 'charity', 'claire',
        'clips', 'coq-rocq', 'cu-prolog', 'curry-kics2', 'epigram', 'escher', 'godel',
        'kaleidoscope', 'lean-mathlib', 'logtalk', 'visual-prolog'
    ]),
    ('Smart Contracts & Web3', [
        'solidity', 'vyper', 'move', 'cairo', 'clarity', 'sway', 'cadence', 'plutus',
        'michelson', 'scilla', 'foundry', 'viem', 'cairo-zero', 'daml'
    ]),
    ('Description Matérielle & Open Hardware', [
        'vhdl', 'verilog', 'systemverilog', 'chisel', 'bluespec', 'acis', 'aml', 'apt',
        'arduino-c', 'cadence-flair', 'chisel-3', 'drakon', 'eagle', 'esterel', 'g-code',
        'handel-c', 'ladder-logic', 'legoscript', 'lustre', 'rapid', 'scade', 'skill',
        'spin-propeller', 'stateflow', 'xod'
    ]),
    ('Systèmes Modulaires & Wirth', [
        'modula-2', 'oberon', 'modula', 'modula-3', 'object-oberon'
    ]),
    ('Langages Hybrides & Spécifiques', [
        'ballerina', 'vala', 'red', 'rebol', 'dylan', 'icon', 'ceylon', 'fantom',
        'nemerle', 'boo', 'pike', 'io', 'ring', 'ur-web', 'abcl', 'abcl-r', 'agora',
        'ambienttalk', 'avail', 'boo-lang', 'cecil', 'deesel', 'dylan-opendylan',
        'emerald', 'falcon', 'fancy', 'genie', 'haxe', 'hx-cpp', 'ioke', 'joule',
        'lava', 'leda', 'neko', 'newspeak', 'oz', 'prograph', 'pwct', 'topaz', 'unicon'
    ]),
    ('Langages Historiques & Pionniers', [
        'algol', 'basic', 'cobol', 'forth', 'logo', 'pli', 'simula', 'smalltalk',
        'snobol', 'postscript', 'tex', 'a-zero', 'abc', 'action', 'actor', 'act-iii',
        'algol-58', 'algol-60', 'algol-68', 'algol-n', 'algol-w', 'alphard', 'altran',
        'amigabasic', 'analytical-engine', 'apple-pascal', 'app-inventor', 'arexx',
        'argus', 'atari-basic', 'atlas-autocode', 'b-lang', 'babbage-lang', 'babytalk',
        'basic-dartmouth', 'basic-plus', 'bbc-basic', 'bcpl', 'beta', 'bliss', 'blockly',
        'bywater-basic', 'c-talk', 'cbasic', 'cesil', 'clist', 'clu', 'clx', 'comal',
        'concurrent-pascal', 'cool', 'cpl', 'edinburgh-imp', 'elan', 'espol', 'etoys',
        'euclid', 'euler', 'flavors', 'flow-matic', 'focal', 'fp', 'franz-lisp', 'gwbasic',
        'hope', 'hopscotch', 'hypertalk', 'ibm-basic', 'ipl', 'iswim', 'joss', 'karel',
        'kcl', 'lingo', 'lisa', 'mad', 'mesa', 'metafont', 'miranda', 'newtonscript',
        'pharo', 'pilot', 'plankalkul', 'pop-11', 'quickbasic', 'ratfor', 'refal',
        'sail', 'scratch', 'self', 'slip', 'squeak', 'teco', 'turing', 'tutor', 'ucb-logo',
        'ucsd-pascal', 'watfiv', 'zeno', 'zetalisp'
    ]),
    ('Automatisation Desktop & Web Scripting', [
        'applescript', 'autohotkey', 'vbscript', 'actionscript', 'coffeescript', 'hack',
        'appscript', 'autohotkey-v2', 'autoit', 'fastlane', 'livecode', 'nsis',
        'vba', 'vba-excel', 'winbatch'
    ]),
    ('Ésotériques & Théorie Informatique', [
        'brainfuck', 'befunge', 'whitespace', 'malbolge', 'befunge-98', 'bloop',
        'chef', 'chomski', 'core-war', 'cow', 'redcode', 'shakespeare'
    ]),
    ('Langages Émergents & Recherche', [
        'mojo', 'carbon', 'koka', 'hare', 'roc', 'bosque', 'carbon-lang'
    ]),
    ('Frameworks, Runtimes & Écosystèmes', [
        'react', 'vue', 'svelte', 'flutter', 'tailwind-css', 'bootstrap', 'tanstack',
        'swr', 'tauri', 'actix', 'yew', 'dioxus', 'leptos', 'laravel', 'ruby-on-rails',
        'jinja', 'trpc', 'vite', 'babel', 'node-js', 'prisma', 'prisma-client',
        'prisma-migrate', 'prisma-studio', 'prisma-accelerate', 'aida', 'ant', 'cdi',
        'crystal-amber', 'crystal-kemal', 'delphi-firemonkey', 'deno-ts', 'django-orm',
        'elm-tea', 'fastapi', 'mochatest', 'nest-js', 'qml', 'swift-server', 'vlang-ui'
    ])
]

def run():
    all_files = set(f for f in os.listdir(LANG_DIR) if f.endswith('.md'))
    total_count = len(all_files)

    category_blocks = []
    assigned_files = set()

    for cat_title, slugs in CATEGORIES:
        badges = []
        for slug in slugs:
            filename = f"{slug}.md"
            if filename in all_files:
                assigned_files.add(filename)
                # extract title from file or format slug
                filepath = os.path.join(LANG_DIR, filename)
                name = slug.replace('-', ' ').title()
                with open(filepath, 'r', encoding='utf-8') as f:
                    first_line = f.readline()
                    m = re.search(r'##\s+(.*?)\s+—', first_line)
                    if m:
                        name = m.group(1).strip()
                
                badge_name = name.replace(' ', '_').replace('-', '_').replace('+', '%2B').replace('#', '%23')
                badge_url = f"https://img.shields.io/badge/{badge_name}-000000?style=for-the-badge"
                badges.append(f"[![{name}]({badge_url})](languages/{filename})")
        
        if badges:
            badges_str = ' '.join(badges)
            category_blocks.append(f"### {cat_title} ({len(badges)})\n\n{badges_str}\n")

    # Remaining files
    unassigned = sorted(list(all_files - assigned_files))
    if unassigned:
        badges = []
        for filename in unassigned:
            filepath = os.path.join(LANG_DIR, filename)
            name = filename.replace('.md', '').replace('-', ' ').title()
            with open(filepath, 'r', encoding='utf-8') as f:
                first_line = f.readline()
                m = re.search(r'##\s+(.*?)\s+—', first_line)
                if m:
                    name = m.group(1).strip()
            badge_name = name.replace(' ', '_').replace('-', '_').replace('+', '%2B').replace('#', '%23')
            badge_url = f"https://img.shields.io/badge/{badge_name}-000000?style=for-the-badge"
            badges.append(f"[![{name}]({badge_url})](languages/{filename})")
        
        badges_str = ' '.join(badges)
        category_blocks.append(f"### Autres Fiches Documentaires ({len(badges)})\n\n{badges_str}\n")

    readme_content = f"""<div align="center">
  <img src="assets/logo.png" alt="docs-languages logo" width="200">

  <p align="center">
    <img src="https://img.shields.io/badge/Format-Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white" alt="Markdown" />
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="MIT" /></a>
    <img src="https://img.shields.io/badge/Fiches-{total_count}-38BDF8?style=for-the-badge" alt="{total_count} fiches" />
  </p>
  <p align="center">
    <i>Grande Encyclopédie Universelle des Langages de Programmation ({total_count} fiches documentaires standardisées).</i><br>
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

""" + '\n'.join(category_blocks) + """
## Modèle

Pour ajouter ou proposer une nouvelle fiche, suivez le format défini dans [TEMPLATE.md](TEMPLATE.md).
"""

    with open(os.path.join(BASE_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"README.md mis à jour avec succès : {total_count} fiches répertoriées !")

if __name__ == '__main__':
    run()
