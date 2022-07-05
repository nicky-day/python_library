text = "Life is too short, You need python."

d = dict()
for key in text:
    if key not in d:
        d[key] = 0
    d[key] += 1


print(d)

from collections import defaultdict

text = "Life is too short, You need python."

d = defaultdict(int)

for key in text:
    d[key] += 1

print(dict(d))
