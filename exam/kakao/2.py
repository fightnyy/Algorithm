from collections import deque
from pprint import pprint
def findP(MAP):
    p_location = []
    for row in range(len(MAP)):
        for col in range(len(MAP[0])):
            if MAP[row][col] == "P":
                p_location.append([row, col, 0])
    return deque(p_location)

def dfs(MAP,row, col, count, visited):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    tmp = 1
    for cr, cc in zip(dr, dc):
        next_row = row + cr
        next_col = col + cc
        next_count = count + 1 


        if next_count >= 3 or 0>next_row or next_row>=5 or 0>next_col or next_col>=5 or [next_row,next_col] in visited or MAP[next_row][next_col] == 'X':
            continue
        elif MAP[next_row][next_col] == 'P':
            return 0
        else :
            visited.append([row,col])
            tmp=dfs(MAP, next_row, next_col, next_count, visited)
        if tmp == 0:
                # print(next_row,next_col)
            break

        # print("After one iter")
    return tmp

def solution(places):
    answer = []
    for MAP in places:
        # stack 에 들어 있는것은 row, col, count
        p_location = findP(MAP)
        result = 1
        for row, col, count in p_location:
            result=dfs(MAP,row, col, count,[])
            # print("End at here")
            if result == 0:
                break
        answer.append(result)
        # print("\n\n\n\n\n")
    return(answer)


places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]

print(solution(places))
