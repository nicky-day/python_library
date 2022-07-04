import textwrap

text = textwrap.shorten(
    "Life is too short, you need python", width=15, placeholder="..."
)
print(text)
