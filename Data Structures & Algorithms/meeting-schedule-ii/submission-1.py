"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

2 pointers, 2 arrays (start time, end time) approach
- determine how many rooms you need
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        start_times, end_times = [], []
        for i in intervals:
            start_times.append(i.start)
            end_times.append(i.end)
        start_times.sort()
        end_times.sort()


        i, j = 0, 0 # 2 pointers
        rooms = 0   # rooms needed...?
        max_rooms = 0
        while True:
            if i == n or j == n:
                break # easier to use while True + break 
 
            if start_times[i] < end_times[j]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)

                i += 1 # adv start

            else:
                rooms -= 1
                j += 1 # adv end


        return max_rooms
        

        