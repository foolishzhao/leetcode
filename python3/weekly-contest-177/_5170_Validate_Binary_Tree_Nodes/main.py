from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        hasParent, validParent = {0}, {0}
        for parent, left, right in zip(range(n), leftChild, rightChild):
            if parent not in validParent and (left != -1 or right != -1):
                return False
            else:
                if left != -1:
                    if left in hasParent:
                        return False
                    hasParent.add(left)
                    validParent.add(left)

                if right != -1:
                    if right in hasParent:
                        return False
                    hasParent.add(right)
                    validParent.add(right)

        return True


if __name__ == '__main__':
    obj = Solution()
    print(obj.validateBinaryTreeNodes(5, [1, 3, -1, -1, -1], [-1, 2, 4, -1, -1]))
