class Solution:
    def decodeString(self, s: str) -> str:
        countSt, strSt = list(), list()
        curCount, curStr = 0, ""

        for c in s:
            if c.isdigit():
                curCount = curCount * 10 + int(c)
            elif c == '[':
                countSt.append(curCount)
                strSt.append(curStr)
                curCount, curStr = 0, ""
            elif c == ']':
                curStr = strSt.pop() + curStr * countSt.pop()
            else:
                curStr += c

        return curStr
