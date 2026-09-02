import os
import json
import re

BASE_DIR = '/home/dev_redious/Documents/Dev/docs-languages'
LANG_DIR = os.path.join(BASE_DIR, 'languages')
OUTPUT_JSON = os.path.join(BASE_DIR, 'data', 'languages.json')
os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)

# Import BRAND_DB and CATEGORIES from our existing scripts
from fix_badges import BRAND_DB, DOMAIN_FALLBACKS
from generate_complete_readme import CATEGORIES

# Reverse lookup for categories
CATEGORY_MAP = {}
for cat_name, slugs in CATEGORIES:
    for s in slugs:
        CATEGORY_MAP[s] = cat_name

# Usage categorization heuristics
USAGE_RULES = [
    ('Web Frontend', ['javascript', 'typescript', 'html', 'css', 'webassembly', 'react', 'vue', 'svelte', 'elm', 'purescript', 'livescript', 'flow-js', 'reasonml', 'bootstrap', 'tailwind-css', 'tanstack', 'swr']),
    ('Web Backend & API', ['python', 'php', 'ruby', 'go', 'node-js', 'elixir', 'csharp', 'java', 'kotlin', 'scala', 'rust', 'crystal', 'fastapi', 'nest-js', 'django-orm', 'laravel', 'ruby-on-rails', 'actix', 'deno-ts', 'trpc', 'cfml', 'coldfusion-script', 'lasso', 'opa', 'ballerina']),
    ('Systèmes & Bas Niveau', ['c', 'cpp', 'rust', 'zig', 'nim', 'd', 'assembly', 'fortran', 'ada', 'pascal', 'odin', 'v', 'c-minus-minus', 'bliss', 'b-lang', 'bcpl', 'cyclone', 'felix', 'ficl', 'hal-s', 'holyc', 'nasm', 'occam', 'p4', 'seed7', 'spark-ada', 'bitc', 'c11', 'c23', 'c99']),
    ('Jeux Vidéo & 3D', ['gdscript', 'unrealscript', 'gml', 'squirrel', 'angelscript', 'cplusplus', 'csharp', 'godot-csharp', 'unreal-blueprints', 'verse', 'sourcepawn', 'quakec', 'wren', 'processing', 'div-games', 'gamemonkey', 'goal', 'hollywood', 'dinkc', 'cl-opengl']),
    ('Data Science, IA & Calcul', ['python', 'r', 'julia', 'matlab', 'scilab', 'octave', 'wolfram', 'apl', 'j', 'k', 'q', 'bqn', 'sas', 'maple', 'maxima', 'mathcad', 'spss', 'stata', 'numpy-c', 'julia-flux', 'lantern', 'cuneiform', 'biojava', 'bioperl', 'biopython']),
    ('Smart Contracts & Web3', ['solidity', 'vyper', 'move', 'cairo', 'cairo-zero', 'clarity', 'sway', 'cadence', 'plutus', 'michelson', 'scilla', 'daml', 'foundry', 'viem']),
    ('Audio & DSP Temps Réel', ['faust', 'supercollider', 'pure-data', 'chuck', 'csound']),
    ('Entreprise, ERP & Mainframe', ['abap', 'rpg', 'mumps', 'progress-abl', 'visual-foxpro', 'clipper', 'rexx', 'powerbuilder', 'pl-sql', 't-sql', 'natural', 'peoplesoft', 'focus', 'clarion', 'dataflex', 'uniface', 'x-plus-plus', 'x-sharp', 'cobol', 'ans-cobol', 'jcl', 'clist']),
    ('Automatisation & Scripting', ['bash', 'zsh', 'fish', 'powershell', 'awk', 'sed', 'applescript', 'autohotkey', 'autohotkey-v2', 'autoit', 'vbscript', 'vba', 'vba-excel', 'fastlane', 'nsis', 'winbatch', 'batch', 'make', 'm4', 'kixstart']),
    ('Spécification & Preuve Formelle', ['tla-plus', 'alloy', 'alloy-4', 'datalog', 'datalog-souffle', 'promela', 'b-method', 'event-b', 'frama-c', 'ttcn-3', 'txl', 'cryptol', 'whiley', 'lean', 'coq', 'agda', 'idris', 'acl2', 'z-notation']),
    ('Hardware & Embarqué (FPGA / IoT)', ['vhdl', 'verilog', 'systemverilog', 'chisel', 'chisel-3', 'bluespec', 'arduino-c', 'xod', 'ladder-logic', 'g-code', 'scade', 'lustre', 'esterel', 'spin-propeller', 'rapid', 'skill']),
    ('Ésotérique & Recherche', ['brainfuck', 'befunge', 'befunge-98', 'whitespace', 'malbolge', 'chef', 'shakespeare', 'core-war', 'cow', 'redcode', 'mojo', 'carbon', 'koka', 'hare', 'roc', 'bosque'])
]

PARADIGM_KEYWORDS = [
    ('Fonctionnel', ['fonctionnel', 'purement fonctionnel', 'monades', 'évaluation paresseuse', 'pattern matching', 'ordre supérieur', 'currying', 'lambda']),
    ('Orienté Objet', ['orienté objet', 'classes', 'héritage', 'polymorphisme', 'encapsulation', 'smalltalk', 'méthodes']),
    ('Impératif / Procédural', ['procédural', 'impératif', 'séquentiel', 'structures de contrôle']),
    ('Déclaratif & Logique', ['déclaratif', 'logique', 'unification', 'retour sur trace', 'backtracking', 'clauses de horn', 'prolog']),
    ('Matriciel (Array)', ['matriciel', 'vectoriel', 'tableaux multidimensionnels', 'apl', 'simd', 'tenseur']),
    ('Concurrence & Acteurs', ['acteurs', 'processus communicants', 'csp', 'concurrence', 'goroutines', 'async/await', 'message passing']),
    ('Orienté Prototype', ['prototype', 'prototypes', 'clonage d\'objets']),
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
        # Fallback heuristic based on content
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
        else:
            usages.add('Développement Général')

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
    print(f"Parsing {len(files)} files...")
    
    for filename in files:
        slug = filename.replace('.md', '')
        filepath = os.path.join(LANG_DIR, filename)
        item = parse_markdown(filepath, slug)
        items.append(item)

    # Sort alphabetically by default
    items.sort(key=lambda x: x['name'].lower())

    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    print(f"Data JSON compiled successfully with {len(items)} languages to: {OUTPUT_JSON}")

if __name__ == '__main__':
    build_data()
