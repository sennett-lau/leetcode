class ListNode(object):
    def __init(self, val=0, next=None):
        self.val = val
        self.next= next

def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    x = 0
    r = ListNode(0)
    p = r

    while (l1 or l2 or x):
        v1 = l1.val if l1 is not None else 0
        v2 = l2.val if l2 is not None else 0

        tmp = x + v1 + v2
        v = tmp % 10
        x = tmp // 10

        p.next = ListNode(v)
        p = p.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return r.next