class Twitter:

    def __init__(self):
        #do exactly as it is asked here 
        self.time=0
        self.following=defaultdict(set)
        #meaning this userid follows how many people 
        self.tweets=defaultdict(list)
        #in this we will arrange userid with the time and tweetid

    def postTweet(self, userId: int, tweetId: int) -> None:
        #here for that tweet we need to store the time and the tweetId
        self.time+=1
        self.tweets[userId].append((self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        #here we need to return the ten most recent tweets so sorting in reverse order also needs to be done 
        alltweets=[]
        #so here we use the current user also
        users=self.following[userId]|{userId}
        for user in users:
            #lets store them in alltweets
            alltweets.extend(self.tweets[user])
        #now lets sort in reverse order
        alltweets.sort(reverse=True)
        return [tweetId for time,tweetId in alltweets[:10]]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)