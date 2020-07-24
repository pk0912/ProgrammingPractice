T = int(input())
N = []
A = []
for t in range(T):
    n = int(input())
    N.append(n)
    a = input().split()
    A.append([int(i.strip()) for i in a])
for i in range(len(N)):
    total_sum = N[i]
    given_sum = 0
    for j in range(len(A[i])):
        total_sum += j + 1
        given_sum += A[i][j]
    print(total_sum - given_sum)
