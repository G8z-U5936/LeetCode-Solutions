# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = []
        big = []
# remember this is not a space efficient solution.sc -- 0(n)
        curr = head
        while curr:
            if curr.val < x:
                small.append(curr.val)
            else:
                big.append(curr.val)
            curr = curr.next
        
        arr = small + big

        dummy = ListNode(0)
        curr = dummy

        for value in arr:
            curr.next = ListNode(value)
            curr = curr.next
        
        return dummy.next
        
# space efficient solution --- 0(1):  --- by linked list ---- mst

        

