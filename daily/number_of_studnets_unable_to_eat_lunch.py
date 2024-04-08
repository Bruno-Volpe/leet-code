from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        c = 0
        # Iterate until all students are checked or until sandwiches stack is empty
        while students:
            if sandwiches[0] == students[0]:
                # If the sandwich matches the student's preference, remove both from queues
                sandwiches.pop(0)
                students.popleft()
                c = 0
            else:
                # If the sandwich doesn't match the student's preference, move student to the end of the queue
                students.append(students.popleft())
                c += 1
                # Check if all students are checked without finding a match
                if c == len(students):
                    break
        
        return len(students)
