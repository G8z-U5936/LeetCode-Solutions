# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head:
        #     return 
        # slow = head
        # fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # return slow

        # arr = []
        # curr = head 
        # while curr:
        #     arr.append(curr)
        #     curr = curr.next
        # curr.val is incorrect bcoz we have to return nodes not the value.so,arr.append(curr) is correct and arr.append(curr.val) is incorrrect for this questiom.
        # mid = len(arr) // 2
        # return arr[mid] 

        length = 0
        curr = head 
        while curr:
            length += 1
            curr = curr.next
        curr = head
        mid = length // 2
        for _ in range(mid):
            curr = curr.next
        return curr
        






        
        


