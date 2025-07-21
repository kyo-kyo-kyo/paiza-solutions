v = list(map(int,input().split()))
N,M = v[0],v[1]
gondola = []
for _ in range(N):
    gondola.append(int(input()))

peo = []
for _ in range(M):
    peo.append(int(input()))

print(N,M,gondola,peo)
excess = 0
gondola_count = []
j = 0
i = 0
while j < M:#客数が最大以上にならないように
        excess = 0
        i = i % N
        print("１周")
        print(i,j)    
        if (peo[j] - gondola[i]) > 0:#余りが出るなら
            gondola_count.append(gondola[i])
            excess = peo[j] - gondola[i]
            peo[j] = 0
            flag = False
            while (excess-gondola[i]) <= 0:
                j += 1
                gondola_count.append(gondola[i])
                excess = gondola_count[j] - gondola[i]
            j += 1
            """gondola_count.append(excess)
            excess = 0"""
            i += 1
            print("b",gondola_count,peo,excess)
        elif (peo[j] - gondola[i]) <= 0:#余りが出ないなら
            gondola_count.append(peo[j])
            peo[j] = 0
            j += 1 
            print("c",gondola_count,peo,excess)
        i += 1
        