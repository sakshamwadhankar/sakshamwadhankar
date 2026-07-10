with open('ascii-art (1).txt', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

# Find the minimum leading spaces for non-empty lines
min_indent = min(len(line) - len(line.lstrip()) for line in lines if line.strip())

# Remove the minimum indent and strip trailing whitespace to make it clean
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

ascii_text = '\n'.join(clean_lines)

# Now read README.md and put it back
with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = "<!-- ═══════════════════════════════════════════════════════════════\n     SECTION 1 — ASCII PORTRAIT + TERMINAL INFO PANEL\n     ═══════════════════════════════════════════════════════════════ -->"
end_marker = "<br/>\n\n```js"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    # Use standard markdown code block
    new_section = f"{start_marker}\n\n```text\n{ascii_text}\n```\n\n"
    text = text[:start_idx] + new_section + text[end_idx:]

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Reverted to text and optimized spacing.")
