class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort the intervals on the basis of endtime
        intervals.sort(key=lambda x:x[1])
        count=0
        #now create a lastend variable
        lastend=-sys.maxsize
        #traverse through the intervals
        for start,end in intervals:
            if(start>=lastend):
                #means no overlap
                lastend=end
            else:
                count+=1
        return count
               
       