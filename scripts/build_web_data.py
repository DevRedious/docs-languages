import os
import json
import re

BASE_DIR = '/home/dev_redious/Documents/Dev/docs-languages'
LANG_DIR = os.path.join(BASE_DIR, 'languages')
OUTPUT_JSON = os.path.join(BASE_DIR, 'data', 'languages.json')
OUTPUT_JS = os.path.join(BASE_DIR, 'data', 'languages.js')
os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)

from fix_badges import BRAND_DB, DOMAIN_FALLBACKS
from generate_complete_readme import CATEGORIES

# Reverse lookup for categories
CATEGORY_MAP = {}
for cat_name, slugs in CATEGORIES:
    for s in slugs:
        CATEGORY_MAP[s] = cat_name

# Advanced granular usage classification rules
USAGE_RULES = [
    ('Web Frontend', ['javascript', 'typescript', 'html', 'css', 'webassembly', 'react', 'vue', 'svelte', 'elm', 'purescript', 'livescript', 'flow-js', 'reasonml', 'bootstrap', 'tailwind-css', 'tanstack', 'swr', 'clojurescript-core', 'amber', 'topaz', 'opal', 'yew', 'dioxus', 'leptos', 'inkscape-svg']),
    ('Web Backend & API', ['python', 'php', 'ruby', 'go', 'node-js', 'elixir', 'csharp', 'java', 'kotlin', 'scala', 'rust', 'crystal', 'fastapi', 'nest-js', 'django-orm', 'laravel', 'ruby-on-rails', 'actix', 'deno-ts', 'trpc', 'cfml', 'coldfusion-script', 'lasso', 'opa', 'ballerina', 'ur-web', 'caveman2', 'crystal-amber', 'crystal-kemal', 'swift-server', 'vite', 'babel', 'graphql', 'prisma', 'prisma-client', 'prisma-migrate', 'prisma-studio', 'prisma-accelerate']),
    ('Systèmes & Bas Niveau', ['c', 'cpp', 'rust', 'zig', 'nim', 'd', 'assembly', 'fortran', 'ada', 'pascal', 'odin', 'v', 'c-minus-minus', 'bliss', 'bliss-32', 'b-lang', 'bcpl', 'cyclone', 'felix', 'ficl', 'hal-s', 'holyc', 'nasm', 'occam', 'occampi', 'p4', 'seed7', 'spark-ada', 'bitc', 'c-11', 'c-23', 'c-99', 'c-plus-plus-11', 'c-plus-plus-20', 'c-plus-plus-23', 'chill', 'chill-96', 'ch', 'concurrent-c', 'cms-2', 'coral-66', 'dynace', 'gnat-ada', 'hermes', 'hla', 'hume', 'jovial', 'lc-3', 'limbo', 'linoleum', 'masm', 'microcode', 'mmix', 'newp', 'orca', 'parasail', 'pl-m', 'pl360', 'sympl', 'tacpol', 'yacc', 'zen', 'zopl', 'acc', 'accent', 'alef', 'amiga-e', 'ansi-c', 'assembly-arm', 'assembly-riscv', 'assembly-x86', 'assembly-mips', 'assembly-sparc', 'assembly-68k', 'assembly-ppc', 'assembly-z80', 'assembly-6502', 'bal-assembly', 'modula', 'modula-2', 'modula-3', 'oberon', 'object-oberon']),
    ('Jeux Vidéo & 3D', ['gdscript', 'unrealscript', 'gml', 'squirrel', 'angelscript', 'godot-csharp', 'unreal-blueprints', 'verse', 'sourcepawn', 'sourcepawn-sp', 'quakec', 'wren', 'processing', 'div-games', 'gamemonkey', 'goal', 'hollywood', 'dinkc', 'cl-opengl', 'advsys', 'carmack-script', 'chip-8', 'emberward-odin', 'amos-basic', 'inform-6', 'inform-7', 'lpc', 'lsl', 'mel', 'nwscript', 'vvvv', 'glsl', 'hlsl', 'wgsl', 'metal', 'cg', 'cuda-ptx', 'povray-sdl']),
    ('Data Science, IA & Calcul', ['python', 'r', 'julia', 'matlab', 'scilab', 'octave', 'wolfram', 'apl', 'j', 'k', 'q', 'bqn', 'sas', 'maple', 'maxima', 'mathcad', 'spss', 'stata', 'numpy-c', 'julia-flux', 'lantern', 'cuneiform', 'biojava', 'bioperl', 'biopython', 'aimms', 'aldor', 'algae', 'ampl', 'ampl-solver', 'apl-dyalog', 'apl-ngn', 'apl2', 'arena', 'asymptote', 'asymptote-vec', 'bc', 'bqn-array', 'c-star', 'cant', 'church', 'fortress', 'gap', 'gauss', 'gnuplot', 'gpss', 'magma', 'mupad', 'nesl', 'netlogo', 'nial', 'octave-forge', 'openqasm', 'pari-gp', 'q-sharp', 's-plus', 'sasl', 'sawzall', 'simscript', 'sisal', 'telemac', 'titanium', 'x10', 'yacas', 'yorick', 'zpl', 'anorm', 'clickhouse-sql', 'sparql', 'cypher', 'cypher-iso-gql', 'kql', 'prql', 'xquery', 'xpath', 'xslt', 'elasticsearch-dsl', 'daffodil', 'omnimark']),
    ('Smart Contracts & Web3', ['solidity', 'vyper', 'move', 'cairo', 'cairo-zero', 'clarity', 'sway', 'cadence', 'plutus', 'michelson', 'scilla', 'daml', 'foundry', 'viem']),
    ('Audio & DSP Temps Réel', ['faust', 'supercollider', 'pure-data', 'chuck', 'csound']),
    ('Entreprise, ERP & Mainframe', ['abap', 'abap-objects', 'rpg', 'mumps', 'mumps-iris', 'progress-abl', 'visual-foxpro', 'clipper', 'rexx', 'rexx-regina', 'powerbuilder', 'pl-sql', 't-sql', 'natural', 'peoplesoft', 'focus', 'clarion', 'clarion-win', 'dataflex', 'uniface', 'x-plus-plus', 'x-sharp', 'cobol', 'ans-cobol', 'jcl', 'clist', 'acu-cobol', 'apex', 'appian-sail', 'bbx', 'bpel', 'cach-objectscript', 'egl', 'filemaker', 'harbour', 'linc', 'lotusscript', 'magik', 'proiv', 'simpol', 'sqr', 'visual-objects', 'cal', 'c-al']),
    ('Automatisation & Scripting', ['bash', 'bash-posix', 'zsh', 'fish', 'fish-shell-4', 'powershell', 'awk', 'awk-gawk', 'awk-mawk', 'sed', 'sed-gnu', 'applescript', 'appscript', 'autohotkey', 'autohotkey-v2', 'autoit', 'vbscript', 'vba', 'vba-excel', 'fastlane', 'nsis', 'winbatch', 'batch', 'make', 'm4', 'kixstart', 'tcl', 'xotcl', 'yoix', 'agena', 'autolisp', 'emacs-lisp', 'metasploit-ruby', 'webdna', 'csh', 'dcl', 'arexx', 'snobol', 'icon', 'unicon']),
    ('Spécification & Preuve Formelle', ['tla-plus', 'alloy', 'alloy-4', 'datalog', 'datalog-souffle', 'promela', 'b-method', 'event-b', 'frama-c', 'ttcn-3', 'txl', 'cryptol', 'cryptol-verif', 'whiley', 'lean', 'lean-mathlib', 'coq', 'coq-rocq', 'agda', 'idris', 'acl2', 'acronym', 'act-one', 'adele', 'adl', 'alf', 'alma', 'alma-0', 'anubis', 'averest', 'bcompile', 'boomerang', 'casl', 'casl-spec', 'cayenne', 'charity', 'claire', 'clips', 'clymer', 'cu-prolog', 'curry', 'curry-kics2', 'e-lang', 'epigram', 'escher', 'godel', 'kaleidoscope', 'logtalk', 'prolog', 'visual-prolog', 'wyvern', 'z-notation', 'cel']),
    ('Hardware & Embarqué (FPGA / IoT)', ['vhdl', 'verilog', 'systemverilog', 'chisel', 'chisel-3', 'bluespec', 'arduino-c', 'xod', 'ladder-logic', 'g-code', 'scade', 'lustre', 'esterel', 'spin-propeller', 'rapid', 'skill', 'acis', 'aml', 'apt', 'cadence-flair', 'drakon', 'eagle', 'handel-c', 'legoscript']),
    ('Ésotérique & Recherche', ['brainfuck', 'befunge', 'befunge-98', 'whitespace', 'malbolge', 'chef', 'shakespeare', 'core-war', 'cow', 'redcode', 'mojo', 'carbon', 'carbon-lang', 'koka', 'hare', 'roc', 'bosque', 'bloop', 'chomski']),
    ('Langages Fonctionnels Purs & Applicatifs', ['haskell', 'haskell-ghc', 'ocaml', 'standard-ml', 'alice-ml', 'elixir', 'erlang', 'erlang-otp', 'clojure', 'clojure-clr', 'common-lisp', 'scheme', 'racket', 'janet', 'fennel', 'hy', 'shen', 'carp', 'fsharp', 'elm', 'purescript', 'gleam', 'gleam-otp', 'crystal', 'unison', 'flix', 'chapel', 'pony', 'clean', 'factor', 'factor-stack', 'joy', 'miranda', 'pico', 'picolisp', 'pyret', 'acl', 'alex', 'arc', 'arc-anarki', 'bert', 'caml-light', 'caml-special-light', 'cat', 'clasp', 'daisy', 'fl', 'gauche', 'gauche-scheme', 'guile', 'newlisp', 'lucid']),
    ('Objets & Ingénierie Logicielle', ['smalltalk', 'pharo', 'squeak', 'simula', 'eiffel', 'eiffel-studio', 'sather', 'pizza', 'golo', 'j-sharp', 'j-plus-plus', 'jython', 'netrexx', 'vb-net', 'xtend', 'a-sharp', 'axum', 'dart-flutter', 'jasmin', 'beanshell', 'aspect-j', 'aspectj', 'abcl', 'abcl-r', 'agora', 'ambienttalk', 'avail', 'cecil', 'deesel', 'dylan', 'dylan-opendylan', 'emerald', 'falcon', 'fancy', 'genie', 'haxe', 'hx-cpp', 'ioke', 'joule', 'lava', 'leda', 'neko', 'newspeak', 'oz', 'prograph', 'pwct', 'vala', 'red', 'rebol', 'ceylon', 'fantom', 'nemerle', 'boo', 'pike', 'io', 'ring']),
    ('Pionniers & Histoire du Calcul', ['algol', 'algol-58', 'algol-60', 'algol-68', 'algol-n', 'algol-w', 'basic', 'basic-dartmouth', 'basic-plus', 'bbc-basic', 'gwbasic', 'quickbasic', 'bywater-basic', 'atari-basic', 'amigabasic', 'ibm-basic', 'cbasic', 'cobol', 'forth', 'logo', 'ucb-logo', 'pli', 'simula', 'smalltalk', 'snobol', 'postscript', 'tex', 'tex-latex', 'a-zero', 'abc', 'action', 'actor', 'act-iii', 'alphard', 'altran', 'analytical-engine', 'apple-pascal', 'app-inventor', 'argus', 'atlas-autocode', 'babbage-lang', 'babytalk', 'beta', 'blockly', 'c-talk', 'cesil', 'clu', 'clx', 'comal', 'concurrent-pascal', 'cool', 'cpl', 'edinburgh-imp', 'elan', 'espol', 'etoys', 'euclid', 'euler', 'flavors', 'flow-matic', 'focal', 'fp', 'franz-lisp', 'hope', 'hopscotch', 'hypertalk', 'ipl', 'iswim', 'joss', 'karel', 'kcl', 'lingo', 'lisa', 'mad', 'mesa', 'metafont', 'newtonscript', 'pilot', 'plankalkul', 'pop-11', 'ratfor', 'refal', 'sail', 'scratch', 'self', 'slip', 'teco', 'turing', 'tutor', 'ucsd-pascal', 'watfiv', 'zeno', 'zetalisp'])
]

