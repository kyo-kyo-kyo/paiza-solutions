N = int(input())

memo = {}

def climb(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    
    if N in memo:
        return memo[N]
    
    memo[N] = climb(N-1) + climb(N-2)
    return memo[N]

print(climb(N))