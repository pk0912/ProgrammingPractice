import heapq
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListWrapper:
    def __init__(self, list_node):
        self.list_node = list_node

    def __lt__(self, other):
        if self.list_node and other.list_node:
            return self.list_node.val < other.list_node.val
        return False


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        heapq.heapify(min_heap)
        output = None
        curr = None
        for l in lists:
            if l:
                t = (l.val, ListWrapper(l.next))
                heapq.heappush(min_heap, t)
        while min_heap:
            val, list_node = heapq.heappop(min_heap)
            if output:
                output.next = ListNode(val)
                output = output.next
            else:
                output = ListNode(val)
                curr = output
            if list_node.list_node:
                heapq.heappush(min_heap, (list_node.list_node.val, ListWrapper(list_node.list_node.next)))
        return curr


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(-2)
    list3 = ListNode(-3, ListNode(-2, ListNode(1)))
    output_list = Solution().mergeKLists([[], list2, list3])
    while output_list:
        print(output_list.val)
        output_list = output_list.next
