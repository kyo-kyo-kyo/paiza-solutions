v = input().split()
H,W = int(v[0]),int(v[1])
S = []
for _ in range(H):
    S.append(list(input()))
    
Donut_point = 0

for i in range(0,H-2):
    for j in range(0,W-2):   
        flag = True     
        if S[i][j:j+3] != ['#', '#', '#']:
            flag = False
        if S[i+1][j:j+3] != ['#','.','#']:
            flag = False
        if S[i+2][j:j+3] != ['#', '#', '#']:
            flag = False
        
        if flag:
            Donut_point = Donut_point + 1
    
print(Donut_point)