import heapq

if __name__ == "__main__":
    V, E = map(int, input().split())
    visited = [False] * V
    answer = 0
    q = []
    for i in range(E):
        start, end, cost = map(int, input().split())
        start -= 1
        end -= 1
        heapq.heappush(q,[cost, start, end]) #걸리는 시간, 시작점, 도착점
    while q:
        # import pdb; pdb.set_trace()
        tmp = heapq.heappop(q)
        for val in q : #val == 걸리는 시간, 시작점, 도착점
            tmp_list = []
            if tmp[2] == val[1] and not visited[val[1]]: #tmp의 도착점과 val의 시작점이 같고 val을 한번도 방문한적이 없으면
                tmp_list.append(val)

        for a in tmp_list:
            answer += a[0]
            heapq.heappush(q,[a[0],a[1],a[2]])
            visited[a[1]] = True
            visited[a[2]] = True
    print(visited)
    print(answer)

