class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = 0
        
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            if count > len(nums) // 2:
                major = nums[i]
                break
        
        return major