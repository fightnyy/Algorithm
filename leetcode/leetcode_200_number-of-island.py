import pdb

"""
1은 땅을 나타내고
0은 물을 나타낸다.
"""
"""
해당 문제를 푸는 메커니즘을 설명해보자면 연결된 부분은 다 0으로 만든다는 것이다. 즉 하나의 땅이 우선 1로 되어있으면 그 땅과 연결된 모든 땅을 
0으로 만들어서 물로 만든다 즉 더이상 쓸모없는 땅으로 만드는 것이다. 
"""

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]


def numIslands(grid) -> int:
    def dfs(i, j):
        """
        #더이상 땅이 아닌 경우 종료
        """
        pdb.set_trace()
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return

        grid[i][j] = 0

        """
        동서남북 검색
        """
        dfs(i + 1, j)  # 북
        dfs(i - 1, j)  # 남
        dfs(i, j + 1)  # 서
        dfs(i, j - 1)  # 동

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            """섬이면"""
            if grid[i][j] == "1":
                dfs(i, j)
                """
                모든 육지 탐색후 카운트 1 증가
                """
                count += 1
    return count


numIslands(grid)
