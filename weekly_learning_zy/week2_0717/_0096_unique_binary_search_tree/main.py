from math import factorial


def numTrees2( n: int) -> int:
    # 初始化一个数组，并将首个元素初始化为1
    s = [0] * (n + 1)
    s[0] = 1
    # 开始循环遍历
    for i in range(1, n + 1):
        # 为节约内存，首先算出i-1的值
        b = i - 1
        # 为节约内存，只遍历一半，并将这个结果乘以2即可
        for j in range(i // 2):
            s[i] += s[j] * s[b - j]
        s[i] *= 2
        # 当i为奇数时，还要将s[i//2]的值加上
        if i % 2 == 1:
            s[i] += s[i // 2] ** 2
    # 返回数组最后一个元素
    return s
# DP
def xrange(param, param1):
    pass


def numTrees1(self, n):
    res = [0] * (n+1)
    res[0] = 1
    for i in xrange(1, n+1):
        for j in xrange(i):
            res[i] += res[j] * res[i-1-j]
    return res[n]

class Solution:
    def numTrees(self, n: int) -> int:
        return factorial(2*n)//factorial(n)//factorial(n)//(n+1)


if __name__ == '__main__':
   print(numTrees2(5))
