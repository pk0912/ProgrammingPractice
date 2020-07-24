from collections import deque


class StackUnderflowError(Exception):
    def __str__(self):
        return "Stack Underflow Error"


class Stack:
    def __init__(self, max_size):
        self.stack = deque()
        self.max_size = max_size

    def get_max_size(self):
        return self.max_size

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def push(self, element):
        if self.size() == self.max_size:
            raise OverflowError("Stack overflow error")
        self.stack.appendleft(element)

    def pop(self):
        if self.size() == 0:
            raise StackUnderflowError()
        return self.stack.popleft()

    def top(self):
        if self.is_empty():
            return None
        return self.stack[0]


st = Stack(3)
st.push(1)
st.push(2)
st.push(3)
# st.push(4)  # This will lead to stack overflow exception
print(st)
print(st.size())
print(st.top())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.is_empty())
# print(st.pop())  # This will lead to stack underflow exception
