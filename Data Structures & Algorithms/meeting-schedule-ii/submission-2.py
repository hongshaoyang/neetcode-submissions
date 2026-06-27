"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

pq (min heap) approach
    - size of pq = total of rooms needed at that point in time
    - return max size of pq = max rooms needed for all meetings
"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)

        h = []
        max_rooms = 0
        for i in intervals:
            if len(h) == 0: # trivial case
                heapq.heappush(h, i.end)
                max_rooms = max(max_rooms, 1) 
                continue

            '''
            compare
            - i.start - start of next meeting
            - h[0]    - earliest end of meetings currently happening
            '''
            if i.start < h[0]:
                heapq.heappush(h, i.end)
            else:
                heapq.heappop(h)
                heapq.heappush(h, i.end)

            max_rooms = max(max_rooms, len(h))

        return max_rooms





        
        