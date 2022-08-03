import heapq

def solution(price):
    price_day_list = []
    heap = []
    answer = [-1] * len(price)

    price_day_list=[[p, idx+1] for idx, p in enumerate(price)]
        
    heapq.heappush(heap, price_day_list[0])

    last_price = price[0]
    for price_day in price_day_list[1:]:
        heapq.heappush(heap, price_day)
        while heap:
            min_price_heap = heap[0]
            if min_price_heap[0] < price_day[0]: # heap[0] = [price, day]
                heap_out_price_day = heapq.heappop(heap)
                ans = price_day[1] - heap_out_price_day[1]
                answer[min_price_heap[1]-1] = ans
            else:
                break

    return answer