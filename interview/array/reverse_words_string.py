class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words_arr = s.split()
        
        start = 0
        end = len(words_arr) - 1
        
        while start < end:
            words_arr[start], words_arr[end] = words_arr[end], words_arr[start]
            start += 1
            end -= 1
            
        return ' '.join(words_arr)