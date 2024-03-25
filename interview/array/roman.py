class Solution:  
    def romanToInt(self, s: str) -> int:
        romandDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        arr = list(s)
        sum = 0
        i = 0
        while i < len(arr):
            if i == len(arr) - 1 or romandDict[arr[i]] >= romandDict[arr[i+1]]:
                sum += romandDict[arr[i]]
            else:
                sum -= romandDict[arr[i]]
            i += 1
                
        return sum