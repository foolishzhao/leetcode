from typing import List
import random


def mergeSort(nums: List[int]):
    if not nums:
        return

    mergeSortHelper(nums, 0, len(nums) - 1)


def mergeSortHelper(nums: List[int], begin: int, end: int):
    if begin >= end:
        return

    mid = (end - begin) // 2 + begin
    mergeSortHelper(nums, begin, mid)
    mergeSortHelper(nums, mid + 1, end)

    t = []

    i, j = begin, mid + 1
    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            t.append(nums[i])
            i += 1
        else:
            t.append(nums[j])
            j += 1

    while i <= mid:
        t.append(nums[i])
        i += 1

    while j <= end:
        t.append(nums[j])
        j += 1

    for k in range(begin, end + 1):
        nums[k] = t[k - begin]


if __name__ == '__main__':
    li = [i for i in range(10)]
    random.shuffle(li)

    print("before sort: ", li)
    mergeSort(li)
    print("after sort: ", li)
