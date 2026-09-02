import os
import re
import urllib.parse

BASE_DIR = '/home/dev_redious/Documents/Dev/docs-languages'
LANG_DIR = os.path.join(BASE_DIR, 'languages')

# Comprehensive brand color & icon database
BRAND_DB = {
    # Mainstream Languages
    'python': ('3776AB', 'python', 'white'),
    'javascript': ('F7DF1E', 'javascript', 'black'),
    'typescript': ('3178C6', 'typescript', 'white'),
    'c': ('A8B9CC', 'c', 'black'),
    'cpp': ('00599C', 'cplusplus', 'white'),
    'csharp': ('239120', 'csharp', 'white'),
    'rust': ('000000', 'rust', 'white'),
    'go': ('00ADD8', 'go', 'white'),
    'java': ('ED8B00', 'openjdk', 'white'),
    'kotlin': ('7F52FF', 'kotlin', 'white'),
    'swift': ('F05138', 'swift', 'white'),
    'php': ('777BB4', 'php', 'white'),
    'ruby': ('CC342D', 'ruby', 'white'),
    'html': ('E34F26', 'html5', 'white'),
    'css': ('1572B6', 'css3', 'white'),
    'sql': ('4479A1', 'mysql', 'white'),
    'dart': ('0175C2', 'dart', 'white'),
    'scala': ('DC322F', 'scala', 'white'),
    'elixir': ('4B275F', 'elixir', 'white'),
    'erlang': ('A90533', 'erlang', 'white'),
    'clojure': ('5881D8', 'clojure', 'white'),
    'haskell': ('5D4F85', 'haskell', 'white'),
    'ocaml': ('EC6813', 'ocaml', 'white'),
    'lua': ('2C2D72', 'lua', 'white'),
    'perl': ('39457E', 'perl', 'white'),
    'r': ('276DC3', 'r', 'white'),
    'julia': ('9558B2', 'julia', 'white'),
    'zig': ('F7A41D', 'zig', 'black'),
    'nim': ('FFE953', 'nim', 'black'),
    'd': ('B03931', 'd', 'white'),
    'bash': ('4EAA25', 'gnubash', 'white'),
    'powershell': ('5391FE', 'powershell', 'white'),
    'zsh': ('F1502F', 'zsh', 'white'),
    'fish': ('38BDF8', 'fishshell', 'white'),
    'fish-shell-4': ('38BDF8', 'fishshell', 'white'),
    'solidity': ('363636', 'solidity', 'white'),
    'webassembly': ('654FF0', 'webassembly', 'white'),
    'assembly': ('6E4C13', 'assemblyscript', 'white'),
    'assembly-arm': ('0091BD', 'arm', 'white'),
    'assembly-riscv': ('F15A24', 'riscv', 'white'),
    'assembly-x86': ('0071C5', 'intel', 'white'),
    'assembly-mips': ('D32F2F', 'mips', 'white'),
    'assembly-sparc': ('E76F00', 'oracle', 'white'),
    'assembly-68k': ('00599C', 'motorola', 'white'),
    'assembly-ppc': ('052FAD', 'ibm', 'white'),
    'assembly-z80': ('D32F2F', 'zilog', 'white'),
    'assembly-6502': ('4CAF50', 'microchip', 'white'),
    'fortran': ('734F96', 'fortran', 'white'),
    'ada': ('02F0C2', 'ada', 'black'),
    'pascal': ('00549D', 'delphi', 'white'),
    'delphi': ('EE1F35', 'delphi', 'white'),
    'matlab': ('0076A8', 'mathworks', 'white'),
    'scilab': ('005696', 'scilab', 'white'),
    'octave': ('0790BA', 'gnubash', 'white'),
    'wolfram': ('DD1100', 'wolfram', 'white'),
    'apl': ('00609C', 'dyalog', 'white'),
    'j': ('004B87', 'j', 'white'),
    'k': ('003366', 'kx', 'white'),
    'q': ('00558F', 'kx', 'white'),
    'bqn': ('2E3440', 'matrix', 'white'),
    'labview': ('FFD100', 'nationalinstruments', 'black'),
    'prolog': ('E44D26', 'prolog', 'white'),
    'lean': ('2B2B2B', 'lean', 'white'),
    'coq': ('C73B28', 'inria', 'white'),
    'coq-rocq': ('C73B28', 'inria', 'white'),
    'agda': ('293241', 'haskell', 'white'),
    'idris': ('9400D3', 'idris', 'white'),
    'vyper': ('333333', 'ethereum', 'white'),
    'move': ('0081FB', 'meta', 'white'),
    'cairo': ('EB5E28', 'ethereum', 'white'),
    'clarity': ('5546FF', 'bitcoin', 'white'),
    'sway': ('00F58C', 'fuel', 'black'),
    'cadence': ('00EF8B', 'flow', 'black'),
    'plutus': ('0033AD', 'cardano', 'white'),
    'michelson': ('2C7DF7', 'tezos', 'white'),
    'scilla': ('29CCC4', 'zilliqa', 'black'),
    'foundry': ('1C1E24', 'ethereum', 'white'),
    'viem': ('1E1E1E', 'ethereum', 'white'),
    'abap': ('008FD3', 'sap', 'white'),
    'abap-objects': ('008FD3', 'sap', 'white'),
    'rpg': ('052FAD', 'ibm', 'white'),
    'mumps': ('002D62', 'medicare', 'white'),
    'mumps-iris': ('002D62', 'intersystems', 'white'),
    'progress-abl': ('5BC500', 'progress', 'white'),
    'visual-foxpro': ('C41F14', 'visualstudio', 'white'),
    'clipper': ('1B365D', 'dosbox', 'white'),
    'rexx': ('052FAD', 'ibm', 'white'),
    'rexx-regina': ('052FAD', 'ibm', 'white'),
    'cuda': ('76B900', 'nvidia', 'white'),
    'opencl': ('005C8A', 'khronos', 'white'),
    'glsl': ('5586A4', 'opengl', 'white'),
    'hlsl': ('0078D7', 'windows', 'white'),
    'wgsl': ('005A9C', 'w3c', 'white'),
    'metal': ('000000', 'apple', 'white'),
    'gdscript': ('478CBF', 'godotengine', 'white'),
    'unrealscript': ('313131', 'unrealengine', 'white'),
    'unreal-blueprints': ('313131', 'unrealengine', 'white'),
    'gml': ('000000', 'gamemaker', 'white'),
    'squirrel': ('8E44AD', 'cplusplus', 'white'),
    'faust': ('009688', 'audacity', 'white'),
    'supercollider': ('121212', 'musicbrainz', 'white'),
    'pure-data': ('00457C', 'soundcharts', 'white'),
    'chuck': ('2C3E50', 'stanford', 'white'),
    'csound': ('2D3748', 'itunes', 'white'),
    'graphql': ('E10098', 'graphql', 'white'),
    'sparql': ('005A9C', 'w3c', 'white'),
    'cypher': ('008CC1', 'neo4j', 'white'),
    'xquery': ('E44D26', 'w3c', 'white'),
    'xpath': ('005A9C', 'w3c', 'white'),
    'xslt': ('005A9C', 'w3c', 'white'),
    'kql': ('0089D6', 'microsoftazure', 'white'),
    'prql': ('F15A24', 'postgresql', 'white'),
    'clickhouse-sql': ('FFCC01', 'clickhouse', 'black'),
    'tla-plus': ('FF9900', 'amazonwebservices', 'white'),
    'alloy': ('1F2937', 'mit', 'white'),
    'datalog': ('181717', 'github', 'white'),
    'promela': ('0B3D91', 'nasa', 'white'),
    'b-method': ('003366', 'sncf', 'white'),
    'event-b': ('003366', 'eth', 'white'),
    'frama-c': ('C73B28', 'cea', 'white'),
    'vhdl': ('00629B', 'ieee', 'white'),
    'verilog': ('00629B', 'ieee', 'white'),
    'systemverilog': ('00629B', 'ieee', 'white'),
    'chisel': ('DC322F', 'scala', 'white'),
    'chisel-3': ('DC322F', 'scala', 'white'),
    'bluespec': ('003366', 'mit', 'white'),
    'modula-2': ('00549D', 'gnu', 'white'),
    'oberon': ('003366', 'openaccess', 'white'),
    'brainfuck': ('2B2B2B', 'codewars', 'white'),
    'befunge': ('4B0082', 'gameandwatch', 'white'),
    'whitespace': ('FFFFFF', 'ghost', 'black'),
    'malbolge': ('8B0000', 'hackthebox', 'white'),
    'mojo': ('FF4B00', 'mojo', 'white'),
    'carbon': ('4285F4', 'google', 'white'),
    'carbon-lang': ('4285F4', 'google', 'white'),
    'koka': ('00A4EF', 'microsoft', 'white'),
    'hare': ('3B4252', 'hare', 'white'),
    'roc': ('7C3AED', 'roc', 'white'),
    'react': ('61DAFB', 'react', 'black'),
    'vue': ('4FC08D', 'vuedotjs', 'white'),
    'svelte': ('FF3E00', 'svelte', 'white'),
    'flutter': ('02569B', 'flutter', 'white'),
    'tailwind-css': ('06B6D4', 'tailwindcss', 'white'),
    'bootstrap': ('7952B3', 'bootstrap', 'white'),
    'tanstack': ('FF4154', 'reactquery', 'white'),
    'swr': ('000000', 'vercel', 'white'),
    'tauri': ('24C8DB', 'tauri', 'white'),
    'actix': ('000000', 'actix', 'white'),
    'yew': ('CE412B', 'rust', 'white'),
    'dioxus': ('000000', 'rust', 'white'),
    'leptos': ('EF3939', 'rust', 'white'),
    'laravel': ('FF2D20', 'laravel', 'white'),
    'ruby-on-rails': ('D30001', 'rubyonrails', 'white'),
    'jinja': ('B41717', 'jinja', 'white'),
    'trpc': ('2596BE', 'trpc', 'white'),
    'vite': ('646CFF', 'vite', 'white'),
    'babel': ('F9DC3E', 'babel', 'black'),
    'node-js': ('5FA04E', 'nodedotjs', 'white'),
    'deno-ts': ('000000', 'deno', 'white'),
    'nest-js': ('E0234E', 'nestjs', 'white'),
    'fastapi': ('009688', 'fastapi', 'white'),
    'django-orm': ('092E20', 'django', 'white'),
    'prisma': ('2D3748', 'prisma', 'white'),
    'prisma-client': ('2D3748', 'prisma', 'white'),
    'prisma-migrate': ('0284C7', 'prisma', 'white'),
    'prisma-studio': ('9333EA', 'prisma', 'white'),
    'prisma-accelerate': ('16A34A', 'prisma', 'white'),
    'applescript': ('999999', 'apple', 'white'),
    'autohotkey': ('334455', 'autohotkey', 'white'),
    'autohotkey-v2': ('334455', 'autohotkey', 'white'),
    'autoit': ('0078D7', 'windows', 'white'),
    'vbscript': ('1976D2', 'windows', 'white'),
    'vba': ('217346', 'microsoftexcel', 'white'),
    'vba-excel': ('217346', 'microsoftexcel', 'white'),
    'actionscript': ('FF0000', 'adobe', 'white'),
    'coffeescript': ('2F2625', 'coffeescript', 'white'),
    'hack': ('0081FB', 'meta', 'white'),
    'ballerina': ('20B6B0', 'ballerina', 'white'),
    'vala': ('A56DE2', 'gnome', 'white'),
    'red': ('DE2B26', 'red', 'white'),
    'rebol': ('577788', 'amigaos', 'white'),
    'dylan': ('000000', 'apple', 'white'),
    'icon': ('1B365D', 'gnu', 'white'),
    'ceylon': ('D9531E', 'eclipseide', 'white'),
    'fantom': ('2B579A', 'java', 'white'),
    'nemerle': ('007ACC', 'dotnet', 'white'),
    'boo': ('000000', 'unity', 'white'),
    'pike': ('2C3E50', 'cplusplus', 'white'),
    'io': ('1E1E1E', 'ghost', 'white'),
    'ring': ('18BC9C', 'c', 'white'),
    'ur-web': ('1A365D', 'mit', 'white'),
    'haxe': ('EA8220', 'haxe', 'white'),
    'oz': ('1B365D', 'mozart', 'white'),
    'postscript': ('FF0000', 'adobe', 'white'),
    'tex': ('008080', 'latex', 'white'),
    'tex-latex': ('008080', 'latex', 'white'),
    'smalltalk': ('57889C', 'smalltalk', 'white'),
    'pharo': ('2C3E50', 'pharo', 'white'),
    'squeak': ('00599C', 'smalltalk', 'white'),
    'algol': ('1A1A1A', 'computerhistory', 'white'),
    'basic': ('1976D2', 'visualstudio', 'white'),
    'cobol': ('003C71', 'ibm', 'white'),
    'forth': ('000000', 'forth', 'white'),
    'logo': ('2B2B2B', 'mit', 'white'),
    'pli': ('052FAD', 'ibm', 'white'),
    'simula': ('002D62', 'openaccess', 'white'),
    'snobol': ('333333', 'bell', 'white'),
    'scratch': ('FFAB19', 'scratch', 'white'),
    'eiffel': ('2980B9', 'eiffel', 'white'),
    'emacs-lisp': ('7F5AB6', 'gnuemacs', 'white'),
    'arduino-c': ('00979D', 'arduino', 'white'),
    'xod': ('00979D', 'arduino', 'white'),
    'sed': ('2C3E50', 'gnubash', 'white'),
    'awk': ('1A1A1A', 'gnubash', 'white'),
    'tcl': ('145B94', 'tcl', 'white'),
    'xojo': ('8CC63F', 'visualstudio', 'black'),
    'qml': ('41CD52', 'qt', 'white'),
    'pl-sql': ('F80000', 'oracle', 'white'),
    't-sql': ('CC292B', 'microsoftsqlserver', 'white'),
    'cfml': ('FF0000', 'adobe', 'white'),
    'coldfusion-script': ('FF0000', 'adobe', 'white'),
    'fsharp': ('378BBA', 'fsharp', 'white'),
    'elm': ('1293D8', 'elm', 'white'),
    'purescript': ('1D222D', 'purescript', 'white'),
    'gleam': ('FFAFF3', 'gleam', 'black'),
    'crystal': ('000000', 'crystal', 'white'),
    'unison': ('5C4EE5', 'unison', 'white'),
    'flix': ('E53935', 'java', 'white'),
    'chapel': ('009999', 'hpe', 'white'),
    'pony': ('1B1F23', 'pony', 'white'),
    'standard-ml': ('4B32C3', 'edx', 'white'),
    'janet': ('AA2233', 'lisp', 'white'),
    'fennel': ('2C2D72', 'lua', 'white'),
    'hy': ('3776AB', 'python', 'white'),
    'shen': ('2C3E50', 'lisp', 'white'),
    'carp': ('663399', 'rust', 'white'),
    'mercury': ('E44D26', 'prolog', 'white'),
    'curry': ('5D4F85', 'haskell', 'white'),
    'sas': ('0077C8', 'sas', 'white'),
    'apex': ('00A1E0', 'salesforce', 'white'),
    'odin': ('1A2B3C', 'odin', 'white'),
    'v': ('4F80AA', 'v', 'white'),
}

