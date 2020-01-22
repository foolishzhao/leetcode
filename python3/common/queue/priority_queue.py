import heapq

if __name__ == '__main__':
    # default min heap
    nums = [1, 2]
    heapq.heapify(nums)
    heapq.heappush(nums, 3)

    # can remove elem from list, then heapify again
    nums.remove(2)
    heapq.heapify(nums)

    while nums:
        # first elem is the top elem
        print(nums[0])
        print(heapq.heappop(nums))

    print()

    # use minus to simulate max heap
    heapq.heappush(nums, -3)
    heapq.heappush(nums, -2)
    heapq.heappush(nums, -1)
    while nums:
        print(-heapq.heappop(nums))

    print()

    heapq.heappush(nums, (1, 2))
    heapq.heappush(nums, (2, 3))
    heapq.heappush(nums, (2, 1))
    while nums:
        print(heapq.heappop(nums))
