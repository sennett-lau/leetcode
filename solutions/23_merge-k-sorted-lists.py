# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        m = len(lists) // 2

        list1 = self.mergeKLists(lists[:m])
        list2 = self.mergeKLists(lists[m:])

        return self.mergeLists(list1, list2)

    def mergeLists(self, l1, l2):
        r = ListNode()
        p = r

        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next

            p = p.next

        p.next = l1 or l2

        return r.next