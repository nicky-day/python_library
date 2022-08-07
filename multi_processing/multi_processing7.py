from re import T, sub
import subprocess

with open("out.txt", "wb") as f:
    out = subprocess.run(["ls", "-l"], capture_output=True, text=True)
    f.write(out.stdout)
ß
