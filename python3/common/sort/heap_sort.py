class MinHeap:
    def __init__(self):
        self.n = 0
        self.arr = list()

    # x: int
    def push(self, x):
        self.n += 1
        self.arr.append(x)

        i = self.n - 1  # child
        j = (i - 1) // 2  # parent
        while i > 0 and self.arr[j] > self.arr[i]:
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            i = j
            j = (i - 1) // 2

    # return min value
    def pop(self):
        if not self.n:
            return None

        res = self.arr[0]

        self.arr[0] = self.arr[self.n - 1]
        self.n -= 1

        i = 0
        while 2 * i + 1 <= self.n - 1:
            j = 2 * i + 1
            if j + 1 <= self.n - 1 and self.arr[j + 1] < self.arr[j]:
                j += 1

            if self.arr[i] <= self.arr[j]:
                break

            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            i = j

        return res


if __name__ == '__main__':
    mh = MinHeap()
    nums = [4, 5, 2, 7, 8, 1, 9, 6, 3, 0]

    for i in nums:
        mh.push(i)

    for i in range(len(nums)):
        print(mh.pop())
