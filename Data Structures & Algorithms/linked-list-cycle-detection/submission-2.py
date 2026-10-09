# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False
        turtle = head

        hare = head.next

        while turtle and hare and hare.next:
            if turtle == hare:
                return True
            
            hare = hare.next.next
            turtle = turtle.next
        return False