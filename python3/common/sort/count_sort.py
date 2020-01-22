from typing import List
import random


def countSort(nums: List[int]):
    if not nums:
        return

    n, mn, mx = len(nums), min(nums), max(nums)
    count = [0] * (mx - mn + 1)

    for i in range(n):
        count[nums[i] - mn] += 1

    i = 0
    for j, cnt in enumerate(count):
        for _ in range(cnt):
            nums[i] = j
            i += 1


def countSort2(nums: List[int]):
    if not nums:
        return

    n, mn, mx = len(nums), min(nums), max(nums)
    count = [0] * (mx - mn + 1)

    for i in range(n):
        count[nums[i] - mn] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    res = [0] * n
    for i in range(n - 1, -1, -1):
        idx = nums[i] - mn
        res[count[idx] - 1] = nums[i]
        count[idx] -= 1

    for i in range(n):
        nums[i] = res[i]


if __name__ == '__main__':
    li = [i for i in range(50)]
    random.shuffle(li)

    print("before sort: ", li)
    countSort2(li)
    print("after sort: ", li)
