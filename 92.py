head = None
tmp_list = []
while head:
    tmp_list.append(head.val)
    head = head.next

reverse_queue = tmp_list[left-1,right-1].reverse()
new_list = tmp_list[:left] + reverse_queue + tmp_list[right-1:]

val = new_list.popleft()
head = ListNode()
head.val = val
cur = head

while new_list:
    val = new_list.popleft()
    tmp_node = ListNode()
    tmp_node.val = val
    cur.next = tmp_node
    cur = cur.next