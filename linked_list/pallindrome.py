from linked_list.linked_list_implementation import LinkedList, Node


def is_palindrome(head: Node) -> bool:
    if head is None:
        return False
    if head.next is None:
        return True
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    second_half = slow.next
    prev_node = None
    curr_node = second_half
    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    while prev_node is not None:
        if prev_node.data != head.data:
            return False
        prev_node = prev_node.next
        head = head.next
    return True


ll = LinkedList([1, 2, 2, 1])
print(is_palindrome(ll.head))
