class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(l1, l2) :
    cout = 0
    plus_result_list = []
    while(l1 != None or l2 != None):        
        if (l1):
            a = l1.val
        else:
            a = 0
        if (l2):
            b = l2.val
        else :
            b= 0
        result = a + b + cout
        if(result>= 10):
            result = result - 10
            cout = 1
        else:
            cout = 0
        plus_result_list.append(result)
        l1 = l1.next
        l2 = l2.next

    list_node_list = [ListNode() for _ in range(len(plus_result_list))]
    for i in range(len(plus_result_list)):
        list_node_list[i].val = plus_result_list[i]
        if i == len(plus_result_list) -1:
            list_node_list[i].next = None
        else :
            list_node_list[i].next= list_node_list[i+1]
    import pdb;pdb.set_trace()
    return list_node_list[0];

if __name__ == "__main__":
    l1 = [ListNode() for _ in range(3)]
    l2 = [ListNode() for _ in range(3)]
    l1[0].val = 2
    l1[0].next = l1[1]
    l1[1].val = 4
    l1[1].next = l1[2]
    l1[2].val = 3 

    l2[0].val = 5
    l2[0].next = l2[1]
    l2[1].val = 6
    l2[1].next = l2[2]
    l2[2].val = 4

    solution(l1[0], l2[0])