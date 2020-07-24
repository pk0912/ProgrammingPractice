T = int(input())
N = []
A = []
for t in range(T):
    n = int(input().strip())
    N.append(n)
    a = input().split()
    A.append([int(i.strip()) for i in a])
for i in range(len(N)):
    start = 0
    current_sum = 0
    max_sum = A[i][start]
    j = 1
    while j <= N[i]:
        if current_sum + A[i][j - 1] >= 0:
            current_sum += A[i][j - 1]
            if current_sum > max_sum:
                max_sum = current_sum
        else:
            start = j
            current_sum = 0
        j += 1
    print(max_sum)
