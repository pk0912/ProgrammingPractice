from collections import deque
T = int(input())
N = []
A = []
for _ in range(T):
    n = input().strip()
    a = input().strip()
    N.append(int(n))
    A.append([int(i) for i in a.split()])
for i in range(T):
    output = dict()
    stack = deque()
    for num in A[i]:
        while 1:
            if stack:
                if num > stack[0]:
                    output[stack.popleft()] = num
                else:
                    break
            else:
                break
        stack.appendleft(num)
        output[num] = -1
    for j in A[i]:
        print(output[j], end=" ")
    print()
