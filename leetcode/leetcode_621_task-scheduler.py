# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         result = 0
#         counter = Counter(tasks)
#         while True:
#             sub_task = 0 # 몇개를 뺄지
#             for task,_ in counter.most_common(n+1):
#                 result += 1 # 얼마나 지났나
#                 sub_task += 1  # 겹치는것이 얼마인지 확인하려고

#                 counter.subtract(task)
#                 counter+=Counter()

#             if not counter:
#                 break

#             result += n - sub_task + 1 # idle check

#         return result
