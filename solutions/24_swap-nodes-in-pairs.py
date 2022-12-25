# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        prev, curr, r = None, head, head.next

        while curr and curr.next:
            adj = curr.next
            if prev:
                prev.next = adj

            curr.next, adj.next = adj.next, curr
            prev, curr = curr, curr.next

        return r or head