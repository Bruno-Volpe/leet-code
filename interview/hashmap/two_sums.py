class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        right = 0
        
        while right < len(nums):
            if target - nums[right] in hash_map:
                return [hash_map[target - nums[right]], right]
            else:
                hash_map[nums[right]] = right
                right += 1