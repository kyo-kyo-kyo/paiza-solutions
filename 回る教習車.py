N = int(input())
car_namber = []
for _ in range(N):
    car_namber.append(int(input()))

#print(N,car_namber)
i = 1#出るべき車番
orbit_index = []
while i < N :#教習車がすべて出るまで
    #for i in range(1,N+1):
        for j in car_namber:#先頭から車番を調べる
            
            if i == j:#出るべき車番と今の車番が同じなら
                #car_namber.remove(j)#教習車を出す
                #print("a","i=",i,"j=",j,car_namber,orbit_index)
                i += 1#出したなら次の教習車を探す
            elif i != j:    
                orbit_index.append(j)#１周足す
                #print("b","i=",i,"j=",j,car_namber,orbit_index)

            
print(orbit_index.count(N))
                

    
        
# 周回indexを用意
# for_iで一周をはかり、for_jで車番を数える。一周ごとにtimeへ+1する
# whileで最後の教習車が出るまで続ける
# #