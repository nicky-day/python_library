from fileinput import filename
import os
import pathlib


def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        if os.path.isdir(filepath):
            search(filepath)
        elif os.path.isfile(filepath):
            name, ext = os.path.splitext(filepath)
            if ext == ".py":
                print(filepath)


search("c:\projects\pylib")


def search(dirname):
    for p in pathlib.Path(dirname).rglob("*.py"):
        print(p)


search("c:\projects\pylib")
