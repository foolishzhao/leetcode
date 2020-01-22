from typing import List
import random


def bubbleSort(nums: List[int]):
    if not nums:
        return

    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


if __name__ == '__main__':
    li = [i for i in range(10)]
    random.shuffle(li)

    print("before sort: ", li)
    bubbleSort(li)
    print("after sort: ", li)
