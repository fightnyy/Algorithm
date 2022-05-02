import sys
from typing import List
from copy import deepcopy


def minCostConnectPoints(points: List[List[int]]) -> int:
    """
    Input: points = [[3,12],[-2,5],[-4,1]]
    Output: 18
    """
    n_points = len(points)
    x_distances = [[sys.maxsize] * n_points for _ in range(n_points)]
    y_distances = deepcopy(x_distances)
    distances = deepcopy(x_distances)
    visited = [False] * n_points
    result = 0

    for idx in range(n_points):
        for jdx in range(n_points):
            if idx == jdx:
                continue
            x_distances[idx][jdx] = abs(points[idx][0] - points[jdx][0])
            y_distances[idx][jdx] = abs(points[idx][1] - points[jdx][1])
            distances[idx][jdx] = x_distances[idx][jdx] + y_distances[idx][jdx]

    print(f"distance : {distances}")
    for idx in range(n_points):
        while not visited[idx]:
            min_at_point = min(distances[idx])
            min_val_idx = distances[idx].index(min_at_point)
            if not (visited[min_val_idx] and visited[idx]):
                visited[idx] = True
                visited[min_val_idx] = True
                result += min_at_point
                break
            else:
                print("a")
                distances[idx][min_val_idx] = sys.maxsize
    print(f"final distance : {distances}")
    return result


if __name__ == "__main__":
    points = [[2, -3], [-17, -8], [13, 8], [-17, -15]]
    print(minCostConnectPoints(points))
