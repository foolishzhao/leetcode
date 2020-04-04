import collections
import math


class TweetCounts:

    def __init__(self):
        self.tweet = collections.defaultdict(list)
        self.freq = {'minute': 60, 'hour': 3600, 'day': 86400}

    # first index, i.e. li[index] >= val
    def _search(self, li, val):
        left, right = 0, len(li) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if li[mid] >= val:
                if mid == left or li[mid - 1] < val:
                    return mid
                right = mid - 1
            else:
                left = mid + 1

        return left

    def recordTweet(self, tweetName: str, time: int) -> None:
        li = self.tweet[tweetName]
        li.insert(self._search(li, time), time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        freq = self.freq[freq]
        n = math.ceil((endTime - startTime + 1) / freq)
        res, li = [0] * n, self.tweet[tweetName]
        for t in li:
            if startTime <= t <= endTime:
                res[(t - startTime) // freq] += 1

        return res
