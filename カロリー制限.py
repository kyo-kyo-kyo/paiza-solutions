N,M = map(int,input().split())#N.弁当の種類,M.カロリー上限
cal = list(map(int,input().split()))#カロリー
sat = list(map(int,input().split()))#満足度
dis = list(map(int,input().split()))#おかずの種類
print(N,M,cal,sat,dis)



best = 0
print(dis.count(1),dis.count(2),dis.count(3))
for i in range(dis.count(1)):
    for j in range(dis.count(2)):
        for k in range(dis.count(3)):
            if cal[i] + cal[j] + cal[k] <= M:
                best = max(best,sat[i],sat[j],sat[k])

    
print(best)

max_sat_1,m_s_1_cal,m_s_1_dis = 0,0,0
max_sat_2,m_s_2_cal,m_s_2_dis= 0,0,0
max_sat_3,m_s_3_cal,m_s_3_dis = 0,0,0


for j in range(N):
    
    for i in range(N):
        if dis[i] == 1 and sat[i] > max_sat_1:
            max_sat_1 = sat[i]
            m_s_1_cal = cal[i]
            m_s_1_dis = dis[i]
        elif dis[i] == 2 and sat[i] > max_sat_2:
            max_sat_2 = sat[i]
            m_s_2_cal = cal[i]
            m_s_2_dis = dis[i]
        elif dis[i] == 3 and sat[i] > max_sat_3:
            max_sat_3 = sat[i]
            m_s_3_cal = cal[i]
            m_s_3_dis = dis[i]
            
    #if sum(m_s_1_cal,m_s_2_cal,m_s_3_cal) <= M:
        

        
    
        
print(max_sat_1,max_sat_2,max_sat_3)
print(m_s_1_cal,m_s_2_cal,m_s_3_cal)
print(m_s_1_dis,m_s_2_dis,m_s_3_dis)