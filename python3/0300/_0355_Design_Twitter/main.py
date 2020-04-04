from typing import List
import collections
import heapq


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # assume larger tweetId is more recent
        self.tweets = collections.defaultdict(list)
        self.followees = collections.defaultdict(set)
        self.ts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.ts += 1
        self.tweets[userId].append((tweetId, self.ts))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId] = self.tweets[userId][1:]

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        candidates = list(self.followees[userId])
        candidates.append(userId)

        maxHeap = []
        for c in candidates:
            for tweetId, ts in self.tweets[c]:
                heapq.heappush(maxHeap, (-ts, tweetId))

        feeds = []
        while len(feeds) < 10 and maxHeap:
            _, tweetId = heapq.heappop(maxHeap)
            feeds.append(tweetId)

        return feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
