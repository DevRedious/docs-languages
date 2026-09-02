import os
import re

BASE_DIR = '/home/dev_redious/Documents/Dev/docs-languages'
LANG_DIR = os.path.join(BASE_DIR, 'languages')

# Comprehensive mapping of official GitHub repositories
GITHUB_REPOS = {
    # Core Systems & Compilers
    'rust': 'https://github.com/rust-lang/rust',
    'go': 'https://github.com/golang/go',
    'python': 'https://github.com/python/cpython',
    'typescript': 'https://github.com/microsoft/TypeScript',
    'javascript': 'https://github.com/tc39/ecma262',
    'cpp': 'https://github.com/isocpp/CppCoreGuidelines',
    'c': 'https://github.com/llvm/llvm-project',
    'csharp': 'https://github.com/dotnet/csharplang',
    'java': 'https://github.com/openjdk/jdk',
    'kotlin': 'https://github.com/JetBrains/kotlin',
    'swift': 'https://github.com/swiftlang/swift',
    'php': 'https://github.com/php/php-src',
    'ruby': 'https://github.com/ruby/ruby',
    'dart': 'https://github.com/dart-lang/sdk',
    'scala': 'https://github.com/scala/scala3',
    'elixir': 'https://github.com/elixir-lang/elixir',
    'erlang': 'https://github.com/erlang/otp',
    'clojure': 'https://github.com/clojure/clojure',
    'haskell': 'https://github.com/ghc/ghc',
    'haskell-ghc': 'https://github.com/ghc/ghc',
    'ocaml': 'https://github.com/ocaml/ocaml',
    'lua': 'https://github.com/lua/lua',
    'perl': 'https://github.com/Perl/perl5',
    'julia': 'https://github.com/JuliaLang/julia',
    'zig': 'https://github.com/ziglang/zig',
    'nim': 'https://github.com/nim-lang/Nim',
    'd': 'https://github.com/dlang/dmd',
    'odin': 'https://github.com/odin-lang/Odin',
    'v': 'https://github.com/vlang/v',
    'crystal': 'https://github.com/crystal-lang/crystal',
    'gleam': 'https://github.com/gleam-lang/gleam',
    'gleam-otp': 'https://github.com/gleam-lang/otp',
    'unison': 'https://github.com/unisonweb/unison',
    'flix': 'https://github.com/flix/flix',
    'chapel': 'https://github.com/chapel-lang/chapel',
    'pony': 'https://github.com/ponylang/ponyc',
    'janet': 'https://github.com/janet-lang/janet',
    'fennel': 'https://github.com/bakpakin/Fennel',
    'hy': 'https://github.com/hylang/hy',
    'shen': 'https://github.com/Shen-Language/shen-cl',
    'carp': 'https://github.com/carp-lang/Carp',
    'fsharp': 'https://github.com/dotnet/fsharp',
    'elm': 'https://github.com/elm/compiler',
    'purescript': 'https://github.com/purescript/purescript',
    'r': 'https://github.com/r-devel/r-svn',
    'solidity': 'https://github.com/ethereum/solidity',
    'vyper': 'https://github.com/vyperlang/vyper',
    'cairo': 'https://github.com/starkware-libs/cairo',
    'cairo-zero': 'https://github.com/starkware-libs/cairo-lang',
    'move': 'https://github.com/move-language/move',
    'clarity': 'https://github.com/stacks-network/clarity',
    'sway': 'https://github.com/FuelLabs/sway',
    'cadence': 'https://github.com/onflow/cadence',
    'plutus': 'https://github.com/IntersectMBO/plutus',
    'michelson': 'https://github.com/oxheadalpha/morley',
    'scilla': 'https://github.com/Zilliqa/scilla',
    'daml': 'https://github.com/digital-asset/daml',
    'foundry': 'https://github.com/foundry-rs/foundry',
    'viem': 'https://github.com/wevm/viem',
    'lean': 'https://github.com/leanprover/lean4',
    'lean-mathlib': 'https://github.com/leanprover-community/mathlib4',
    'coq': 'https://github.com/coq/coq',
    'coq-rocq': 'https://github.com/coq/coq',
    'agda': 'https://github.com/agda/agda',
    'idris': 'https://github.com/idris-lang/Idris2',
    'prolog': 'https://github.com/SWI-Prolog/swipl-devel',
    'mercury': 'https://github.com/Mercury-Language/mercury',
    'curry': 'https://github.com/kics2/kics2',
    'curry-kics2': 'https://github.com/kics2/kics2',
    'mojo': 'https://github.com/modular/mojo',
    'carbon': 'https://github.com/carbon-language/carbon-lang',
    'carbon-lang': 'https://github.com/carbon-language/carbon-lang',
    'koka': 'https://github.com/koka-lang/koka',
    'roc': 'https://github.com/roc-lang/roc',
    'bosque': 'https://github.com/microsoft/BosqueLanguage',
    'ballerina': 'https://github.com/ballerina-platform/ballerina-lang',
    'vala': 'https://github.com/GNOME/vala',
    'red': 'https://github.com/red/red',
    'rebol': 'https://github.com/Oldes/Rebol3',
    'dylan': 'https://github.com/dylan-lang/opendylan',
    'dylan-opendylan': 'https://github.com/dylan-lang/opendylan',
    'ceylon': 'https://github.com/eclipse/ceylon',
    'fantom': 'https://github.com/fantom-lang/fantom',
    'nemerle': 'https://github.com/rsdn/nemerle',
    'boo': 'https://github.com/boo-lang/boo',
    'boo-lang': 'https://github.com/boo-lang/boo',
    'pike': 'https://github.com/pikelang/Pike',
    'io': 'https://github.com/IoLanguage/io',
    'ring': 'https://github.com/ring-lang/ring',
    'ur-web': 'https://github.com/urweb/urweb',
    'haxe': 'https://github.com/HaxeFoundation/haxe',
    'hx-cpp': 'https://github.com/HaxeFoundation/hxcpp',
    'neko': 'https://github.com/HaxeFoundation/neko',
    'wren': 'https://github.com/wren-lang/wren',
    'gdscript': 'https://github.com/godotengine/godot',
    'godot-csharp': 'https://github.com/godotengine/godot',
    'squirrel': 'https://github.com/albertodemichelis/squirrel',
    'angelscript': 'https://github.com/codecat/angelscript-mirror',
    'faust': 'https://github.com/grame-cncm/faust',
    'supercollider': 'https://github.com/supercollider/supercollider',
    'pure-data': 'https://github.com/pure-data/pure-data',
    'chuck': 'https://github.com/ccrma/chuck',
    'csound': 'https://github.com/csound/csound',
    'graphql': 'https://github.com/graphql/graphql-spec',
    'cypher': 'https://github.com/opencypher/openCypher',
    'cypher-iso-gql': 'https://github.com/opencypher/openCypher',
    'kql': 'https://github.com/microsoft/Kusto-Query-Language',
    'prql': 'https://github.com/PRQL/prql',
    'clickhouse-sql': 'https://github.com/ClickHouse/ClickHouse',
    'daffodil': 'https://github.com/apache/daffodil',
    'elasticsearch-dsl': 'https://github.com/elastic/elasticsearch',
    'anorm': 'https://github.com/playframework/anorm',
    'chisel': 'https://github.com/chipsalliance/chisel',
    'chisel-3': 'https://github.com/chipsalliance/chisel',
    'bluespec': 'https://github.com/B-Lang-org/bsc',
    'arduino-c': 'https://github.com/arduino/ArduinoCore-avr',
    'xod': 'https://github.com/xodio/xod',
    'tla-plus': 'https://github.com/tlaplus/tlaplus',
    'alloy': 'https://github.com/AlloyTools/org.alloytools.alloy',
    'alloy-4': 'https://github.com/AlloyTools/org.alloytools.alloy',
    'datalog': 'https://github.com/souffle-lang/souffle',
    'datalog-souffle': 'https://github.com/souffle-lang/souffle',
    'promela': 'https://github.com/nimble-code/Spin',
    'frama-c': 'https://github.com/Frama-C/Frama-C-snapshot',
    'event-b': 'https://github.com/rodin-b-sharp/rodin',
    'ttcn-3': 'https://github.com/eclipse/titan.core',
    'umple': 'https://github.com/umple/umple',
    'whiley': 'https://github.com/Whiley/WhileyCompiler',
    'wyvern': 'https://github.com/wyvernlang/wyvern',
    'cel': 'https://github.com/google/cel-spec',
    'cryptol': 'https://github.com/GaloisInc/cryptol',
    'cryptol-verif': 'https://github.com/GaloisInc/cryptol',
    'scilab': 'https://github.com/scilab/scilab',
    'octave': 'https://github.com/gnu-octave/octave',
    'octave-forge': 'https://github.com/gnu-octave/octave',
    'bqn': 'https://github.com/mlochbaum/BQN',
    'bqn-array': 'https://github.com/dzaima/CBQN',
    'q-sharp': 'https://github.com/microsoft/qsharp',
    'openqasm': 'https://github.com/openqasm/openqasm',
    'gap': 'https://github.com/gap-system/gap',
    'maxima': 'https://github.com/andrejv/maxima',
    'yacas': 'https://github.com/grzegorzmazur/yacas',
    'asymptote': 'https://github.com/vectorgraphics/asymptote',
    'asymptote-vec': 'https://github.com/vectorgraphics/asymptote',
    'biojava': 'https://github.com/biojava/biojava',
    'bioperl': 'https://github.com/bioperl/bioperl-live',
    'biopython': 'https://github.com/biopython/biopython',
    'numpy-c': 'https://github.com/numpy/numpy',
    'julia-flux': 'https://github.com/FluxML/Flux.jl',
    'lantern': 'https://github.com/feiwang3311/Lantern',
    'netlogo': 'https://github.com/NetLogo/NetLogo',
    'pari-gp': 'https://github.com/Bordeaux-Calcul-Formel/pari',
    'yorick': 'https://github.com/LLNL/yorick',
    'bash': 'https://github.com/bminor/bash',
    'bash-posix': 'https://github.com/bminor/bash',
    'zsh': 'https://github.com/zsh-users/zsh',
    'fish': 'https://github.com/fish-shell/fish-shell',
    'fish-shell-4': 'https://github.com/fish-shell/fish-shell',
    'powershell': 'https://github.com/PowerShell/PowerShell',
    'awk-gawk': 'https://github.com/gawk-mirror/gawk',
    'awk-mawk': 'https://github.com/ThomasDickey/mawk-snapshots',
    'sed-gnu': 'https://github.com/mirror/sed',
    'make': 'https://github.com/mirror/make',
    'm4': 'https://github.com/mirror/m4',
    'cython': 'https://github.com/cython/cython',
    'raku': 'https://github.com/rakudo/rakudo',
    'reasonml': 'https://github.com/reasonml/reason',
    'livescript': 'https://github.com/gkz/LiveScript',
    'flow-js': 'https://github.com/facebook/flow',
    'emacs-lisp': 'https://github.com/emacs-mirror/emacs',
    'autohotkey': 'https://github.com/AutoHotkey/AutoHotkey',
    'autohotkey-v2': 'https://github.com/AutoHotkey/AutoHotkey',
    'autoit': 'https://github.com/ahkscript/awesome-AutoHotkey',
    'fastlane': 'https://github.com/fastlane/fastlane',
    'nsis': 'https://github.com/kichik/nsis',
    'coffeescript': 'https://github.com/jashkenas/coffeescript',
    'hack': 'https://github.com/facebook/hhvm',
    'react': 'https://github.com/facebook/react',
    'vue': 'https://github.com/vuejs/core',
    'svelte': 'https://github.com/sveltejs/svelte',
    'flutter': 'https://github.com/flutter/flutter',
    'tailwind-css': 'https://github.com/tailwindlabs/tailwindcss',
    'bootstrap': 'https://github.com/twbs/bootstrap',
    'tanstack': 'https://github.com/TanStack/query',
    'swr': 'https://github.com/vercel/swr',
    'tauri': 'https://github.com/tauri-apps/tauri',
    'actix': 'https://github.com/actix/actix-web',
    'yew': 'https://github.com/yewstack/yew',
    'dioxus': 'https://github.com/DioxusLabs/dioxus',
    'leptos': 'https://github.com/leptos-rs/leptos',
    'laravel': 'https://github.com/laravel/laravel',
    'ruby-on-rails': 'https://github.com/rails/rails',
    'jinja': 'https://github.com/pallets/jinja',
    'trpc': 'https://github.com/trpc/trpc',
    'vite': 'https://github.com/vitejs/vite',
    'babel': 'https://github.com/babel/babel',
    'node-js': 'https://github.com/nodejs/node',
    'deno-ts': 'https://github.com/denoland/deno',
    'nest-js': 'https://github.com/nestjs/nest',
    'fastapi': 'https://github.com/fastapi/fastapi',
    'django-orm': 'https://github.com/django/django',
    'prisma': 'https://github.com/prisma/prisma',
    'prisma-client': 'https://github.com/prisma/prisma',
    'prisma-migrate': 'https://github.com/prisma/prisma-engines',
    'prisma-studio': 'https://github.com/prisma/studio',
    'prisma-accelerate': 'https://github.com/prisma/prisma',
    'mochatest': 'https://github.com/mochajs/mocha',
    'vlang-ui': 'https://github.com/vlang/ui',
    'swift-server': 'https://github.com/vapor/vapor',
    'crystal-amber': 'https://github.com/amberframework/amber',
    'crystal-kemal': 'https://github.com/kemalcr/kemal',
    'pharo': 'https://github.com/pharo-project/pharo',
    'squeak': 'https://github.com/squeak-smalltalk/squeak-app',
    'scratch': 'https://github.com/scratchfoundation/scratch-gui',
    'blockly': 'https://github.com/google/blockly',
    'guile': 'https://github.com/bminor/guile',
    'clisp': 'https://github.com/coreutils/gnulib',
    'picolisp': 'https://github.com/picolisp/picolisp',
    'pyret': 'https://github.com/brownplt/pyret-lang',
    'racket': 'https://github.com/racket/racket',
    'common-lisp': 'https://github.com/sbcl/sbcl',
    'factor': 'https://github.com/factor/factor',
    'factor-stack': 'https://github.com/factor/factor',
    'nasm': 'https://github.com/netwide-assembler/nasm',
    'yacc': 'https://github.com/Distrotech/byacc',
    'harbour': 'https://github.com/harbour/core',
    'x-sharp': 'https://github.com/X-Sharp/XSharpDev',
    'gnat-ada': 'https://github.com/AdaCore/gnatcoll-core',
    'spark-ada': 'https://github.com/AdaCore/spark2014',
    'beanshell': 'https://github.com/beanshell/beanshell',
    'aspect-j': 'https://github.com/eclipse-aspectj/aspectj',
    'aspectj': 'https://github.com/eclipse-aspectj/aspectj',
    'gwbasic': 'https://github.com/microsoft/GW-BASIC',
    'action': 'https://github.com/pfusik/action',
    'bcompile': 'https://github.com/webyrd/Barliman',
    'cuneiform': 'https://github.com/joergenb/cuneiform',
    'golo': 'https://github.com/eclipse/golo',
    'arc': 'https://github.com/arclanguage/anarki',
    'arc-anarki': 'https://github.com/arclanguage/anarki',
    'clasp': 'https://github.com/clasp-developers/clasp',
    'caveman2': 'https://github.com/fukamachi/caveman',
    'cl-opengl': 'https://github.com/3b/cl-opengl',
    'zen': 'https://github.com/zenlang/zen',
    'befunge': 'https://github.com/catseye/Befunge-93',
    'befunge-98': 'https://github.com/catseye/Befunge-93',
    'malbolge': 'https://github.com/ksprotte/malbolge',
    'core-war': 'https://github.com/mtsr/corewar'
}

