import math
H,M = map(int,input().split())
light_bulb = list(map(int,input().split()))
Q = int(input())
search_light = [list(map(int,input().split())) for _ in range(Q)]
print(H,M,light_bulb,Q,search_light)

for q in range(Q):
    light_ave = sum(light_bulb[search_light[q][0]-1:search_light[q][1]-1]) / (search_light[q][1] - search_light[q][0] + 1)
    
    for i in range(search_light[q][0] - 1,search_light[q][1] - 1):
            if light_ave > light_bulb[i]:
                light_bulb[i] += math.ceil(light_ave) - light_bulb[i]
                print(light_bulb)
                
print(light_bulb)
                
    

