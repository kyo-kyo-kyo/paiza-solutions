S = list(map(int,input().split()))
N = S[0]
M = S[1]
K = S[2]
for _ in range(N):
    A = list(map(int,input().split()))
    point = A.count(K)
    print(point)
    