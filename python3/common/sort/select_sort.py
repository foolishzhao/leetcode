from typing import List
import random


def selectSort(nums: List[int]):
    if not nums:
        return

    n = len(nums)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if nums[j] < nums[k]:
                k = j
        nums[i], nums[k] = nums[k], nums[i]


if __name__ == '__main__':
    li = [i for i in range(10)]
    random.shuffle(li)

    print("before sort: ", li)
    selectSort(li)
    print("after sort: ", li)
