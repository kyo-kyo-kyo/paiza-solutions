def wall_search(up,down,left,right):
    
    wall_info = []#調べた壁の上下左右の情報
    
    if up not in un_up:
        wall_info.append(1)
    else:
        wall_info.append(0)
            
    if down not in un_down:
        wall_info.append(1)
    else:
        wall_info.append(0)
        
    if left not in un_left:
        wall_info.append(1)
    else:
        wall_info.append(0)
            
    if right not in un_right:
        wall_info.append(1)
    else:
        wall_info.append(0)

    return wall_info
    """return [
        1 if up not in un_up else 0,
        1 if down not in un_down else 0,
        1 if left not in un_left else 0,
        1 if right not in un_right else 0
    ]"""
    
def wall_change():
    
        if wall_info == [0,0,1,1]:
            return "1"
        elif wall_info == [1,1,0,0]:
            return "2"
        elif wall_info == [1,0,0,1]:
            return "3"
        elif wall_info == [0,1,0,1]:
            return "4"
        elif wall_info == [0,1,1,0]:
            return "5"
        elif wall_info == [1,0,1,0]:
            return "6"
        else:
            return "?"
    

N = int(input())#遺跡の縦横の広さ

walls = []#壁
for _ in range(N):
    walls.append(list(input()))

#print(N,walls)#確認

#各方向にあってはならない壁
un_up = ["0","1","3","6"]
un_down = ["0","1","4","5"]
un_left = ["0","2","5","6"]
un_right = ["0","2","3","4"]


for i in range(N):#行の壁のインデックス

    
    for j in range(N):#列の壁のインデックス
        
        if walls[i][j] == "7":
            up = walls[i-1][j] if i > 0 else "0"
            down = walls[i+1][j] if i < N-1 else "0"
            left = walls[i][j-1] if j > 0 else "0"
            right = walls[i][j+1] if j < N-1 else "0"
        
            wall_info = wall_search(up,down,left,right)
            #print(wall_info)
            wall_info = wall_change()
            #print(wall_info)
            walls[i][j] = wall_info
            
for wall in walls:
    print(*wall,sep="")
        
        
    
        
#７（壊れている壁）を探す
#上下左右、どこに壁があるか調べる（上から時計回りに1，2，3，4など番号を振る）
#７（壊れている壁）を対応した壁に置き換える
#最後まで調べ切ったらループ終わり
#
#
#
#
#