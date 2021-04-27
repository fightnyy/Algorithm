"""
dfs 를 활용한 풀이

모든 코스는 "JFK"로 시작하기 떄문에 JFK를 시작 값으로 넣어준다.
만약 값이 코스가 여러개가 가능하다면 사전 순으로 리턴하라는 조건이 있다.
또한 조건으로 티켓은 모두 사용되어야 하고 또한 사용이 안되는 경우는 없음
즉 [JFK,  KUL],[JFK,  NRT],[NRT,  JFK] 라는 입력이 주어졌다고 생각해보면
JFK -> NRT -> JFK -> KUL 과 
"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = []
        graph = collections.defaultdict(list)
        for f, t in sorted(tickets, reverse=True):
            graph[f].append(t)

        def _dfs(cos):
            while graph[cos]:
                _dfs(graph[cos].pop())
            answer.append(cos)

        _dfs("JFK")

        return answer[::-1]
