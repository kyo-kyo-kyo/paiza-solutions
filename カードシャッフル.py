N,M,K = map(int,input().split())
cards = [i for i in range(1,N+1)]
#print(N,M,K,cards)

for k in range(K):
    
    set_cards = []
    shuffle_cards = []
    
    for i in range(0,N,M):
        slice_cards = []
        if N - i < M :
                #slice_cards = [cards[k] for k in range(N-i)]
                set_cards.append([cards[i+k] for k in range(N-i)])
        else:
                set_cards.append(cards[i:i+M])
    
    for item in reversed(set_cards):
        shuffle_cards.append(item)
        
    #print(shuffle_cards)
    
    cards = [i for row in shuffle_cards for i in row]
for i in cards:
    print(i)
    
"""N, M, K = map(int, input().split())

# カードを初期化（1〜N）
cards = list(range(1, N + 1))

# K回シャッフルを繰り返す
for _ in range(K):
    # M枚ずつ分割
    groups = [cards[i:i + M] for i in range(0, N, M)]
    # 分割したグループを逆順に積み直す
    cards = [num for group in reversed(groups) for num in group]

# 結果を出力
print(*cards, sep="\n")
"""