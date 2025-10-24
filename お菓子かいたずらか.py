N,M,K = map(int,input().split())
angry_boys = []
for _ in range(M):
    angry_boys.append(int(input()))

print(N,M,K,angry_boys)
sweets = 0
wow = 0
for i in range(1,N+1):
    
        if i in angry_boys :
            wow += 1
        else:    
            sweets += 1
            wow = 0
            
        if wow == K :
            break
        
print(sweets)