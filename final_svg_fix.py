import os

with open('ascii-art (1).txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

# Find the minimum leading spaces for non-empty lines
min_indent = min(len(line) - len(line.lstrip()) for line in lines if line.strip())

# Remove the minimum indent and strip trailing whitespace
clean_lines = []
for line in lines:
    if line.strip():
        clean_lines.append(line[min_indent:].rstrip())
    else:
        clean_lines.append('')

# Trim top and bottom empty lines
while clean_lines and not clean_lines[0].strip():
    clean_lines.pop(0)
while clean_lines and not clean_lines[-1].strip():
    clean_lines.pop()

char_width = 7.2
line_height = 12

width = int(max(len(line) for line in clean_lines) * char_width) + 20
height = len(clean_lines) * line_height + 20

svg_content = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">',
    '  <style>',
    '    text {',
    '      font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;',
    '      font-size: 12px;',
    '      fill: #E6EDF3;',
    '    }',
    '  </style>',
    '  <g transform="translate(10, 15)">'
]

y = 0
for line in clean_lines:
    line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    svg_content.append(f'    <text x="0" y="{y}" xml:space="preserve">{line}</text>')
    y += line_height

svg_content.append('  </g>')
svg_content.append('</svg>')

os.makedirs('assets', exist_ok=True)
with open('assets/ascii.svg', 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg_content))

# Update README to use SVG
with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = "<!-- ═══════════════════════════════════════════════════════════════\n     SECTION 1 — ASCII PORTRAIT + TERMINAL INFO PANEL\n     ═══════════════════════════════════════════════════════════════ -->"
end_marker = "<br/>\n\n```js"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_section = f"{start_marker}\n\n<img src=\"assets/ascii.svg\" width=\"100%\" alt=\"ASCII Portrait\" />\n\n"
    text = text[:start_idx] + new_section + text[end_idx:]

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated SVG and README.")
