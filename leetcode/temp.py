a = [1, 2, 3, 4]
b = [1, 2, 2]
from collections import Counter

counter = Counter(a)
counterb = Counter(b)
for q in counter.most_common(4):
    counter.subtract(q)
    print("e")  # 2
# print(counter.subtract(counterb))
# counter.subtract(counterb)
# print("what is counter : ",counter)
# counter+=Counter()
# print(counter)
# print(counter.most_common(4))
# for _ in a:
#     if _ == 1:
#         a.remove(_)
#         a.remove(2)
#     print("hello")
#     print(_)
#     print(a)