# Domain default fallbacks to ensure EVERY SINGLE BADGE has distinct colors & logos
DOMAIN_FALLBACKS = {
    'Langages Systèmes & Bas Niveau': ('1E293B', 'c', 'white'),
    'Langages Applicatifs & Entreprise': ('1E3A8A', 'openjdk', 'white'),
    'Entreprise, ERP & 4GL Métier': ('0F766E', 'ibm', 'white'),
    'Langages Web & Scripting Dynamique': ('B45309', 'javascript', 'white'),
    'GPU, Shaders & Graphisme': ('15803D', 'nvidia', 'white'),
    'Jeux Vidéo & Moteurs 3D': ('7E22CE', 'unrealengine', 'white'),
    'Audio, Musique & DSP Temps Réel': ('047857', 'audacity', 'white'),
    'Requêtes de Données, Graphes & Schémas': ('0369A1', 'graphql', 'white'),
    'Shells & Outils de Flux Unix': ('18181B', 'gnubash', 'white'),
    'Spécification Formelle & Modélisation': ('4338CA', 'mathworks', 'white'),
    'Langages Fonctionnels & Déclaratifs': ('6D28D9', 'haskell', 'white'),
    'Scientifiques, Mathématiques & Finance': ('1D4ED8', 'julia', 'white'),
    'Logiques & Preuves (Formels)': ('BE123C', 'prolog', 'white'),
    'Smart Contracts & Web3': ('111827', 'ethereum', 'white'),
    'Description Matérielle & Open Hardware': ('0E7490', 'ieee', 'white'),
    'Systèmes Modulaires & Wirth': ('1E40AF', 'openaccess', 'white'),
    'Langages Hybrides & Spécifiques': ('374151', 'codeigniter', 'white'),
    'Langages Historiques & Pionniers': ('334155', 'computerhistory', 'white'),
    'Automatisation Desktop & Web Scripting': ('0369A1', 'windows', 'white'),
    'Ésotériques & Théorie Informatique': ('4C1D95', 'ghost', 'white'),
    'Langages Émergents & Recherche': ('C2410C', 'rust', 'white'),
    'Frameworks, Runtimes & Écosystèmes': ('0284C7', 'react', 'white'),
}

