# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # dummy = ListNode(0)
        # dummy.next = head
        # curr = dummy
        # while curr:
            # if curr.next == node:
            #     curr.next = curr.next.next
            #     curr = curr.next
            # else:
            #     curr = curr.next

        
        
        node.val = node.next.val
        node.next = node.next.next
                