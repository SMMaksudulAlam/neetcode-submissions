# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def process(head):
            nonlocal k
            if(not head):
                return None
            cur = head
            count = 1
            while(count<k):
                if(cur):
                    cur = cur.next
                    count += 1
                else:
                    return head, None
            if(not cur):
                return head, None
            next_head = cur.next
            cur.next = None
            prev = None
            cur = head
            while(cur):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            return prev, next_head

        dummy = ListNode()
        dummy_cur = dummy
        cur = head
        while(cur):
            attach, cur = process(cur)

            dummy_cur.next = attach
            while(dummy_cur.next):
                dummy_cur = dummy_cur.next
        return dummy.next

            


