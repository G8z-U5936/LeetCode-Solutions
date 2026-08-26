# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            # print("entire linked list is empty")
            return False

        if head.next is None:
            # print("there is a single node in the ll")
            return False
        
        
        curr = head
        second = head.next
        while second and second.next:
            curr = curr.next
            second = second.next.next

            if curr == second:
                return True
                
        return False
        
 



 
         



        