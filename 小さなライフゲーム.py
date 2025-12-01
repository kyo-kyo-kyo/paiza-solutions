S,T = input().split()
S,T = list(S),list(T)
#print(S,T)
new_S = S[:]
change_S = S[:]
S_memo = []
def lifegame(left,right):
    if new_S[left] == new_S[right] == "-":
        return T[0]
    elif new_S[left] == "-" and new_S[right] == "+":
        return T[1]
    elif new_S[left] == "+" and new_S[right] == "-":
        return T[2]
    elif new_S[left] == new_S[right] == "+":
        return T[3]
    else:
        return "ERROR"
    

    
point = 0
    

while 10000:
    for i in range(10):
        if i == 0:
            change_S[i] = lifegame(9,1)
            #print(1,change_S,i,change_S[i])
        elif i == 9:
            change_S[i] = lifegame(i-1,0)
            #print(2,change_S,i,change_S[i])
        else:
            change_S[i] = lifegame(i-1,i+1)
            #print(3,change_S,i,change_S[i])
            
    
    
    if S == change_S:
        print("YES")
        break
    elif change_S in S_memo:
        print("NO")
        break
    else:
        new_S = change_S[:]
        
    S_memo.append(change_S[:])

            
    point += 1
    

            
    
