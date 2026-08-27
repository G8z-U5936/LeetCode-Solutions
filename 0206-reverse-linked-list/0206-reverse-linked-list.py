# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        # temp = 
     
        while curr:
            next_temp = curr.next
            curr.next = prev
  
            prev = curr 
            curr = next_temp
# tc:o(n)  
        # new_haed
        return prev

# 2nd approach:-------------------(using array)----------------------tc:o(n)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        curr = head
        while curr:
            curr.val = arr.pop()
            curr = curr.next
        
        return head
        
        
        










        















# 3rd approach using stack:
#         # Convert linked list to array
#         arr = []
#         temp = self.head
#         while temp:
#             arr.append(temp.val)
#             temp = temp.next
        
#         # Reverse the array
#         arr.reverse()
        
#         # Recreate linked list from reversed array
#         self.head = None
#         self.size = 0
        
#         for val in arr:
#             self.addAtTail(val)