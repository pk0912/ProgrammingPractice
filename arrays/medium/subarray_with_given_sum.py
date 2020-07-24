# code
T = int(input())
N = []
S = []
A = []
for t in range(T):
    n, s = input().split()
    N.append(int(n))
    S.append(int(s))
    a = input().split()
    A.append([int(i) for i in a])
for i in range(len(N)):
    start = 0
    end = 0
    current_sum = A[i][0]
    j = 0
    while j < N[i]:
        if current_sum == S[i]:
            print(start + 1, end + 1)
            break
        elif current_sum < S[i]:
            end += 1
            if end < N[i]:
                current_sum += A[i][end]
            else:
                print(-1)
            j += 1
        else:
            current_sum -= A[i][start]
            start += 1
