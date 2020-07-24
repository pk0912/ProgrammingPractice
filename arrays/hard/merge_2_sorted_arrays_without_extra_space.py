T = int(input())
X = []
Y = []
P = []
Q = []
for t in range(T):
    x, y = input().split()
    X.append(int(x))
    Y.append(int(y))
    p = input().split()
    q = input().split()
    P.append([int(i) for i in p])
    Q.append([int(i) for i in q])
for i in range(len(X)):
    sorted_list = P[i] + Q[i]
    sorted_list = sorted(sorted_list)
    for j in sorted_list:
        print(j, end=" ")
    print()
