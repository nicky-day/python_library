import glob
import os
import shutil
import pathlib
import collections

for file_path in glob.glob("%s/*.txt" % os.getcwd()):
    parent = os.path.dirname(file_path)
    filename = os.path.basename(file_path)
    new_path = os.path.join(parent, "archive", filename)
    shutil.move(file_path, new_path)


for p in pathlib.Path.cwd().glob("*.txt"):
    new_p = p.parent.joinpath("archive", p.name)
    p.replace(new_p)


# 현재 디렉터리의 모든 파일을 조사하여 확장자별 개수 구하기
collections.Counter([p.suffix for p in pathlib.Path.cwd().iterdir()])
