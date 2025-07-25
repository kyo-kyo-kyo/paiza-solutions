N,M = list(map(int,input().split()))
jan = []
for i in range (M):
    jan.append(list(map(int,input().split())))

print(N,M,jan)

for i in range(M-1):
    if jan[i][0] == jan[i+1][1]:
        del jan[i+1][1]
        jan[i+1].extend(jan[i])
        print(jan) 
print(jan)
max_len = 0
max_tie = []
for i in range(M):
    if max_len == len(str(jan[i])):
        max_tie.append(jan[i][0])
        print("a",len(str(jan[i])),max_len,max_tie,i)
    elif max_len < len(str(jan[i])):
        max_len = jan[i][0]
        max_tie = []
        max_tie.append(jan[i][0])
        print("b",len(str(jan[i])),max_len,max_tie,i)


for i in range(len(max_tie)):
    
    print(f"{max_tie[i]}")
        
    
        
        
        
# リストを調べ、前の番号と後ろの番号が同じものを見つける
# 最後の要素を削除し、リストの内容ごとくっつける
# 最終的に文字数が一番多いところを表示
# #