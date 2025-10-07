H,W = map(int,input().split())
N = int(input())

target = []
for _ in range(N):
    target.append(list(map(int,input().split())))

M = int(input())

strike = []
for _ in range(M):
    strike.append(list(map(int,input().split())))

#print(H,W,N,target,M,strike)
hit_point = 0
directions = [(-1,-1),(-1,0),(-1,1),
              (0,-1),       (0,1),
              (1,-1),(1,0),(1,1)]
for i in range(N):
    for j in range(M):
        r,c,p,q, = target[i]
        a,b = strike[j]
        if a == r and b == c:
            hit_point += p
            #print(hit_point,p,"a")
        else:
            for dr,dc, in directions:
                if a == r + dr and b == c + dc:
                    hit_point += q
                    #print(hit_point,q,"b")
                    break
                
print(hit_point)