PARADIGM_KEYWORDS = [
    ('Fonctionnel', ['fonctionnel', 'purement fonctionnel', 'monades', 'évaluation paresseuse', 'pattern matching', 'ordre supérieur', 'currying', 'lambda', 'haskell', 'ml', 'lisp', 'scheme']),
    ('Orienté Objet', ['orienté objet', 'classes', 'héritage', 'polymorphisme', 'encapsulation', 'smalltalk', 'méthodes', 'objet']),
    ('Impératif / Procédural', ['procédural', 'impératif', 'séquentiel', 'structures de contrôle', 'boucles', 'instructions']),
    ('Déclaratif & Logique', ['déclaratif', 'logique', 'unification', 'retour sur trace', 'backtracking', 'clauses de horn', 'prolog', 'contraintes']),
    ('Matriciel (Array)', ['matriciel', 'vectoriel', 'tableaux multidimensionnels', 'apl', 'simd', 'tenseur', 'matrice']),
    ('Concurrence & Acteurs', ['acteurs', 'processus communicants', 'csp', 'concurrence', 'goroutines', 'async/await', 'message passing', 'parallèle']),
    ('Orienté Prototype', ['prototype', 'prototypes', 'clonage d\'objets', 'self', 'javascript']),
    ('Concaténatif / Pile', ['concaténatif', 'basé sur une pile', 'stack-based', 'forth', 'factor', 'postfixe'])
]

