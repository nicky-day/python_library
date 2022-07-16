import itertools

students = ["한민서", "황지민", "이영철", "이광수", "김승민"]
rewards = ["사탕", "초콜릿", "젤리"]

results = itertools.zip_longest(students, rewards, fillvalue="새우깡")
print(list(results))
