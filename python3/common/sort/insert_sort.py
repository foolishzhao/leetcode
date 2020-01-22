from typing import List
import random


def insertSort(nums: List[int]):
    if not nums:
        return

    n = len(nums)
    for i in range(1, n):
        j, t = i - 1, nums[i]
        while j >= 0 and nums[j] > t:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = t


if __name__ == '__main__':
    li = [i for i in range(10)]
    random.shuffle(li)

    print("before sort: ", li)
    insertSort(li)
    print("after sort: ", li)
