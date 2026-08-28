# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # --- edge cases---
        # Empty list or one node
        if not head:
            return head
        if not head.next or k == 0:
            return head
            
        # Find the length
        length = 1
        current = head

        while current.next:
            current = current.next
            length += 1

        # Avoid unnecessary rotations
        k = k % length

        # Rotate k times
        for i in range(k):

            current = head

            # Find second-last node
            while current.next.next:
                current = current.next

            # Store last node
            new_node = current.next

            # Remove last node
            current.next = None

            # Put last node at the front
            new_node.next = head
            head = new_node

        return head
        

















# -------------------2nd method ---------------
        # for i in range(k):

        #     current = head
        #     while current.next.next:
        #         current = current.next

        #     new_node = current.next

        #     current.next = None

        #     new_node.next = head
    
        #     head = new_node
    
        # return head
            
    
                
    