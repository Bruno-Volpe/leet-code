class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(intervals: List[List[int]]) -> List[List[int]]:
            intervals.sort(key=lambda x: x[0])
            merged = []
            
            for interval in intervals:
                if not merged or merged[-1][1] < interval[0]:
                    merged.append(interval)
                else:
                    merged[-1][1] = max(merged[-1][1], interval[1])
            
            return merged
        
        merged_intervals = merge(intervals)
        #Verificar se newInstervals esta presente em new intervals
        for interval in merged_intervals: 
            if newInterval[0] > interval[1]:
                continue
            elif newInterval[1] < interval[0]:
                continue
            else:
                if newInterval[0] < interval[0]:
                    interval[0] = newInterval[0]
                if newInterval[1] > interval[1]:
                    interval[1] = newInterval[1]
                break
        else:
            merged_intervals.append(newInterval)
        merged_intervals = merge(merged_intervals)
                        
            
        return merged_intervals