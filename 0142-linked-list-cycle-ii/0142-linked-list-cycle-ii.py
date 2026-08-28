# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case
        if not head:
            return head
        if not head.next:
            return None
        # Step 1: Detect the cycle

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        # No cycle
        if slow != fast:
            return None

        # Step 2: Find the beginning of the cycle
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow