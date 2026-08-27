# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # base cases
        if not head:
            return False
        if not head.next:
            return True
        
        lst = []
        curr = head 
        while curr:
            lst.append(curr.val)
            curr = curr.next
        n = len(lst)
        i = 0
        j = n - 1
        while i <= j:
            if lst[i] == lst[j]:
                i += 1
                j -= 1
            else:
                return False

        return True