from typing import List
import itertools
import random


# time complexity: O(k * n)
# space complexity: O(1)
def radixSort(nums: List[str]):
    if not nums:
        return

    k = len(nums[0])
    for i in range(k - 1, -1, -1):
        nums.sort(key=lambda x: x[i])


if __name__ == '__main__':
    li = [''.join(x) for x in list(itertools.permutations(['a', 'b', 'c', 'd']))]
    random.shuffle(li)

    print("before sort: ", li)
    radixSort(li)
    print("after sort: ", li)
