n,T = input().split()
S = input()
n = int(n)

alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(n,T,S)

n = n % 26
        
print(n)


new_S = []
for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j] and (j + n) < len(T):
            new_S.append(alp[j+n])
            print(new_S)
            break
        elif S[i] == T[j] and (j + n) >= len(T):
            new_S.append(alp[j+n-len(T)])
            print(new_S)
            break         


    
    
    
print(new_S)