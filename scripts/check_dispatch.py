#!/usr/bin/env python3
from pathlib import Path
import re, sys
root = Path(__file__).resolve().parents[1]
commands = sorted((root/'commands').glob('finow-*.md'))
errors=[]
for cmd in commands:
    name=cmd.stem
    wrapper=root/'.claude'/'commands'/cmd.name
    if not wrapper.exists(): errors.append(f'missing wrapper {cmd.name}'); continue
    w=wrapper.read_text(encoding='utf-8')
    if f'commands/{cmd.name}' not in w: errors.append(f'bad wrapper dispatch {cmd.name}')
    if f'/{name}' not in (root/'AGENTS.md').read_text(encoding='utf-8'):
        errors.append(f'AGENTS dispatcher missing /{name}')
if errors:
    print('Dispatch check: FAILED'); [print('- '+e) for e in errors]; sys.exit(1)
print(f'Dispatch check: PASS ({len(commands)} commands)')
