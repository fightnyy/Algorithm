"""
내풀이
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        candidate_list = list()
        ttlist = []  # gas, cost
        for idx in range(len(gas)):
            ttlist.append([gas[idx], cost[idx]])

        for tt in ttlist:
            if tt[0] >= tt[1]:
                candidate_list.append(tt)

        for cnd in candidate_list:
            current_node = ttlist.index(cnd)
            visited = []
            have_gas = 0
            while True:
                have_gas += ttlist[current_node][0]
                visited.append(current_node)
                if have_gas - ttlist[current_node][1] < 0:
                    break
                if len(visited) == len(ttlist):
                    return ttlist.index(cnd)
                have_gas -= ttlist[current_node][1]
                current_node += 1
                current_node %= len(ttlist)
        return -1


"""
모든 주유소 탐색
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start in range(len(gas)):
            fuel = 0
            can_travel = True
            for happend in range(start, len(gas) + start):
                idx = happend % len(gas)

                if gas[idx] + fuel < cost[idx]:
                    can_travel = False
                    break
                else:
                    fuel += gas[idx] - cost[idx]

            if can_travel:
                return start
        return -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):

            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start
