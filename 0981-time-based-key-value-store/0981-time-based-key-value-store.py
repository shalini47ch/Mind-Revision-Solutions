from collections import defaultdict

class TimeMap:
    def __init__(self):
        #use hmap along with storing timestamps to solve this 
        self.hmap=defaultdict(int)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key]=[]
        self.hmap[key].append([value,timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        values=self.hmap.get(key,[])
        #first parameter is value and the other is the timestamp
        start=0
        end=len(values)-1
        res="" #here we will store the largest value based on comparing with timestamp
        while(start<=end):
            mid=start+(end-start)//2
            if(values[mid][1]<=timestamp):
                res=values[mid][0]
                #and we need larger values so handle that as well
                start=mid+1
            else:
                end=mid-1
        return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)