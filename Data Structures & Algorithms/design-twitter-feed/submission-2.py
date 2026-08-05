class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        #Need to know who the user follows and keep fetching the latest tweet.
        res = []
        self.followMap[userId].add(userId)
        minHeap = []
        for followeeId in self.followMap[userId]:
            #If the person they follow has tweeted before
            if followeeId in self.tweetMap:
                #Get the index of the latest tweet from their list, the time, and the tweetId
                #We get index so we can push their second more recent tweet later
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                minHeap.append((time, tweetId, followeeId, index))
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index > 0:
                nextTime, nextTweetId = self.tweetMap[followeeId][index-1]
                heapq.heappush(minHeap, (nextTime, nextTweetId, followeeId, index - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        
