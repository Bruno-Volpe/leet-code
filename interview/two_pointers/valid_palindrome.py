class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(e for e in s if e.isalnum()).lower()
        inicio = 0
        fim = len(s) - 1
        
        for _ in range((fim // 2) + 1):
            if s[inicio] != s[fim]:
                return False
            inicio += 1
            fim -= 1
        return True