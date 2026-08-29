class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #first insert and then apply the logic of merge intervals
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        ans=[]
        ans.append(intervals[0])
        for i in range(1,len(intervals)):
            if(ans[-1][1]>=intervals[i][0]):
                ans[-1][1]=max(ans[-1][1],intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans
       