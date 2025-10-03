N,H,W,P,Q = map(int,input().split())
res = []
for _ in range(N):
    res.append(list(map(int,input().split())))
#print(N,H,W,P,Q,res)
all = []
for i in range(H):
    for j in range(W):
       all.append([i,j]) 

#print(all)

Abs_seat = []
for i in range(len(all)):
    Abs_number = abs(int(all[i][0]) - P) + abs(int(all[i][1]) - Q)
    Abs_seat.append(Abs_number)
    
#print(Abs_seat)
min_Abs = float("inf")
#for i in range(len(all)):
for i, seat in enumerate(all):
    if Abs_seat[i] < min_Abs and seat not in res:
        min_Abs = Abs_seat[i]

        """flag = True
        for j in range(N):
            if all[i][0] == int(res[j][0]) and all[i][1] == int(res[j][1]):
                flag = False
                
        if flag == True:"""
        
#print(min_Abs)

for i, seat in enumerate(all):
    if Abs_seat[i] < min_Abs and seat not in res:
        print(f"{seat[0]}",f"{seat[1]}")
"""for i in range(len(all)):
    flag = True
    if min_Abs == Abs_seat[i]:
        for j in range(N):
            if all[i][0] == int(res[j][0]) and all[i][1] == int(res[j][1]):
                flag = False
                
        if flag == True:
            print(f"{all[i][0]}", f"{all[i][1]}")"""