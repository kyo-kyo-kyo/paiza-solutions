n = int(input())
fruit = []
for i in range (n):
    fruit.append(input().split())
    
for i in range (n):
  
    for j in range (n - 1,i,-1):
       
        if int(fruit[j][0]) > int(fruit[j - 1][0]):
            
            fruit[j],fruit[j - 1] = fruit[j - 1],fruit[j]
            
        if int(fruit[j][1]) > int(fruit[j - 1][1]) and int(fruit[j][0]) == int(fruit[j - 1][0]):
            
            fruit[j],fruit[j - 1] = fruit[j - 1],fruit[j] 

for i in range (n):
    print(f"{fruit[i][0]}"" "f"{fruit[i][1]}")
    
