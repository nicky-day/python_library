from collections import deque

a = [1, 2, 3, 4, 5]
q = deque(a)
q.rotate(2)
result = list(q)
print(result)


d = deque([1, 2, 3, 4, 5])
d.append(6)
print(d)
d.appendleft(0)
print(d)
print(d.pop())
print(d)
d.popleft()
print(d)
