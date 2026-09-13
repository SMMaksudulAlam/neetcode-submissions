import heapq as hq
class Twitter:

    def __init__(self):
        self.followees = {}
        self.tweets = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if(userId not in self.tweets):
            self.tweets[userId] = set()
            self.followees[userId] = set([userId])
        self.tweets[userId].add((self.time, tweetId))
        self.time+=1
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        count = 0
        for follwee in self.followees.get(userId, set()):
            for tweet in self.tweets.get(follwee, set()):
                if(count<10):
                    hq.heappush(h, (tweet[0], tweet[1]))
                    count+=1
                else:
                    if(h[0][0]<tweet[0]):
                        hq.heappop(h)
                        hq.heappush(h, (tweet[0], tweet[1]))
        ans = []
        while(h):
            tweet = hq.heappop(h)
            ans.append(tweet[1])
        return ans[::-1]
    def follow(self, followerId: int, followeeId: int) -> None:
        if(followerId not in self.followees):
            self.followees[followerId] = set([followerId])
        self.followees[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followerId in self.followees):
            if(followeeId in self.followees[followerId]):
                self.followees[followerId].remove(followeeId)
        return
