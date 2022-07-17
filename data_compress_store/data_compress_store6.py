import tarfile

# 여러 파일 합치기
with tarfile.open("mytext.tar", "w") as mytar:
    mytar.add("a.txt")
    mytar.add("b.txt")
    mytar.add("c.txt")

# 여러 파일 합치기
with tarfile.open("mytext.tar", "w:gz") as mytar:
    mytar.add("a.txt")
    mytar.add("b.txt")
    mytar.add("c.txt")

# 여러 파일 해제하기
with tarfile.open("mytext.tar") as mytar:
    mytar.extractall()

with tarfile.open("mytext.tar") as mytar:
    mytar.extract("a.txt")