def extract_year(text):
    m = re.search(r'\b(18\d\d|19\d\d|20\d\d)\b', text)
    return int(m.group(1)) if m else None

def parse_markdown(filepath, slug):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract Title
    title = slug.replace('-', ' ').title()
    m_title = re.search(r'##\s+(.*?)\s+—\s+histoire', content, re.IGNORECASE)
    if m_title:
        title = m_title.group(1).strip()

    # Extract Histoire bullets
    history_bullets = []
    m_hist = re.search(r'##\s+.*?histoire\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL | re.IGNORECASE)
    if m_hist:
        history_bullets = [re.sub(r'^\s*-\s*', '', line).strip() for line in m_hist.group(1).strip().split('\n') if line.strip().startswith('-')]

    # Extract Utilité bullets
    utility_bullets = []
    m_util = re.search(r'##\s+.*?utilité\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL | re.IGNORECASE)
    if m_util:
        utility_bullets = [re.sub(r'^\s*-\s*', '', line).strip() for line in m_util.group(1).strip().split('\n') if line.strip().startswith('-')]

    # Extract Resources
    website_url = None
    m_web = re.search(r'-\s+Site officiel\s*:\s*\[(.*?)\]\((.*?)\)', content)
    if m_web:
        website_url = m_web.group(2).strip()

    github_url = None
    m_gh = re.search(r'-\s+Dépôt GitHub\s*:\s*\[(.*?)\]\((.*?)\)', content)
    if m_gh:
        github_url = m_gh.group(2).strip()

    # Determine Year
    year = None
    for b in history_bullets:
        y = extract_year(b)
        if y:
            year = y
            break
    if not year:
        year = extract_year(content) or 2000

    # Determine Category
    category = CATEGORY_MAP.get(slug, "Langages Spécialisés & Hybrides")

    # Determine Usage Types
    usages = set()
    for usage_name, slug_list in USAGE_RULES:
        if slug in slug_list:
            usages.add(usage_name)
    if not usages:
        content_lower = content.lower()
        if 'web' in content_lower or 'html' in content_lower:
            usages.add('Web Backend & API')
        elif 'jeu' in content_lower or 'game' in content_lower:
            usages.add('Jeux Vidéo & 3D')
        elif 'système' in content_lower or 'compil' in content_lower:
            usages.add('Systèmes & Bas Niveau')
        elif 'math' in content_lower or 'calcul' in content_lower or 'scientifique' in content_lower:
            usages.add('Data Science, IA & Calcul')
        elif 'gestion' in content_lower or 'entreprise' in content_lower or 'erp' in content_lower:
            usages.add('Entreprise, ERP & Mainframe')
        elif 'script' in content_lower or 'automatisation' in content_lower:
            usages.add('Automatisation & Scripting')
        else:
            usages.add('Objets & Ingénierie Logicielle')

    # Determine Paradigms
    paradigms = set()
    full_text = content.lower()
    for p_name, keywords in PARADIGM_KEYWORDS:
        if any(kw in full_text for kw in keywords):
            paradigms.add(p_name)
    if not paradigms:
        paradigms.add('Impératif / Procédural')

    # Color & Logo
    clean_slug = slug.lower().strip()
    if clean_slug in BRAND_DB:
        color, logo, logo_color = BRAND_DB[clean_slug]
    else:
        color, logo, logo_color = DOMAIN_FALLBACKS.get(category, ('1E293B', 'code', 'white'))

    return {
        'id': slug,
        'name': title,
        'year': year,
        'category': category,
        'usages': sorted(list(usages)),
        'paradigms': sorted(list(paradigms)),
        'color': color,
        'logo': logo,
        'logo_color': logo_color,
        'website_url': website_url,
        'github_url': github_url,
        'history': history_bullets,
        'utility': utility_bullets,
        'summary': utility_bullets[0] if utility_bullets else "Fiche documentaire standardisée."
    }

def build_data():
    items = []
    files = sorted([f for f in os.listdir(LANG_DIR) if f.endswith('.md')])
    print(f"Parsing all {len(files)} language files...")
    
    for filename in files:
        slug = filename.replace('.md', '')
        filepath = os.path.join(LANG_DIR, filename)
        item = parse_markdown(filepath, slug)
        items.append(item)

    items.sort(key=lambda x: x['name'].lower())

    # Write JSON
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    # Write JS file with embedded fallback
    with open(OUTPUT_JS, 'w', encoding='utf-8') as f:
        f.write("window.ALL_LANGUAGES_DATA = " + json.dumps(items, ensure_ascii=False) + ";\n")

    print(f"Grand data build complete: {len(items)} / {len(files)} languages fully cataloged in JSON and JS!")

if __name__ == '__main__':
    build_data()
