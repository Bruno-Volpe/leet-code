from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:  
            return 0 

        # Remove duplicates
        nums = set(nums)
        longest_sequence = 0

        for num in nums:
            if num - 1 not in nums:  # Check if num is the start of a sequence
                current_num = num
                current_sequence = 1

                while current_num + 1 in nums:  # Extend the sequence
                    current_num += 1
                    current_sequence += 1

                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence
