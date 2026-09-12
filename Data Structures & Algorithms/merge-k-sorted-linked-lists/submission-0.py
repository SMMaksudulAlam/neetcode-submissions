# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq as hq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for i in range(len(lists)):
            if(lists[i]):
                hq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        
        dummy_head = ListNode()
        cur = dummy_head

        while(h):
            val, ind = hq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            if(lists[ind]):
                hq.heappush(h, (lists[ind].val, ind))
                lists[ind] = lists[ind].next
        
        return dummy_head.next
        