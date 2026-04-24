# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val <= list2.val:
            head = list1
            curr1 = head.next
            curr2 = list2
        else:
            head = list2
            curr1 = list1
            curr2 = head.next
        
        tail = head

        while curr1 and curr2:

            if curr1.val <= curr2.val:
                tail.next = curr1
                tail = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                tail = curr2
                curr2 = curr2.next
        
        if curr1 == None:
            tail.next = curr2
        else:
            tail.next = curr1


        return head


        