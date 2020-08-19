from collections import deque

T = int(input())
A = []
for _ in range(T):
    A.append(input().strip())
for expr in A:
    stack = deque()
    print_flag = False
    traversed_length = 0
    for c in expr:
        if c in ['(', '{', '[']:
            stack.appendleft(c)
        else:
            if not stack:
                print("not balanced")
                print_flag = True
                break
            else:
                popped_char = stack.popleft()
                if c == ")":
                    if popped_char != "(":
                        print("not balanced")
                        print_flag = True
                        break
                elif c == "]":
                    if popped_char != "[":
                        print("not balanced")
                        print_flag = True
                        break
                else:
                    if popped_char != "{":
                        print("not balanced")
                        print_flag = True
                        break
        traversed_length += 1
    if len(stack) > 0:
        if not print_flag:
            print("not balanced")
    else:
        if traversed_length == len(expr):
            print("balanced")
