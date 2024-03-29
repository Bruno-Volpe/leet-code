from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        hash_map = {}
        sub_arrays = []
        
        for i, num in enumerate(nums):
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
                
                
        aux_arr = []
        for i in range(len(nums)):
            if hash_map[nums[i]] >= k:
                aux_arr.append(nums[i])
            else:
                if aux_arr:
                    sub_arrays.append(aux_arr)
                    aux_arr = []    

        return len(sub_arrays)