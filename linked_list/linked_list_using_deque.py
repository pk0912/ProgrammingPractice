from collections import deque

llist = deque([1, 2, 3])

# insertion
# at end
llist.append("c")

# at beginning
llist.appendleft("a")

# in middle
llist.insert(1, "b")

print(llist)

# can be iterated
print(llist[0])  # First element
print(llist[-1])  # Last element
for i in llist:
    print(i)

# deletion
# at end
print(llist.pop())  # returns popped value

# at start
print(llist.popleft())  # returns popped value

# at any position
del llist[2]  # don't get deleted value; can result in IndexError: deque index out of range

# remove using values
llist.remove("b")  # returns None; can result in ValueError: deque.remove(x): x not in deque

print(llist)

print(llist.index(3, 1, 2))  # looks for value in the index range provided by 2nd and 3rd params

print(llist.count(1))

llist.pop()
print(llist[0])
llist.pop()
print(len(llist) == 0)
# print(llist[0])  # will result in IndexError: deque index out of range
# llist.pop() # will result in IndexError: pop from an empty deque

a = deque([1, 2, 3])
a.insert(-100, 4)
print(a[0])
