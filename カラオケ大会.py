#def karaoke_index (max_point):

                 

N,M = map(int,input().split())

correct_Hz = []
for _ in range(M):
    correct_Hz.append(int(input()))

challenge_Hz = []
for _ in range(N):
    a = []
    
    for _ in range(M):
        a.append(int(input()))
    
    challenge_Hz.append(a)

#print(N,M,correct_Hz,challenge_Hz)

challenge_point = 0
for i in range(N):
    max_point = 100
    
    for j in range(M):
            diff = abs(correct_Hz[j] - challenge_Hz[i][j])
            if diff <= 5:
                max_point -= 0
            elif diff > 5 and diff <= 10:
                max_point -= 1
            elif diff > 10 and diff <= 20:
                max_point -= 2
            elif diff > 20 and diff <= 30:
                max_point -= 3
            else:
                max_point -= 5
    
    if challenge_point <= max_point:
        challenge_point = max_point
        
print(challenge_point)
    

