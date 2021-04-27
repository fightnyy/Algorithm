"""
itertools.permutations 를 사용한 방법
"""


class Solution:
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))


"""
dfs를 사용한 방법
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        answer : 정답을 의미하는 list
        new_list : dfs가 호출될때마다 한개씩 적어진 element로 초기화 되는값 결국 0이면 모든것을 prev_list에 주었다는것을 의미
        prev_list : nums를 하나씩 추가해가면서 문제해결하는것 결국 new_list의 len이 0이면 복사해서 answer에 추가
        복사하는 이유는 복사안하면 prev_list가 dfs해가면서 변화하기 때문에 주소보다는 값을 준다고 생각
        그런데 _dfs해서 나가면 prev_list 가장 마지막에 들어갔던것을 pop 해야함 예를 들어 1,2,3이 들어왔을때
        1,2,3이 결국 다되면 우선 마지막 즉 3이 들어오고 이제 _dfs나갈때 3 빼고
        그다음에 e가 2일때 어차피 2 이제 끝나고 그다음 e가 3일 때로 바뀔때 1,3,2가 되려면 prev_list가 1이 되어야하니까
        또 pop이 됨
        """
        prev_list = []
        answer = []

        def _dfs(elements):

            if len(elements) == 0:
                answer.append(prev_list[:])

            for e in elements:
                new_elements = elements[:]
                prev_list.append(e)
                new_elements.remove(e)
                _dfs(new_elements)
                prev_list.pop()

        _dfs(nums)

        return answer
