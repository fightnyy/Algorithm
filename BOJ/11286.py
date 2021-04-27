import heapq
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())



    heap = []



    for _ in range(n):
        tmp = int(input())
        if tmp == 0:
            if not heap:
                print(0)
                continue
            min_v = heapq.heappop(heap)[1]
            print(min_v)
            while heap:
                if min_v == heap[0]:
                    heapq.heappop(heap)
                else:
                    break
        else :
            heapq.heappush(heap, [abs(tmp),tmp])
