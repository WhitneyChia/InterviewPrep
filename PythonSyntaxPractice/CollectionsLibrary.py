import collections

print("\n")
print("Default dict example list value")
ans = collections.defaultdict(list)
print(ans)
ans['Whitney'].append('Chia')
print(ans)
print(ans["Mandy"])

print("\n")
print("Default dict example int value")
ans = collections.defaultdict(int)
print(ans)
ans["W"] += 1
print(ans)

print("\n")
print("Counter Example")
test = "WhitneyChia"
print(collections.Counter(test))

print("\n")
print("Deque Example")
queue = collections.deque(["Whitney"])
queue.append("Mandy")
queue.append("Kenny")
print(queue)
first_in_pop = queue.popleft()
last_in_pop = queue.pop()
print(first_in_pop)
print(last_in_pop)
