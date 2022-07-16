import glob

for filename in glob.glob("**/*.txt", recursive=True):
    print(filename)
