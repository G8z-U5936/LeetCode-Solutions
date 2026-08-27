# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        first = dummy 
        second = dummy

        for _ in range(n+1):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        return dummy.next
        # t.c ------ o(L)
        # s.c ---------- o(1) -- no extra space used
        
# 3rd approach --- using only n<n and then temp.next = temp.next.next. only single pointer is enough for this approach:
#  n+1 -- only works in two pointer to reach the n-1th node.

        lenght = head
        temp = head
        while temp:
            lenght += 1
            temp = temp.next
            
        if n == lenth:
            return head.next
        
        temp = head
        for _ in range(length-n-1):
            temp = temp.next

        temp.next = temp.next.next

        return head












