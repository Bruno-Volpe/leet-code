from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        bad = mi = ma = -1
        
        res = 0
        
        for i, n in enumerate(nums):
            if not minK <= n <= maxK:
                bad = i
                
            if minK == n:
                mi = i
                
            if maxK == n:
                ma = i
                
            start = min(mi, ma)
            
            if start > bad:
                res += start - bad
            
        return res


#O(n^2) - nao passa no teste de performance
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
