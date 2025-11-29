N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
    
print(nums)

for i in range (N):
    for j in range (N - 1,i,-1):
        if nums[j] > nums[j - 1]:
            nums[j],nums[j - 1] = nums[j - 1],nums[j]
        print(nums)
for i in range (N):
    print(f"{nums[i]}")
"""
while(i < N):
    j = N - 1
    print(j)
    while(i >= j ):
        
        if list[(j-1)] > list[j]:
                list[j] = rip
                print(rip)
                list[j] = list[(j-1)]
                list[(j-1)] = rip
        
        j = j - 1
        print(list)
        print(j)
        
    i = i + 1
    print(i)
"""
    