# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def is_continue(h):
            for _ in range(k):
                if h:
                    h = h.next
                else:
                    return False
            return True

        tmp = ListNode(None)
        sub = tmp

        while is_continue(head):
            end = head
            for _ in range(k):
                next_node = head.next
                head.next = sub.next
                sub.next = head
                head = next_node
            sub = end

        sub.next = head
        return tmp.next