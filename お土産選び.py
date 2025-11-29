N = int(input())

pack = []

for _ in range(3):
    pack.append(list(map(int,input().split())))
    
print(pack)
print(N / pack[0][0])
min_now = 0
manju = 0
max_loop1,max_loop2,max_loop3 = math.ceil(N / pack[0][0]),N / pack[1][0],N / pack[2][0]

print(max_loop1,max_loop2,max_loop3)

    

"""while manju <= 20:
    min = 0"""