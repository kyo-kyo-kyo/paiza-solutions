H,W = list(map(int,input().split()))
field = []
for i in range(H):
    field.append(list(input()))
    
#print(H,W,field)
#爆弾のある行と列を記録
bomb_rows = set()
bomb_cols = set()

for i in range(H):#爆弾の位置を探す
    for j in range(W):
        if field[i][j] == "#":
            bomb_rows.add(i)
            bomb_cols.add(j)
            
#行と列を"#"に変える
for i in range(H):
    for j in range(W):
        if i in bomb_rows or j in bomb_cols:
            field[i][j] = "#"
            
count = 0

for i in range(H):
    for j in range(W):
        if field[i][j] == "#":
            count += 1
            
print(count)
        




# 爆弾(#)を探す
# field[i][全部]とfield[全部][i]を#にかえる
# 全て調べ終わったら終了#