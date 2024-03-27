class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            next_number = 0
            for digit in str(n):
                next_number += int(digit) ** 2
            n = next_number

        return n == 1
