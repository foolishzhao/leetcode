from typing import List
import random


def quickSort(nums: List[int]):
    if not nums:
        return

    quickSortHelper(nums, 0, len(nums) - 1)


def quickSortHelper(nums: List[int], begin: int, end: int):
    if begin >= end:
        return

    pivot = nums[end]
    i, j = begin, begin
    while j < end:
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

    nums[i], nums[end] = nums[end], nums[i]

    quickSortHelper(nums, begin, i - 1)
    quickSortHelper(nums, i + 1, end)


if __name__ == '__main__':
    li = [i for i in range(10)]
    random.shuffle(li)

    print("before sort: ", li)
    quickSort(li)
    print("after sort: ", li)
