from typing import List
import random


# O(n^1.3~2)
def shellSort(nums: List[int]):
    if not nums:
        return

    n = len(nums)
    d = n // 2
    while d:
        for i in range(d, n):
            j, t = i - d, nums[i]
            while j >= 0 and nums[j] > t:
                nums[j + d] = nums[j]
                j -= d
            nums[j + d] = t

        d //= 2


if __name__ == '__main__':
    li = [i for i in range(10)]
    random.shuffle(li)

    print("before sort: ", li)
    shellSort(li)
    print("after sort: ", li)
