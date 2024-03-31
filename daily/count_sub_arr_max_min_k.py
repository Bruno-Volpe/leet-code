from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left = 0
        subarrays = 0
        
        for right in range(len(nums)):
            if nums[right] >= minK and nums[right] <= maxK:
                subarrays += right - left + 1
            else:
                left = right + 1
                    
        return subarrays


# O(n^2) - nao passa no teste de performance
# class Solution:
#     def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
#         subarrays = 0
        
#         for i in range(len(nums)):
#             max_sub = nums[i]
#             min_sub = nums[i]
#             for j in range(i, len(nums)):
#                 max_sub = max(max_sub, nums[j])
#                 min_sub = min(min_sub, nums[j])
#                 if max_sub == maxK and min_sub == minK:
#                     subarrays += 1
                
#         return subarrays
