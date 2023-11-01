class Twitter:

    def __init__(self):
        self.count = 0 #to track the chronology(latest first)
        self.tweetMap = defaultdict(list) #userId - [[count,tweetId]]
        self.followMap = defaultdict(set) #userId - followerId

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -= 1
        print(self.tweetMap)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap = []
        answer = []
        self.followMap[userId].add(userId)
        for follower in self.followMap[userId]:
            if follower in self.tweetMap:
                index = len(self.tweetMap[follower]) - 1 #latest tweet 
                count, tweetId = self.tweetMap[follower][index]
                maxheap.append([count,tweetId,follower,index - 1])
        heapq.heapify(maxheap)
        
        while maxheap and len(answer) < 10:
            count, tweetId, follower, index = heapq.heappop(maxheap)
            answer.append(tweetId)
            if index >=0:
                count, tweetId = self.tweetMap[follower][index]
                heapq.heappush(maxheap,[count,tweetId,follower,index - 1]) 
        return answer

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].remove(followeeId)
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)