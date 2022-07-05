import itertools
import operator
import pprint

data = [
    {"name": "이민서", "blood": "O"},
    {"name": "이명순", "blood": "B"},
    {"name": "이상호", "blood": "AB"},
    {"name": "김지민", "blood": "B"},
    {"name": "최상현", "blood": "AB"},
    {"name": "김지아", "blood": "A"},
    {"name": "손우진", "blood": "A"},
    {"name": "박은주", "blood": "A"},
]

# data = sorted(data, key=operator.itemgetter("blood"))
grouped_data = itertools.groupby(data, key=operator.itemgetter("blood"))
# print(grouped_data)

result = {}
for key, group_data in grouped_data:
    result[key] = list(group_data)

pprint.pprint(result)
