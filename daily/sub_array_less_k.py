class Solution:
    def find_all_subsequences(self, nums: List[int]) -> List[List[int]]:
        subsequences = []
        for i in range(len(nums)):
            subsequences.append([nums[i]])
            for j in range(i + 1, len(nums)):
                subsequences.append(nums[i:j + 1])
        return subsequences
    
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        mult = 1
        
        sub_arrays = []
        all_sub_arrays = self.find_all_subsequences(nums)
        
        for sub_array in all_sub_arrays:
            for num in sub_array:
                mult *= num
            if mult < k:
                sub_arrays.append(sub_array)
            mult = 1

        return len(sub_arrays)