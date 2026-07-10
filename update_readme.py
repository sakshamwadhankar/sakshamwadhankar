with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

# The ASCII art is between lines 15 and 51
# We can find it by looking for the first code block in SECTION 1
start_marker = "<!-- ═══════════════════════════════════════════════════════════════\n     SECTION 1 — ASCII PORTRAIT + TERMINAL INFO PANEL\n     ═══════════════════════════════════════════════════════════════ -->"
end_marker = "<br/>\n\n```js"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    # replace everything between start_marker and end_marker with our img tag
    new_section = f"{start_marker}\n\n<img src=\"assets/ascii.svg\" width=\"100%\" alt=\"ASCII Portrait\" />\n\n"
    text = text[:start_idx] + new_section + text[end_idx:]

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("README.md updated.")
