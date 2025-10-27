N,M = map(int,input().split())#n作業回数を表す整数 m作物の種類を表す整数
H,W = map(int,input().split())#H畑の行数 w畑の列数
p_v = []
for _ in range(N):#[左上のｘ座標,左上のｙ座標,右下のｘ座標,右下のｙ座標,その時期植える作物の種類]
    p_v.append(list(map(int,input().split())))

field = []
for i in range(H):
    field.append([])
    for _ in range(W):
        field[i].append(0)
        
#print(N,M,H,W,p_v,field)

veg_count = []
for _ in range(M+1):
    veg_count.append(0)

for n in range(N):
    #print(n+1,"期目")
    for h in range(H):
        for w in range(W):
            if (p_v[n][0]-1) <= h <= (p_v[n][1]-1) and (p_v[n][2]-1) <= w <= (p_v[n][3]-1):
                #print((p_v[n][0]-1),"<=",h,"<=",(p_v[n][1]-1),"and",(p_v[n][2]-1),"<=",w,"<=",(p_v[n][3]-1))
                veg_count[field[h][w]] += 1
                #print(field[h][w],"は",veg_count[field[h][w]],"つ収穫")
                field[h][w] = p_v[n][4]
                
#print(veg_count,field)

for i in veg_count[1:]:
    print(f"{i}")

new_field = []
for h in range(H):
    new_field.append([])
    for w in range(W):
        if field[h][w] == 0:
            field[h][w] = "."
            new_field[h].append(field[h][w])
        else:
            new_field[h].append(str(field[h][w]))
            
    #print(new_field)

for i in range(H):
    print("".join(new_field[i]))
        