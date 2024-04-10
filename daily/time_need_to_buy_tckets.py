from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        while True:
            for c in range(len(tickets)):
                if tickets[c] > 0:
                    tickets[c] -= 1  # Corrected: Subtract 1, not k
                    count += 1      # Corrected: Update the count
                    if c == k and tickets[c] == 0:
                        return count
