from typing import List
import random


# k bucket, every bucket n / k elem
# time complexity: k * (n / k) * log(n / k) = n * log(n / k)
# space complexity: O(n)
def bucketSort(nums: List[int]):
    if not nums:
        return

    n, k, mn, mx = len(nums), 5, min(nums), max(nums)
    gap = (mx - mn + 1) / k

    bucket = [[] for _ in range(k)]
    for i in range(n):
        idx = int((nums[i] - mn) / gap)
        bucket[idx].append(nums[i])

    i = 0
    for _, u in enumerate(bucket):
        # sort inside bucket, (n / k) * log(n / k)
        u.sort()
        for _, v in enumerate(u):
            nums[i] = v
            i += 1


if __name__ == '__main__':
    li = [i for i in range(50)]
    random.shuffle(li)

    print("before sort: ", li)
    bucketSort(li)
    print("after sort: ", li)
