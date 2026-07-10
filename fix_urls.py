with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace github-readme-stats with working alternative
text = text.replace('github-readme-stats.vercel.app', 'github-readme-stats-sigma-five.vercel.app')

# Comment out Trophies as the public instance is down
trophy_str = '<img src="https://github-profile-trophy.vercel.app/?username=sakshamwadhankar&theme=darkhub&no-bg=true&no-frame=false&column=7&margin-w=8&margin-h=8&title_color=00FF41&border_color=00FF41" width="90%" alt="Trophies"/>'
trophy_replacement = f'<!-- The github-profile-trophy service is currently down (402 Payment Required). -->\n<!-- {trophy_str} -->'
text = text.replace(trophy_str, trophy_replacement)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed broken URLs in README.md")
