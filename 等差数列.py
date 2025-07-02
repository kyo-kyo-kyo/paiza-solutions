PI = input().split()
H,W = int(PI[0]),int(PI[1])
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
diff1,diff2 = nums1[1] - nums1[0],nums2[0] - nums1[0]
print(H,W,nums1,nums2,diff1,diff2)
seq = [nums1]
for i in range(2,H):
    for j in range(2,W):
       seq.append(int(int(nums1[H - 1])+diff1))
       print(seq)
