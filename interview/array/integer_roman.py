class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        romanDict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 
                     50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 
                     900: 'CM', 1000: 'M'}
        
        for key in sorted(romanDict.keys(), reverse=True):
            while num >= key:
                roman += romanDict[key]
                num -= key
            
        return roman
    
    
"""
O(1) 
class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hrns = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        ths = ["","M","MM","MMM"]
        
        return ths[num//1000] + hrns[(num%1000)//100] + tens[(num%100)//10] + ones[num%10]
"""