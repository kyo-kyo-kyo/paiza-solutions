def change_def(change_add,change_reduce,change_move):
    change_add = [
    [8],#0
    [7],#1
    [],#2
    [9],#3
    [],#4
    [6,9],#5
    [8],#6
    [],#7
    [],#8
    [8]#9
    ] 

    change_reduce = [
    [],#0
    [],#1
    [],#2
    [],#3
    [],#4
    [],#5
    [5],#6
    [1],#7
    [0,6,9],#8
    [3,5]#9
    ]

    change_move = [
    [6,9],#0
    [],#1
    [3],#2
    [2,5],#3
    [],#4
    [3],#5
    [0,9],#6
    [],#7
    [],#8
    [0,6]#9
    ]

    if change_move[i] != None:
        for v in change_move:
            S_copy = S
            S_copy[j] = v
            print(S_copy)
    elif change_add[i] != None:
        for v in change_reduce:
            if v != None:
                S_copy = S
                S_copy[j] = v
                print(S_copy)     
    
    
S = list(input())
S = int(S)


for i in range(10):#0~9まで
    change_S = []
    S_copy = S
    for j in range(len(str(S))):
        if S[j] == i:
            
            
# 数字それぞれに変わりうる数字を設定する
# その設定は「取り除くだけで完成する数字」「ほかの数字と協力しないと完成しない数字」が存在する
# 最初にchange_moveに存在している変更できる数字を変えて出力していく
# 次にaddとreduceの中からマッチ棒を交換し合える組み合わせを探しそれによって変更された数字を出力する
# #