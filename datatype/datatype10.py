import bisect

result = []

for score in [33, 99, 77, 70, 89, 90, 100]:
    pos = bisect.bisect_left([60, 70, 80, 90], score)
    grade = "FDCBA"[pos]
    result.append(grade)

print(result)

a = [60, 70, 80, 90]
bisect.insort(a, 85)
print(a)
