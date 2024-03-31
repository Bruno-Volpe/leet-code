# O(n) time complexity
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        set_chars = set()
        ans = i = j = 0
        while i < n and j < n:
            if s[j] not in set_chars:
                set_chars.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                set_chars.remove(s[i])
                i += 1
        return ans

# O(n^2) time complexity
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         possibles_substrings = []
        
#         for i in range(len(s)):
#             substring = s[i]
#             for j in range(i+1, len(s)):
#                 if s[j] not in substring:
#                     substring += s[j]
#                 else:
#                     break
#             possibles_substrings.append(substring)
        
#         if len(possibles_substrings) == 0:
#             return 0
        
#         return max([len(substring) for substring in possibles_substrings])