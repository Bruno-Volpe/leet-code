from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        res = 0
        left_far = 0
        left_near = 0
        for right in range(len(nums)):
            count[nums[right]] += 1
            while len(count) > k:
                count[nums[left_near]] -= 1
                if count[nums[left_near]] == 0:
                    count.pop(nums[left_near])
                left_near += 1
                left_far = left_near
            while len(count) > 0 and count[nums[left_near]] > 1:
                count[nums[left_near]] -= 1
                left_near += 1
            if len(count) == k:
                res += left_near - left_far + 1
        return res
