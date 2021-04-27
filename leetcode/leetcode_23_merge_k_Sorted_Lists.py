# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # result는 다른 노드를 횡단해야해서 root 는 정답으로 return 할때
        result = root = ListNode()

        # heap은 default로 minHeap임
        heap = []
        """        
        heap에 저장되는 형태는 저렇게 튜플 형태로 저장됨.
        여기서 맨처음은 우선순위임
        idx를 넣어주는 이유는 만약 value가 같을때
        즉, 우선순위가 같을때, 그다음에 오는것에 
        default comparison way가 없으면 error 가 발생됨
        따라서 idx는 int값이기 때문에 lists[idx].value값이 같아도 idx의 값이 
        무조건 다르기 때문에 이를 기준으로 또 우선순위를 나누면 됨
        """
        for idx in range(len(lists)):
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx, lists[idx]))
        """
        모든 힙이 다 나오면 다 정렬이 된것
        __초기값__만 잘 생각해보면 알 수 있다.
        __초기값__에는 앞의 예시로 생각해보면 result.next의 값으로 1이 나온것을 알 수 있다.
        그런데 이제 1뒤에의 next가 있는데 이값들도 다 넣어줘서 다시 min_heap()과정을 거친다.
        이때 idx는 0 ,1, 2중에 하나인데 이는 만약에 1의 뒤에 2의 처음값과 같으면 다시
        break가 걸리는 것을 idx가 이를 방지해준다.
        그리고 result = result.next를 해줌으로서 result를 이동하고 여기서 next가 있는것
        을 확인해주는 절차를 거친다.
        """
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next
