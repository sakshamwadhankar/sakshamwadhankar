import os

with open('ascii-art (1).txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

# Trim empty lines at start and end
while lines and not lines[0].strip():
    lines.pop(0)
while lines and not lines[-1].strip():
    lines.pop()

# Create SVG content
# We will use font-size 12px and dy 12px
# 70 characters wide * ~7.2px per char = ~504px width
char_width = 7.2
line_height = 12

width = int(max(len(line) for line in lines) * char_width) + 20
height = len(lines) * line_height + 20

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
for line in lines:
    line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    svg_content.append(f'    <text x="0" y="{y}" xml:space="preserve">{line}</text>')
    y += line_height

svg_content.append('  </g>')
svg_content.append('</svg>')

# Save to assets/ascii.svg
os.makedirs('assets', exist_ok=True)
with open('assets/ascii.svg', 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg_content))

print("SVG created at assets/ascii.svg")
