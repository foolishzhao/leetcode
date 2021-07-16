class Solution:
    def removeDuplicates(self,array):
        array[:] = sorted(set(array))
        print(array)
        return len(array)
if __name__ == '__main__':
    Solution().removeDuplicates([2,3,2,1,1,5,6,7])