# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        dummy1 = ListNode(0)
        dummy2 = ListNode(0)

        curr1 = dummy1
        curr2 = dummy2

        curr = head
        idx = 1

        while curr:
            if idx % 2 == 0:
                curr2.next = curr
                curr2 = curr2.next
                curr = curr.next
                idx += 1
            else:
                curr1.next = curr
                curr1 = curr1.next
                curr = curr.next
                idx += 1
        curr2.next = None
        curr1.next = dummy2.next
        
        return dummy1.next

