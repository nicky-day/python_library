import itertools

it = itertools.combinations(range(1, 46), 6)

# for num in it:
#     print(num)

print(len(list(it)))

# 로또번호가 중복을 허용할 때
print(len(list(itertools.combinations_with_replacement(range(1, 46), 6))))
