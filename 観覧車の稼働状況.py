N,M = map(int,input().split())
gondola = [int(input()) for _ in range(N)]
groups = [int(input()) for _ in range(M)]

total_rides = [0] * N
ride_index = 0

for group in groups:
    remaining = group
    while remaining > 0:
        cap = gondola[ride_index]
        if remaining <= cap:
            total_rides[ride_index] += remaining
            remaining = 0
        else:
            total_rides[ride_index] += cap
            remaining -= cap
        ride_index = (ride_index + 1) % N
        
for ride in total_rides:
    print(ride)
"""excess = 0
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
            """"""gondola_count.append(excess)
            excess = 0""""""
            i += 1
            print("b",gondola_count,peo,excess)
        elif (peo[j] - gondola[i]) <= 0:#余りが出ないなら
            gondola_count.append(peo[j])
            peo[j] = 0
            j += 1 
            print("c",gondola_count,peo,excess)
        i += 1
        """