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