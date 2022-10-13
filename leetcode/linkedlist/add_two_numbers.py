from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cf = 0
        l1_head = l1
        l2_head = l2
        prev = l1
        while l1 and l2:
            prev = l1
            l1.val += l2.val + cf
            if l1.val > 9:
                cf = 1
                l1.val -= 10
            else:
                cf = 0
            l2.val = l1.val
            l1 = l1.next
            l2 = l2.next
        if l1:
            prev = l1
            while l1 and cf != 0:
                prev = l1
                l1.val += cf
                if l1.val > 9:
                    cf = 1
                    l1.val -= 10
                else:
                    cf = 0
                l1 = l1.next
            if cf != 0:
                prev.next = ListNode(cf)
            return l1_head
        elif l2:
            prev = l2
            while l2 and cf != 0:
                prev = l2
                l2.val += cf
                if l2.val > 9:
                    cf = 1
                    l2.val -= 10
                else:
                    cf = 0
                l2 = l2.next
            if cf != 0:
                prev.next = ListNode(cf)
            return l2_head
        else:
            if cf != 0:
                prev.next = ListNode(cf)
            return l1_head


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    print(Solution().addTwoNumbers(l1, l2))
