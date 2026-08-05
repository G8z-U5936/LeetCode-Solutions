# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # handle the first pair separately
        new_head = head.next
        prev = None
        curr = head

        while curr and curr.next:
            first = curr
            second = curr.next
            next_pair = second.next

            # swap two pairs
            second.next = first
            first.next = next_pair

            if prev:
                prev.next = second
            
            prev = first
            curr = next_pair

        return new_head

























