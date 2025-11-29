"""
nums1,nums2 = "1 2 3 4 5 6","8 1 3 3 1 8"
print(int(len(nums1.split()))+int(len(nums2.split())))
"""

nums = [
    [1, 2, 3, 4, 5, 6],
    [8, 1, 3, 3, 1, 8]
]

total_elements = sum(len(row) for row in nums)
print(total_elements)