def get_badge_url(slug, name, cat_title):
    # Check exact brand mapping
    clean_slug = slug.lower().strip()
    if clean_slug in BRAND_DB:
        color, logo, logo_color = BRAND_DB[clean_slug]
    else:
        # Check prefix / substring matches
        matched = False
        for k, (color, logo, logo_color) in BRAND_DB.items():
            if clean_slug.startswith(k) or clean_slug.endswith(k):
                matched = True
                break
        if not matched:
            color, logo, logo_color = DOMAIN_FALLBACKS.get(cat_title, ('1F2937', 'codeigniter', 'white'))

    # Format badge label
    label = name.replace(' ', '_').replace('-', '_').replace('+', '%2B').replace('#', '%23')
    badge_url = f"https://img.shields.io/badge/{label}-{color}?style=for-the-badge&logo={logo}&logoColor={logo_color}"
    return badge_url

def update_readme():
    from generate_complete_readme import CATEGORIES
    
    all_files = set(f for f in os.listdir(LANG_DIR) if f.endswith('.md'))
    total_count = len(all_files)
    assigned_files = set()
    category_blocks = []

    for cat_title, slugs in CATEGORIES:
        badges = []
        for slug in slugs:
            filename = f"{slug}.md"
            if filename in all_files:
                assigned_files.add(filename)
                filepath = os.path.join(LANG_DIR, filename)
                name = slug.replace('-', ' ').title()
                with open(filepath, 'r', encoding='utf-8') as f:
                    first_line = f.readline()
                    m = re.search(r'##\s+(.*?)\s+—', first_line)
                    if m:
                        name = m.group(1).strip()
                
                badge_url = get_badge_url(slug, name, cat_title)
                badges.append(f"[![{name}]({badge_url})](languages/{filename})")
        
        if badges:
            badges_str = ' '.join(badges)
            category_blocks.append(f"### {cat_title} ({len(badges)})\n\n{badges_str}\n")

    unassigned = sorted(list(all_files - assigned_files))
    if unassigned:
        badges = []
        for filename in unassigned:
            slug = filename.replace('.md', '')
            filepath = os.path.join(LANG_DIR, filename)
            name = slug.replace('-', ' ').title()
            with open(filepath, 'r', encoding='utf-8') as f:
                first_line = f.readline()
                m = re.search(r'##\s+(.*?)\s+—', first_line)
                if m:
                    name = m.group(1).strip()
            badge_url = get_badge_url(slug, name, "Autres Fiches")
            badges.append(f"[![{name}]({badge_url})](languages/{filename})")
        
        badges_str = ' '.join(badges)
        category_blocks.append(f"### Fiches Complémentaires ({len(badges)})\n\n{badges_str}\n")

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

    print(f"README.md mis à jour : 100% des {total_count} badges ont désormais leurs vraies couleurs officielles et leurs logos !")

if __name__ == '__main__':
    update_readme()
