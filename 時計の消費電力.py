time_str = input().replace(":", "")
time_int = [int(x) for x in time_str]
K = int(input())

#print(time_int,K)

use_ele = [4,5,2,3,3,1,5,4,1,2]

#time_int[0],time_int[1],time_int[2],time_int[3] = time_int[0],time_int[1],time_int[2],time_int[3]

while K > 0:
    print(time_int,K)
    true_time = time_int[:]
    time_int[3] += 1#1秒進める
    
    if time_int[3] == 10:#ｓ１の繰り上がり
        time_int[3] = 0
        K -= use_ele[9]
        time_int[2] += 1
    else:
        K -= use_ele[time_int[3]-1]
    
    if time_int[2] == 6:#ｓ１０の繰り上がり
        time_int[2] = 0
        K -= 2
        time_int[1] += 1
        K -= use_ele[time_int[1]-1]

    if time_int[1] == 10:
        time_int[1] = 0
        K -= use_ele[9]
        
    if time_int[1] == 4 and time_int[0] == 2:
        time_int[0] = 0
        K -= 3
        time_int[1] = 0
        K -= 3


        
        
print(f"{true_time[0]}{true_time[1]}:{true_time[2]}{true_time[3]}")
            