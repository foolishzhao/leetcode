from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res, buffer, block, i, n = list(), "", False, 0, len(source)
        while i < n:
            line = source[i]
            if block:
                idx3 = line.find("*/")
                if idx3 != -1:
                    block = False
                    source[i] = line[idx3 + 2:]
                else:
                    i += 1
            else:
                idx1 = line.find("//")
                idx2 = line.find("/*")
                if idx1 == -1 and idx2 == -1:
                    buffer += line
                    i += 1
                else:
                    if idx2 == -1 or (idx1 != -1 and idx2 > idx1):
                        buffer += line[:idx1]
                        i += 1
                    else:
                        block = True
                        buffer += line[:idx2]
                        source[i] = line[idx2 + 2:]

                if buffer and not block:
                    res.append(buffer)
                    buffer = ""
        return res

    def removeComments2(self, source: List[str]) -> List[str]:
        res, buffer, block = list(), "", False
        for line in source:
            n, i = len(line), 0
            while i < n:
                if block:
                    if line[i] == '*' and i + 1 < n and line[i + 1] == '/':
                        block = False
                        i += 1
                else:
                    if line[i] == '/' and i + 1 < n and line[i + 1] == '/':
                        break
                    elif line[i] == '/' and i + 1 < n and line[i + 1] == '*':
                        block = True
                        i += 1
                    else:
                        buffer += line[i]
                i += 1

            if buffer and not block:
                res.append(buffer)
                buffer = ""
        return res
