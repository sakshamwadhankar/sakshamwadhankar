import re

with open('m.md', 'r', encoding='utf-8') as f:
    m_lines = f.read()

with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

# We know the first section is bounded by <!-- SECTION 1... --> and <!-- SECTION 2... -->
start_marker = "<!-- ═══════════════════════════════════════════════════════════════\n     SECTION 1 — ASCII PORTRAIT + TERMINAL INFO PANEL\n     ═══════════════════════════════════════════════════════════════ -->"
end_marker = "```js"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_section = f"{start_marker}\n\n```\n{m_lines}\n```\n\n<br/>\n\n"
    text = text[:start_idx] + new_section + text[end_idx:]

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(text)
