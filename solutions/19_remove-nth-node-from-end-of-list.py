# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        h, t = head, head

        for i in range(n):
            h = h.next

        if not h:
            return head.next

        while h.next:
            h = h.next
            t = t.next

        t.next = t.next.next

        return head
