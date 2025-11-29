N = int(input())

senko = []

for i in range(N):
    senko.append(list(map(int,input().split())))
M = N*N // 4
print(senko,N,M)

right = N-1
bottom = N-1
left = 0
top = 0

senko_time = 0



for _ in range(4):
    
    now = M
    while now > 0:
        for i in range(left,right+1):
            if now == 0:
                break
            else:
                senko_time += senko[top][i]
                now -= 1
        top += 1
        
        for i in range(top,bottom+1):
            if now == 0:
                break
            else:
                senko_time += senko[i][right]
                now -= 1
        right -= 1
        
        for i in range(right,left-1,-1):
            if now == 0:
                break
            else:
                senko_time += senko[bottom][i]
                now -= 1
        bottom -= 1
        
        for i in range(bottom,top - 1,-1):
            if now == 0:
                break
            else:
                senko_time += senko[i][left]
                now -= 1
        left += 1
        
    print(senko_time)
        