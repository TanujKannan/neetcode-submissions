class Twitter:

    def __init__(self):
        self.followerMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        self.followerMap[userId].add(userId)
        for followeeId in self.followerMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                heap.append((time, index, tweetId, followeeId))
        heapq.heapify(heap)

        while heap and len(res) < 10:
            time, index, tweetId, followeeId = heapq.heappop(heap)
            res.append(tweetId)
            if index > 0:
                newTime, newTweetId = self.tweetMap[followeeId][index - 1]
                heapq.heappush(heap, (newTime, index-1, newTweetId, followeeId))
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].discard(followeeId)