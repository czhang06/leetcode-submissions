class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        for uid in self.following[userId] | {userId}:
            if self.tweets[uid]:
                i = len(self.tweets[uid]) - 1
                t, tid = self.tweets[uid][i]
                heapq.heappush(heap, (-t, tid, uid, i))
        feed = []
        while heap and len(feed) < 10:
            _, tid, uid, i = heapq.heappop(heap)
            feed.append(tid)
            if i > 0:
                t, ntid = self.tweets[uid][i - 1]
                heapq.heappush(heap, (-t, ntid, uid, i - 1))
        return feed

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