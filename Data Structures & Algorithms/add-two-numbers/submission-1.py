# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry == 1:
            if not l1:
                l1_val = 0
            else:
                l1_val = l1.val
                l1 = l1.next
            
            if not l2:
                l2_val = 0
            else:
                l2_val = l2.val
                l2 = l2.next
            
            current_val = l1_val + l2_val + carry

            if current_val >= 10:
                current_val -= 10
                carry = 1
            else:
                carry = 0

            current.next = ListNode(current_val)
            current = current.next

        return dummy.next