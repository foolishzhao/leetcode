import math


class Solution:
    # t round, t+1 based encoding
    #
    # n pig, t round, can handle (t + 1) ^ n buckets
    # for 0 <= bucket <= ((t + 1) ^ n) - 1, if it's t + 1 based encoded.
    # bucket's each position's value k, 0 <= k <= t, denotes pig dies in k round, 0 means never die.
    # bucket's width 1 <= j <= n, n pig can map to a bucket's n position, i.e. pig j denotes position j.
    #
    # for round r from 1 to t, if a bucket's j position is r, feed the pig j
    # finally, if pig j die at r round, target bucket's position j should be r, then we get the target
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log(buckets, minutesToTest // minutesToDie + 1))