def update_files():
    updated = 0
    for filename in os.listdir(LANG_DIR):
        if not filename.endswith('.md'):
            continue
        
        slug = filename.replace('.md', '')
        filepath = os.path.join(LANG_DIR, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if we have a github repo for this slug
        github_url = GITHUB_REPOS.get(slug)
        if not github_url:
            continue

        # If already has github repo line, skip
        if 'Dépôt GitHub :' in content or 'GitHub :' in content:
            continue
        
        # Check if resources section exists
        if '— ressources' in content:
            # Append github repo under Site officiel
            # Replace the resources section properly
            pattern = r'(##\s+[^\n]+—\s+ressources\s*\n\s*-\s+Site officiel\s*:\s*\[[^\]]+\]\([^\)]+\))'
            replacement = r'\1\n- Dépôt GitHub : [' + github_url + r'](' + github_url + r')'
            
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated += 1
            else:
                # If site officiel format differs slightly
                lines = content.split('\n')
                new_lines = []
                for line in lines:
                    new_lines.append(line)
                    if '— ressources' in line:
                        pass
                # append at end
                if not any('Dépôt GitHub' in l for l in lines):
                    content = content.rstrip() + f"\n- Dépôt GitHub : [{github_url}]({github_url})\n"
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    updated += 1

    print(f"Mise à jour terminée : {updated} fiches documentaires enrichies avec leur lien GitHub officiel.")

if __name__ == '__main__':
    update_files()
