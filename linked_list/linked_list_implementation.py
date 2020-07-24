class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self, data=[]):
        self.head = None
        nodes = iter(data)
        for node in nodes:
            self.append(node)

    def is_empty(self):
        return self.head is None

    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            for node in self:
                pass
            node.next = new_node

    def append_left(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    def __chk_index__(self, index):
        if index < 0:
            index = len(self) - abs(index)
            if index < 0:
                return 0
            return index
        return index

    def insert(self, index, element):
        index = self.__chk_index__(index)
        new_node = Node(element)
        node = self.head
        if index == 0:
            self.append_left(element)
        elif index >= len(self):
            self.append(element)
        else:
            for i in range(0, index - 1):
                node = node.next
            new_node.next = node.next
            node.next = new_node

    def add_after(self, target_element, element):
        if self.is_empty():
            raise Exception("Linked list is empty")
        new_node = Node(element)
        for node in self:
            if node.data == target_element:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception(f"Linked list does not have {target_element}")

    def add_before(self, target_element, element):
        if self.is_empty():
            raise Exception("Linked list is empty")
        new_node = Node(element)
        if self.head.data == target_element:
            return self.append_left(element)
        prev_node = self.head
        for node in self:
            if node.data == target_element:
                new_node.next = node
                prev_node.next = new_node
                return
            prev_node = node
        raise Exception(f"Linked list does not have {target_element}")

    def remove(self, element):
        if self.is_empty():
            raise Exception("Linked list is empty")
        if self.head.data == element:
            self.head = self.head.next
            return
        prev_node = self.head
        for node in self:
            if node.data == element:
                prev_node.next = node.next
                return
            prev_node = node
        raise Exception(f"Linked list does not have {element}")

    @staticmethod
    def __find_mid__(head):
        first = head
        second = head.next
        while second is not None and second.next is not None:
            first = first.next
            second = second.next.next
        return first

    def find_mid(self):
        if self.is_empty():
            raise Exception("Linked list is empty")
        return LinkedList.__find_mid__(self.head)

    def reverse(self):
        def handler(node):
            if node.next is None:
                self.head = node
                return node
            next_node = node
            head = handler(node.next)
            next_node.next = None
            head.next = next_node
            return next_node

        if self.head is None:
            return self
        handler(self.head)

    def reverse_in_group(self, group_size=0):
        def handler(node, k):
            prev_node = None
            curr_node = node
            next_node = None
            count = 0
            while curr_node is not None and count < k:
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node
                count += 1
            if next_node is not None:
                node.next = handler(next_node, k)
            return prev_node
        if group_size == 0:
            return
        self.head = handler(self.head, group_size)

    def rotate(self, count):
        node = self.head
        if count == 0 or node is None:
            return
        while node is not None and node.next is not None and count - 1 > 0:
            count -= 1
            node = node.next
        if node.next is None:
            return
        new_head = node.next
        node.next = None
        new_node = new_head
        while new_node.next is not None:
            new_node = new_node.next
        new_node.next = self.head
        self.head = new_head

    @staticmethod
    def __sorted_merge__(left, right, reverse):
        if left is None:
            return right
        if right is None:
            return left
        if reverse:
            if left.data >= right.data:
                result = left
                result.next = LinkedList.__sorted_merge__(left.next, right, reverse)
            else:
                result = right
                result.next = LinkedList.__sorted_merge__(left, right.next, reverse)
        else:
            if left.data <= right.data:
                result = left
                result.next = LinkedList.__sorted_merge__(left.next, right, reverse)
            else:
                result = right
                result.next = LinkedList.__sorted_merge__(left, right.next, reverse)
        return result

    def sort(self, reverse=True):
        def handler(head):
            if head is None or head.next is None:
                return head
            middle = LinkedList.__find_mid__(head)
            next_to_middle = middle.next
            middle.next = None
            left = handler(head)
            right = handler(next_to_middle)
            sorted_list = LinkedList.__sorted_merge__(left, right, reverse)
            return sorted_list
        self.head = handler(self.head)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __str__(self):
        return " ".join([str(node) for node in self])

    def __len__(self):
        node = self.head
        length = 0
        while node is not None:
            node = node.next
            length += 1
        return length


# ll = LinkedList(['a', 'b', 'c'])
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append_left(0)
# lls = LinkedList()
# lls.append_left(0)
# print(ll)
# print(len(ll))
# print(lls)
# print(len(lls))
# ll.insert(4, 'd')
# ll.insert(5, 'e')
# print(ll)
# print(len(ll))
# lls.insert(0, 1)
# print(lls)
# print(len(lls))
# lls.insert(-2, 4)
# print(lls)
# ll.insert(-1, 4)
# print(ll)
# ll.insert(-100, "start")
# print(ll)
# lls.insert(-2, 5)
# print(lls)
# lls.add_after(5, 6)
# print(lls)
# ll.add_after(3, "end")
# print(ll)
# ll.add_before("start", "ready")
# print(ll)
# ll.add_after("start", "go")
# print(ll)
# ll.add_before("end", 5)
# print(ll)
# ll.remove("ready")
# print(ll)
# print(len(ll))
# lls.remove(0)
# print(lls)
# lls.remove(4)
# print(lls)
# print(len(lls))
# ll2 = LinkedList([1, 2, 3, 4, 5])
# print(ll2)
# print(ll2.find_mid())
# ll2.reverse()
# print(ll2)
# ll3 = LinkedList([1, 2, 3, 4, 5])
# ll3.rotate(2)
# print(ll3)
# ll4 = LinkedList([1, 2, 3, 4, 5])
# print(ll4)
# ll4.reverse_in_group(3)
# print(ll4)
# ll5 = LinkedList([1, 2, 3, 4, 5, 6])
# print(ll5 is ll4)
# print(ll5.find_mid())
# ll4.sort()
# print(ll4)
# ll6 = LinkedList([2, 20, 40])
# ll6.sort()
# print(ll6)
# ll7 = LinkedList([1, 2, 2, 1, 2, 0, 2, 2])
# ll7.sort(reverse=False)
# print(ll7)
