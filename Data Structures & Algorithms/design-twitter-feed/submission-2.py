class Twitter:

    def __init__(self):
        self.follows = {}
        self.users = {} # userId - [(time, tweetID)] list
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId] = self.users.get(userId, []) + [(self.time, tweetId)]
        self.time += 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = list(self.users.get(userId, []))
        for f in self.follows.get(userId, []):
            tweets.extend(self.users[f])

        tweets.sort(reverse=True)
        return [tid for _, tid in tweets[:10]]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if self.follows.get(followerId, 0) == 0:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)        
