PI = input().split()
H,W = int(PI[0]),int(PI[1])
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
diff1,diff2 = nums1[1] - nums1[0],nums2[0] - nums1[0]
seq = []
for i in range(H):
    val = []
    
    for j in range(W):
        val.append(nums1[0] + diff2 * i + diff1 * j)
    
    seq.append(val)
for i in range(H):
    print(*seq[i])    