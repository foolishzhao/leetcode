from typing import List


# no duplicate, search target
def binarySearch(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = ((right - left) >> 1) + left
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# duplicate, search first target
def binarySearchFirst(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = ((right - left) >> 1) + left
        if nums[mid] == target:
            if mid == left or nums[mid - 1] != target:
                return mid
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# duplicate, search last target
def binarySearchLast(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = ((right - left) >> 1) + left
        if nums[mid] == target:
            if mid == right or nums[mid + 1] != target:
                return mid
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# duplicate, search first >= target
def binarySearchFirstGE(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = ((right - left) >> 1) + left
        if nums[mid] >= target:
            if mid == left or nums[mid - 1] < target:
                return mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1

    return -1


# duplicate, search first <= target
def binarySearchFirstLE(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = ((right - left) >> 1) + left
        if nums[mid] <= target:
            if mid == right or nums[mid + 1] > target:
                return mid
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    pass
