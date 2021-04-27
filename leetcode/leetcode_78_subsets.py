"""
dfs로 풀이
설명 
8번쨰 줄은 공집합도 포함 되어야하기 때문에 처음부터 [](공집합) 은 넣어진두ㅏ.

그다음 처음으로 _dfs에 index 값으로 0을 넣어준다.
[1,2,3]이 nums 라고 가정하였을때
처음의 index 0 은 우선 입력에 들어가고 그 후에 answer로 [1], [1,2] , [1,2,3] [1,3] ,[2] , [2,3] ,[3] 으로 풀이된다. 
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]

        prev_list = []

        def _dfs(index):
            for e in range(index, len(nums)):
                prev_list.append(nums[e])
                answer.append(prev_list[:])
                print(answer)
                _dfs(e + 1)
                prev_list.pop()

        _dfs(0)
        return answer
